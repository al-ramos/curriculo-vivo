<#
  Publica o Currículo Vivo: comita e envia para o GitHub.

  Uso:  .\publicar.ps1              mensagem automática
        .\publicar.ps1 "mensagem"   mensagem própria

  O index.html normalmente já chega pronto. A regeração local a partir do
  markdown é opcional — veja ferramentas\LEIA-ME.md.
#>

param([string]$Mensagem = "")

# Sem "Stop": programas externos escrevem em stderr o tempo todo (git e python
# inclusive) e isso não é erro. Conferimos o código de saída explicitamente.
$ErrorActionPreference = "Continue"
Set-Location $PSScriptRoot

function Falhou($passo) {
    Write-Host ""
    Write-Host "Falhou em: $passo" -ForegroundColor Red
    exit 1
}

# ---------- 1. regeração opcional da página ----------
$temMarkdown = $false
if (Get-Command python -ErrorAction SilentlyContinue) {
    & python -c "import markdown" *> $null
    $temMarkdown = ($LASTEXITCODE -eq 0)
}

if ($temMarkdown) {
    Write-Host "Regerando a página a partir do markdown..." -ForegroundColor DarkGray
    Push-Location ferramentas
    & python build.py
    $okBuild = ($LASTEXITCODE -eq 0)
    if ($okBuild) { & python page.py; $okBuild = ($LASTEXITCODE -eq 0) }
    Pop-Location
    if ($okBuild) {
        Copy-Item ferramentas\curriculo-vivo.html index.html -Force
        Write-Host "Página regerada." -ForegroundColor DarkGray
    } else {
        Write-Host "Regeração falhou — publicando o index.html como está." -ForegroundColor Yellow
    }
} else {
    Write-Host "Publicando o index.html como está." -ForegroundColor DarkGray
}

# ---------- 2. limpar travas da ponte de arquivos ----------
Remove-Item .git\*.lock, .git\objects\*.lock -Force -ErrorAction SilentlyContinue
Get-ChildItem .git\objects -Recurse -Filter tmp_obj_* -ErrorAction SilentlyContinue |
    Remove-Item -Force -ErrorAction SilentlyContinue

# ---------- 3. comitar e enviar ----------
& git add -A
if ($LASTEXITCODE -ne 0) { Falhou "git add" }

$pendente = & git status --porcelain
if (-not $pendente) {
    Write-Host "Nada novo para publicar — o repositório já está em dia." -ForegroundColor DarkGray
    exit 0
}

if (-not $Mensagem) {
    $Mensagem = "Atualiza o Currículo Vivo — $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
}

& git commit -m $Mensagem
if ($LASTEXITCODE -ne 0) { Falhou "git commit" }

& git push origin main
if ($LASTEXITCODE -ne 0) { Falhou "git push" }

Write-Host ""
Write-Host "Publicado." -ForegroundColor Green
Write-Host "  https://al-ramos.github.io/curriculo-vivo/"
Write-Host ""
Write-Host "Acompanhe o workflow com:  gh run watch"

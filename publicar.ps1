# Publica o Currículo Vivo: regera a página, comita e envia para o GitHub.
# Uso:  .\publicar.ps1            (mensagem automática)
#       .\publicar.ps1 "mensagem" (mensagem própria)

param([string]$Mensagem = "")

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# 1. Regerar a página a partir do markdown, se o Python estiver disponível
if (Get-Command python -ErrorAction SilentlyContinue) {
    Push-Location ferramentas
    python build.py
    python page.py
    Copy-Item curriculo-vivo.html ..\index.html -Force -ErrorAction SilentlyContinue
    Pop-Location
}

# 2. Limpar travas que o git possa ter deixado
Remove-Item .git\*.lock, .git\objects\*.lock -Force -ErrorAction SilentlyContinue
Get-ChildItem .git\objects -Recurse -Filter tmp_obj_* -ErrorAction SilentlyContinue | Remove-Item -Force

# 3. Comitar e enviar
git add -A
$temMudanca = git status --porcelain
if ($temMudanca) {
    if (-not $Mensagem) {
        $Mensagem = "Atualiza o Currículo Vivo — $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
    }
    git commit -m $Mensagem
} else {
    Write-Host "Nada novo para comitar." -ForegroundColor DarkGray
}

git push origin main

Write-Host ""
Write-Host "Publicado. A página estará no ar em um ou dois minutos:" -ForegroundColor Green
Write-Host "  https://al-ramos.github.io/curriculo-vivo/"
Write-Host ""
Write-Host "Acompanhe o workflow com:  gh run watch"

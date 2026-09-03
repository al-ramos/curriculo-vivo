# Ferramentas

`build.py` converte o markdown de `conteudo/texto/` em um fragmento HTML
(`_body.html`), e `page.py` monta a página final (`curriculo-vivo.html`),
que é copiada para `livro.html` na raiz.

Rodar isso localmente é **opcional**. A página normalmente chega pronta;
o `publicar.ps1` só regenera se as dependências estiverem instaladas.

Para habilitar a regeração local:

```powershell
python -m pip install markdown
```

Depois, `.\publicar.ps1` passa a reconstruir a página antes de publicar.

`_body.html` é intermediário e está no `.gitignore`.

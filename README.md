# Currículo Vivo

**Engenharia de Software: Envelhecimento Macro** — um currículo organizado por uma
pergunta só: em quanto tempo cada conhecimento envelhece.

Vinte e um capítulos distribuídos em quatro camadas de velocidade. Cada seção declara
meia-vida, estado, data da próxima revisão e os gatilhos que forçam revisão antes do prazo.
Um livro sobre obsolescência que não pode envelhecer em silêncio.

## Camadas

| Camada | Meia-vida | Capítulos |
|---|---|---|
| 0 · A Lente | — | 1 |
| 1 · Permanente | sem erosão observada | 5 |
| 2 · Geracional | 15–20 anos | 6 |
| 3 · Cíclico | 5–15 anos | 7 |
| 4 · Sazonal | 1–5 anos | 3 |

Três dos vinte e um capítulos são de fato perecíveis. A ansiedade que o mercado produz se
concentra em 14% do currículo.

## Estado

- Camadas 0 e 1: texto integral (~5.800 palavras)
- Camadas 2 a 4: índice completo, texto pendente
- Datas e atribuições das fontes primárias ainda não conferidas contra as edições originais

## Estrutura

```
index.html                    portal — a linha do tempo que costura tudo
livro.html                    o livro
estudos.html                  o plano mestre de estudos
conteudo/linha-do-tempo.md    as 8 fases, 39 meses
conteudo/indice-v3.md         índice do livro, 21 capítulos
conteudo/texto/               texto do livro por camada
conteudo/plano-estudos.md     as 6 trilhas e a bibliografia
conteudo/plano.md             plano editorial e técnico do site
ferramentas/                  geração das páginas a partir do markdown
```

## A regra que costura tudo

Cada capítulo do livro é escrito **depois** da trilha de estudo que o sustenta, nunca
antes. O capítulo é o entregável escrito da trilha — e é por isso que escrever o livro
não compete com estudar, mas faz parte do estudo.

## Publicação

`main` publica automaticamente em GitHub Pages via `.github/workflows/pages.yml`.

Para regerar a página depois de editar o texto:

```bash
cd ferramentas && python3 build.py && python3 page.py
```

## Licença

Conteúdo sob [CC BY-SA 4.0](LICENSE-CONTEUDO). Código sob [MIT](LICENSE-CODIGO).

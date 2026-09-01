# A linha do tempo

## A regra que costura tudo

O portal tinha três planos que não se falavam: o índice do livro, o plano técnico do site
e o plano de estudos. Esta página os transforma em uma sequência só, e ela se apoia numa
regra única:

> **Cada capítulo do livro é escrito depois da trilha de estudo que o sustenta — nunca
> antes. O capítulo é o entregável escrito da trilha.**

Isso resolve dois problemas ao mesmo tempo. O plano de estudos exige um texto público ao
fim de cada trilha, e escrever esse texto some do orçamento de tempo porque ele já era o
capítulo. E o livro deixa de ser opinião sobre assuntos estudados de véspera: cada
capítulo chega depois de seis meses de leitura dirigida e um projeto entregue.

Três consequências que valem declarar:

**Os capítulos contextuais não seguem trilha.** Ensino formal, contexto brasileiro,
economia da decisão e ética não se aprendem em livro técnico — exigem pesquisa de fonte
primária, legislação e dado. Eles ficam concentrados no terceiro ano, quando a fundação
já não compete por atenção.

**O capítulo sobre IA é escrito por último, de propósito.** É o mais perecível do livro.
Escrevê-lo cedo garante que ele estará errado na publicação — e um livro sobre
envelhecimento que erra assim perde o direito de dar lição.

**O portal evolui junto, não depois.** Cada fase carrega uma melhoria técnica do site,
dimensionada para caber ao lado do estudo, não para competir com ele.

---

## Fase 0 · Fundação
**Duas semanas · agora**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 0 — diagnóstico, cinco artefatos guardados | Fichas de todos os 21 capítulos preenchidas, sem prosa | Três páginas no ar, navegação entre elas |

**Entregável:** o portal navegável e um retrato honesto do ponto de partida. Os cinco
artefatos do diagnóstico ficam guardados para comparação no fim do segundo ano.

---

## Fase 1 · A fundação que falta
**Meses 1 a 6**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 1 — Skiena como espinha; CSAPP e OSTEP de apoio; interpretador como projeto | **1.4 Cognição e metacognição** e **2.1 Paradigmas de programação** | Migração para Astro com o schema Zod da ficha; a compilação passa a falhar sem data de revisão |

Por que estes dois capítulos: 1.4 se apoia direto no *The Programmer's Brain*, lido na
trilha; 2.1 exige a experiência de escrever um interpretador para falar de paradigmas sem
repetir manual.

**Marco:** prever por escrito onde uma função sua quebra por volume, e acertar.

---

## Fase 2 · Dados e sistemas distribuídos
**Meses 7 a 12**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 2 — Kleppmann como espinha; Petrov, Winand e Nygard de apoio; serviço resiliente como projeto | **2.2 Dados e persistência** e **2.3 Sistemas distribuídos** | Radar de frescor e glossário vivo, gerados do frontmatter |

Os dois capítulos mais valiosos do livro para o seu perfil, escritos no momento em que
você acabou de provar as garantias em código. A seção "do campo" de 2.2 sai da sua
experiência com Sybase e SQL Server em produção contínua.

**Marco:** o livro passa a ter cinco capítulos escritos e um radar que aponta sozinho o
que está vencendo.

---

## Fase 3 · Projeto e arquitetura
**Meses 13 a 18**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 3 — Ousterhout como espinha; Fowler, Evans, Feathers e Newman de apoio; estrangulamento do legado VB6 como projeto | **3.1 Arquitetura de software** e **1.5 Comunicação e escrita técnica** | Grafo de pré-requisitos e matriz de dependências |

Aqui a integração fica mais evidente: os três ADRs exigidos pela trilha 3 são o material
bruto do capítulo 1.5. Você escreve sobre escrita técnica tendo acabado de praticá-la sob
pressão de um sistema real.

**Marco:** um arquiteto que não conhece o sistema reconstrói sua decisão lendo só os ADRs.

---

## Fase 4 · Qualidade e testes
**Meses 19 a 22**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 4 — Khorikov como espinha; Beck, Freeman & Pryce, Fowler de apoio; caracterização de legado como projeto | **3.3 Qualidade, testes e débito técnico** | Linha do tempo 1847–2026, ancorada nas quatro fases |

**Marco:** você defende com dados do próprio projeto a forma da sua pirâmide de testes — e
sabe apresentar o argumento contrário, que é o que 3.3.6 exige.

---

## Fase 5 · Plataforma, confiabilidade e segurança
**Meses 23 a 26**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 5 — SRE do Google como espinha; Shostack e Anderson de apoio; SLO e falha controlada como projeto | **4.1 Segurança e cadeia de suprimentos** e **4.2 Ferramentas e infraestrutura** | Arco de transformação do aluno, derivado dos pré-requisitos |

Trilha curta porque sua experiência já cobre a maior parte. É a fase em que o livro anda
mais rápido que o estudo — dois capítulos em quatro meses, porque a matéria-prima é o seu
trabalho diário.

**Marco:** existe um orçamento de erro publicado e uma decisão de priorização tomada com
base nele.

---

## Fase 6 · Os capítulos sem trilha
**Meses 27 a 32**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 6 em regime contínuo — Brooks, DeMarco & Lister, Larson | **2.4 Linguagens**, **2.5 Requisitos e IHC**, **2.6 Carreira**, **3.2 Processos** | Verificação de todas as fontes primárias, com checagem de link na CI |

Quatro capítulos que dependem menos de estudo novo e mais de organizar o que você já viveu
— trinta anos de linguagens, requisitos mal levantados, transições de carreira e a
travessia do RUP ao ágil dentro de banco.

---

## Fase 7 · A camada contextual
**Meses 33 a 36**

| Estudo | Livro | Portal |
|---|---|---|
| Pesquisa de fonte primária: DCN e SBC, legislação, dados de mercado | **3.4 Ética e legislação**, **3.5 Ensino formal**, **3.6 Contexto brasileiro**, **3.7 Economia da decisão** | Bibliografia completa e revisão de frescor de tudo escrito antes |

É a fase mais brasileira do livro e a que mais depende de fonte verificável. Deixá-la para
o fim é deliberado: exige mais rigor de citação do que de leitura técnica, e é o tipo de
trabalho que se faz melhor com o resto do argumento já de pé.

---

## Fase 8 · O capítulo perecível e o fechamento
**Meses 37 a 39**

| Estudo | Livro | Portal |
|---|---|---|
| — | **4.3 IA no ciclo de desenvolvimento**, escrito por último | Geração de PDF e EPUB; versão 1.0 |

O capítulo mais volátil do livro é escrito na última janela possível, com meia-vida
declarada de um a dois anos e data de revisão já marcada na ficha. É a única forma
honesta de publicá-lo.

---

## O quadro completo

| Fase | Meses | Trilha | Capítulos escritos | Acumulado |
|---|---|---|---|---|
| 0 | 0–0,5 | 0 | — (fichas) | 4 de 21 |
| 1 | 1–6 | 1 | 1.4, 2.1 | 6 |
| 2 | 7–12 | 2 | 2.2, 2.3 | 8 |
| 3 | 13–18 | 3 | 3.1, 1.5 | 10 |
| 4 | 19–22 | 4 | 3.3 | 11 |
| 5 | 23–26 | 5 | 4.1, 4.2 | 13 |
| 6 | 27–32 | 6 | 2.4, 2.5, 2.6, 3.2 | 17 |
| 7 | 33–36 | pesquisa | 3.4, 3.5, 3.6, 3.7 | 21 |
| 8 | 37–39 | — | 4.3 + revisão | 21 + v1.0 |

Trinta e nove meses. Pouco mais de três anos, no ritmo de seis a oito horas por semana —
e ao fim deles existem duas coisas que não existiam: uma formação que cobre as lacunas
reais do seu perfil, e um livro publicado que é a prova de que ela aconteceu.

## O que fazer se atrasar

Vai atrasar. Todo plano de três anos atrasa, e a pergunta útil é o que cortar.

**Corte escopo, nunca cadência.** Três fases bem-feitas valem mais que oito atropeladas.

**A ordem das fases 1 a 3 é inegociável.** São dependências reais: não dá para escrever
sobre arquitetura sem ter os fundamentos de distribuídos, e a trilha 2 pressupõe a
complexidade da trilha 1.

**As fases 6 e 7 podem trocar de lugar** conforme a oportunidade — se aparecer material de
pesquisa ou um contato acadêmico, antecipe a contextual.

**A fase 8 fica sempre por último.** Se ela for antecipada, o capítulo sobre IA estará
desatualizado na publicação, e o livro perde exatamente o argumento que veio defender.

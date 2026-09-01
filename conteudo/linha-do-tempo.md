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
| Trilha 0 — diagnóstico, cinco artefatos guardados | Fichas dos 22 capítulos preenchidas, sem prosa | Três páginas no ar, navegação entre elas |

**Entregável:** o portal navegável e um retrato honesto do ponto de partida. Os cinco
artefatos do diagnóstico ficam guardados para comparação no fim do segundo ano.

---

## Fase 1 · A fundação que falta
**Meses 1 a 6 · Teoria: 1.4 e 2.1 · Prática: Trilha 1**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 1 — Skiena como espinha; CSAPP e OSTEP de apoio; interpretador como projeto | **1.4 Cognição e metacognição** e **2.1 Paradigmas de programação** | Migração para Astro com o schema Zod da ficha; a compilação passa a falhar sem data de revisão |

Por que estes dois capítulos, e não os da Camada 1: o 1.1 e o 1.2 já estão escritos, e o
que a trilha de fato destrava é outra coisa. O 1.4 se apoia direto no *The Programmer's
Brain*, lido na trilha; e o 2.1 exige a experiência de escrever um interpretador para falar
de paradigmas sem repetir manual.

**Marco:** prever por escrito onde uma função sua quebra por volume, e acertar.

---

## Fase 2 · Dados e sistemas distribuídos
**Meses 7 a 12 · Teoria: 2.2 e 2.3 · Prática: Trilha 2**

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
**Meses 13 a 18 · Teoria: 3.1 e 1.5 · Prática: Trilha 3**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 3 — Ousterhout como espinha; Fowler, Evans, Feathers e Newman de apoio; estrangulamento do legado VB6 como projeto | **3.1 Arquitetura de software** e **1.5 Comunicação e escrita técnica** | Grafo de pré-requisitos e matriz de dependências |

Aqui a integração fica mais evidente: os três ADRs exigidos pela trilha 3 são o material
bruto do capítulo 1.5. Você escreve sobre escrita técnica tendo acabado de praticá-la sob
pressão de um sistema real.

**Marco:** um arquiteto que não conhece o sistema reconstrói sua decisão lendo só os ADRs.

---

## Fase 4 · Qualidade e testes
**Meses 19 a 22 · Teoria: 3.3 · Prática: Trilha 4**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 4 — Khorikov como espinha; Beck, Freeman & Pryce, Fowler de apoio; caracterização de legado como projeto | **3.3 Qualidade, testes e débito técnico** | Linha do tempo 1847–2026, ancorada nas quatro fases |

**Marco:** você defende com dados do próprio projeto a forma da sua pirâmide de testes — e
sabe apresentar o argumento contrário, que é o que 3.3.6 exige.

---

## Fase 5 · Plataforma, confiabilidade e segurança
**Meses 23 a 26 · Teoria: 4.1 e 4.2 · Prática: Trilha 5**

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
**Meses 27 a 32 · Teoria: 2.4, 2.5, 2.6 e 3.2 · Prática: Trilha 6, contínua**

| Estudo | Livro | Portal |
|---|---|---|
| Trilha 6 em regime contínuo — Brooks, DeMarco & Lister, Larson | **2.4 Linguagens**, **2.5 Requisitos e IHC**, **2.6 Carreira**, **3.2 Processos** | Verificação de todas as fontes primárias, com checagem de link na CI |

Quatro capítulos que dependem menos de estudo novo e mais de organizar o que você já viveu
— trinta anos de linguagens, requisitos mal levantados, transições de carreira e a
travessia do RUP ao ágil dentro de banco.

---

## Fase 7 · A camada contextual
**Meses 33 a 36 · Teoria: 3.4 a 3.7 · Prática: pesquisa de fonte primária**

| Estudo | Livro | Portal |
|---|---|---|
| Pesquisa de fonte primária: DCN e SBC, legislação, dados de mercado | **3.4 Ética e legislação**, **3.5 Ensino formal**, **3.6 Contexto brasileiro**, **3.7 Economia da decisão** | Bibliografia completa e revisão de frescor de tudo escrito antes |

É a fase mais brasileira do livro e a que mais depende de fonte verificável. Deixá-la para
o fim é deliberado: exige mais rigor de citação do que de leitura técnica, e é o tipo de
trabalho que se faz melhor com o resto do argumento já de pé.

---

## Fase 8 · O capítulo perecível e o fechamento
**Meses 37 a 39 · Teoria: 4.3 · Prática: revisão e publicação**

| Estudo | Livro | Portal |
|---|---|---|
| — | **4.3 IA no ciclo de desenvolvimento**, escrito por último | Geração de PDF e EPUB; versão 1.0 |

O capítulo mais volátil do livro é escrito na última janela possível, com meia-vida
declarada de um a dois anos e data de revisão já marcada na ficha. É a única forma
honesta de publicá-lo.

---

## Conceito e prática, lado a lado

A linha do tempo diz *quando*. Esta tabela diz *o que corresponde a quê* — o capítulo do
livro à esquerda, a exigência prática que o sustenta à direita.

| No livro | Na prática |
|---|---|
| **1.1 a 1.3 — Fundação e invariantes.** Os alicerces que sobrevivem a mudanças de paradigma: Conway, Lehman, Brooks, Parnas, e o critério que separa o perene do que só parece. | **Trilha 1 — a base cognitiva.** Os dez atemporais lidos antes do avanço técnico, e um interpretador escrito do zero como prova de que a fundação é operacional, não decorativa. |
| **1.4 — Cognição e metacognição.** Carga cognitiva, níveis de abstração, depuração como método científico, a habilidade de desaprender. | **Trilha 1 — o marco.** Prever por escrito em que volume uma função real quebra, e conferir a previsão contra a medição. |
| **2.2 e 2.3 — Dados e sistemas distribuídos.** As regras duradouras de persistência e rede, com o CAP lido como ele é e o "exactly-once" desmontado. | **Trilha 2 — engenharia de resiliência.** Um serviço com dependência instável: idempotência, backoff, circuit breaker, e um teste de partição que confirma o comportamento previsto. |
| **3.1 — Arquitetura de software.** A evolução dos sistemas, do monolito ao estrangulamento de legado, com a decisão registrada em ADR. | **Trilha 3 — refatoração estrutural.** Estrangular uma capacidade do legado VB6/Sybase, com fachada, coexistência, caminho de volta e três ADRs. |
| **3.3 — Qualidade e débito técnico.** A degradação inevitável, a definição de Feathers, e a cobertura tratada como armadilha e não como meta. | **Trilha 4 — ação corretiva.** Cobrir um módulo antigo com testes de caracterização até poder refatorá-lo, e defender a forma da própria pirâmide com dados. |
| **4.1 e 4.2 — Segurança, plataforma e confiabilidade.** A operação como disciplina: SLI, SLO, orçamento de erro, cadeia de suprimentos, post-mortem sem culpado. | **Trilha 5 — simulação e processo.** SLO publicado, falha controlada executada, e um post-mortem escrito sobre o processo, sem nomes. |
| **1.5 — Comunicação e escrita técnica.** A escrita como artefato de engenharia: ADR, RFC, Diátaxis, diagramas que explicam. | **Trilha 6 — influência contínua.** A escrita como exercício perpétuo, com o marco de maturidade sendo um texto seu citado por quem você não conhece. |
| **2.6 — Comportamento e carreira.** A gestão do envelhecimento da própria carreira, e por que comportamento é infraestrutura. | **Trilha 6 — o projeto.** O próprio livro: ele consome as cinco trilhas anteriores e é a prova de que elas aconteceram. |

A leitura da tabela nos dois sentidos é deliberada. Da esquerda para a direita, ela diz o
que estudar para poder escrever. Da direita para a esquerda, diz o que se está de fato
aprendendo ao executar cada projeto — e é essa direção que sustenta a regra de abertura.

## O quadro completo

| Fase | Meses | Trilha | Capítulos escritos | Acumulado |
|---|---|---|---|---|
| 0 | 0–0,5 | 0 | — (fichas) | 4 de 22 |
| 1 | 1–6 | 1 | 1.4, 2.1 | 6 |
| 2 | 7–12 | 2 | 2.2, 2.3 | 8 |
| 3 | 13–18 | 3 | 3.1, 1.5 | 10 |
| 4 | 19–22 | 4 | 3.3 | 11 |
| 5 | 23–26 | 5 | 4.1, 4.2 | 13 |
| 6 | 27–32 | 6 | 2.4, 2.5, 2.6, 3.2 | 17 |
| 7 | 33–36 | pesquisa | 3.4, 3.5, 3.6, 3.7 | 22 |
| 8 | 37–39 | — | 4.3 + revisão | 22 + v1.0 |

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

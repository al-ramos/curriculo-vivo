# Currículo Vivo — Índice v3
## Engenharia de Software: Envelhecimento Macro

> Classificação por **velocidade de envelhecimento**, eixo único. O assunto de cada
> capítulo (técnico, humano, contextual) é etiqueta na ficha, não divisão estrutural.
> Numeração decimal, sem letras. 21 capítulos, ~160 seções.
> URL canônica de cada capítulo é um slug estável; o número é apenas exibição.

| Camada | Meia-vida | Capítulos | Fatia do livro |
|---|---|---|---|
| **0 · A Lente** | — | 1 | instrumento |
| **1 · Permanente** | sem erosão observada | 5 | 24% |
| **2 · Geracional** | 15–20 anos | 6 | 29% |
| **3 · Cíclico** | 5–15 anos | 7 | 33% |
| **4 · Sazonal** | 1–5 anos | 3 | **14%** |

O último número é o achado da reclassificação: apenas três dos vinte e um capítulos são
de fato perecíveis. A ansiedade que o mercado produz se concentra em 14% do currículo.

---

# CAMADA 0 — A LENTE

## 0 · Como ler este livro
`/como-ler` · *o instrumento de leitura das camadas 1 a 4*

- **0.1** O modelo em quatro fases — Emergência → Consolidação → Erosão → Arqueologia
- **0.2** As quatro camadas — e por que a classificação é por velocidade, não por assunto
- **0.3** A ficha de envelhecimento — o instrumento que torna o currículo auditável
- **0.4** A armadilha do currículo estático
- **0.5** O professor como arqueólogo e futurista
- **0.6** Três modos de leitura: aluno, professor, profissional em transição

---

# CAMADA 1 — PERMANENTE
*Sem erosão observada em nenhum ciclo tecnológico da disciplina*

Cognição e escrita técnica sobem para cá, vindas do antigo bloco "humano". O livro já
afirmava que aprender a aprender supera qualquer framework; agora a estrutura concorda
com o argumento.

## 1.1 · Fundação conceitual
`/fundacao` · *etiquetas: técnico, teórico*

- **1.1.1** Pensamento lógico e abstração
- **1.1.2** Matemática subjacente — lógica, discreta, grafos, probabilidade, complexidade
- **1.1.3** Computabilidade e limites — Turing, problema da parada, indecidibilidade
- **1.1.4** Princípios universais de engenharia — trade-off, restrição, margem, modo de falha
- **1.1.5** O evento que fundou a disciplina — NATO 1968 e a "crise do software"
- **1.1.6** O que 1968 já sabia e nós ainda não resolvemos

## 1.2 · Os invariantes nomeados
`/invariantes` · *etiquetas: técnico, teórico*

- **1.2.1** Lei de Conway — a arquitetura imita a estrutura de comunicação
- **1.2.2** Leis de Lehman — mudança contínua e complexidade crescente
- **1.2.3** Brooks — mítico homem-mês, ausência de bala de prata, essencial vs. acidental
- **1.2.4** Parnas — ocultação de informação; decompor por decisão de projeto
- **1.2.5** Entropia de software
- **1.2.6** Acoplamento e coesão como estrutura, não estilo
- **1.2.7** O custo da mudança tardia — a curva de Boehm e a controvérsia sobre a evidência
- **1.2.8** O que isso significa para o professor

## 1.3 · O teste de perenidade
`/perenidade` · *etiquetas: teórico, meta*

- **1.3.1** O critério: sobreviver a três rupturas de paradigma independentes
- **1.3.2** Os três eixos de ruptura — hardware, escala, modelo de custo
- **1.3.3** O cemitério dos falsos invariantes — OO universal, SOLID como lei, pirâmide de
  testes, requisitos congelados, UML como documentação viva, "a nuvem é mais barata"
- **1.3.4** Como o leitor deve duvidar deste livro

## 1.4 · Cognição e metacognição
`/cognicao` · *etiquetas: humano, cognitivo*

- **1.4.1** Carga cognitiva e os limites da memória de trabalho
- **1.4.2** Os quatro níveis de abstração
- **1.4.3** Debugging como método científico — hipótese, experimento, bisseção
- **1.4.4** A meta-habilidade de aprender e desaprender
- **1.4.5** Modelos mentais e transferência entre tecnologias
- **1.4.6** Por que isso supera qualquer linguagem ou framework
- **1.4.7** Prática deliberada e o platô do profissional intermediário

## 1.5 · Comunicação e escrita técnica
`/escrita` · *etiquetas: humano, prática*

- **1.5.1** Escrita como artefato de engenharia
- **1.5.2** ADR, RFC e documento de proposta de design
- **1.5.3** Documentação que sobrevive — README, runbook, o modelo Diátaxis
- **1.5.4** Diagramas que explicam (modelo C4) e diagramas que enfeitam
- **1.5.5** Comunicação assíncrona em time distribuído
- **1.5.6** Apresentar decisão técnica para quem não é técnico

---

# CAMADA 2 — GERACIONAL
*Meia-vida de 15 a 20 anos*

## 2.1 · Paradigmas de programação
`/paradigmas` · *etiquetas: técnico*

- **2.1.1** Imperativo e procedural
- **2.1.2** Orientação a objetos — o que sobrou depois da crítica dos anos 2010
- **2.1.3** Funcional — da academia ao mainstream por absorção, não por substituição
- **2.1.4** Reativo e assíncrono
- **2.1.5** Orientado a eventos
- **2.1.6** Tipagem como paradigma transversal — estática, dinâmica, gradual
- **2.1.7** Concorrência e paralelismo — threads, atores, CSP, async/await

## 2.2 · Dados e persistência
`/dados` · *etiquetas: técnico*

- **2.2.1** Modelagem relacional e normalização
- **2.2.2** Transações, ACID e níveis de isolamento
- **2.2.3** O movimento NoSQL — o que era hype e o que ficou
- **2.2.4** Modelos além do relacional — documento, chave-valor, grafo, colunar, série temporal
- **2.2.5** Consistência, replicação e CAP — o teorema mais mal citado da computação
- **2.2.6** OLTP vs. OLAP; warehouse, lake, lakehouse
- **2.2.7** Migração e versionamento de esquema
- **2.2.8** *Do campo:* bases críticas em Sybase e SQL Server em produção contínua

## 2.3 · Sistemas distribuídos: fundamentos
`/distribuidos` · *etiquetas: técnico*

Separado de Arquitetura de propósito: o fundamento é geracional, a arquitetura é cíclica.
Misturar os dois é o mecanismo que faz currículo envelhecer mal.

- **2.3.1** As oito falácias da computação distribuída
- **2.3.2** Latência e throughput — as ordens de grandeza que todo dev deveria saber de cor
- **2.3.3** Falha parcial: timeout, retry, backoff, idempotência
- **2.3.4** Relógios, ordenação, quórum e consenso
- **2.3.5** Garantias de entrega — at-most-once, at-least-once e o mito do exactly-once
- **2.3.6** Padrões de resiliência — circuit breaker, bulkhead, backpressure
- **2.3.7** Por que este capítulo é geracional e o 3.1 é cíclico

## 2.4 · Linguagens de programação
`/linguagens` · *etiquetas: técnico*

Fica aqui, e não na camada sazonal, por um motivo que vira conteúdo do capítulo:
linguagens individuais envelhecem rápido, mas **o padrão pelo qual envelhecem** é estável
há cinquenta anos.

- **2.4.1** Linha do tempo por geração (1ª a 6ª)
- **2.4.2** O padrão de envelhecimento — adoção, platô, nicho, manutenção
- **2.4.3** Por que COBOL não morreu, e o que isso ensina sobre o resto
- **2.4.4** Ecossistema e gerenciador de pacotes decidem mais que sintaxe
- **2.4.5** Runtimes e interoperabilidade — JVM, CLR, WASM
- **2.4.6** Como escolher uma linguagem sem escolher uma moda

## 2.5 · Requisitos, produto e IHC
`/requisitos` · *etiquetas: humano, produto*

- **2.5.1** Levantamento e descoberta — o problema atrás do pedido
- **2.5.2** Requisito funcional, não funcional e atributo de qualidade
- **2.5.3** Histórias, critérios de aceite e a fronteira com teste
- **2.5.4** Fundamentos de IHC e usabilidade — heurísticas de Nielsen
- **2.5.5** Acessibilidade (WCAG) e internacionalização como requisito, não retrofit
- **2.5.6** Pesquisa com usuário para quem não é designer
- **2.5.7** Por que quem entende o negócio envelhece mais devagar

## 2.6 · Comportamento e carreira
`/carreira` · *etiquetas: humano*

- **2.6.1** Por que comportamento é infraestrutura
- **2.6.2** Competências — colaboração, conflito produtivo, feedback
- **2.6.3** Autonomia, propriedade e senioridade — o que o mercado de fato compra
- **2.6.4** Trilha técnica vs. gestão, e o mito da escada única
- **2.6.5** A transição de carreira e a reinvenção por década
- **2.6.6** Síndrome do impostor e obsolescência percebida
- **2.6.7** O envelhecimento do comportamento — de 1990 a 2026, remoto e assíncrono

---

# CAMADA 3 — CÍCLICO
*Meia-vida de 5 a 15 anos · onde mora a maior parte do que se ensina hoje no Brasil*

## 3.1 · Arquitetura de software
`/arquitetura` · *etiquetas: técnico*

- **3.1.1** Monolito — e a redescoberta do monolito modular
- **3.1.2** Camadas, hexagonal, ports & adapters, Clean Architecture
- **3.1.3** SOA e o legado do ESB
- **3.1.4** Microsserviços — promessa, custo real, e quando **não** usar
- **3.1.5** Serverless e computação de borda
- **3.1.6** Event-driven, CQRS e Event Sourcing
- **3.1.7** Estrangulamento de legado (Strangler Fig) e migração incremental
- **3.1.8** ADR — decisão arquitetural como documento versionado
- **3.1.9** Team Topologies — a arquitetura da organização é a do sistema
- **3.1.10** O pêndulo centralizar ↔ distribuir: por que a indústria oscila a cada década

## 3.2 · Processos e metodologias
`/processos` · *etiquetas: humano, organizacional* · **estado: erosão**

- **3.2.1** A era pré-metodológica — code and fix
- **3.2.2** Waterfall — o que Royce realmente escreveu, e a ironia de ter fundado o que criticava
- **3.2.3** Processos pesados — RUP, CMMI e o MPS.BR
- **3.2.4** A era ágil — manifesto, XP, Scrum, Kanban
- **3.2.5** Escala — SAFe, LeSS e o mito do "modelo Spotify"
- **3.2.6** Pós-ágil — fluxo, produto, descoberta contínua, agile washing
- **3.2.7** Estimativa, #NoEstimates e a política das estimativas
- **3.2.8** *Do campo:* ágil dentro de janela de GMUD em ambiente bancário

## 3.3 · Qualidade, testes e débito técnico
`/qualidade` · *etiquetas: técnico, prática*

- **3.3.1** Evolução do conceito de qualidade — conformidade → adequação ao uso → experiência
- **3.3.2** Débito técnico — a metáfora de Cunningham e o que ela virou como desculpa
- **3.3.3** Os quadrantes de débito; dívida versus desleixo
- **3.3.4** Código legado — a definição de Feathers: legado é código sem teste
- **3.3.5** Testes: de fase final a cultura — TDD, BDD
- **3.3.6** Pirâmide, trophy, honeycomb — uma disputa em aberto, não um consenso
- **3.3.7** Cobertura como métrica e como armadilha
- **3.3.8** DORA Metrics e SPACE — e os limites de medir produtividade
- **3.3.9** Refatoração como prática contínua, não projeto

## 3.4 · Ética, legislação e impacto
`/etica` · *etiquetas: humano, contextual*

- **3.4.1** Por que ética não é optativa
- **3.4.2** Legislação que afeta a arquitetura — LGPD, GDPR, privacidade por design
- **3.4.3** Marco Civil da Internet e regime de responsabilidade
- **3.4.4** Ética em IA — viés, explicabilidade, atribuição, deslocamento de trabalho
- **3.4.5** Green software e o custo ambiental da computação
- **3.4.6** Software em domínio regulado — financeiro, saúde, setor público
- **3.4.7** O envelhecimento da ética em TI — o que era aceitável e deixou de ser

## 3.5 · O ensino formal
`/ensino` · *etiquetas: contextual, pedagógico*

- **3.5.1** O núcleo histórico permanente das grades
- **3.5.2** Disciplinas que amadureceram e viraram base
- **3.5.3** Disciplinas que estão surgindo
- **3.5.4** As DCN e o Currículo de Referência da SBC — o obrigatório e o eletivo
- **3.5.5** ENADE e o efeito da avaliação sobre o que se ensina
- **3.5.6** A lacuna persistente — produção, operação, legado e trabalho em time
- **3.5.7** Bootcamp, graduação e certificação: o que cada um entrega de fato

## 3.6 · Contexto brasileiro
`/brasil` · *etiquetas: contextual*

- **3.6.1** Da reserva de mercado (1984) à abertura
- **3.6.2** Lei de Informática, Lei do Bem e mecanismos de fomento
- **3.6.3** Universidades brasileiras e a pesquisa em Engenharia de Software
- **3.6.4** O profissional brasileiro no mercado global — nearshore e o efeito câmbio
- **3.6.5** PJ vs. CLT e a estrutura de contratação do setor
- **3.6.6** Desafios estruturais — evasão, inglês, acesso, concentração regional
- **3.6.7** Legado como setor econômico — bancos, governo, COBOL e VB6 vivos em 2026
- **3.6.8** Tendências positivas

## 3.7 · Economia da decisão
`/economia` · *etiquetas: contextual, gestão*

- **3.7.1** Toda decisão técnica é uma decisão de custo
- **3.7.2** FinOps — custo por requisição, por time, por funcionalidade
- **3.7.3** Build vs. buy vs. open source
- **3.7.4** Custo total de propriedade e o custo de sair — lock-in
- **3.7.5** Eficiência energética como restrição de projeto
- **3.7.6** Como justificar refatoração em linguagem de negócio

---

# CAMADA 4 — SAZONAL
*Meia-vida de 1 a 5 anos · 14% do livro · nenhuma ferramenta sem o princípio que sobrevive a ela*

## 4.1 · Segurança e cadeia de suprimentos
`/seguranca` · *etiquetas: técnico, prática* · meia-vida ~4 anos

- **4.1.1** Por que segurança deixou de ser fase final
- **4.1.2** Modelagem de ameaças (STRIDE) e superfície de ataque
- **4.1.3** OWASP Top 10 como currículo mínimo
- **4.1.4** SAST, DAST e SCA — o que cada um pega e o que não pega
- **4.1.5** Segredos, rotação e gestão de identidade
- **4.1.6** Cadeia de suprimentos — dependências, SBOM, assinatura de artefato
- **4.1.7** Shift left e a fadiga de alerta
- **4.1.8** *Do campo:* SonarQube e Veracode dentro de pipeline corporativo

## 4.2 · Ferramentas e infraestrutura
`/ferramentas` · *etiquetas: técnico, prática* · meia-vida 2–5 anos

- **4.2.1** Controle de versão — de CVS a Git; trunk-based vs. GitFlow
- **4.2.2** Infraestrutura — bare metal → VM → contêiner → orquestração → serverless
- **4.2.3** Infraestrutura como código e a ideia de declaratividade
- **4.2.4** CI/CD — integração contínua, entrega, deploy; pipeline como código
- **4.2.5** Estratégias de release — blue-green, canário, feature flag
- **4.2.6** Observabilidade — logs, métricas, traces; SLI, SLO e error budget
- **4.2.7** SRE — operação como disciplina de engenharia
- **4.2.8** Post-mortem sem culpado
- **4.2.9** Plataforma interna como produto — platform engineering
- **4.2.10** O que sobra quando a ferramenta morre — o princípio por trás de cada uma

## 4.3 · IA no ciclo de desenvolvimento
`/ia` · *etiquetas: técnico, humano* · **volátil: meia-vida 1–2 anos**

- **4.3.1** Por que este é o capítulo mais perecível do livro — e por que isso é honesto
- **4.3.2** Assistentes de código — ganho real, dívida oculta, efeito sobre a formação do júnior
- **4.3.3** O deslocamento da habilidade: de escrever para especificar e revisar
- **4.3.4** Revisão de código gerado — a nova competência crítica
- **4.3.5** LLM como componente de sistema — RAG, avaliação, custo, não-determinismo
- **4.3.6** LLMOps — versionamento de prompt, eval, guardrail, observabilidade
- **4.3.7** O que a IA não deslocou — os invariantes da Camada 1, um a um
- **4.3.8** O risco pedagógico: o atalho que remove o atrito que ensina

---

# APÊNDICES
*Gerados a partir do conteúdo, nunca escritos à mão — é isso que os mantém corretos*

| Apêndice | Fonte |
|---|---|
| Linha do tempo 1847–2026 | `dados/timeline.yml`, ancorada nas quatro fases de 0.1 |
| Glossário vivo | Frontmatter das seções + estado por verbete |
| Arco do aluno — ano 1 a 4 | Derivado de pré-requisitos e objetivos |
| Matriz de pré-requisitos | Campo `prerequisitos` de todas as fichas |
| Radar de frescor | Campos `ultima_revisao` e `revisar_em` |
| Bibliografia | Campo `fontes`, com verificação de link na CI |

---

# NOTAS DE VERSÃO

**v3 (01/09/2026) — reclassificação por eixo único.** Blocos A/B/C/D substituídos por
quatro camadas de velocidade; assunto vira etiqueta. Numeração decimal, sem letras.
Cognição e Escrita técnica sobem para Permanente. Linguagens desce de sazonal para
geracional, com a justificativa incorporada ao capítulo. Slug estável por capítulo, para
que renumerações futuras não quebrem links — um livro sobre envelhecimento não pode ter
URL que apodrece.

**v2 (01/09/2026) — enriquecimento.** De ~60 para ~160 seções. Sete capítulos novos:
teste de perenidade, dados e persistência, sistemas distribuídos, segurança e cadeia de
suprimentos, IA no ciclo de desenvolvimento, requisitos/produto/IHC, comunicação e escrita
técnica, economia da decisão. Invariantes nomeados um a um. Postura editorial nova:
fonte obrigatória em afirmação datada, controvérsias apresentadas como controvérsias,
seções "do campo" em primeira pessoa.

**v1** — índice original em quatro blocos e quatorze camadas.

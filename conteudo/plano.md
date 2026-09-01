# Plano — "Engenharia de Software: Envelhecimento Macro"
### Currículo vivo · v2 de arquitetura de conteúdo, stack e publicação
Documento de planejamento — 01/09/2026. Nada implementado ainda.

---

## 1. A ideia que amarra tudo

O livro afirma que o conhecimento envelhece em velocidades diferentes. Se o próprio
livro for um artefato estático, ele se refuta. Então a decisão central do projeto é:

> **A metadata de envelhecimento não é um enfeite editorial — é um schema validado no
> build, e a CI falha (ou abre issue) quando um capítulo vence.**

Tudo abaixo é consequência disso.

---

## 2. Arquitetura de conteúdo — v2

Mudanças em relação ao índice atual, com justificativa:

| Movimento | Justificativa |
|---|---|
| Meta-teoria (ex-C13) sai do fim e vira **Parte 0** | É a lente de leitura das 14 camadas. Hoje o leitor só entende o critério de organização na última parte. |
| Numeração passa a ser **por bloco** (A1, B1, C1, D1) | C10 no bloco D, C11 no C e C14 no A tornam o sumário imprevisível. |
| **Qualidade e débito técnico** migra de D para B | Débito técnico é conhecimento técnico de envelhecimento lento, não contexto. |
| **Disciplinas e ensino** migra de C para D | "O que as universidades ensinam" varia por país e década — é contextual, não humano. |
| **Sistemas distribuídos** vira camada própria, separada de Arquitetura | O fundamento (latência, particionamento, consistência) é lento; a arquitetura (microsserviços, serverless) é rápida. Misturar os dois é o erro que faz currículo envelhecer. |
| **Cognição** passa à frente de Comportamento no bloco C | É pré-requisito: aprender a aprender antecede carreira. |

### Estrutura proposta

**Parte 0 — Como ler este livro**
- 0.1 O modelo em quatro fases · 0.2 Velocidades e meia-vida · 0.3 A ficha de envelhecimento
- 0.4 A armadilha do currículo estático · 0.5 O professor como arqueólogo e futurista

**Bloco A — Invariantes** *(o que é eterno)*
- A1 Fundação conceitual — lógica, abstração, matemática subjacente, NATO 1968
- A2 Os invariantes nomeados — **precisa listar**: Conway, leis de Lehman, Brooks
  (não há bala de prata), Parnas (ocultação de informação), complexidade essencial
  vs. acidental, entropia de software
- A3 **[novo]** O teste de perenidade — critério falsificável: sobreviveu a N mudanças
  de paradigma de hardware / linguagem / escala. Sem isso, "eterno" é opinião.

**Bloco B — Técnico** *(ordenado do mais lento ao mais rápido)*
- B1 Paradigmas de programação
- B2 **[novo]** Dados e persistência — modelagem, transações, consistência
- B3 **[novo]** Sistemas distribuídos: fundamentos
- B4 Arquitetura de software
- B5 Processos e metodologias
- B6 Qualidade, testes e débito técnico *(ex-C10)*
- B7 **[novo]** Segurança e cadeia de suprimentos — AppSec, SAST/DAST, segredos, SBOM
- B8 Ferramentas e infraestrutura — CI/CD, observabilidade
- B9 Linguagens de programação
- B10 **[novo]** IA no ciclo de desenvolvimento — hoje é o maior vetor isolado de
  obsolescência curricular e está reduzido a um subtópico de ética

**Bloco C — Humano**
- C1 Cognição e metacognição · C2 Comportamento e carreira
- C3 **[novo]** Requisitos, produto e IHC *(IHC hoje só existe no glossário)*
- C4 **[novo]** Comunicação e escrita técnica como artefato de engenharia
- C5 Ética, legislação e impacto

**Bloco D — Contextual**
- D1 O ensino formal *(ex-C7)* — ancorar nas DCN e no Currículo de Referência da SBC
- D2 Contexto brasileiro — reserva de mercado e Lei de Informática (1984), fomento,
  ENADE, PJ vs. CLT, nearshore, bootcamps, êxodo de talento
- D3 **[novo]** Economia da decisão — custo, FinOps, sustentabilidade *(absorve Green Software)*

**Apêndices gerados automaticamente do conteúdo** (não escritos à mão):
linha do tempo, glossário vivo com estado por verbete, matriz de pré-requisitos,
radar de frescor, bibliografia.

---

## 3. A ficha de envelhecimento (schema obrigatório por camada e subtópico)

```yaml
id: B5.4
bloco: B
titulo: "Era Ágil"
objetivos:            # verificáveis, verbo de ação
  - "Distinguir prática ágil de ritual ágil em um caso real"
prerequisitos: [B5.2, A2]
avaliacao: "Auditar um time real contra os 4 valores; entregar 1 página"
velocidade: medio     # invariante | lento | medio | rapido | volatil
meia_vida_anos: 8
estado: em_erosao     # emergente | consolidado | em_erosao | obsoleto
ultima_revisao: 2026-09-01
revisar_em: 2027-03-01
gatilhos:             # o que força revisão antes da data
  - "Novo State of Agile / DORA report"
  - "Mudança de posição de signatário do manifesto"
fontes: [...]         # toda afirmação histórica com fonte
```

Um Zod schema no Astro torna esses campos **obrigatórios**: se faltar `revisar_em`,
o build quebra. O livro passa a ser incapaz de envelhecer em silêncio.

---

## 4. Stack recomendada

**Astro 5 + Starlight**, conteúdo em MDX, deploy Cloudflare Pages via GitHub Actions.

Por quê, em vez de Next.js (que você já domina):

- **Content Collections + Zod** entregam de graça exatamente a validação da seção 3.
  Em Next/Nextra isso vira código próprio.
- Starlight já traz busca (Pagefind), tema claro/escuro, navegação lateral, i18n e
  tipografia de leitura longa — o "elegante e bonito" sai do padrão, não de CSS artesanal.
- Zero JS por padrão; ilhas React só onde houver interação (radar, grafo, glossário filtrável).
- Deploy no mesmo lugar do Radar Carreira — nenhuma stack nova de infraestrutura para você.

Complementos:
- **Ilhas React** para: Radar de Envelhecimento (dispersão velocidade × frescor),
  grafo de pré-requisitos, glossário filtrável por estado, linha do tempo interativa.
- **Tipografia**: uma serifada para corpo (leitura longa) e uma mono para código —
  a identidade visual do livro nasce da tipografia, não de gradientes.
- **PDF/EPUB**: rota `/print` + Paged.js, ou Pandoc/Typst na release. Fonte única → web + livro.

Alternativa se você preferir ficar em casa: **Next.js + Fumadocs** no Cloudflare Workers.
Bonito, mas o schema fica por sua conta.

---

## 5. Repositório e automações

`al-ramos/engenharia-software-envelhecimento`

```
content/
  partes/00-como-ler/
  blocos/a/ b/ c/ d/          # 1 arquivo .mdx por subtópico
  dados/timeline.yml
  dados/glossario.yml
src/
  content.config.ts           # Zod: a ficha de envelhecimento
  components/                 # Radar, Grafo, Glossario, Timeline
  pages/apendices/            # tudo derivado do conteúdo
.github/workflows/
  build-deploy.yml            # PR → preview; main → produção
  validar-frescor.yml         # cron mensal: abre issue por camada vencida
  qualidade.yml               # link check (lychee) + estilo pt-BR (Vale/textlint)
  release.yml                 # tag → gera PDF/EPUB e anexa à release
```

`validar-frescor.yml` é a peça que faz o livro ser vivo de fato: uma vez por mês varre
o frontmatter, compara `revisar_em` com hoje, e abre uma issue por capítulo vencido com
os gatilhos listados. O backlog de revisão do livro deixa de depender da sua memória.

Licença sugerida: conteúdo **CC BY-SA 4.0**, código **MIT**.

---

## 6. Fases

| Fase | Entrega | Escopo |
|---|---|---|
| **0** | Fundação | Repo, Astro+Starlight, schema Zod, CI de deploy, **uma camada piloto ponta a ponta** (B5 — Processos, onde você está) |
| **1** | Esqueleto vivo | Todos os ~60 subtópicos criados **só com a ficha preenchida**, sem prosa. O radar e os apêndices já funcionam. Este é o marco que prova a tese. |
| **2** | Conteúdo migrado | O que já está escrito: Bloco A, B1–B5, D1 |
| **3** | Conteúdo novo | As 7 camadas novas — prioridade B10 (IA), B7 (segurança), B2 (dados) |
| **4** | Apêndices e livro | Linha do tempo, glossário, arco do aluno, grafo; PDF/EPUB na release |

A ordem importa: **fichas antes de prosa**. Escrever capítulo por capítulo produz um
livro pela metade; preencher todas as fichas primeiro produz um mapa completo e
publicável na fase 1, que já tem valor sozinho.

---

## 7. O que mais sugiro

1. **Fonte para toda afirmação histórica.** O livro vai fazer dezenas de alegações
   datadas (1968, 1984, 2001). Campo `fontes` obrigatório no frontmatter, com link check
   na CI. É o que separa este livro de um post longo.
2. **Honestidade no Bloco A.** Aplique o teste de perenidade contra os seus próprios
   candidatos. Pirâmide de testes, SOLID e OO-como-padrão já erodiram. Um livro sobre
   envelhecimento que preserva ídolos perde autoridade na primeira resenha.
3. **Voz autoral.** O maior risco do projeto não é técnico: é a prosa homogênea de texto
   gerado. Sua trajetória — B3, Itaú, Bradesco, sustentação de legado com GMUD, VB6 vivo
   em 2026 — é a matéria-prima que nenhum modelo tem. Cada camada merece uma seção curta
   "do campo", em primeira pessoa. É o que o mercado brasileiro não encontra em outro lugar.
4. **Amarrar D1 às DCN/SBC.** Vira documento citável por coordenação de curso, não opinião.
5. **Público desde o commit 1.** Um livro sobre currículo desatualizado que nasce em repo
   privado por seis meses começa contradizendo a própria tese. Issues abertas viram revisão
   por pares gratuita.
6. **Versionar o livro como software.** SemVer + CHANGELOG: `MINOR` para camada nova,
   `PATCH` para revisão de frescor, `MAJOR` quando um invariante cai. O changelog do livro
   vira, ele mesmo, um dado sobre envelhecimento.
7. **Métrica de dogfooding.** Publique na home a idade média do conteúdo e o % de capítulos
   dentro do prazo. Um livro sobre obsolescência que mostra o próprio frescor é o argumento
   mais forte que ele pode fazer.

---

## 8. Decisões tomadas (01/09/2026)

| Decisão | Escolha |
|---|---|
| Stack | **Astro 5 + Starlight**, deploy Cloudflare Pages via GitHub Actions |
| Primeiro entregável | **Esqueleto de todas as fichas** — ~60 subtópicos só com metadata; radar e apêndices funcionando |
| Repositório | **Público desde o commit 1**; conteúdo CC BY-SA 4.0, código MIT |
| PDF/EPUB | **Depois da fase 2** — foco no site primeiro |

Consequência para a fase 0: a fundação técnica e o esqueleto de fichas viram um único
entregável. A camada piloto B5 deixa de ser marco separado e passa a ser o primeiro
subtópico com prosa, dentro da fase 2.

### Nomes e endereços definidos (01/09/2026)

| Item | Escolha |
|---|---|
| Repositório | `al-ramos/curriculo-vivo` — conceito, não descrição; sobrevive a outros volumes da série |
| Checkout local | `C:\GitHub\curriculo-vivo` — fora do OneDrive (sync corrompe worktree em sessão) |
| URL inicial | `curriculo-vivo.pages.dev` |
| Domínio alvo | `curriculovivo.dev` (US$ 9,99/ano, disponível em 01/09/2026); alternativa `curriculovivo.com` (US$ 11,25). O `.com.br` precisa ser conferido no registro.br. |
| Quando registrar | Só na fase 2, quando houver prosa publicada |

O título completo do livro vive no README e no `<title>`, não no nome do repositório.

### Pendência única antes de executar
Conectar a pasta `C:\GitHub\` (ou criá-la e conectar) pelo botão "Add folder" no app
desktop — não há `gh` no container e nenhuma pasta está conectada.

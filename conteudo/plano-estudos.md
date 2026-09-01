# Plano mestre de estudos
## Engenharia de Software — um currículo autodirigido, calibrado

---

## Antes do mapa: onde você começa

Um plano honesto tem que começar dizendo uma coisa desconfortável: **você não começa do
zero, e tratar você como iniciante custaria um ano.**

O ponto de partida real é mais de uma década em ambientes de missão crítica no mercado
financeiro, sustentação de legado com alta volumetria, ciclos de entrega com GMUD, bases
críticas em SQL Server, Oracle e Sybase, e uma migração já feita para stack moderna —
.NET 8, React com TypeScript, Terraform, GitHub Actions, contêineres em AWS. Isso não é a
base de um currículo: é a metade dele já cumprida, por experiência em vez de por livro.

Isso muda duas coisas no desenho do plano.

**A primeira é o que sai.** Não há trilha de "introdução à programação", nem de
"fundamentos de banco de dados", nem de "o que é CI/CD". Você opera essas coisas há anos.
O que falta nelas não é o conteúdo — é o vocabulário formal que permite discutir a decisão
em vez de executá-la. Isso se resolve com leitura dirigida, não com curso.

**A segunda é onde estão as lacunas de verdade.** Quem vem de sustentação de legado e
infraestrutura costuma ter uma fundação melhor do que imagina e três buracos previsíveis:
o formalismo de **algoritmos e complexidade**, que nunca foi exercitado porque o trabalho
não pedia; a teoria de **sistemas distribuídos**, que foi aprendida por sintoma e não por
princípio; e a **escrita técnica de projeto** — ADR, RFC, proposta de arquitetura —, que é
o que separa quem executa decisões de quem as toma.

Este plano ataca esses três primeiro. Se ao final do diagnóstico você discordar do
recorte, ele se reorganiza; mas comece duvidando da vontade de recomeçar do começo, que é
a armadilha mais cara de quem tem experiência e sente defasagem.

---

## Como o plano é organizado

Seis trilhas, em ordem de dependência. Cada uma tem **um livro-espinha** — o que se lê de
capa a capa — e livros de apoio, que se consultam por capítulo conforme a necessidade
aparece. Ler cinco livros em paralelo é o modo mais confiável de não terminar nenhum.

Cada trilha tem quatro elementos obrigatórios:

**Pré-requisito** — o que precisa estar de pé antes, e por quê.
**Projeto** — uma entrega concreta. Trilha sem projeto vira leitura, e leitura sem uso
evapora em seis meses.
**Marco verificável** — uma frase que você consegue provar que é verdadeira ou falsa. Não
"entendi sistemas distribuídos", mas "reproduzi uma falha de partição e o sistema degradou
como eu previ por escrito antes do teste".
**Escrita** — cada trilha termina em um texto público. É o que transforma leitura em
conhecimento defensável, e é a habilidade da trilha 6 sendo treinada desde a primeira.

### Cadência

O plano assume **6 a 8 horas por semana** — o que sobra de quem trabalha em tempo integral
sem destruir o resto da vida. Nesse ritmo, o arco completo leva de dois anos e meio a três.

Se a tentação for comprimir, comprima **escopo**, nunca cadência: três trilhas bem-feitas
valem mais que seis atropeladas, e a fundação que você pular vai reaparecer como teto
daqui a cinco anos.

| Trilha | Foco | Duração | Situação de partida |
|---|---|---|---|
| 0 | Diagnóstico | 2 semanas | — |
| 1 | A fundação que falta | 5–6 meses | lacuna real |
| 2 | Dados e sistemas distribuídos | 6 meses | lacuna real |
| 3 | Projeto e arquitetura | 6 meses | parcial |
| 4 | Qualidade, testes e refatoração | 4 meses | parcial |
| 5 | Plataforma, confiabilidade e segurança | 3–4 meses | forte |
| 6 | Escrita, influência e carreira | contínua | lacuna real |

---

## Trilha 0 · Diagnóstico
**Duas semanas. Não pule — é o que impede o plano de te ensinar o que você já sabe.**

Cinco tarefas. Cada uma revela uma lacuna específica, e o resultado reordena as trilhas
seguintes.

1. **Escreva, sem consultar nada, a diferença entre `at-least-once` e `exactly-once` na
   entrega de mensagens, e por que a segunda é discutível.** Revela a lacuna de
   distribuídos.
2. **Pegue uma consulta lenta de um sistema que você mantém, leia o plano de execução e
   explique por escrito por que o otimizador escolheu aquele caminho.** Revela a lacuna
   entre operar banco e entender banco.
3. **Implemente um cache LRU do zero, sem biblioteca, e justifique a estrutura de dados
   escolhida em termos de complexidade.** Revela a lacuna de algoritmos.
4. **Escreva um ADR de uma página sobre uma decisão técnica que você tomou nos últimos
   dois anos** — contexto, alternativas, decisão, consequências. Revela a lacuna de escrita.
5. **Descreva a arquitetura de um sistema que você mantém em um diagrama de contexto e um
   de contêineres (modelo C4).** Revela se você consegue subir o nível de abstração.

Guarde os cinco artefatos. Ao fim da trilha 3, refaça os itens 1, 4 e 5 e compare — é a
sua única medida honesta de progresso.

---

## Trilha 1 · A fundação que falta
**5 a 6 meses · pré-requisito: nenhum**

O objetivo não é passar em entrevista de algoritmos. É adquirir o vocabulário que permite
raciocinar sobre custo, e a intuição de que toda estrutura de dados é uma aposta sobre
qual operação vai ser frequente.

**Livro-espinha:** *The Algorithm Design Manual* — **Steven Skiena**. Escolhido no lugar do
CLRS de propósito: o CLRS é referência de consulta e livro de curso, denso em prova formal;
o Skiena é escrito para quem vai *usar*, tem um catálogo de problemas que funciona como
dicionário, e as "war stories" mostram o raciocínio de escolha, que é exatamente o que
falta a quem aprendeu na prática.

**Apoio:**
- *Introduction to Algorithms* — **Cormen, Leiserson, Rivest, Stein**. Consulta, não leitura.
- *Grokking Algorithms* — **Aditya Bhargava**. Se a intuição visual ajudar no arranque; é curto e honesto sobre ser uma porta de entrada.
- *Computer Systems: A Programmer's Perspective* — **Bryant & O'Hallaron**. O melhor livro para entender o que acontece embaixo do seu código: memória, cache, ligação, concorrência.
- *Operating Systems: Three Easy Pieces* — **Arpaci-Dusseau**. Gratuito e excelente. Virtualização, concorrência, persistência — os três problemas que todo sistema resolve.
- *Introduction to the Theory of Computation* — **Michael Sipser**. Leitura seletiva: os capítulos de decidibilidade e complexidade. É o que dá base ao capítulo 1.1.3 do livro.
- *The Programmer's Brain* — **Felienne Hermans**. Curto, sobre carga cognitiva e como se aprende a ler código. Encaixa direto na camada 1.4.

**Projeto:** escrever um interpretador seguindo *Crafting Interpreters* — **Robert Nystrom**
(gratuito online). É o projeto de melhor relação entre esforço e retorno que existe nesta
fase: obriga a lidar com estruturas de dados, recursão, árvores, tabelas de símbolos,
gerenciamento de memória e design de linguagem, tudo com feedback imediato.

**Marco verificável:** dada uma função de um sistema real que você mantém, você consegue
declarar a complexidade dela, apontar a estrutura de dados que a domina e prever em que
volume ela quebra — antes de medir. Depois meça e confira a previsão.

**Escrita:** um texto explicando a decisão de estrutura de dados de um trecho de código
real seu, para um público de desenvolvedores juniores.

---

## Trilha 2 · Dados e sistemas distribuídos
**6 meses · pré-requisito: trilha 1 (complexidade e concorrência)**

A trilha mais valiosa do plano para o seu perfil, e a que mais muda a conversa em uma
entrevista sênior. Você já opera sistemas distribuídos; falta o modelo mental que explica
por que eles falham do jeito que falham.

**Livro-espinha:** *Designing Data-Intensive Applications* — **Martin Kleppmann**. Se você
ler um único livro técnico nos próximos três anos, é este. Ele costura banco de dados,
replicação, particionamento, transações, consenso e processamento de fluxo em um argumento
só, e é escrito com um rigor de citação que quase nenhum livro da área tem.

**Apoio:**
- *Database Internals* — **Alex Petrov**. O andar de baixo do Kleppmann: árvores B, LSM, motores de armazenamento, protocolos de replicação.
- *SQL Performance Explained* — **Markus Winand**. Curto, direto, sobre índices e planos de execução. Retorno imediato no seu dia a dia com bases críticas.
- *Distributed Systems* — **Maarten van Steen & Andrew Tanenbaum** (gratuito). O tratado acadêmico, para quando o Kleppmann apontar um tema e você quiser o fundamento.
- *Release It!* — **Michael Nygard**. Padrões de estabilidade e antipadrões de falha, escrito por quem viu sistemas caírem. Circuit breaker, bulkhead, e o mais importante: por que os sistemas caem em cascata.
- *Streaming Systems* — **Akidau, Chernyak, Lax**, se processamento de eventos entrar no seu caminho.

**Projeto:** construir um serviço com uma dependência externa instável e provar as
garantias. Idempotência real, retry com backoff e jitter, circuit breaker, fila com
entrega ao menos uma vez, e um teste que injeta partição de rede e latência. O entregável
não é o código: é o **documento que previu o comportamento antes do teste** e o resultado
comparado.

**Marco verificável:** você consegue explicar, sem consultar, por que "exactly-once" é uma
propriedade de processamento e não de entrega — e mostrar no seu código onde a
idempotência sustenta essa afirmação.

**Escrita:** um post sobre a diferença entre o que o CAP diz e o que as pessoas citam que
ele diz.

---

## Trilha 3 · Projeto e arquitetura
**6 meses · pré-requisito: trilhas 1 e 2**

Aqui entra a parte que você já pratica sem o vocabulário formal. O risco desta trilha é o
oposto do das anteriores: excesso de literatura opinativa. A ordem abaixo é deliberada — o
Ousterhout primeiro porque é curto, contrário ao senso comum e desarma o dogmatismo dos
outros.

**Livro-espinha:** *A Philosophy of Software Design* — **John Ousterhout**. Cento e
noventa páginas sobre uma única ideia — profundidade de módulo e ocultação de informação —
que é Parnas atualizado. Discorda explicitamente de partes do *Clean Code*, e ler os dois
em sequência é o melhor exercício de julgamento arquitetural disponível.

**Apoio, em ordem de leitura:**
- *Clean Code* — **Robert C. Martin**. Leia sabendo que é contestado: os capítulos sobre nomes e funções envelheceram bem, as regras rígidas de tamanho e os exemplos, nem tanto. Vale pelo contraste com o Ousterhout.
- *Refactoring* (2ª ed.) — **Martin Fowler**. O catálogo. Consulta permanente.
- *Working Effectively with Legacy Code* — **Michael Feathers**. Para o seu caso específico, este é quase um manual de trabalho: costuras, caracterização, como testar o que não foi feito para ser testado.
- *Design Patterns* — **Gamma, Helm, Johnson, Vlissides**. Histórico e ainda útil, com a ressalva de que metade dos padrões existe para contornar limitações de linguagens dos anos 1990.
- *Patterns of Enterprise Application Architecture* — **Martin Fowler**. O vocabulário que ainda sustenta quase todo sistema corporativo.
- *Domain-Driven Design* — **Eric Evans**, e *Implementing Domain-Driven Design* — **Vaughn Vernon**. Comece pelo Vernon, que é mais prático, e volte ao Evans pelos capítulos estratégicos.
- *Fundamentals of Software Architecture* e *Software Architecture: The Hard Parts* — **Mark Richards & Neal Ford**. O segundo é o melhor livro existente sobre decomposição e trade-off explícito.
- *Building Microservices* (2ª ed.) — **Sam Newman**. Leia especialmente os capítulos sobre quando *não* usar.
- *Team Topologies* — **Matthew Skelton & Manuel Pais**. Conway aplicado. Curto.

**Projeto:** aplicar *strangler fig* em um sistema legado real — e você tem o caso ideal
em mãos, com VB6 e Sybase. Extraia **uma** capacidade para um serviço novo, com fachada,
migração de dados, coexistência e caminho de volta. Entregue com três ADRs.

**Marco verificável:** um arquiteto sênior que não conhece o sistema consegue, lendo só
os seus três ADRs, reconstruir a decisão e apontar em que condição ela estaria errada.

**Escrita:** os três ADRs, publicados.

---

## Trilha 4 · Qualidade, testes e refatoração
**4 meses · pré-requisito: trilha 3**

**Livro-espinha:** *Unit Testing: Principles, Practices, and Patterns* — **Vladimir
Khorikov**. Escolhido no lugar dos clássicos porque é o mais rigoroso sobre a pergunta que
importa — o que torna um teste valioso — e porque os exemplos são em C#, o que elimina
atrito de tradução no seu caso.

**Apoio:**
- *Test-Driven Development by Example* — **Kent Beck**. Curto, original, e diferente do TDD que se prega hoje.
- *Growing Object-Oriented Software, Guided by Tests* — **Freeman & Pryce**. O TDD de fora para dentro, com testes de aceitação guiando o desenho.
- *xUnit Test Patterns* — **Gerard Meszaros**. Consulta: o dicionário de dublês e cheiros de teste.
- *Accelerate* — **Forsgren, Humble, Kim**. A base empírica das métricas DORA, e o argumento de que qualidade e velocidade não se opõem.

**Projeto:** pegar um módulo legado sem teste algum e cobri-lo com testes de
caracterização até poder refatorá-lo com segurança. Meça antes e depois: tempo de ciclo,
taxa de falha em mudança.

**Marco verificável:** você consegue defender, com dados do seu próprio projeto, por que
sua pirâmide de testes tem a forma que tem — e sabe apresentar o argumento contrário.

**Escrita:** um texto sobre cobertura como métrica e como armadilha.

---

## Trilha 5 · Plataforma, confiabilidade e segurança
**3 a 4 meses · pré-requisito: trilha 2 · você já está forte aqui**

Trilha curta de propósito: é onde sua experiência já cobre a maior parte. O objetivo é
formalizar e preencher o que a prática não ensina — sobretudo segurança e confiabilidade
como disciplinas, não como ferramentas.

**Livro-espinha:** *Site Reliability Engineering* — **Google** (gratuito). SLI, SLO,
orçamento de erro, post-mortem sem culpado, trabalho manual como dívida.

**Apoio:**
- *Continuous Delivery* — **Jez Humble & David Farley**. O livro fundador do que você faz todo dia; vale pelo raciocínio, não pelas ferramentas.
- *The DevOps Handbook* — **Kim, Humble, Debois, Willis**.
- *Building Secure and Reliable Systems* — **Google** (gratuito). A ponte entre segurança e confiabilidade.
- *Threat Modeling* — **Adam Shostack**. STRIDE e como conduzir a sessão.
- *Security Engineering* (3ª ed.) — **Ross Anderson** (gratuito). O tratado. Consulta por capítulo.
- *Terraform: Up & Running* — **Yevgeniy Brikman**.

**Projeto:** definir SLI e SLO reais para um serviço em produção, instrumentar, e conduzir
um exercício de falha controlada com post-mortem escrito.

**Marco verificável:** existe um orçamento de erro publicado, e pelo menos uma decisão de
priorização foi tomada com base nele.

**Escrita:** o post-mortem, publicado sem nomes.

---

## Trilha 6 · Escrita, influência e carreira
**Contínua, do primeiro dia ao último**

Não é uma trilha final. É a que roda em paralelo a todas as outras, porque cada uma delas
termina em um texto.

**Livro-espinha:** *The Mythical Man-Month* — **Fred Brooks**. Cinquenta anos e continua
descrevendo a sua semana.

**Apoio:**
- *Peopleware* — **Tom DeMarco & Timothy Lister**. Sobre por que problemas de projeto quase nunca são técnicos.
- *The Pragmatic Programmer* (ed. de 20 anos) — **Hunt & Thomas**. O livro de postura profissional que mais envelheceu bem.
- *Staff Engineer* e *An Elegant Puzzle* — **Will Larson**. A trilha técnica sênior, que é a sua, descrita sem romantismo.
- *The Manager's Path* — **Camille Fournier**. Leia mesmo sem querer ser gestor: descreve o outro lado da mesa.
- *Docs for Developers* — **Bhatti, Corleissen, Lambourne, Nunez, Waterhouse**. Documentação como produto.
- *On Writing Well* — **William Zinsser**. Escrita de não ficção. O ganho por página é maior do que o de qualquer livro técnico desta lista.
- O framework **Diátaxis** (diataxis.fr) para estruturar documentação.

**Projeto:** o livro que você já está escrevendo. É o projeto desta trilha, e ele consome
tudo das outras cinco.

**Marco verificável:** um texto seu foi citado ou usado por alguém que você não conhece.

---

## Os dez atemporais

Se o tempo apertar e só couberem dez, esta é a lista — escolhida por sobreviver à mudança
de linguagem, de plataforma e de moda:

1. *Designing Data-Intensive Applications* — Kleppmann
2. *The Mythical Man-Month* — Brooks
3. *A Philosophy of Software Design* — Ousterhout
4. *The Pragmatic Programmer* — Hunt & Thomas
5. *Working Effectively with Legacy Code* — Feathers
6. *Refactoring* — Fowler
7. *The Algorithm Design Manual* — Skiena
8. *Release It!* — Nygard
9. *Site Reliability Engineering* — Google
10. *Peopleware* — DeMarco & Lister

Cinco deles têm mais de vinte anos. Isso não é acidente: é a tese do outro livro deste
portal aplicada à própria bibliografia.

---

## Seis regras que decidem se o plano funciona

**Um livro-espinha por vez.** Os de apoio existem para consulta. Cinco livros em paralelo
é o modo mais confiável de terminar nenhum.

**Nenhuma trilha sem projeto.** Leitura sem uso evapora em seis meses, e você não vai
perceber que evaporou.

**Escreva em público.** O texto no fim de cada trilha não é enfeite: é o teste de que você
entendeu. Explicar é o único jeito honesto de descobrir que não entendeu.

**Não estude camada sazonal por livro.** Ferramenta se aprende na documentação e no uso.
Livro sobre ferramenta nasce desatualizado — e o tempo dele sai do seu orçamento de
fundamentos.

**Releia.** Os livros das trilhas 3 e 6 mudam de sentido conforme sua experiência muda.
*The Mythical Man-Month* lido aos vinte anos de carreira é outro livro.

**Meça pelo marco, não pelas páginas.** Terminar um livro não é um marco. Prever um
comportamento por escrito e acertar, é.

---

## O que ficou deliberadamente de fora

**Frontend moderno em profundidade.** Você já opera React com TypeScript no nível que o
seu trabalho exige, e essa área envelhece rápido demais para investimento de fundação.

**Mobile.** Não aparece na sua trajetória nem no seu destino aparente. Entra se o destino
mudar.

**Aprendizado de máquina como campo.** O que importa para engenharia de software está na
trilha 2 e no capítulo 4.3 do livro: LLM como componente de sistema, com custo, avaliação
e não-determinismo. Formação em ML é outro currículo, não um módulo deste.

**Certificações.** Não são conhecimento; são sinalização — e sinalização tem valor real no
mercado brasileiro. Se forem necessárias, tire-as em paralelo, sem consumir o orçamento
das trilhas.

---

## Correspondência com o livro

Este plano e o *Envelhecimento Macro* são o mesmo mapa visto de dois ângulos: o livro
descreve o território, o plano descreve o percurso.

| Trilha | Capítulos correspondentes |
|---|---|
| 1 · Fundação | 1.1, 1.2, 1.4, 2.1 |
| 2 · Dados e distribuídos | 2.2, 2.3 |
| 3 · Projeto e arquitetura | 3.1, 1.2 |
| 4 · Qualidade e testes | 3.3 |
| 5 · Plataforma e segurança | 4.1, 4.2 |
| 6 · Escrita e carreira | 1.5, 2.6, 3.4 |

A camada 4 do livro — sazonal — não tem trilha própria de propósito. Ela se aprende
trabalhando, e é a única parte do currículo que não vale planejar com três anos de
antecedência.

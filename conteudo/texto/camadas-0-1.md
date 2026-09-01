# Engenharia de Software: Envelhecimento Macro
## Camadas 0 e 1 — texto integral

---

# CAMADA 0 — A LENTE
*Sem meia-vida: é o instrumento de leitura das camadas 1 a 4*

## 0.1 O modelo em quatro fases

Todo conhecimento técnico percorre o mesmo arco. Ele nasce como uma proposta esquisita
defendida por poucos, vira consenso, começa a ser questionado, e termina como assunto de
manutenção — mantido vivo não por convicção, mas por sistemas que dependem dele. Chamo
essas quatro etapas de Emergência, Consolidação, Erosão e Arqueologia.

Na **Emergência**, uma ideia aparece resolvendo um problema que a prática dominante não
resolvia. Ela é minoritária, mal documentada, e seus defensores são mais entusiastas do
que rigorosos. A literatura desse período é feita de manifestos e relatos de experiência,
não de evidência. Microsserviços em 2012, contêineres em 2014, ágil em 1999, orientação
a objetos em 1985 — todos passaram por aqui. Do ponto de vista de quem ensina, a fase de
emergência é a mais perigosa: é quando o professor sente mais pressão para atualizar a
grade, e quando tem menos base para decidir o que vai sobrar.

Na **Consolidação**, a ideia vira padrão. Surgem livros de referência, ferramentas maduras,
vagas que exigem a competência pelo nome, e — o marcador mais confiável — a ideia começa a
ser adotada por quem não a entende. É a fase em que a tecnologia é ensinada sem ressalva,
como se fosse a forma natural de fazer as coisas. Também é a fase em que o custo real
começa a aparecer, porque agora existe volume suficiente de projetos fracassados para
alguém contar a história.

Na **Erosão**, o consenso racha. Ninguém anuncia o fim; o que acontece é mais sutil.
Aparecem artigos com títulos na forma "quando não usar X". Empresas grandes publicam
relatos de migração de volta. A comunidade se divide entre quem defende a versão ortodoxa
e quem defende uma versão diluída. O vocabulário sobrevive mais que a prática: as pessoas
continuam dizendo "somos ágeis" e "usamos microsserviços" enquanto fazem outra coisa. É
aqui que mora a maior parte do conteúdo que as universidades brasileiras ensinam hoje.

Na **Arqueologia**, o conhecimento sai do centro e vira especialidade. Não desaparece — e
essa é a parte que quase todo currículo erra. COBOL não morreu; ele saiu da grade e
continuou rodando folha de pagamento. Mainframe não morreu. VB6 não morreu. O que muda é
que o conhecimento deixa de ser formação e passa a ser nicho, geralmente bem pago e mal
ensinado, sustentado por profissionais que envelhecem junto com o sistema.

Duas observações sobre o modelo, para que ele não seja usado de forma ingênua.

A primeira: **as fases não são um julgamento de qualidade**. Uma tecnologia em erosão não
é pior do que uma em emergência. Frequentemente é o contrário — ela erodiu justamente
porque foi usada o bastante para revelar limites que a novidade ainda esconde. Um
currículo que persegue apenas a fase de emergência forma profissionais que sabem o que
ainda não foi testado.

A segunda: **o arco não é irreversível**. Programação funcional passou décadas em
arqueologia acadêmica e voltou por absorção — não como paradigma dominante, mas como
conjunto de ideias incorporadas por linguagens imperativas. Monolitos foram declarados
mortos e voltaram como "monolito modular". A oscilação é frequente o bastante para merecer
nome próprio, e ela reaparece em 3.1.10 como o pêndulo entre centralizar e distribuir.

## 0.2 As quatro camadas

Se todo conhecimento envelhece, a pergunta útil não é *se*, mas *em quanto tempo*. Este
livro é organizado por essa resposta, e por nenhuma outra. Não há bloco de conteúdo
"técnico" separado de um bloco "humano": há quatro camadas de velocidade, e o assunto de
cada capítulo é uma etiqueta na ficha, não uma divisão estrutural.

A escolha é deliberada, e vale explicar o que ela custa. Classificar por assunto é mais
confortável — é como toda ementa é escrita — mas obriga a decidir se ética é um tema humano
ou contextual, e a resposta honesta é que é os dois. Classificar por velocidade obriga a uma
única decisão por capítulo, e é uma decisão que o livro precisa defender de qualquer forma.

**Camada 1 — Permanente.** Não observamos erosão em nenhum ciclo tecnológico desde que a
disciplina existe. Lógica, abstração, decomposição, a relação entre estrutura organizacional
e estrutura de sistema, a forma como uma pessoa aprende e escreve. O capítulo 1.3 existe
para submeter essa afirmação a um teste, em vez de pedir que você acredite nela.

**Camada 2 — Geracional.** Meia-vida de quinze a vinte anos. Paradigmas de programação,
fundamentos de dados, fundamentos de sistemas distribuídos, requisitos, carreira. Coisas que
mudam de vocabulário mais rápido do que mudam de substância. Quem aprendeu modelagem
relacional em 2005 continua competente em 2026; quem aprendeu uma ferramenta de ETL de 2005,
não.

**Camada 3 — Cíclico.** Meia-vida de cinco a quinze anos. Arquitetura, metodologia,
qualidade, ética aplicada, ensino, mercado, custo. Aqui a mudança é real, mas deixa legado:
quem viveu a transição do RUP para o ágil entende melhor o pós-ágil do que quem chegou já
dentro dele. É também a camada onde mora a maior parte do que se ensina hoje no Brasil.

**Camada 4 — Sazonal.** Meia-vida de um a cinco anos. Segurança, ferramentas e
infraestrutura, inteligência artificial no ciclo de desenvolvimento. É a camada que domina a
ansiedade profissional e que menos deveria dominar um currículo. Cada capítulo aqui é
escrito sob uma regra: nenhuma ferramenta é apresentada sem o princípio que sobrevive a ela.

Dentro da camada sazonal há um caso extremo que merece nome próprio. O capítulo 4.3, sobre
inteligência artificial, se declara **volátil**: meia-vida de um a dois anos. Escrever um
capítulo com prazo de validade assumido é desconfortável, e é exatamente o que este livro
está defendendo.

Vale reparar na distribuição, porque ela é o achado mais tranquilizador do livro para quem
está começando: dos **vinte e um capítulos de conteúdo** — a Camada 0 é o instrumento de
leitura, não uma matéria —, apenas **três** estão na camada sazonal. A ansiedade que o
mercado produz se concentra em algo próximo de quinze por cento do currículo. Os outros
oitenta e cinco por cento envelhecem devagar o bastante para que aprendê-los bem seja um
investimento, e não uma corrida.

A meia-vida não é um número decorativo. Ela é o que define a frequência de revisão de cada
capítulo, registrada na ficha da seção seguinte.

## 0.3 A ficha de envelhecimento

Um livro que afirma que o conhecimento envelhece, mas não diz quando cada parte dele
envelhece, é um livro que se refuta na prática. Por isso cada seção deste texto carrega
uma ficha, e a ficha não é prosa: são campos.

São eles: os **objetivos de aprendizagem**, escritos como verbos verificáveis, porque
"entender microsserviços" não é avaliável e "justificar por escrito a decisão de não usar
microsserviços em um caso dado" é; os **pré-requisitos**, que tornam explícita a ordem de
leitura e alimentam a matriz do apêndice; o **instrumento de avaliação**, porque um
currículo sem avaliação é um índice; a **velocidade** e a **meia-vida**, da seção anterior;
o **estado atual** no arco de quatro fases; a **data da última revisão** e a **data da
próxima**; os **gatilhos**, que são eventos capazes de forçar revisão antes do prazo — a
publicação de um novo relatório DORA, uma mudança de licença relevante, a saída de uma
versão que quebra compatibilidade; e as **fontes**, obrigatórias em toda afirmação datada.

O campo mais incomum é o de gatilhos, e é o mais importante. Data de revisão sozinha
produz revisão burocrática: chega o prazo, alguém relê e não muda nada. Gatilho produz
revisão quando há motivo. Um capítulo bem escrito sabe dizer o que precisaria acontecer no
mundo para que ele estivesse errado.

Quando este material for publicado como site, essas fichas deixam de ser convenção
editorial e viram schema validado na compilação: capítulo sem data de revisão não compila,
e capítulo com data vencida gera uma pendência automática. A promessa de "currículo vivo"
passa a ter um mecanismo, e não apenas uma intenção.

## 0.4 A armadilha do currículo estático

A ementa de uma disciplina universitária brasileira é aprovada em colegiado, registrada em
projeto pedagógico e revista, no melhor caso, a cada renovação de reconhecimento do curso.
O intervalo típico é de três a cinco anos. Para a camada permanente, isso é irrelevante.
Para a camada sazonal, é a diferença entre ensinar a prática vigente e ensinar arqueologia
sem avisar ao aluno que é arqueologia.

A armadilha não está no atraso. Está na **ausência de sinalização do atraso**. Um aluno
que aprende uma ferramenta descontinuada sabendo que ela está descontinuada aprendeu
história da computação, o que é legítimo e útil. O mesmo aluno, aprendendo a mesma
ferramenta como se fosse prática corrente, aprendeu algo pior do que nada: aprendeu um
mapa errado do território, e vai levar anos para descobrir.

O sintoma clássico no Brasil é a disciplina de Engenharia de Software que dedica metade da
carga a diagramas UML como artefato de documentação — não como ferramenta de pensamento,
o que ainda faz sentido, mas como entregável a ser mantido em sincronia com o código, o
que praticamente ninguém faz há quinze anos. O aluno não sai mal informado por ter
aprendido UML. Sai mal informado por não ter sido avisado de que aquilo está na fase de
erosão desde meados dos anos 2000.

A saída não é atualizar mais rápido — nenhuma estrutura acadêmica vai competir em
velocidade com o mercado, e tentar isso produz grades que perseguem moda. A saída é
**estratificar**: dizer ao aluno, para cada conteúdo, em que camada de velocidade ele está.
Um curso que ensina Kubernetes avisando que a orquestração específica tem meia-vida de
poucos anos, mas que o problema que ela resolve é permanente, forma alguém capaz de
sobreviver à próxima substituição. Um curso que ensina Kubernetes como se fosse um
invariante forma alguém que vai precisar ser resgatado.

## 0.5 O professor como arqueólogo e futurista

Ensinar tecnologia exige duas competências que raramente moram na mesma pessoa.

A primeira é **arqueológica**: saber por que as coisas são como são. Por que o Git venceu
o Subversion, por que o REST venceu o SOAP, por que o ágil surgiu como reação a algo
concreto e não como preferência estética. Sem isso, o professor transmite práticas como
arbitrariedades a serem decoradas, e o aluno não desenvolve critério — apenas repertório.
Repertório envelhece; critério, não.

A segunda é **prospectiva**: saber distinguir o que está emergindo do que está apenas
fazendo barulho. Essa competência é mais difícil e menos ensinável, e a honestidade aqui
importa: ninguém acerta consistentemente. O que se pode fazer é reduzir o erro usando
sinais — a tecnologia resolve um problema que as pessoas já tinham antes dela existir? Ela
tem adoção fora do círculo de quem a criou? Existe caso documentado de uso em escala e em
produção, não apenas em conferência? Há gente publicando sobre os limites dela, o que é
sinal de maturidade, e não de fraqueza?

O professor que só é arqueólogo forma profissionais competentes e desatualizados. O que só
é futurista forma profissionais atualizados e sem fundação, que trocam de stack a cada dois
anos sem acumular nada. As duas competências não se somam: elas se corrigem mutuamente. O
arqueólogo impede o futurista de vender moda como avanço; o futurista impede o arqueólogo
de transformar a aula em museu.

## 0.6 Três modos de leitura

Este livro tem três leitores previstos, e eles não devem lê-lo do mesmo jeito.

O **aluno** deve ler na ordem, e deve prestar atenção especial à Camada 1 e ao capítulo 1.4,
sobre cognição. A tentação natural de quem está começando é pular direto para a camada sazonal,
porque é ela que aparecem nas vagas. É um erro previsível e caro: a camada
sazonal é a única que o aluno vai ter que reaprender inteira três ou quatro vezes ao longo
da carreira, e a fundação é o que torna cada reaprendizado barato.

O **professor** deve ler primeiro a Camada 0 e o capítulo 3.5, sobre ensino formal, e depois
usar as fichas como instrumento de auditoria da própria ementa. A pergunta operacional é:
quanto da minha carga horária está em conteúdo sazonal, e esse conteúdo está
sinalizado como tal para o aluno?

O **profissional em transição** — e este é o leitor mais numeroso no Brasil de 2026 — deve
ler pelo diagnóstico. Vá ao apêndice de radar, identifique em que camadas está a sua
experiência atual, e procure as lacunas nas camadas 1 e 2, não na 4. Quem trabalha
há dez anos com sustentação de legado normalmente tem uma fundação melhor do que imagina e
uma defasagem menor do que teme; o que costuma faltar não é a ferramenta da moda, e sim
um dos capítulos geracionais que nunca foi formalizado — quase sempre 2.3, sistemas distribuídos,
ou 1.5, escrita técnica.

---

# CAMADA 1 — PERMANENTE
*Meia-vida: sem erosão observada em nenhum ciclo tecnológico da disciplina*

## 1.1 · Fundação conceitual

### 1.1.1 Pensamento lógico e abstração

Abstração é a operação de decidir o que ignorar. Essa definição, deliberadamente
desconfortável, é mais útil do que a versão de manual — "representar o essencial ocultando
o detalhe" — porque deixa explícito que abstrair é sempre uma perda deliberada de
informação, e que a qualidade de uma abstração se mede pelo que ela permite esquecer sem
consequência.

Uma boa abstração tem uma propriedade verificável: quem a usa não precisa saber o que há
embaixo para usá-la corretamente. Uma abstração ruim vaza — obriga o usuário a conhecer a
implementação para prever o comportamento. A diferença entre as duas não é estética; é
econômica, e se paga em tempo de depuração.

O pensamento lógico associado a isso é menos glamouroso do que a palavra sugere. Na prática
diária, ele se reduz a três hábitos: distinguir o que foi observado do que foi inferido;
saber o que tornaria falsa a hipótese que se está defendendo; e resistir à conclusão que
explica os fatos disponíveis mas não foi testada contra os fatos ausentes. São hábitos que
aparecem de novo em 1.4.3, quando o assunto for depuração — porque depurar é a atividade em
que a fragilidade lógica de um profissional fica mais visível.

Nada disso depende de linguagem, paradigma, década ou ferramenta. É o exemplo mais limpo
de conteúdo invariante que a disciplina tem.

### 1.1.2 Matemática subjacente

A relação entre matemática e programação é mal contada nas duas direções. Há quem diga que
programar exige matemática avançada, o que é falso para a maioria do trabalho profissional,
e há quem diga que não exige nenhuma, o que é falso de um jeito mais caro.

O que efetivamente se usa é um conjunto pequeno e estável.

**Lógica proposicional e de predicados** aparece em toda condicional, em toda cláusula
`WHERE`, em toda regra de negócio. O erro mais comum e mais caro do ofício — a negação
malfeita de uma condição composta — é um erro de lógica elementar, e ele custa horas de
produção todo mês em algum lugar do mundo.

**Matemática discreta e teoria dos conjuntos** sustentam bancos de dados relacionais de
forma tão direta que quem entende álgebra relacional escreve SQL melhor sem ter estudado
SQL a mais.

**Grafos** aparecem em dependências de build, em roteamento, em modelagem de relacionamentos,
em detecção de ciclo de importação. É a estrutura mais reutilizada e menos reconhecida da
prática.

**Probabilidade e estatística** ficaram obrigatórias com observabilidade e com sistemas
distribuídos: quem não entende a diferença entre média e percentil não sabe ler um painel
de latência, e vai otimizar o caso que não importa.

**Complexidade assintótica** importa menos do que as entrevistas sugerem e mais do que os
céticos admitem. Ninguém calcula ordens no dia a dia; mas quem não tem a intuição de que
um laço aninhado sobre uma coleção que cresce vai um dia derrubar o sistema comete esse
erro pelo menos uma vez.

O que muda ao longo das décadas é a ênfase — probabilidade ganhou peso, autômatos perderam
— mas o conjunto em si não erodiu em cinquenta anos.

### 1.1.3 Computabilidade e limites

Existe uma classe de problemas que nenhum programa resolve, em nenhuma linguagem, em
nenhum hardware, por mais tempo que se dê. Turing demonstrou isso em 1936, antes de existir
computador no sentido moderno, e a demonstração continua valendo — é provavelmente o
resultado mais robusto que a computação possui.

O caso canônico é o problema da parada: não existe programa capaz de, dado um programa
qualquer e uma entrada qualquer, decidir sempre se aquela execução termina. A consequência
prática é frequentemente subestimada. Ela é o motivo pelo qual nenhum analisador estático
pode ser simultaneamente completo e correto; por isso toda ferramenta de análise de código
escolhe entre deixar passar problemas reais ou apontar problemas inexistentes. Quando um
desenvolvedor reclama que o SonarQube "dá falso positivo", está encostando, sem saber, num
limite matemático, e não numa deficiência do produto.

Ensinar isso tem um efeito colateral valioso: alunos que sabem que existem limites teóricos
param de procurar a ferramenta perfeita e passam a escolher entre trade-offs conhecidos.
É formação de julgamento, não de repertório — e é por isso que uma disciplina de teoria da
computação, que parece a mais distante da prática, é uma das que menos envelhece.

### 1.1.4 Princípios universais de engenharia

Engenharia de software é jovem, mas engenharia não é. Alguns princípios vieram prontos das
disciplinas mais velhas e nunca precisaram ser revistos.

O primeiro é que **toda decisão é um trade-off**. Não existe escolha arquitetural sem custo;
existe escolha cujo custo ainda não apareceu. Quando alguém apresenta uma tecnologia listando
apenas benefícios, o que falta não é honestidade — é experiência com ela em produção.

O segundo é que **restrições são informação, não obstáculo**. Prazo, orçamento, equipe,
regulação e compatibilidade não atrapalham o projeto: eles o definem. Um projeto sem
restrição declarada não tem critério para escolher entre duas soluções corretas.

O terceiro é a **margem**. Nenhuma outra engenharia dimensiona um sistema para exatamente a
carga esperada; todas trabalham com folga. Software é a única disciplina em que se considera
normal dimensionar para o caso médio e descobrir o pico em produção.

O quarto é que **falha é um estado de projeto, não um acidente**. A pergunta correta nunca
foi "como impedir que falhe", e sim "como ele se comporta quando falhar". Esse princípio
reaparece inteiro em 2.3.3 e 2.3.6, e é a diferença entre um sistema distribuído que degrada
e um que desaba.

### 1.1.5 O evento que fundou a disciplina

Em outubro de 1968, cerca de cinquenta pessoas se reuniram em Garmisch, na Alemanha, numa
conferência patrocinada pelo Comitê de Ciência da OTAN. O termo escolhido para o título —
"software engineering" — foi deliberadamente provocativo: a intenção era sugerir que a
produção de software deveria se comportar como uma engenharia, e a provocação estava
justamente no fato de que ela não se comportava.

O relatório da conferência, editado por Peter Naur e Brian Randell, é um documento
desconfortável de ler hoje. Os problemas relatados são: projetos que estouram prazo e
orçamento de forma sistemática, sistemas entregues sem confiabilidade aceitável, dificuldade
de estimar, dificuldade de manter, e a percepção de que a complexidade cresce mais rápido
que a capacidade de gerenciá-la. A expressão que ficou foi "crise do software".

Duas leituras erradas circulam sobre esse evento, e vale desfazer as duas.

A primeira é que 1968 inventou a disciplina. Não inventou; nomeou. Havia software complexo
sendo feito havia mais de uma década, e o próprio diagnóstico da conferência veio da
experiência acumulada de quem já estava fracassando.

A segunda, mais interessante, é que a crise foi resolvida. Não foi. O que aconteceu foi que
a indústria aprendeu a operar dentro dela. Os números de fracasso de projeto melhoraram,
mas o padrão descrito em Garmisch — estimativa não confiável, complexidade crescente,
manutenção cara — continua reconhecível em qualquer empresa em 2026.

### 1.1.6 O que 1968 já sabia e ainda não resolvemos

Este é o teste de fogo do livro inteiro, e ele merece ser aplicado logo no começo: quanto do
diagnóstico de cinquenta e oito anos atrás ainda está aberto?

**A estimativa continua não confiável.** Todas as tentativas de resolver o problema por
método — pontos de função, COCOMO, planning poker, story points — mudaram o vocabulário sem
mudar o resultado. O movimento mais honesto da última década, o #NoEstimates, não resolveu
o problema: propôs parar de fingir que ele estava resolvido.

**A complexidade continua crescendo mais rápido que a capacidade de gerenciá-la.** Cada
geração de ferramenta reduz a complexidade acidental e a indústria imediatamente consome o
ganho aumentando o escopo. Um sistema típico de 2026 tem mais partes móveis, não menos, do
que um de 1998 — a diferença é que agora elas estão distribuídas por rede.

**A manutenção continua sendo a maior parte do custo e a menor parte do currículo.** Este é
o descompasso mais gritante entre o que a disciplina sabe desde 1968 e o que ela ensina em
2026, e é o tema do capítulo 3.5.6.

O que efetivamente melhorou foi concreto e não trivial: controle de versão, testes
automatizados, integração contínua e observabilidade tornaram o trabalho reversível e
visível. Nenhuma dessas quatro coisas reduz a complexidade — todas reduzem o custo de errar
dentro dela. É uma vitória real, e é uma vitória de natureza diferente da que Garmisch
esperava.

---

## 1.2 · Os invariantes nomeados

Um capítulo sobre invariantes que não lista invariantes é uma promessa vazia. Estes são os
candidatos, cada um com o enunciado, o que ele realmente afirma, e onde ele reaparece no
livro. O capítulo 1.3 os submete a um teste; aqui eles são apenas apresentados.

### 1.2.1 Lei de Conway

Melvin Conway, em 1968, num artigo que a *Harvard Business Review* recusou e a *Datamation*
publicou: organizações que projetam sistemas produzem projetos que copiam a estrutura de
comunicação da própria organização.

O que torna essa observação um invariante, e não uma metáfora, é que ela se sustenta
independentemente de tecnologia. Quatro times que não conversam vão produzir quatro
componentes com integração ruim, seja em COBOL nos anos 1970, em CORBA nos 1990 ou em
microsserviços em 2026. A lei não descreve uma tendência cultural; descreve uma restrição
de fluxo de informação.

A consequência prática é a chamada manobra inversa: se a estrutura do sistema vai imitar a
estrutura do time, então mudar a arquitetura sem mudar a organização é caro e geralmente
fracassa. Metade dos fracassos de migração para microsserviços que aparecem em 3.1.4 são
casos de organização inalterada. O tema volta com nome próprio em 3.1.9, Team Topologies.

### 1.2.2 As leis de Lehman

Manny Lehman, ao longo dos anos 1970 e 1980, estudou a evolução de sistemas reais ao longo
de várias versões e formulou um conjunto de leis. Duas delas bastam para o argumento deste
livro.

A **lei da mudança contínua** diz que um sistema usado em um ambiente real precisa mudar
continuamente, ou se torna progressivamente menos útil. A obsolescência não é causada por
degradação do software — bits não enferrujam — mas pelo movimento do mundo ao redor dele.
Um sistema parado num mundo em movimento fica errado sem ter mudado uma linha.

A **lei da complexidade crescente** diz que, à medida que um sistema evolui, sua
complexidade aumenta, a menos que se trabalhe deliberadamente para reduzi-la. Note a
condicional: a complexidade não cresce por fatalidade, cresce por omissão. Esse é o
fundamento teórico do que 3.3 vai chamar de refatoração contínua, e é o motivo pelo qual
"não mexer no que está funcionando" é uma estratégia que funciona até o dia em que para
de funcionar de uma vez.

Uma ressalva de honestidade intelectual: as leis de Lehman foram formuladas a partir de um
conjunto limitado de sistemas, e a base empírica é mais estreita do que a confiança com que
elas costumam ser citadas. Elas são apresentadas aqui como generalizações bem sustentadas
pela experiência, não como resultado com força de teorema.

### 1.2.3 Brooks

Fred Brooks contribuiu com três ideias que sobreviveram intactas.

O **mítico homem-mês**, de 1975: adicionar pessoas a um projeto atrasado atrasa mais o
projeto. O mecanismo é aritmético — os canais de comunicação crescem com o quadrado do
número de pessoas, e cada novo integrante consome tempo de quem já estava produzindo. Não
existe conserto tecnológico para isso; é um resultado sobre pessoas.

A **ausência de bala de prata**, de 1986: nenhuma inovação isolada produzirá uma melhoria de
uma ordem de grandeza em produtividade, confiabilidade e simplicidade dentro de uma década.
O argumento vale a pena reconstruir porque a conclusão é frequentemente citada sem ele.

Brooks separa a dificuldade de construir software em duas partes. A **complexidade
essencial** está no problema: entender o domínio, especificar o comportamento correto,
lidar com requisitos que se contradizem. A **complexidade acidental** está nas ferramentas:
gerenciar memória manualmente, escrever assembly, compilar por meia hora. A tese é que as
ferramentas só podem atacar a parte acidental, e que essa parte já havia encolhido o
bastante para que eliminá-la completamente não produzisse ganho de ordem de grandeza.

Trinta e nove anos depois, o argumento continua sendo o teste mais afiado disponível para
avaliar qualquer promessa de revolução na produtividade — inclusive, e principalmente, as
do capítulo 4.3.

### 1.2.4 Parnas

David Parnas, em 1972, respondeu a uma pergunta que parecia trivial: quando decomponho um
sistema em módulos, qual critério uso?

A resposta corrente na época era decompor por etapas de processamento — um módulo para
cada fase do fluxo. Parnas mostrou, com um exemplo trabalhado, que essa decomposição produz
módulos que mudam juntos, o que é o oposto do objetivo. E propôs outro critério: cada módulo
deve **esconder uma decisão de projeto** que pode mudar. A fronteira do módulo é o contorno
do que pode ser trocado sem afetar o resto.

Esse único artigo é a origem intelectual de encapsulamento, de interface, de API, do
princípio de inversão de dependência e da arquitetura hexagonal. Praticamente tudo em 3.1.2
é aplicação de Parnas com nomes diferentes. É provavelmente o texto de maior densidade por
página da disciplina, e a maior parte dos profissionais aplica suas conclusões sem nunca
tê-lo lido.

### 1.2.5 Entropia de software

Software não se degrada fisicamente, mas se degrada organizacionalmente. Cada alteração
feita sob pressão, cada exceção acrescentada sem revisão da estrutura, cada correção que
trata sintoma, empurra o sistema na direção de menos ordem. O efeito é cumulativo e não
tem reversão espontânea.

O que torna isso um invariante é que o mecanismo não é técnico, é econômico: a alteração
correta é sempre mais cara no curto prazo do que a alteração suficiente, e o incentivo de
quem entrega prazo é sempre o curto prazo. Mude a linguagem, a arquitetura e o processo — o
incentivo permanece. É por isso que a solução para entropia nunca foi ferramenta, e sim
prática deliberada e contínua, tema de 3.3.9.

### 1.2.6 Acoplamento e coesão

Coesão alta dentro do módulo, acoplamento baixo entre módulos. A formulação é dos anos
1970, veio da programação estruturada, e sobreviveu a toda mudança de paradigma desde então
sem alteração de conteúdo — apenas de escala.

Isso é o que a torna especialmente interessante para este livro: os mesmos dois conceitos
descrevem a relação entre funções, entre classes, entre módulos, entre serviços e entre
times. Quando alguém diz que um microsserviço "não deveria compartilhar banco com outro",
está reenunciando acoplamento. Quando alguém diz que um time deveria conseguir entregar sem
depender de outro, está reenunciando a mesma coisa em 2.6.

Um princípio que atravessa cinco ordens de grandeza sem perder validade não é uma regra de
estilo. É estrutura.

### 1.2.7 O custo da mudança tardia — e a controvérsia sobre ele

O gráfico é conhecido: o custo de corrigir um defeito cresce exponencialmente conforme ele
avança pelas fases do projeto, sendo ordens de grandeza mais caro em produção do que em
requisitos. Ele aparece em incontáveis apresentações, quase sempre atribuído a Barry Boehm,
e é o argumento padrão para justificar teste antecipado, revisão de código e "shift left".

Este livro inclui essa curva com uma ressalva importante, e a ressalva é o motivo de a
seção existir.

A base empírica original é mais estreita e mais antiga do que o uso que se faz dela. Os
dados vêm de projetos grandes, de metodologia sequencial, dos anos 1970 e 1980 — um contexto
em que o ciclo entre escrever e implantar era medido em meses. A crítica sistemática mais
conhecida a esse tipo de citação é a de Laurent Bossavit, que rastreou várias "verdades
consagradas" da engenharia de software até fontes que não sustentam a afirmação na forma
em que ela circula.

A posição defensável é intermediária. A direção do efeito é sólida e coerente com qualquer
experiência prática: defeito descoberto tarde custa mais. A magnitude específica — os
multiplicadores de 10, 100, 1000 — não tem base para ser citada como fato, e o próprio
mecanismo mudou: onde há entrega contínua, a distância entre escrever e implantar é de
minutos, e a curva que descrevia meses não se aplica sem tradução.

Manter esse caso no livro é deliberado. Ele é o exemplo mais didático disponível de um
conhecimento que envelheceu **sem que ninguém percebesse**, porque continuou sendo citado
com a mesma confiança enquanto o contexto que o gerava desaparecia.

### 1.2.8 O que isso significa para o professor

Os sete invariantes acima têm uma característica pedagógica em comum: nenhum deles é
ensinável como conteúdo isolado. Não existe aula de Lei de Conway. Eles funcionam como
lente — são apresentados uma vez, e depois aplicados repetidamente sobre o conteúdo das camadas seguintes.

Isso sugere uma estrutura de curso diferente da usual. Em vez de uma disciplina introdutória
que "passa" os princípios no primeiro semestre e nunca mais volta a eles, o mais eficaz é
retomar cada invariante toda vez que um capítulo sazonal o exemplificar. Conway aparece
quando o aluno estuda microsserviços. Parnas aparece quando ele estuda API. Brooks aparece
quando ele estuda assistentes de IA. O invariante é reforçado pelo conteúdo perecível, e o
conteúdo perecível ganha um lugar na estrutura em vez de flutuar como novidade.

É o inverso do que a maioria das grades faz, e é a recomendação central desta camada.

---

## 1.3 · O teste de perenidade

### 1.3.1 O critério

Afirmar que algo é eterno é a afirmação mais forte que um livro sobre envelhecimento pode
fazer, e é a que mais precisa de critério. O que se propõe aqui é simples e verificável:

> Um conhecimento é candidato a invariante se permaneceu válido, sem reformulação de
> conteúdo, através de pelo menos três rupturas de paradigma independentes entre si.

Três detalhes importam. **Sem reformulação de conteúdo** exclui princípios que sobrevivem
apenas porque foram reescritos de forma cada vez mais vaga — a vagueza é a forma mais comum
de falsa perenidade. **Rupturas independentes** exclui o caso de um princípio que atravessou
três mudanças que eram, na verdade, a mesma mudança. E **candidato** é intencional: o teste
elimina, mas não prova. Um invariante é uma hipótese que ainda não foi refutada.

### 1.3.2 Os três eixos de ruptura

As rupturas que valem como teste são as que mudaram as premissas econômicas ou físicas da
computação, não as que mudaram sintaxe ou moda.

O **eixo de hardware** contém a passagem do processamento em lote para o interativo, do
mainframe para o cliente-servidor, do desktop para o móvel, e do aumento de frequência de
relógio para o aumento de núcleos. Cada uma dessas invalidou práticas que pareciam
fundamentais na véspera.

O **eixo de escala** vai do sistema de um único usuário ao de milhares, ao de milhões, e à
operação global com replicação geográfica. Escala é o eixo que mais quebra abstrações:
quase tudo o que funciona com mil usuários falha de forma qualitativamente diferente com
dez milhões.

O **eixo de modelo de custo** é o menos discutido e o mais decisivo. Quando o recurso caro
era o tempo de máquina, otimizar código era racional e a legibilidade era luxo. Quando o
recurso caro passou a ser o tempo de programador, a hierarquia se inverteu. Com a nuvem, o
custo voltou a ser variável e mensurável por requisição, o que reabriu discussões que
pareciam encerradas — e é a razão de existir o capítulo 3.7.

### 1.3.3 O cemitério dos falsos invariantes

Aplicar o teste tem um custo, e ele deve ser pago publicamente. Estes são conhecimentos que
foram ensinados como fundamentos e não sobreviveram.

**Orientação a objetos como forma natural de organizar qualquer programa.** Ensinada nos
anos 1990 e 2000 como se fosse o modo correto de pensar software. Não sobreviveu ao eixo de
escala — hierarquias profundas de herança se mostraram frágeis — nem à absorção de ideias
funcionais pelas linguagens mainstream. O que sobrou de OO é real e continua útil:
encapsulamento, que é Parnas com outro nome, e polimorfismo. O que caiu foi a pretensão de
universalidade.

**SOLID como lei.** Um conjunto de heurísticas úteis, formulado num contexto específico de
OO empresarial, que foi promovido a princípio universal e recitado como se cada letra
tivesse a mesma solidez. Não passa no critério de "sem reformulação": cada princípio hoje é
defendido em versão consideravelmente mais fraca do que a original.

**A pirâmide de testes.** Continua sendo a heurística padrão, mas está em erosão aberta —
disputada por modelos alternativos que deslocam o peso para testes de integração, motivados
justamente por mudanças de arquitetura e de custo de execução. Ensiná-la como consenso, em
2026, é impreciso. O tema é tratado em 3.3.6.

**Requisitos congelados como pré-condição de qualidade.** Premissa central dos processos
pesados. Morreu no eixo de modelo de custo: quando implantar passou a custar minutos em vez
de meses, congelar requisito deixou de ser prudência e virou desperdício.

**UML como documentação viva.** Sobreviveu como ferramenta de pensamento e de comunicação
pontual; não sobreviveu como artefato mantido em sincronia com o código. Continua ocupando
carga horária desproporcional em grades brasileiras.

**"A nuvem é mais barata".** Nunca foi um invariante, mas foi ensinada como se fosse. É uma
afirmação sobre modelo de custo, e portanto é exatamente o tipo de coisa que muda quando o
modelo de custo muda.

### 1.3.4 Como o leitor deve duvidar deste livro

O Camada 1 afirma sete invariantes. É estatisticamente improvável que todos os sete resistam
às próximas décadas, e seria desonesto encerrá-lo sem dizer isso.

Meu candidato a primeiro a cair é 1.2.7, a curva de custo da mudança tardia — e ela já entrou
neste livro com a ressalva. O segundo candidato é a lei de Conway, não por estar errada, mas
porque o pressuposto que a sustenta é que a comunicação humana é o gargalo do projeto; se
uma parte substancial da produção de código deixar de passar por comunicação entre pessoas,
o mecanismo da lei muda de natureza. Não afirmo que isso vai acontecer; afirmo que é o
gatilho a vigiar, e ele está registrado na ficha deste capítulo.

O teste que proponho ao leitor é o mesmo que apliquei: quando encontrar neste livro uma
afirmação de perenidade, procure a ruptura que a testaria. Se não conseguir imaginar
nenhuma, desconfie — de mim, não do conceito. Uma afirmação que nada poderia falsificar não
é um invariante. É uma opinião bem escrita.

---

## Fontes desta camada

As referências primárias citadas são, na ordem em que aparecem: Naur, P. e Randell, B.
(eds.), *Software Engineering: Report on a Conference Sponsored by the NATO Science
Committee*, Garmisch, 1968 · Conway, M., "How Do Committees Invent?", *Datamation*, 1968 ·
Lehman, M., "Programs, Life Cycles, and Laws of Software Evolution", *Proceedings of the
IEEE*, 1980 · Brooks, F., *The Mythical Man-Month*, 1975, e "No Silver Bullet: Essence and
Accidents of Software Engineering", 1986 · Parnas, D., "On the Criteria To Be Used in
Decomposing Systems into Modules", *Communications of the ACM*, 1972 · Turing, A., "On
Computable Numbers, with an Application to the Entscheidungsproblem", 1936 · Boehm, B.,
*Software Engineering Economics*, 1981 · Bossavit, L., *The Leprechauns of Software
Engineering*, 2015.

*Datas e atribuições devem ser conferidas contra as fontes primárias antes da publicação.*

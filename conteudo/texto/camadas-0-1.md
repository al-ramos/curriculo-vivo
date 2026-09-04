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

## 1.4 · Cognição e metacognição

O capítulo mais negligenciado de qualquer currículo de tecnologia, e o único cujo conteúdo
não mudou em cinquenta anos porque não é sobre computadores: é sobre a máquina que os
programa. Ele está na camada Permanente por um motivo simples — os limites da atenção
humana não receberam atualização de versão.

### 1.4.1 Carga cognitiva e os limites da memória de trabalho

A memória de trabalho é o gargalo de toda atividade intelectual, e é ridiculamente pequena.
A cifra que circula, os sete elementos mais ou menos dois de Miller, é de 1956 e foi
revisada para baixo: as estimativas contemporâneas ficam em torno de quatro elementos
simultâneos. Quatro. É esse o orçamento com que se lê uma função, se acompanha uma reunião
de arquitetura e se depura um problema em produção às três da manhã.

A teoria da carga cognitiva, formulada por John Sweller, separa esse orçamento em partes.
A **carga intrínseca** vem da dificuldade inerente do material — uma árvore B é mais
complexa que uma lista ligada, e nada muda isso. A **carga estranha** vem da forma como o
material é apresentado: nomes ruins, indireção desnecessária, formatação inconsistente,
documentação espalhada. É a única parte que se pode atacar, e é onde mora praticamente todo
o valor prático do conceito. Havia ainda uma terceira categoria na formulação original, a
carga "relevante", que a própria literatura passou a tratar com desconfiança — vale
registrar, porque o livro pede rigor sobre o que envelheceu.

A consequência para quem escreve código é direta e desconfortável: **legibilidade não é
questão de gosto, é questão de orçamento**. Um nome ruim consome um slot dos quatro. Uma
indireção desnecessária consome outro. Quando os quatro acabam, o leitor não fica um pouco
mais lento — ele para de conseguir raciocinar sobre o problema e passa a raciocinar sobre o
código, que é outra coisa.

O mecanismo que quebra esse limite é o **agrupamento**. Um iniciante que lê
`for (int i = 0; i < n; i++)` processa cinco elementos; alguém experiente processa um: "laço
sobre a coleção". A perícia não amplia a memória de trabalho — ela aumenta o tamanho de cada
peça que cabe nela. É por isso que a experiência não se transfere por explicação: o
agrupamento se constrói por exposição repetida, e não há atalho conhecido.

Felienne Hermans, em *The Programmer's Brain*, propõe uma distinção operacional que vale
carregar: quando você trava diante de um código, o problema é **falta de conhecimento**
(não sei o que essa palavra-chave faz), **falta de informação** (sei o que faz, mas não sei
o que essa função devolve) ou **falta de capacidade de processamento** (sei tudo, mas são
peças demais para segurar de uma vez). Os três parecem iguais por dentro e pedem remédios
diferentes: estudar, consultar, ou anotar em papel. Confundi-los é a causa mais comum de
tempo perdido em depuração.

### 1.4.2 Os quatro níveis de abstração

Todo código pode ser lido em quatro alturas, e a maior parte das confusões de projeto vem
de duas pessoas conversando em alturas diferentes sem perceber.

**Nível 1 — o que a máquina faz.** Linha a linha: esta variável recebe, este laço percorre,
esta chamada bloqueia. É o nível do depurador e do rastreamento de pilha, e é o único onde
o computador tem razão por definição.

**Nível 2 — qual é a intenção do trecho.** "Isto valida o CPF", "isto tenta de novo com
espera crescente". Um trecho legível é aquele em que o nível 2 é dedutível sem passar pelo
nível 1. Quando alguém diz que um código está limpo, quase sempre está dizendo isso.

**Nível 3 — qual é o papel no sistema.** Este módulo é a fronteira com o mundo externo,
aquele guarda a regra de negócio, este outro existe só para isolar uma decisão que pode
mudar. É o nível de Parnas, e o nível em que arquitetura acontece.

**Nível 4 — qual problema do mundo isso resolve.** Por que existe essa regra, quem paga por
ela, o que acontece com o negócio se ela estiver errada.

O valor de nomear os quatro níveis é diagnóstico. Um desenvolvedor júnior tipicamente opera
bem no nível 1 e adivinha o 2. Um pleno domina 1 e 2 e trata o 3 como decoração. A
senioridade começa quando a pessoa transita nos quatro **de propósito** — e sabe dizer em
qual está. Reuniões improdutivas quase sempre são pessoas presas em níveis distintos: uma
argumenta implementação enquanto a outra argumenta negócio, e as duas acham que a outra não
entendeu.

Há um teste rápido: peça a alguém para explicar um trecho que escreveu. Se a explicação for
uma tradução do nível 1 para o português — "aqui eu faço um laço e verifico se é nulo" —, a
pessoa ainda não subiu. A explicação madura começa no nível 3.

### 1.4.3 Debugging como método científico

Depurar não é uma habilidade de ferramenta; é a aplicação do método científico sob pressão
de tempo, e é a atividade em que a disciplina intelectual de um profissional fica mais
visível.

O ciclo é sempre o mesmo. **Observação**: o que exatamente acontece, em termos verificáveis,
sem interpretação. **Hipótese**: uma explicação que, se verdadeira, produziria essa
observação. **Predição**: se a hipótese for verdadeira, então tal experimento dará tal
resultado — e este é o passo que quase todo mundo pula. **Experimento**: o menor possível,
mudando uma coisa por vez. **Conclusão**: e o registro do que foi eliminado.

Dois erros dominam a prática.

O primeiro é **buscar confirmação em vez de refutação**. Formulada a hipótese, a tentação é
procurar evidência a favor. O experimento valioso é o que teria potencial de derrubá-la — é
o mesmo princípio que sustenta o capítulo 1.3 deste livro, aplicado em escala de minutos em
vez de décadas.

O segundo é **mudar mais de uma coisa por vez**. Duas alterações simultâneas e o sistema
volta a funcionar: você não sabe o que consertou, e portanto não consertou — apenas parou de
ver. Esse é o mecanismo pelo qual defeitos "resolvidos" reaparecem meses depois.

A técnica mais subestimada é a **bisseção**: em vez de raciocinar sobre a causa, corte o
espaço de busca ao meio e repita. Com mil revisões entre a última versão boa e a ruim, dez
testes bastam. `git bisect` é a versão automatizada disso, mas o valor está no raciocínio,
não no comando — a mesma bisseção funciona sobre dados de entrada, sobre configuração e
sobre a lista de serviços de uma cadeia de chamadas.

Uma observação sobre ferramentas, coerente com a tese do livro: depurador contra registro em
log é uma discussão de camada sazonal. O método não muda. Quem sabe formular hipótese e
cortar espaço de busca é eficaz com qualquer uma das duas; quem não sabe fica igualmente
perdido com as duas, só que com telas mais bonitas.

### 1.4.4 A meta-habilidade de aprender e desaprender

Aprender uma tecnologia nova é a parte fácil, e é a única que os cursos endereçam. A parte
cara é **desaprender**.

O motivo é que conhecimento antigo não fica inerte: ele interfere. Quem passou quinze anos
em orientação a objetos empresarial carrega intuições — sobre onde colocar estado, sobre
como modelar comportamento, sobre o que é "óbvio" — que atrapalham ativamente ao aprender
um paradigma funcional. O iniciante absoluto aprende mais devagar no começo e às vezes chega
mais longe, não por talento, mas por não ter nada para desmontar antes.

Isso tem duas consequências práticas.

A primeira: **nomear o modelo antigo é metade do trabalho**. Enquanto a intuição permanece
implícita, ela opera sem ser examinada. Escrever "eu presumo que estado mutável compartilhado
é a forma natural de coordenar" transforma um reflexo em uma proposição — e proposições
podem ser testadas.

A segunda: a resistência a tecnologias novas raramente é preguiça, e quase nunca é o que
parece. Ela costuma ser o custo real de desmontar um modelo mental que funciona há uma
década — um custo que quem nunca o construiu não enxerga. Isso vale como diagnóstico, não
como desculpa: reconhecer o custo é o que permite pagá-lo deliberadamente em vez de negá-lo.

Vale registrar o que a evidência **não** sustenta: a ideia de estilos de aprendizagem —
visual, auditivo, cinestésico — é popular, intuitiva e não se confirma em teste
experimental. Ensinar cada pessoa no seu "estilo" não melhora o resultado. É um exemplo
particularmente útil para este livro, porque é um falso invariante que se instalou na
educação e continua sendo repetido em treinamento corporativo.

### 1.4.5 Modelos mentais e transferência entre tecnologias

Um modelo mental é a explicação interna que alguém carrega sobre como um sistema funciona.
Ele quase sempre está errado em algum detalhe, e ainda assim é o que permite prever
comportamento sem consultar documentação — o que é a definição operacional de competência.

O ponto que importa para carreira é a **transferência**. Quem aprendeu Git decorando sete
comandos não transfere nada quando muda de ferramenta. Quem entendeu que Git é um grafo
dirigido acíclico de instantâneos, com referências móveis apontando para nós, entende
qualquer sistema de versionamento subsequente em uma tarde — e, melhor, prevê corretamente o
que acontece num caso que nunca viu.

A pergunta que separa os dois é sempre a mesma, e vale carregar como hábito: **o que este
sistema é, por baixo do vocabulário?** Um banco relacional é álgebra de conjuntos com
restrições de integridade. Um contêiner é isolamento de processo com sistema de arquivos em
camadas. Uma fila é um desacoplamento temporal entre produtor e consumidor. Nenhuma dessas
frases é a documentação oficial de nada, e todas sobrevivem à troca do produto.

Esse é o mecanismo concreto pelo qual a Camada 1 protege contra o envelhecimento das
camadas 3 e 4. Não é uma metáfora inspiradora: é que modelos mentais corretos têm meia-vida
de décadas, e listas de comandos têm meia-vida de anos.

### 1.4.6 Por que isso supera qualquer linguagem ou framework

Junte os cinco tópicos anteriores e o argumento se fecha sozinho.

O gargalo do trabalho é a memória de trabalho, e ela não melhora com ferramenta. A
competência que multiplica esse gargalo é o agrupamento, que se constrói por exposição
deliberada. A capacidade de diagnosticar vem de método, não de instrumento. A velocidade de
aprender algo novo depende do custo de desmontar o que já existe. E a transferência entre
tecnologias depende da qualidade dos modelos mentais, não da quantidade de sintaxes
conhecidas.

Nenhum desses cinco itens aparece em anúncio de vaga. Todos os cinco determinam o
desempenho de quem já foi contratado — e, o que interessa mais a este livro, determinam a
velocidade com que a pessoa atravessa cada substituição de camada sazonal ao longo de trinta
anos de carreira.

Há uma consequência pedagógica desconfortável para quem ensina: essas habilidades não são
ensináveis por exposição. Não existe aula de agrupamento. Elas se desenvolvem em ciclos de
tentativa, erro e feedback específico — que é exatamente o formato que o ensino formal tem
mais dificuldade de oferecer em escala, e o motivo pelo qual o capítulo 3.5 vai tratar a
lacuna de ensino como estrutural, e não como desleixo.

### 1.4.7 Prática deliberada e o platô do profissional intermediário

Existe um padrão de carreira suficientemente comum para merecer nome: a pessoa melhora
rápido nos primeiros três a cinco anos, atinge um patamar em que resolve com folga o que o
trabalho exige, e permanece nesse patamar por uma década. Não é falta de esforço — é o
resultado previsível de fazer bem o que já se sabe fazer.

O mecanismo é a **automatização**. Uma habilidade praticada até virar automática deixa de
consumir atenção, o que é ótimo para produtividade e péssimo para desenvolvimento: sem
atenção consciente, não há ajuste. Digitar mais rápido não melhora a digitação de ninguém
depois de certo ponto, e escrever mais do mesmo CRUD não melhora um engenheiro.

O antídoto descrito na literatura é a **prática deliberada**, popularizada a partir dos
estudos de Anders Ericsson: trabalhar deliberadamente logo acima do nível confortável, com
objetivo específico e feedback rápido, aceitando o desconforto e o erro frequente como
sinais de que se está no lugar certo.

Duas ressalvas de honestidade, porque este livro cobra fontes.

A primeira: **a regra das dez mil horas não é de Ericsson** — é uma popularização, e ele
próprio a contestou. Não existe número mágico, e horas acumuladas sem feedback não produzem
progresso; produzem antiguidade.

A segunda: a força da prática deliberada como explicação do desempenho é **menor do que a
divulgação sugere**. Meta-análises posteriores encontram uma fração modesta da variação
explicada por ela, e menor ainda em domínios pouco estruturados — e programação é um domínio
pouco estruturado, diferente de xadrez ou violino. A conclusão defensável não é "pratique
deliberadamente e você chegará lá", e sim "prática sem feedback quase certamente não leva a
lugar nenhum".

Na prática profissional, isso se traduz em coisas pequenas e específicas: pedir revisão de
código de alguém melhor que você em vez de de quem concorda; escolher a tarefa que você não
sabe fazer em vez da que sabe; reimplementar do zero algo que você usa há anos; escrever
sobre o que aprendeu, porque explicar é o teste que revela o que não se entendeu. É também
a razão de este livro exigir um projeto e um texto ao fim de cada trilha do plano de
estudos: leitura sem produção é o platô com aparência de progresso.


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

Para o capítulo 1.4: Miller, G., "The Magical Number Seven, Plus or Minus Two",
*Psychological Review*, 1956, e a revisão posterior para cerca de quatro elementos
(Cowan) · Sweller, J., trabalhos sobre teoria da carga cognitiva · Hermans, F.,
*The Programmer's Brain*, 2021 · Ericsson, K. A., *Peak*, 2016, e a crítica meta-analítica
de Macnamara, Hambrick e Oswald, 2014 · Pashler, H. et al., "Learning Styles: Concepts and
Evidence", 2008.

*Datas e atribuições devem ser conferidas contra as fontes primárias antes da publicação.*


---

# CAMADA 2 — GERACIONAL
*Meia-vida: quinze a vinte anos*

## 2.1 · Paradigmas de programação

Um paradigma não é uma linguagem nem uma coleção de palavras reservadas. É um conjunto de
escolhas que a linguagem torna naturais: onde o estado vive, como o controle avança, em que
unidade o programa é decomposto e que tipo de erro fica difícil de expressar. Linguagens
modernas são quase todas multiparadigma, mas isso não elimina os paradigmas; apenas transfere
para quem programa a responsabilidade de saber qual deles está usando em cada trecho.

Este capítulo não organiza uma competição para eleger o paradigma vencedor. Faz a pergunta
que atravessa o livro: o que cada modelo tornou fácil, que custo escondeu e o que permaneceu
depois que sua fase de domínio passou.

### 2.1.1 Imperativo e procedural

Programação imperativa descreve uma computação como uma sequência de comandos que altera o
estado do programa. Uma variável recebe um valor, depois outro; uma condição escolhe o próximo
comando; um laço repete uma transformação. O significado de uma instrução depende não apenas
do texto, mas do estado produzido pelas instruções anteriores. Ordem, portanto, não é detalhe
de implementação: faz parte do programa.

O modelo se ajustou cedo à máquina de programa armazenado. No vocabulário que John Backus
criticaria em sua palestra do Prêmio Turing, variáveis se parecem com células de memória,
atribuições com operações de carga e armazenamento, e o fluxo de controle com saltos e testes.
Essa proximidade ajudou linguagens imperativas a entregar desempenho previsível e uma tradução
compreensível entre algoritmo e execução. Também deixou como herança a tendência de descrever
o problema nos termos da máquina, mesmo quando havia uma abstração melhor disponível.

**Procedural** não é sinônimo de imperativo. É uma forma de organizar esse fluxo em
procedimentos nomeados, com parâmetros e escopo, para que uma sequência possa ser entendida e
reutilizada como unidade. FORTRAN já tratava, em 1957, a tradução de fórmulas e procedimentos
para código eficiente como problema central. ALGOL 60 consolidou blocos, escopo e declarações
de procedimento. A contribuição duradoura não foi uma sintaxe específica: foi permitir que o
leitor raciocinasse sobre uma parte sem simular o programa inteiro.

A programação estruturada apertou essa disciplina. Sequência, seleção e repetição substituíram
a maior parte dos saltos arbitrários, não porque `goto` tornasse um programa automaticamente
incorreto, mas porque destruía a correspondência visível entre a estrutura do texto e a ordem
da execução. Dijkstra foi mais cuidadoso do que o slogan que herdamos: remover saltos de modo
mecânico também pode produzir um programa opaco. O objetivo era tornar o fluxo acompanhável,
não obedecer a uma proibição lexical.

O custo do paradigma aparece quando o estado mutável escapa da unidade que o controla. Uma
atribuição local é fácil de acompanhar; dez módulos capazes de alterar o mesmo objeto tornam o
resultado dependente de história, ordem e conhecimento espalhado. Concorrência amplia esse
custo, mas não o inventa. A regra prática que sobreviveu é reduzir o perímetro temporal:
manter a mutação perto de quem a usa, dar nome às transições importantes e não expor estado
compartilhado quando se pode expor uma operação.

É por isso que o imperativo permanece sem ser permanente. Enquanto programas precisarem
coordenar efeitos no tempo — gravar, enviar, cobrar, mover — a sequência continuará útil. O
que envelhece a cada geração é quanto desse mecanismo deixamos visível e quanto confinamos
atrás de abstrações mais declarativas.

### 2.1.2 Orientação a objetos — o que sobrou depois da crítica dos anos 2010

Orientação a objetos reuniu tradições diferentes sob o mesmo nome. Em Simula, objetos
modelavam entidades de uma simulação com estado e comportamento. Em Smalltalk, a ênfase de
Alan Kay estava em objetos autônomos trocando mensagens, com ligação tardia e fronteiras que
escondiam representação. Na indústria dos anos 1990 e 2000, o centro de gravidade mudou para
classes, herança, diagramas e grandes grafos de objetos. As três coisas são aparentadas, mas
não são equivalentes.

A crítica dos anos 2010 atingiu principalmente a versão que havia virado ortodoxia: modelar
cada substantivo como classe, usar herança como mecanismo padrão de reúso e distribuir estado
mutável por uma rede de objetos que só funciona quando se conhece sua ordem de chamadas. A
popularização de funções de primeira classe, dados imutáveis e serviços independentes tornou
visível que muito código chamado de orientado a objetos era procedural com cerimônia — e que a
cerimônia não comprava encapsulamento real.

O que sobrou é menos vistoso e mais resistente. **Encapsulamento** continua sendo a capacidade
de proteger uma decisão de representação. **Polimorfismo** continua permitindo que clientes
dependam de um contrato de comportamento, não de uma implementação. **Identidade** continua
necessária quando duas entidades com os mesmos dados não são a mesma entidade. E objetos
continuam sendo uma boa fronteira quando estado e invariantes precisam mudar juntos.

O que não sobreviveu como lei foi a pretensão universal. Herança é uma ferramenta de
substituição sob contrato, não uma árvore genealógica para organizar o domínio. Classe não é a
unidade natural de todo problema. E ocultar campos atrás de métodos que apenas leem e escrevem
os mesmos campos não é encapsular; é acrescentar pontuação.

O teste prático é perguntar se a unidade tem identidade, ciclo de vida e invariantes próprios.
Uma conta, um pedido ou uma conexão frequentemente têm. Uma transformação de texto, uma
consulta e uma regra algébrica frequentemente não têm. Usar objetos no primeiro caso e funções
no segundo não é ecletismo: é recusar que uma técnica local vire cosmologia.

### 2.1.3 Funcional — da academia ao mainstream por absorção, não por substituição

Programação funcional descreve computações pela composição de funções e expressões, reduzindo
a dependência de mudanças de estado observáveis. Sua propriedade mais útil não é concisão nem
elegância: é **substituição**. Se uma expressão produz sempre o mesmo resultado para as mesmas
entradas e não altera o mundo ao redor, pode ser compreendida, testada e reorganizada sem
reconstruir toda a história da execução.

Isso não significa que programas funcionais não tenham efeitos. Um sistema útil ainda lê,
grava, falha e conversa pela rede. A diferença é arquitetural: efeitos são empurrados para
fronteiras explícitas, enquanto o núcleo transforma valores. Imutabilidade reduz o número de
estados possíveis; funções de ordem superior permitem transformar o padrão de iteração em
vocabulário; tipos algébricos e casamento de padrões tornam casos possíveis visíveis no texto.

Durante décadas, essas ideias ficaram associadas a Lisp, ML, Haskell e à pesquisa em
linguagens. O movimento decisivo não foi essas linguagens substituírem as imperativas. Foi
Java, C#, JavaScript, Python, Kotlin e outras absorverem lambdas, coleções imutáveis,
composição, `map`, `filter` e tratamento de funções como valores. O paradigma venceu partes do
programa sem vencer a placa na porta.

Essa absorção corrige também a caricatura inversa. Função pequena não torna um sistema
funcional, e encadear dez operações não elimina custo de memória ou de entrada e saída.
Pureza pode deslocar complexidade para a fronteira em vez de removê-la. Em fluxos com estado
duradouro, interação incremental ou requisitos fortes de desempenho, uma solução híbrida é
frequentemente mais legível do que uma solução que protege a pureza a qualquer preço.

O ganho geracional está no repertório de restrições: preferir valores a lugares mutáveis,
isolar efeitos e compor transformações. Depois de absorvidas, essas escolhas deixam de parecer
funcionais e passam a parecer apenas bom código. É assim que um paradigma acadêmico muda o
mainstream sem substituí-lo.

### 2.1.4 Reativo e assíncrono

Assíncrono descreve uma relação no tempo: quem inicia uma operação pode continuar antes que
ela termine. Não diz que o trabalho rodará em paralelo, em outra máquina ou mesmo em outra
thread. Em entrada e saída, seu valor principal é não ocupar um recurso enquanto o programa
espera pela rede, pelo disco ou pelo usuário.

`async` e `await` foram uma reconciliação importante. O compilador transforma o método numa
máquina de estados, mas o texto preserva a aparência de uma sequência. Isso remove a pirâmide
de callbacks sem restaurar a simplicidade síncrona: o método ainda pode ser suspenso em cada
`await`, o contexto pode ter mudado quando ele voltar, e cancelamento e erro precisam atravessar
a cadeia inteira. Bloquear no meio de uma cadeia assíncrona não é neutralidade; é misturar dois
modelos de espera com contratos diferentes.

**Reativo** é uma palavra mais sobrecarregada. Pode nomear uma interface que reage a eventos,
um fluxo que empurra valores ao consumidor ou uma arquitetura que busca permanecer responsiva
sob falha e variação de carga. O Manifesto Reativo de 2014 ligou responsividade, resiliência,
elasticidade e comunicação por mensagens. É uma proposta arquitetural, não uma definição
universal do termo.

No nível de fluxo, a mudança essencial é de *puxar quando quiser* para *receber quando houver*.
Isso exige um contrato para o caso em que o produtor é mais rápido que o consumidor.
**Backpressure** é esse contrato: desacelerar, acumular dentro de limite, amostrar ou descartar
de forma declarada. Sem ele, o sistema apenas troca espera visível por fila crescente.

O critério não é escolher a API mais moderna. Assincronia serve quando há espera que pode ser
aproveitada; fluxo reativo serve quando valores chegam ao longo do tempo e a pressão precisa
ser propagada. Para uma transformação curta e local, ambos podem acrescentar mais estados de
controle do que removem.

### 2.1.5 Orientado a eventos

Um evento registra algo que já aconteceu. Um comando pede que algo aconteça. Uma mensagem é o
envelope que pode carregar qualquer dos dois. Confundir os três produz contratos frágeis: um
evento chamado `CriarPedido`, por exemplo, ainda é um comando disfarçado porque pode ser
recusado e espera um destinatário responsável.

No paradigma orientado a eventos, produtores publicam fatos sem controlar todos os usos que
serão feitos deles, e consumidores reagem de forma independente. O ganho é desacoplamento de
evolução e de tempo: um novo consumidor pode aparecer sem mudar o produtor, e ambos não
precisam estar ativos no mesmo instante quando existe persistência intermediária. O custo é
que o fluxo deixa de caber numa pilha de chamadas. Para entender uma ação, pode ser necessário
reconstruir uma cadeia espalhada por processos, filas e instantes diferentes.

O evento, sozinho, não promete entrega, ordem ou unicidade. Essas são propriedades do canal e
do protocolo. Um consumidor que pode receber o mesmo fato novamente precisa ser idempotente ou
registrar o que já processou. Um consumidor que depende de ordem precisa declarar a chave e o
escopo dessa ordem. Um sistema que trata essas garantias como propriedades naturais da palavra
"evento" descobre o contrato apenas durante a falha.

Também convém separar três técnicas frequentemente misturadas. **Notificação de evento** pode
carregar apenas um identificador e obrigar o consumidor a consultar o estado atual. **Evento
com estado transferido** leva os dados necessários e aceita duplicação. **Event sourcing** usa
eventos como registro autoritativo do qual o estado é derivado. A terceira opção não é a versão
madura das duas primeiras; é uma decisão de persistência com custo de esquema, replay e
correção histórica.

O paradigma é geracional porque a forma concreta da infraestrutura muda mais rápido do que o
problema. Filas, brokers e bibliotecas são substituídos; os compromissos entre acoplamento,
ordem, entrega e observabilidade permanecem.

### 2.1.6 Tipagem como paradigma transversal — estática, dinâmica, gradual

Tipagem é uma disciplina para classificar valores e operações; não é uma divisão moral entre
linguagens seguras e inseguras. Toda linguagem estabelece o que pode ser somado, chamado ou
acessado. A diferença está em quando essa compatibilidade é verificada, quanto dela pode ser
inferida e o que acontece na fronteira entre partes que conhecem precisões diferentes.

Na tipagem **estática**, parte dessas relações é verificada antes da execução. Isso transforma
certas famílias de defeito em erro de compilação e dá às ferramentas informação para navegar e
refatorar. O teorema de solidez de Milner, de 1978, tornou famosa a formulação de que programas
bem tipados não "dão errado" — dentro de um sistema formal e de uma definição específica de
erro. Fora dessas aspas, um programa bem tipado ainda calcula o preço errado, perde dados e
viola a lei com perfeita correção de tipos.

Na tipagem **dinâmica**, valores carregam informação de tipo e as operações são verificadas
durante a execução. Dinâmica não significa ausência de tipos; significa que o programa pode
chegar a uma combinação inválida que uma análise anterior não excluiu. Em troca, prototipação,
metaprogramação e dados cuja forma só se conhece na borda podem exigir menos tradução
cerimonial.

A tipagem **gradual**, formalizada por Siek e Taha em 2006, reconhece que sistemas reais não
migram de um mundo ao outro de uma vez. Ela permite que regiões com garantias estáticas
convivam com regiões imprecisas, inserindo verificações nas fronteiras. Seu valor principal
não é produzir uma terceira escola, mas tornar a precisão uma decisão incremental.

Termos como "forte" e "fraca" ajudam pouco sem definição: autores diferentes os usam para
coerção, segurança de memória ou possibilidade de burlar o sistema. A pergunta útil é mais
concreta: **que estados inválidos este tipo impede representar, e em qual fronteira a garantia
termina?** Tipos são uma forma executável de documentação quando respondem isso; quando apenas
repetem a estrutura dos dados, viram inventário.

### 2.1.7 Concorrência e paralelismo — threads, atores, CSP, async/await

Concorrência é a composição de atividades que progridem em períodos sobrepostos; paralelismo
é a execução simultânea de atividades. Um programa pode ser concorrente num único núcleo por
intercalação e paralelo sem expor concorrência ao autor quando uma biblioteca divide o
trabalho. A distinção importa porque o primeiro problema é estruturar dependências; o segundo é
usar recursos para obter vazão ou reduzir tempo.

**Threads** oferecem múltiplos fluxos de execução sobre memória compartilhada. São gerais e
próximas do sistema operacional, mas transferem para o programa a disciplina de proteger
estado. Corridas, deadlocks e visibilidade de memória não são acidentes da API: são
consequências do modelo de propriedade compartilhada.

**Atores**, propostos por Hewitt, Bishop e Steiger em 1973, encapsulam estado e se comunicam
por mensagens. **CSP**, apresentado por Hoare em 1978, estrutura processos sequenciais que se
coordenam por comunicação. As duas famílias reduzem a superfície de memória compartilhada,
mas não eliminam ordem, espera ou falha; deslocam esses problemas para caixas postais, canais e
protocolos. O nome da abstração muda, a necessidade de explicitar propriedade permanece.

**`async`/`await`** organiza tarefas que suspendem e retomam, sendo especialmente útil quando
o gargalo é espera por entrada e saída. Não transforma trabalho intensivo de CPU em trabalho
paralelo. Iniciar cem operações assíncronas também não cria capacidade para concluí-las: sem
limite de concorrência, a fila apenas se move para outra camada.

Qualquer modelo sério precisa responder às mesmas perguntas: quem possui cada estado, como o
trabalho é cancelado, onde o erro reaparece, que ordem é garantida e o que impede o produtor de
superar o consumidor. A API que não obriga essas respostas pode ser confortável no exemplo e
hostil em produção.

Este capítulo está na camada Geracional porque seus modelos atravessaram várias gerações de
linguagem e hardware, mas seus pesos mudam. Memória compartilhada parecia natural quando havia
um processador; imutabilidade e troca de mensagens ganharam valor com múltiplos núcleos e
sistemas distribuídos. Paradigmas não se sucedem como versões. Eles se acumulam, são
combinados e voltam a ser avaliados quando o custo dominante muda.

**Fontes primárias do capítulo.** Backus, J. W. et al., [*The FORTRAN Automatic Coding
System*](https://archive.computerhistory.org/resources/text/Fortran/102663113.05.01.acc.pdf),
1957 · Naur, P. (ed.), [*Revised Report on the Algorithmic Language ALGOL
60*](https://archive.computerhistory.org/resources/text/algol/algol_bulletin/EX/RR60/INDEX.HTM),
1963 · Dijkstra, E. W., ["Go To Statement Considered
Harmful"](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf), 1968, e
[*Notes on Structured Programming*](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html),
1970 · Kay, A. C., *The Early History of Smalltalk*, 1993, DOI
10.1145/155360.155364 · Backus, J., *Can Programming Be Liberated from the von Neumann
Style?*, 1978, DOI 10.1145/359576.359579 · Hewitt, C., Bishop, P. e Steiger, R., *A
Universal Modular ACTOR Formalism for Artificial Intelligence*, 1973 · Hoare, C. A. R.,
[*Communicating Sequential Processes*](https://ora.ox.ac.uk/objects/uuid%3A833f1ea8-feba-4d81-b419-83e6f5f24e81),
1978 · Milner, R., *A Theory of Type Polymorphism in Programming*, 1978 · Siek, J. e Taha,
W., [*Gradual Typing for Functional
Languages*](https://web.stanford.edu/class/cs242/materials/old/siek06__gradual.pdf), 2006 ·
Luckham, D., *The Power of Events*, 2002 · [*The Reactive Manifesto*,
v2](https://www.reactivemanifesto.org/), 2014 · Pike, R., [*Concurrency Is Not
Parallelism*](https://go.dev/talks/2012/waza.slide), 2012.

---

## 2.2 · Dados e persistência

Programas são substituídos; dados sobrevivem a eles. É comum que um sistema tenha sido reescrito
três vezes sobre o mesmo esquema, e raro que o oposto tenha acontecido. Essa assimetria é o motivo
de este capítulo estar na camada geracional enquanto boa parte da infraestrutura que o cerca está
na sazonal: o modelo de dados é a decisão mais cara de reverter que uma equipe toma, e a que menos
recebe tempo de projeto.

A persistência é também onde o software encontra o tempo. Enquanto tudo está em memória, o
programa pode fingir que a execução é instantânea e isolada. No momento em que algo precisa
sobreviver a um desligamento, aparecem falha parcial, concorrência, ordenação e a necessidade de
dizer o que significa "gravado". Quase todo conceito difícil do capítulo 2.3 já está aqui, em
escala menor.

Este capítulo trata do que permaneceu. Ele não recomenda um banco.

### 2.2.1 Modelagem relacional e normalização

O artigo de Codd, em 1970, não propôs uma sintaxe nem um produto. Propôs uma separação: o modo
como os dados são descritos deve ser independente do modo como estão armazenados e acessados.
Antes disso, consultar um dado exigia saber por qual caminho navegar até ele — ponteiros,
conjuntos encadeados, a ordem física dos registros. Uma mudança de armazenamento quebrava
programas. O modelo relacional trocou a navegação por uma descrição: o cliente diz que relação
quer, não como chegar nela.

Essa independência é a contribuição que sobreviveu, e vale separá-la do resto. SQL não é o modelo
relacional — é uma linguagem que o implementa de forma parcial e às vezes infiel, com duplicatas,
`NULL` de três valores e ordem de colunas. O que atravessou cinquenta anos foi a ideia de que
existe um esquema lógico ao qual as aplicações se acoplam, e um plano físico que o banco pode
mudar sozinho. Todo otimizador de consulta existe dentro dessa fresta.

A normalização é o procedimento que torna o esquema lógico defensável. Ela parte das dependências
funcionais — que atributo determina que atributo — e elimina redundância que permitiria ao banco
guardar duas versões do mesmo fato. Da primeira à terceira forma normal, e à forma de Boyce-Codd,
o que se persegue é sempre o mesmo: que cada fato esteja registrado em exatamente um lugar. A
motivação não é elegância, é a anomalia de atualização. Um dado repetido em dois lugares vai
divergir; a única questão é quando.

O ditado de campo — normalizar até doer, desnormalizar até funcionar — é bom conselho e péssima
teoria, porque esconde qual das duas operações é reversível. Desnormalizar um esquema normalizado
é uma decisão local, tomada com medição, e possível de desfazer. Normalizar um esquema que nasceu
achatado exige descobrir dependências funcionais em dados que já divergiram, e essa arqueologia
costuma ser mais cara do que a reescrita da aplicação. A ordem importa: normalize primeiro porque
é o estado do qual se pode sair barato.

O custo real do modelo aparece na fronteira com a linguagem de programação. O descasamento de
impedância — objetos com identidade, herança e grafos de referência de um lado; relações,
conjuntos e chaves do outro — produziu trinta anos de camadas de mapeamento, e nenhuma delas
eliminou o problema, porque ele não é de ferramenta. São duas formas legítimas de descrever o
mundo, otimizadas para perguntas diferentes. O mapeador esconde a diferença até o dia em que ela
reaparece como consulta acidentalmente cara.

### 2.2.2 Transações, ACID e níveis de isolamento

Uma transação é uma mentira útil: ela permite que quem programa escreva como se fosse o único
usuário do banco e como se falhas não existissem. Jim Gray formalizou o conceito em 1981;
Härder e Reuter cunharam a sigla ACID em 1983. As quatro letras não têm o mesmo peso, e tratá-las
como bloco único é a origem de boa parte da confusão que se segue.

Atomicidade e durabilidade são propriedades sobre falha: ou tudo acontece ou nada acontece, e o
que foi confirmado sobrevive à queda. São as mais bem implementadas e as menos discutidas.
Consistência, no sentido de ACID, é a mais fraca das quatro — significa apenas que a transação
leva o banco de um estado que satisfaz as restrições declaradas a outro que também as satisfaz.
É uma propriedade da aplicação, não do banco, e não tem relação com o "C" de CAP, uma coincidência
de vocabulário que a seção 2.2.5 vai precisar desfazer.

O isolamento é onde mora o assunto. Serializabilidade — o resultado equivale a alguma execução
sequencial das transações — é a garantia que corresponde à mentira útil. Ela custa caro, e por
isso praticamente nenhum banco a entrega por padrão. O SQL-92 definiu quatro níveis por meio das
anomalias que cada um permite: leitura suja, leitura não repetível e fantasmas. A definição por
anomalia foi um erro de projeto que sobrevive até hoje na norma.

O erro foi demonstrado por Berenson e coautores em 1995. A taxonomia por anomalias é ambígua e não
acomoda o isolamento por instantâneo, que era o que os bancos de fato estavam construindo: o
snapshot isolation evita as três anomalias da norma e mesmo assim não é serializável, porque
admite a escrita enviesada — duas transações leem o mesmo estado, cada uma decide algo válido
isoladamente, e a combinação viola uma invariante que nenhuma das duas quebrou sozinha. O exemplo
clássico é a escala de plantão em que dois médicos, simultaneamente, verificam que há outro de
sobreaviso e se ausentam.

A consequência prática é desconfortável e verificável em qualquer instalação: o nível padrão do
PostgreSQL e do Oracle é read committed; o do MySQL com InnoDB é repeatable read; o do SQL Server
é read committed. Nenhum é serializável. A maioria do código de negócio escrito no mundo assume
uma garantia que o banco não está dando, e funciona porque a concorrência real é baixa o
suficiente para que a janela não seja atingida — até que o volume cresça, e o defeito apareça como
um dado impossível que ninguém consegue reproduzir.

A regra que sobrevive não é "use serializable". É saber declarar, para cada transação que sustenta
uma invariante de negócio, qual anomalia a quebraria e o que impede essa anomalia: o nível de
isolamento, um bloqueio explícito, uma restrição única no banco, ou uma reformulação que torne a
invariante local a uma linha. A restrição declarada no esquema é a mais barata das quatro e a mais
frequentemente esquecida, porque exige admitir que a aplicação não é a única a escrever.

### 2.2.3 O movimento NoSQL — o que era hype e o que ficou

O nome nasceu de um encontro em São Francisco em 2009, e era uma provocação antes de ser uma
categoria. O contexto técnico vinha de dois artigos: o do Bigtable, do Google, em 2006, e o do
Dynamo, da Amazon, em 2007. Ambos descreviam sistemas construídos para uma restrição que a maioria
das empresas não tinha — escala horizontal em hardware comum, com disponibilidade acima de
consistência — e ambos foram lidos como receita geral.

O que era hype pode ser nomeado com precisão, porque envelheceu rápido. Primeiro, a ideia de que
bancos relacionais não escalam: escalavam, e o que não escalava era a junção distribuída e a
transação de duas fases, que são problemas específicos e não o modelo. Segundo, e mais custoso, o
adjetivo *schemaless*. Não existe dado sem esquema; existe esquema não declarado. Quem tira o
esquema do banco não o elimina, move para o código da aplicação — e para todas as versões da
aplicação que já escreveram naquela coleção. O esquema deixa de ser verificado na escrita e passa
a ser descoberto na leitura, geralmente por um `if` defensivo escrito depois do incidente.

O que ficou é substancial e menos vistoso. O particionamento horizontal deixou de ser um recurso
avançado e passou a ser decisão de primeira classe: escolher a chave de partição virou parte da
modelagem, não da operação. A ideia de armazenamento com propósito — usar um motor diferente para
uma carga com padrão de acesso diferente — deixou de ser heresia. E a discussão sobre consistência
saiu do departamento de banco de dados e chegou a quem escreve aplicação, o que era necessário e
está longe de terminar.

O desfecho repete o padrão que o capítulo 2.1 descreveu para a programação funcional: a absorção
venceu a substituição. Bancos relacionais incorporaram tipos JSON com indexação; sistemas
distribuídos com SQL e transações — a linhagem do Spanner, de 2012 — desfizeram a premissa de que
era preciso escolher entre escala e transação; e os bancos ditos NoSQL passaram a oferecer esquema
opcional, índices secundários e alguma forma de transação. Vinte anos depois, a fronteira é menos
uma parede e mais um conjunto de escolhas de projeto que se podem descrever uma a uma.

### 2.2.4 Modelos além do relacional

Cada modelo de dados é uma aposta em um padrão de consulta. Ele torna barata uma forma de
perguntar e cara todas as outras. Descrever os modelos como uma lista de opções equivalentes é o
erro que este capítulo tenta evitar; a pergunta útil não é qual é melhor, é qual consulta é quente
e qual o sistema pode se dar ao luxo de responder devagar.

**Chave-valor** oferece a busca por identificador e nada mais. Em troca, particiona
trivialmente — a chave já é o critério de distribuição — e sustenta latência previsível. Tudo o
que não for acesso por chave conhecida vira varredura ou índice mantido à mão. É o modelo com o
melhor perfil de custo e a menor tolerância a requisitos que mudam.

**Documento** guarda agregados: a unidade de leitura é a mesma unidade de escrita, o que elimina
junções quando o desenho acerta o agregado. O custo é que o agregado é uma decisão irreversível
disfarçada de conveniência. Um dado que precisa aparecer em dois agregados será duplicado, e
mantê-los coerentes volta a ser problema da aplicação — exatamente a anomalia de atualização que a
normalização existia para evitar, agora sem o banco para ajudar.

**Grafo** privilegia a travessia: perguntas cuja resposta depende do caminho, com profundidade
variável e desconhecida na escrita da consulta. Em SQL, isso é junção recursiva, e o custo cresce
de forma que o otimizador estima mal. Fraude, permissões transitivas, cadeias de dependência e
relações societárias são os casos em que o modelo se paga. Quando a profundidade é fixa e pequena,
não se paga.

**Colunar** organiza o armazenamento por coluna e não por linha, o que muda a economia da leitura:
uma agregação sobre uma coluna toca apenas os blocos daquela coluna, e a homogeneidade de tipo
dentro do bloco permite compressão muito melhor. É a base técnica de quase todo sistema analítico
moderno, e é péssimo para ler ou atualizar uma linha inteira — que é a operação dominante da carga
transacional. A seção 2.2.6 depende deste parágrafo.

**Série temporal** assume que a escrita é quase sempre um acréscimo no fim, que a consulta é quase
sempre uma janela de tempo com agregação, e que o dado antigo perde resolução sem perder
utilidade. Sob essas três hipóteses, permite compressão e descarte automático que nenhum modelo
geral alcança. Fora delas, é um banco ruim.

Duas observações fecham a seção. A primeira: o modelo mais frequentemente escolhido pelo motivo
errado é o de documento, porque a fase inicial de um projeto premia a ausência de migração — e a
conta chega no ano dois, quando o agregado errado já tem volume. A segunda: manter vários motores
tem custo operacional real, e a persistência poliglota só se justifica quando a diferença de
padrão de acesso é grande o bastante para pagar backup, monitoramento, plantão e a coerência entre
duas fontes que agora podem discordar.

### 2.2.5 Consistência, replicação e CAP

O teorema CAP é o resultado mais citado e menos lido desta área. A conjectura é de Eric Brewer, em
2000; a prova formal, de Gilbert e Lynch, em 2002. O que ele afirma é estreito: quando há uma
partição de rede, um sistema replicado precisa escolher entre responder com risco de devolver dado
desatualizado e recusar-se a responder. Só isso.

A leitura popular — "escolha dois entre três" — é falsa e faz estrago. Não há um modo de operação
em que se abre mão da tolerância a partição em troca de consistência e disponibilidade: a partição
não é uma opção de projeto, é um evento que a rede impõe. Fora do período de partição, um sistema
pode oferecer consistência forte e alta disponibilidade ao mesmo tempo, e a maioria oferece. O
próprio Brewer publicou, em 2012, uma retratação sobre o quanto a formulação em três letras havia
induzido ao erro.

O modelo mais honesto é o PACELC, de Daniel Abadi, também de 2012: *se* houver partição (P), o
sistema escolhe entre disponibilidade e consistência (A/C); *senão* (E), no regime normal, ele
ainda escolhe entre latência e consistência (L/C). A segunda metade é a que descreve o dia a dia,
porque partições são raras e a espera pela confirmação de réplicas é permanente. É o trade-off que
aparece toda vez que alguém pergunta por que a leitura logo após a escrita não trouxe o valor novo.

A replicação organiza esse espaço em três topologias. **Líder único** dá uma ordem total de
escrita de graça e concentra a disponibilidade de escrita em um nó, transformando a eleição de
novo líder no ponto crítico. **Múltiplos líderes** aceita escrita em mais de um lugar e paga com
conflito, que precisa ser resolvido por alguma regra — última escrita vence, que perde dados de
forma silenciosa; um tipo de dado que converge por construção; ou uma decisão de negócio. **Sem
líder**, com quórum, troca a coordenação por aritmética: leituras e escritas em subconjuntos que
se sobrepõem. A promessa de que R + W > N garante leitura atualizada vale sob hipóteses mais
frágeis do que a fórmula sugere.

Do lado das garantias, o vocabulário precisa ser exato porque quase todo produto usa "consistente"
sem qualificar. **Linearizabilidade** é a mais forte: o sistema se comporta como se houvesse uma
única cópia e cada operação tomasse efeito num instante entre seu início e seu fim. **Consistência
causal** preserva a ordem entre eventos que se causaram, deixando os concorrentes livres, e é
frequentemente o melhor equilíbrio disponível. **Consistência eventual** afirma apenas que, na
ausência de novas escritas, as réplicas convergem — uma promessa sem prazo. Dizer que um sistema é
eventualmente consistente não é dizer quase nada; a pergunta operacional é qual é a janela típica,
qual é a de cauda, e o que a aplicação mostra ao usuário durante ela.

Vale registrar por que essa discussão pertence à camada geracional. Os nomes dos produtos que
implementam cada escolha mudam a cada poucos anos. A escolha em si — coordenar mais e esperar, ou
coordenar menos e conviver com divergência — não mudou desde que existem duas cópias do mesmo dado
em máquinas diferentes, e não há sinal de que mude.

### 2.2.6 OLTP vs. OLAP; warehouse, lake, lakehouse

A separação entre a carga que atende a transação e a carga que responde à pergunta é uma das
distinções mais estáveis da área, e é anterior à sigla. Codd popularizou o termo OLAP em 1993, mas
a prática de manter uma cópia separada para análise já existia porque o conflito é físico: a carga
transacional lê e escreve poucas linhas por vez, muitas vezes por segundo, e precisa de latência
baixa e previsível; a analítica varre milhões de linhas em poucas colunas e tolera segundos. As
duas competem pelo mesmo cache, pelos mesmos bloqueios e pelo mesmo disco. Rodá-las juntas degrada
a que importa mais.

O armazém de dados foi a primeira resposta institucional, e trouxe consigo uma divergência de
projeto que vale conhecer porque ela reaparece em toda plataforma nova. Inmon defendia um modelo
corporativo normalizado como fonte única, do qual saem recortes departamentais; Kimball defendia
esquemas dimensionais orientados ao processo de negócio, construídos de forma incremental. A
disputa nunca foi resolvida por evidência e continua viva com outros nomes. O que ambos acertaram
é o que ficou: transformação declarada, granularidade definida e linhagem rastreável.

O lago de dados foi a reação — e é um caso de manual do arco de quatro fases. Guardar tudo no
formato bruto e adiar o esquema para a leitura resolvia um gargalo verdadeiro, o de que modelar
antes de saber a pergunta descartava dado que depois faria falta. O custo apareceu na fase
seguinte: sem catálogo, sem contrato e sem responsável, um lago vira um pântano, e o adiamento do
esquema se converte em trabalho arqueológico feito por analista sem acesso a quem produziu o dado.
É o mesmo mecanismo do *schemaless* da seção 2.2.3, em escala corporativa.

O lakehouse é a síntese, e sua parte técnica é mais interessante que seu nome de marketing: os
formatos de tabela sobre arquivos — a linhagem do Iceberg, do Delta e do Hudi — devolvem ao lago
transação, evolução de esquema e viagem no tempo, mantendo o armazenamento barato e aberto. É uma
reconquista, não uma invenção: as propriedades sendo readicionadas são as que o armazém já tinha e
o lago abriu mão.

O que o leitor deve extrair não é a taxonomia. É a distinção entre o permanente e o sazonal dentro
dela. Permanente: separar as duas cargas, declarar a transformação, saber a granularidade e a
linhagem. Sazonal: os nomes das plataformas, e a arquitetura da moda que promete unificar as duas
cargas sem custo. Essa promessa reaparece a cada oito ou dez anos.

### 2.2.7 Migração e versionamento de esquema

O esquema é código, com uma diferença que muda tudo: implantar código novo descarta o antigo, e
migrar dados não. Reverter uma versão de aplicação é uma operação de segundos e sem perda.
Reverter uma migração que já removeu uma coluna exige um dado que não existe mais. É por isso que
a migração é, quase sempre, a parte mais arriscada de uma implantação — e a que recebe menos
revisão.

A técnica que resolve isso é antiga, tem vários nomes — expandir e contrair, mudança paralela — e
uma única ideia: nenhuma implantação deve conter simultaneamente uma mudança destrutiva de esquema
e a mudança de código que deixa de usar o que foi destruído. Separam-se em três passos, cada um
implantável e reversível sozinho. Primeiro, expandir: adicionar a estrutura nova sem remover a
antiga, e passar a escrever nas duas. Depois, migrar e ler da nova, com a antiga ainda intacta e o
código anterior ainda funcionando. Por fim, quando nenhuma versão em produção depende mais dela,
contrair: remover a antiga.

O passo do meio é o que costuma ser pulado, e é o que dá a propriedade que importa: durante toda a
janela, duas versões da aplicação coexistem em produção sobre o mesmo banco. Isso não é um detalhe
de sistemas grandes — é a condição de qualquer implantação gradual, de qualquer réplica que recebe
a atualização depois, e de qualquer reversão. Um esquema que só funciona com uma versão da
aplicação de cada vez impõe janela de indisponibilidade, e a impõe justamente no momento em que
seria preciso reverter.

Três exigências práticas decorrem disso, e valem como critério de revisão. Migrações versionadas,
ordenadas e aplicadas pela mesma ferramenta em todos os ambientes, incluindo a máquina de quem
desenvolve — migração aplicada à mão em produção é a origem de divergências que só aparecem meses
depois. Migrações idempotentes ou protegidas contra reaplicação, porque a que falha no meio será
executada de novo. E, para tabela grande, atenção ao bloqueio: alterações que reescrevem a tabela
ou seguram o cadeado por muito tempo derrubam o sistema mesmo quando o comando termina com
sucesso. Adicionar uma coluna anulável costuma ser barato; adicionar uma com valor padrão, ou uma
restrição validada sobre todo o histórico, frequentemente não é — e o comportamento varia entre
motores e versões, o que faz do teste em cópia de produção a única forma honesta de saber.

Ambler e Sadalage documentaram isso como refatoração de banco de dados em 2006, com o mesmo
argumento que Fowler usara para código: mudanças pequenas, com verificação a cada passo, são mais
seguras que a mudança grande e correta feita de uma vez. Vinte anos depois, o argumento continua
válido e a prática continua minoritária, porque o custo de pular o passo do meio só é cobrado no
dia da reversão.

### 2.2.8 Do campo: bases críticas em Sybase e SQL Server em produção contínua

*Esta seção é relato de campo. As afirmações abaixo são o argumento; os episódios concretos que as
sustentam entram na revisão — a regra da seção 1.3.4 vale aqui com força particular, porque
experiência pessoal é a evidência mais fácil de generalizar indevidamente.*

Sybase e SQL Server compartilham ancestral: o Microsoft SQL Server nasceu, no fim dos anos 1980,
de um acordo de licenciamento sobre o código do Sybase, e as bases seguiram caminhos separados
depois de 1994. Herdaram o mesmo T-SQL, o mesmo procedimento armazenado como unidade de
distribuição e a mesma cultura operacional. Para quem trabalhou em instituição financeira
brasileira, essa linhagem não é curiosidade histórica — é a razão de haver, em produção hoje,
sistemas cuja lógica de negócio mora no banco e não na aplicação.

Três observações que a experiência com esse tipo de base sustenta.

A primeira é sobre onde a lógica mora. Colocar regra de negócio em procedimento armazenado foi,
por muito tempo, a decisão correta: garantia transacional, ausência de tráfego de rede por linha e
um ponto único de aplicação da regra para clientes escritos em linguagens diferentes. As
consequências aparecem depois, e não invalidam a decisão original: o banco vira uma dependência
que não se pode testar isoladamente, o código escapa das ferramentas de versionamento e revisão do
resto da equipe, e a migração para qualquer outro motor deixa de ser uma troca de dialeto para se
tornar uma reescrita. É a Lei de Conway da seção 1.2.1 vista do lado dos dados: a estrutura de quem
tinha permissão de escrever ficou registrada no lugar onde a regra foi parar.

A segunda é sobre o custo do bloqueio. O modelo de concorrência tradicional dessa família era
baseado em bloqueio, não em versionamento de linha, e isso significa que leitor e escritor
disputam. Em base transacional com relatório rodando junto, uma consulta analítica mal escrita não
fica lenta apenas para si: ela segura o cadeado e a fila cresce atrás dela. Foi essa dinâmica, mais
do que qualquer argumento de arquitetura, que empurrou a separação entre carga transacional e
analítica da seção 2.2.6 — e é por isso que o isolamento por instantâneo, quando chegou, foi
tratado como recurso de sobrevivência e não como refinamento.

A terceira é sobre longevidade, e é a que interessa ao argumento do livro. Uma base assim é o
exemplo mais limpo do que a seção 0.1 chama de arqueologia: o conhecimento saiu da grade e do
mercado de contratação, continuou rodando operação crítica, e ficou concentrado em profissionais
que envelheceram junto com o sistema. A ferramenta está na camada sazonal; o que se aprende
mantendo-a, não. Modelagem, transação, plano de execução, bloqueio, migração sem janela — a lista
inteira deste capítulo é o que sobra quando o produto sai de cena, e é transferível para qualquer
motor que venha depois. É o argumento que o capítulo 2.6 vai retomar como carreira.

**Fontes primárias do capítulo.** Codd, E. F., ["A Relational Model of Data for Large Shared Data
Banks"](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf), *Communications of the ACM*, 1970 ·
Gray, J., [*The Transaction Concept: Virtues and
Limitations*](https://jimgray.azurewebsites.net/papers/thetransactionconcept.pdf), 1981 · Härder,
T. e Reuter, A., *Principles of Transaction-Oriented Database Recovery*, ACM Computing Surveys,
1983, DOI 10.1145/289.291 · Berenson, H. et al., [*A Critique of ANSI SQL Isolation
Levels*](https://arxiv.org/pdf/cs/0701157), SIGMOD, 1995 · Chang, F. et al., [*Bigtable: A
Distributed Storage System for Structured Data*](https://research.google/pubs/pub27898/), OSDI,
2006 · DeCandia, G. et al., [*Dynamo: Amazon Highly Available Key-value
Store*](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf), SOSP, 2007 ·
Gilbert, S. e Lynch, N., [*Brewer Conjecture and the Feasibility of Consistent, Available,
Partition-Tolerant Web Services*](https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf),
SIGACT News, 2002 · Brewer, E., [*CAP Twelve Years Later: How the Rules Have
Changed*](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/),
IEEE Computer, 2012 · Abadi, D., *Consistency Tradeoffs in Modern Distributed Database System
Design*, IEEE Computer, 2012 · Corbett, J. C. et al., [*Spanner: Globally-Distributed
Database*](https://research.google/pubs/pub39966/), OSDI, 2012 · Inmon, W. H., *Building the Data
Warehouse*, 1992 · Kimball, R., *The Data Warehouse Toolkit*, 1996 · Ambler, S. e Sadalage, P.,
*Refactoring Databases: Evolutionary Database Design*, 2006 · Kleppmann, M., *Designing
Data-Intensive Applications*, 2017.

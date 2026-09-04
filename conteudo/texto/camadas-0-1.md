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

---

## 2.3 · Sistemas distribuídos: fundamentos

A definição mais útil de sistema distribuído é a de Leslie Lamport, e ela é uma piada com
conteúdo técnico: é aquele em que a falha de um computador cuja existência você desconhecia
torna o seu inutilizável. O que a frase captura é a única novidade real da disciplina. Um
programa local falha inteiro ou funciona inteiro; um sistema distribuído falha em partes, e as
partes que continuam funcionando precisam decidir o que fazer sem saber o que aconteceu com as
outras.

Tudo o mais neste capítulo decorre disso. Timeouts existem porque não há como distinguir lento de
morto. Relógios lógicos existem porque não há um agora compartilhado. Consenso é caro porque
concordar exige rodadas de mensagens que podem se perder. Entrega exatamente uma vez é
impossível pelo mesmo motivo. São consequências de uma restrição física, não escolhas de
tecnologia — e é por isso que este capítulo está na camada geracional enquanto o 3.1, que trata
de estilos de arquitetura, está na cíclica.

Uma advertência de leitura: nada aqui é exclusivo de sistemas grandes. Duas máquinas já bastam.
Uma aplicação e um banco em servidores diferentes já é um sistema distribuído, e a maior parte
dos defeitos descritos adiante aparece nessa escala.

### 2.3.1 As oito falácias da computação distribuída

A lista nasceu na Sun Microsystems entre 1994 e 1997, atribuída principalmente a Peter Deutsch,
com a oitava acrescentada por James Gosling. Ela enumera premissas que quem programa carrega da
chamada local para a remota sem perceber: a rede é confiável; a latência é zero; a banda é
infinita; a rede é segura; a topologia não muda; existe um administrador; o custo de transporte é
zero; a rede é homogênea.

O valor da lista não está em cada item, que enunciado sozinho parece óbvio. Está no fato de que
todos os oito são verdadeiros dentro de um processo. Uma chamada de função não falha por perda de
pacote, não custa milissegundos, não tem limite de banda, não é interceptada, não muda de destino
no meio, não tem dono operacional distinto e não atravessa versões incompatíveis. Programar
distribuído é, em boa medida, desaprender oito hábitos que a programação local ensinou como
naturais — o que conecta diretamente à seção 1.4.4, sobre a habilidade de desaprender.

A crítica mais precisa dessa herança está no artigo de Waldo, Wyant, Wollrath e Kendall, de 1994,
*A Note on Distributed Computing*. O argumento é que a chamada remota de procedimento erra na
premissa: tentar fazer o remoto parecer local não simplifica o problema, apenas esconde o momento
em que ele aparece. Latência, memória compartilhada, falha parcial e concorrência não são
detalhes de implementação que uma boa abstração possa encapsular — são diferenças de tipo. A
abstração que promete transparência entrega surpresa, e a surpresa chega em produção.

Trinta anos depois, o padrão se repete a cada geração de ferramenta. O ORB dos anos 1990, o
serviço web dos anos 2000, o cliente HTTP gerado por especificação e a malha de serviços dos anos
2010 são todos, em alguma medida, tentativas de tornar a chamada remota confortável. Todas úteis;
nenhuma capaz de revogar a física. O sinal de alerta é sempre o mesmo: quando o código de chamada
não tem onde declarar timeout, política de nova tentativa e comportamento em falha, a abstração
não removeu essas decisões — apenas as tomou por você, e provavelmente mal.

### 2.3.2 Latência e throughput — as ordens de grandeza

Existe um conjunto de números que decide arquitetura antes de qualquer discussão de estilo, e
quase nenhum currículo pede que sejam memorizados. Não é preciso precisão: o que importa é a
ordem de grandeza, porque as decisões que eles governam mudam quando o expoente muda.

Uma referência de leitura em cache L1 fica na casa do nanossegundo. Um acesso à memória
principal, na casa da centena de nanossegundos — cerca de cem vezes mais. Uma leitura de SSD fica
entre dezenas e centenas de microssegundos; uma busca em disco rotacional, na casa de dez
milissegundos. Uma ida e volta de rede dentro do mesmo centro de dados custa em torno de meio
milissegundo. Entre continentes, a viagem é limitada pela velocidade da luz na fibra e fica na
casa da centena de milissegundos — São Paulo a Frankfurt não sai por menos de uma centena, e
nenhuma otimização de software altera isso.

A conclusão prática que esses números impõem é que a diferença entre memória e rede é de cerca de
mil vezes, e entre rede local e intercontinental, de mais de cem. Uma decisão de projeto que
transforma um acesso em memória numa chamada de rede não é um refinamento: é uma mudança de três
ordens de grandeza. É por isso que a chamada remota dentro de um laço é o defeito de desempenho
mais comum e mais caro em sistemas distribuídos, e por que ele quase nunca aparece em ambiente de
desenvolvimento, onde tudo roda na mesma máquina.

Latência e vazão são independentes e frequentemente confundidas. Vazão é quanto trabalho passa
por unidade de tempo; latência é quanto demora um item. Acrescentar paralelismo aumenta vazão e
não reduz o piso de latência — dez conexões não fazem a luz andar mais rápido. Pior: acrescentar
paralelismo sobre um recurso saturado aumenta a latência, porque a fila cresce. A Lei de Little
formaliza a relação e é a ferramenta mais barata para prever isso: em regime estável, o número
médio de itens no sistema é a taxa de chegada multiplicada pelo tempo médio de permanência.

Por fim, a média mente, e mente de forma sistemática. A distribuição de latência tem cauda longa,
e a experiência do usuário mora na cauda. O artigo de Dean e Barroso, de 2013, mostra por que isso
piora com a escala: se uma requisição consulta cem serviços em paralelo e cada um tem uma chance
em cem de estar lento, a maioria das requisições encontra pelo menos um lento. O percentil 99 de
um componente vira o caso típico da requisição composta. Quem monitora média não vê nada disso, e
otimiza o caso que não importa — é a mesma observação que a seção 1.1.2 faz sobre por que
probabilidade ganhou peso na prática.

### 2.3.3 Falha parcial: timeout, retry, backoff, idempotência

Quando uma chamada local falha, você recebe uma exceção. Quando uma chamada remota não responde,
você não recebe nada — e "nada" é ambíguo de forma irredutível. A requisição pode ter se perdido
na ida, pode ter sido processada com a resposta perdida na volta, ou pode estar sendo processada
neste instante. As três situações são indistinguíveis do lado do cliente, e exigem condutas
diferentes. Este é o problema central do capítulo.

O timeout é o mecanismo que converte "nada" em decisão, e é necessariamente imperfeito: ele adota
um limite arbitrário para declarar morto o que talvez esteja apenas lento. Timeout curto demais
descarta trabalho bom e multiplica carga; longo demais consome a conexão, a thread e a paciência
de quem chamou. A ausência de timeout é a pior das três, e é o padrão de muitos clientes HTTP —
uma chamada sem prazo transfere ao servidor remoto o controle sobre a disponibilidade do seu
sistema.

A nova tentativa é o reflexo natural, e é também a forma mais eficiente de derrubar um sistema que
está apenas degradado. Um serviço lento provoca timeouts; os timeouts provocam novas tentativas;
as novas tentativas triplicam a carga exatamente sobre o componente que já não dava conta. O
sistema entra num estado em que a carga gerada pelo próprio mecanismo de recuperação impede a
recuperação, e remover a causa original não basta para sair dele. Sistemas com essa propriedade
são chamados de metaestáveis, e o padrão é reconhecível: o incidente continua depois que o gatilho
acabou.

Três correções fazem a diferença entre nova tentativa útil e amplificação. Recuo exponencial, para
que a pressão caia enquanto o serviço se recupera. Aleatorização do intervalo, sem a qual todos os
clientes voltam ao mesmo tempo e reproduzem o pico — o efeito de rebanho. E orçamento de tentativa
por caminho, não por camada: quando cada uma de quatro camadas repete três vezes, uma requisição
vira oitenta e uma, e a multiplicação é invisível em qualquer código isolado. Vale acrescentar
uma quarta: só repetir o que ainda importa. Repetir uma requisição cujo cliente já desistiu é
trabalho garantidamente inútil sob a carga máxima.

Nada disso é seguro sem idempotência. Uma operação é idempotente quando executá-la mais de uma vez
produz o mesmo efeito de executá-la uma vez. Leitura costuma ser idempotente de graça; escrita não
é, e é onde o dinheiro está. A técnica padrão é a chave de idempotência: o cliente gera um
identificador único para a intenção, o servidor registra o resultado associado a essa chave dentro
da mesma transação que aplica o efeito, e uma repetição devolve o resultado guardado em vez de
executar de novo. O detalhe que costuma ser errado é o "dentro da mesma transação": registrar a
chave fora da transação do efeito recria exatamente a janela que se queria fechar.

A regra que resume a seção: repetir sem idempotência não é resiliência, é corrupção de dados com
passos adicionais. E a pergunta que todo projeto de integração deveria responder por escrito é
qual operação, no caminho crítico, seria executada duas vezes se a resposta se perdesse — e o que
aconteceria.

### 2.3.4 Relógios, ordenação, quórum e consenso

Não existe um agora compartilhado. Cada máquina tem seu relógio, e relógios divergem: derivam por
temperatura e imprecisão do oscilador, são corrigidos por NTP em saltos que podem andar para trás,
e sofrem com segundos bissextos. A consequência é que comparar dois carimbos de tempo produzidos
em máquinas diferentes não estabelece ordem — estabelece uma suposição.

A distinção mínima que todo programador deveria carregar é entre o relógio de parede, que informa
data e hora e pode saltar, e o relógio monótono, que só avança e serve para medir intervalos.
Medir duração com relógio de parede é a origem de durações negativas em log de produção, e de
timeouts que expiram cedo ou nunca depois de um ajuste de horário. A regra é curta: parede para
registrar quando; monótono para medir quanto tempo.

O caso perigoso é a resolução de conflito por "última escrita vence". Ela parece uma regra de
desempate neutra e é, na prática, uma decisão de descartar dados com base em relógios que ninguém
está auditando. Se o relógio de um nó está adiantado em dois segundos, escritas legítimas feitas
depois são descartadas em favor de escritas mais antigas, silenciosamente e sem erro. É um dos
poucos mecanismos capazes de perder dados confirmados sem produzir nenhum sinal.

Lamport resolveu a parte conceitual em 1978, e a solução é uma das ideias mais elegantes da área:
abandonar o tempo físico e definir ordem por causalidade. Um evento acontece-antes de outro se o
precede no mesmo processo ou se há uma mensagem entre eles; eventos sem essa relação são
concorrentes, e concorrentes não têm ordem — não porque falte informação, mas porque a pergunta
não tem sentido. Relógios lógicos numeram eventos preservando essa relação; relógios vetoriais
permitem detectar concorrência em vez de fingir uma ordem. Quase todo sistema replicado sério usa
alguma variante disso.

Quando a aplicação de fato precisa de uma decisão única e irrevogável — quem é o líder, se a
transação foi confirmada, qual valor ficou registrado —, entra o consenso. É um problema com
resultado de impossibilidade conhecido: Fischer, Lynch e Paterson mostraram, em 1985, que em um
sistema assíncrono não existe algoritmo determinístico que garanta consenso mesmo com um único
processo defeituoso. A prática convive com isso porque relaxa as hipóteses: assume sincronia
parcial, usa timeouts como detectores imperfeitos de falha e aceita perder progresso durante
períodos ruins, sem nunca perder correção. Paxos, descrito por Lamport, e Raft, de Ongaro e
Ousterhout, são as duas famílias dominantes — a segunda projetada explicitamente para ser
compreensível, o que é um objetivo de engenharia legítimo e raramente declarado.

A lição de projeto é econômica, não algorítmica. Consenso custa rodadas de rede e disponibilidade:
sem quórum, não há decisão. Sistemas bem projetados não evitam o consenso, eles o confinam —
usam-no para escolher líder, registrar configuração ou confirmar transação, e mantêm o caminho
quente fora dele. Perguntar "o que aqui realmente exige acordo entre nós?" costuma revelar que a
resposta é bem menos do que o desenho inicial assumia.

### 2.3.5 Garantias de entrega — e o mito do exactly-once

Há três garantias possíveis para a entrega de uma mensagem, e apenas duas delas existem. **No
máximo uma vez** é enviar sem confirmação: nunca há duplicata, e pode haver perda. **Pelo menos
uma vez** é repetir até obter confirmação: nunca há perda, e pode haver duplicata. **Exatamente
uma vez**, como propriedade da rede, não existe.

A impossibilidade é o problema dos dois generais, e o argumento cabe em um parágrafo. Para que o
remetente saiba que a mensagem chegou, precisa de uma confirmação. Para que o destinatário saiba
que a confirmação chegou, precisa de uma confirmação da confirmação. A recursão não termina, e em
nenhum ponto finito os dois lados compartilham certeza. Como não há como saber se a mensagem
chegou, não há como decidir entre reenviar — arriscando duplicata — e não reenviar, arriscando
perda. A escolha entre as duas garantias reais é obrigatória.

O que existe, e é frequentemente vendido sob o nome errado, é o efeito de uma vez só: entrega pelo
menos uma vez combinada com processamento idempotente. A duplicata acontece na rede e é absorvida
no destino, pela chave de idempotência da seção anterior ou por uma operação naturalmente
idempotente. O resultado observável é o de execução única, e o mecanismo que o produz está no
destino — não no transporte.

Vale desfazer a confusão de marketing com precisão, porque ela custa caro em projeto. Quando um
sistema de mensageria anuncia semântica exatamente uma vez, o que ele normalmente oferece é uma
transação que abrange consumir, processar e produzir dentro do seu próprio domínio. É real e é
útil. Mas assim que o processamento toca algo fora desse domínio — cobrar um cartão, enviar um
e-mail, chamar uma API de terceiro —, a garantia termina na fronteira, e o efeito colateral
externo pode acontecer duas vezes. A regra: a garantia vale até onde vai a transação, e nunca
mais longe.

Há um corolário que ordena o projeto de integrações. Como duplicata é inevitável e perda é
inaceitável na maior parte dos casos de negócio, o desenho correto é quase sempre pelo menos uma
vez com consumidor idempotente. Isso transfere o trabalho para o destino, onde ele é resolvível,
em vez de deixá-lo no transporte, onde não é.

### 2.3.6 Padrões de resiliência

Os padrões desta seção têm um objetivo comum, e enunciá-lo primeiro evita tratá-los como
receituário: todos existem para impedir que uma falha local vire uma falha global. A pergunta que
cada um responde é como conter o dano quando uma dependência para de funcionar — e a resposta
nunca é continuar tentando como se nada tivesse acontecido.

O **disjuntor**, popularizado por Michael Nygard em *Release It!*, em 2007, observa a taxa de erro
de uma dependência e, ultrapassado um limiar, passa a falhar imediatamente sem tentar a chamada.
Depois de um intervalo, deixa passar algumas requisições de teste e volta a fechar se elas
funcionarem. O ganho é duplo: o chamador para de gastar threads e prazo esperando o que vai falhar,
e o chamado deixa de receber carga enquanto tenta se recuperar. O erro comum é tratá-lo como
recurso de infraestrutura e esquecer a parte de aplicação — o que a chamada devolve enquanto o
disjuntor está aberto é uma decisão de negócio, não um detalhe técnico.

A **antepara** isola recursos para que o esgotamento em um caminho não consuma o que os outros
precisam. O nome vem da compartimentação de cascos de navio, e a imagem é exata: sem divisórias,
um furo afunda tudo. Na prática significa pools de conexão, filas e limites de concorrência
separados por dependência. É o padrão que evita que um serviço secundário e lento consuma todas as
threads e derrube o fluxo principal, que estava perfeitamente saudável.

A **contrapressão** é a mais importante e a menos implementada. Quando a produção supera o
consumo, alguém precisa desacelerar. Se ninguém desacelera, a fila cresce, e uma fila que cresce
sem limite não é um amortecedor: é um amplificador de latência que termina em falta de memória. A
consequência incômoda, mas correta, é que rejeitar trabalho é um recurso de projeto. Um sistema que
aceita tudo o que lhe oferecem está prometendo o que não pode cumprir, e vai descobrir isso da
pior forma — respondendo devagar para todo mundo em vez de bem para a parte que consegue atender.
Descartar carga cedo e de forma seletiva, preservando o que tem prazo válido e o que é prioritário,
é preferível a degradar uniformemente.

Duas ideias transversais fecham a seção. A primeira é o prazo como orçamento: um prazo definido na
borda deve ser propagado e decrementado a cada salto, de modo que nenhuma camada trabalhe por algo
que já expirou para quem pediu. Timeouts fixos e independentes por camada garantem trabalho
desperdiçado e prazos que somam mais do que o cliente espera. A segunda é a degradação planejada:
decidir de antemão o que o sistema faz sem cada dependência — cache velho, resposta parcial,
recurso desligado com aviso — em vez de descobrir no incidente. É a mesma exigência que a seção
0.3 faz às fichas: um sistema bem projetado sabe dizer o que aconteceria se cada peça sua estivesse
errada.

### 2.3.7 Por que este capítulo é geracional e o 3.1 é cíclico

A separação entre este capítulo e o de arquitetura é a decisão editorial mais defendível do livro,
e vale expor o critério.

Nada do que está aqui mudou de substância nas últimas quatro décadas. As falácias são de 1994 e
descrevem 2026 sem ajuste. O acontece-antes de Lamport é de 1978. A impossibilidade de FLP é de
1985. O problema dos dois generais é anterior à internet comercial. O que mudou foi o vocabulário,
a qualidade das bibliotecas e a frequência com que um programador comum encontra esses problemas —
não os problemas.

Já o capítulo 3.1 trata de estilos: monolito, SOA, microsserviços, sem servidor, monolito modular.
Esses oscilam em ciclos de cinco a quinze anos, e oscilam de verdade, com retornos. A ida e a volta
entre centralizar e distribuir é o pêndulo que a seção 0.1 mencionou, e ele continua se movendo.

Misturar as duas coisas é o mecanismo específico que faz um currículo envelhecer mal, e o efeito é
assimétrico. Quem aprende o fundamento e depois o estilo consegue avaliar o estilo: sabe perguntar
onde está a falha parcial, quanto consenso o desenho exige, o que acontece com a duplicata, quem
exerce contrapressão. Quem aprende só o estilo reproduz o desenho e redescobre cada falha desta
lista pela via cara — e, quando o estilo sai de moda, fica sem nada transferível.

O teste da seção 1.3.1 se aplica bem aqui. Estes conteúdos sobreviveram a mudanças de linguagem,
de hardware, de modelo de implantação e de estilo arquitetural, e não há eixo de ruptura visível
que os ameace: enquanto houver mais de uma máquina e uma rede imperfeita entre elas, valem. É o
que os coloca na camada geracional — e o que justifica estudá-los antes, e não depois, de escolher
uma arquitetura.

**Fontes primárias do capítulo.** Waldo, J., Wyant, G., Wollrath, A. e Kendall, S., [*A Note on
Distributed Computing*](https://scholar.harvard.edu/files/waldo/files/waldo-94.pdf), Sun
Microsystems, 1994 · Deutsch, P. e Gosling, J., *The Eight Fallacies of Distributed Computing*,
Sun Microsystems, 1994–1997 · Lamport, L., [*Time, Clocks, and the Ordering of Events in a
Distributed System*](https://lamport.azurewebsites.net/pubs/time-clocks.pdf), Communications of
the ACM, 1978 · Fischer, M., Lynch, N. e Paterson, M., [*Impossibility of Distributed Consensus
with One Faulty Process*](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf), JACM, 1985 ·
Lamport, L., [*Paxos Made Simple*](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf),
2001 · Ongaro, D. e Ousterhout, J., [*In Search of an Understandable Consensus Algorithm
(Raft)*](https://raft.github.io/raft.pdf), USENIX ATC, 2014 · Dean, J. e Barroso, L. A., [*The
Tail at Scale*](https://research.google/pubs/pub40801/), Communications of the ACM, 2013 ·
Nygard, M., *Release It! Design and Deploy Production-Ready Software*, 2007 · Little, J. D. C.,
*A Proof for the Queuing Formula L = λW*, Operations Research, 1961 · Kleppmann, M., *Designing
Data-Intensive Applications*, 2017, capítulos 8 e 9.

---

## 2.4 · Linguagens de programação

Uma linguagem de programação parece o exemplo perfeito de conhecimento perecível, e é por isso
que este capítulo está na camada geracional e não na sazonal. Linguagens individuais envelhecem;
o padrão pelo qual envelhecem não mudou em cinquenta anos. Quem entende o padrão consegue prever
o comportamento de uma linguagem que ainda não existe, e essa é a única forma de conhecimento
sobre linguagens que vale a pena ensinar como currículo.

O capítulo também precisa desfazer uma expectativa. A pergunta que os alunos fazem — qual
linguagem devo aprender — é a menos útil que se pode fazer sobre o assunto, e a resposta honesta
é decepcionante: a que o trabalho à sua frente exige, e depois mais uma de paradigma diferente,
pelo motivo que a seção 1.4.5 já estabeleceu. O que decide carreira não é a linguagem; é o que se
sabe fazer com qualquer uma delas.

### 2.4.1 Linha do tempo por geração

A taxonomia por gerações é o modo tradicional de contar essa história, e vale contá-la sabendo
que ela própria envelheceu — o que a torna um bom primeiro exemplo do argumento do livro.

A **primeira geração** é a linguagem de máquina: o código que o processador executa, escrito
diretamente em números. A **segunda** é o assembly, que substitui números por mnemônicos e
introduz a primeira abstração real, o montador. Nenhuma das duas desapareceu; ambas migraram para
nichos — compiladores, sistemas embarcados de recurso escasso, otimização pontual, engenharia
reversa.

A **terceira geração** é onde vive quase tudo que se usa hoje: linguagens de alto nível com
comandos, procedimentos e independência relativa da máquina. FORTRAN, em 1957, provou que um
compilador podia gerar código competitivo com o escrito à mão, o que era a objeção central da
época. COBOL, em 1959, apostou numa sintaxe próxima do inglês para que o programa fosse legível
por quem não programava — aposta que não se cumpriu como se esperava, e que mesmo assim produziu
o corpo de código mais longevo da história. ALGOL 60 consolidou blocos e escopo e virou o
ancestral gramatical de quase todo o resto. C, em 1972, ofereceu abstração portável com acesso à
máquina, e por isso continua sendo a língua franca entre sistemas.

A **quarta geração** é onde a taxonomia começa a falhar. A ideia era subir mais um degrau de
abstração com linguagens declarativas e específicas de domínio: geradores de relatório,
ferramentas de banco de dados, ambientes de desenvolvimento rápido. O membro que sobreviveu com
folga é o SQL, e ele sobreviveu por ser genuinamente declarativo — descreve o resultado, não o
caminho, que é a mesma independência da seção 2.2.1. A maioria dos outros 4GLs morreu junto com
o produto que os hospedava, e essa correlação é o assunto da seção 2.4.2.

A **quinta geração** foi definida por objetivo, não por forma: linguagens de programação lógica e
por restrições, associadas à ambição de inteligência artificial dos anos 1980, com Prolog como
representante e o projeto japonês de Quinta Geração como marco. O objetivo não se cumpriu no prazo
prometido, e a categoria ficou órfã — sobreviveram as técnicas, absorvidas por resolvedores de
restrições e por linguagens de propósito geral, no mesmo movimento de absorção que a seção 2.1.3
descreveu para o paradigma funcional.

A **sexta geração** não tem definição estável, e é exatamente aí que a taxonomia deixa de
descrever. Já foi usada para redes neurais, para linguagens visuais e, mais recentemente, para
programação assistida por modelo de linguagem. Um esquema classificatório que precisa ser
reinterpretado a cada década para acomodar o presente parou de ser descritivo e virou vocabulário
cerimonial. Vale ensiná-lo pelo que ele registra até a quarta geração, e vale dizer ao aluno,
explicitamente, que dali em diante ele é um artefato de ementa — o tipo de conteúdo que a seção
0.4 chama de arqueologia ensinada sem aviso.

### 2.4.2 O padrão de envelhecimento — adoção, platô, nicho, manutenção

Linguagens seguem o arco de quatro fases da seção 0.1, com duas particularidades: a escala de
tempo é mais longa que a de frameworks, e a fase final é mais habitada.

Na **adoção**, a linguagem cresce ligada a uma plataforma, a um problema ou a uma empresa que a
patrocina. Quase nenhuma linguagem se populariza por mérito linguístico isolado: ela pega carona.
Java cresceu com a web corporativa e a promessa de portabilidade; JavaScript, por ser a única
opção dentro do navegador; Objective-C e depois Swift, por decisão de uma fabricante; Python, por
uma sucessão de nichos — scripting, ciência, ensino, dados. O mérito técnico importa para que a
linguagem sobreviva à carona, não para conseguir a carona.

No **platô**, ela vira infraestrutura. Aparece em vagas pelo nome, tem livros de referência,
ferramentas maduras e, o marcador mais confiável, é usada por muita gente que não a escolheu.
Nessa fase, a evolução da linguagem passa a ser limitada por compatibilidade retroativa, e o
debate interno da comunidade muda de "o que podemos acrescentar" para "o que podemos acrescentar
sem quebrar o que existe".

No **nicho**, ela deixa de ser escolha padrão para software novo, mas continua dominante em um
recorte. Perl saiu do desenvolvimento web e continuou vivo em processamento de texto e
administração de sistemas; Fortran nunca saiu de computação numérica de alto desempenho; Lisp
permanece onde a manipulação de código como dado é o requisito.

Na **manutenção**, o software novo praticamente cessa e o corpo existente continua rodando,
sustentado por profissionais cada vez mais escassos. É o estado de COBOL, de Visual Basic 6, de
Delphi em muitos contextos — e é o assunto da próxima seção.

A observação mais útil do capítulo é sobre a causa da morte. Linguagens raramente são substituídas
por linguagens melhores; elas morrem quando a plataforma ou o nicho que as sustentava desaparece.
ActionScript não perdeu para uma linguagem: perdeu com o fim do Flash. Visual Basic 6 não perdeu
em uma comparação técnica: perdeu quando a Microsoft mudou de plataforma. A implicação prática é
que, ao avaliar o risco de longo prazo de uma linguagem, a pergunta certa não é sobre a linguagem —
é sobre a saúde e a independência da plataforma à qual ela está amarrada.

### 2.4.3 Por que COBOL não morreu, e o que isso ensina sobre o resto

COBOL é o contraexemplo mais útil da área, porque contraria a intuição de que o melhor vence e a
de que o antigo desaparece. Sessenta e poucos anos depois de criado, ele continua executando
processamento de lote em folha de pagamento, seguro e serviços financeiros — inclusive no Brasil,
inclusive em instituições que se apresentam como modernas.

Três forças explicam a longevidade, e nenhuma é técnica no sentido usual.

A primeira é a assimetria de risco. Reescrever um sistema que funciona e movimenta dinheiro tem
prejuízo ilimitado e ganho limitado: o melhor resultado possível é que tudo continue exatamente
como estava, e qualquer desvio é perda. Nenhum executivo é promovido por uma migração que deu
certo, e vários são demitidos por uma que deu errado. É a mesma economia da decisão que o capítulo
3.7 vai tratar de frente.

A segunda é que a regra de negócio não está documentada em outro lugar. Décadas de exceções
legais, acordos comerciais e correções pontuais foram registradas apenas como código. Reescrever
exige primeiro descobrir o que o sistema faz — e essa descoberta é uma pesquisa arqueológica, não
um projeto de engenharia com escopo previsível. É o mesmo mecanismo da seção 2.2.8, quando a regra
mora no procedimento armazenado.

A terceira é que COBOL é bom no que faz. Processamento sequencial de grandes volumes com aritmética
decimal exata é precisamente o problema para o qual ele foi projetado, e a aritmética decimal não é
detalhe: representar dinheiro em ponto flutuante binário produz erro de arredondamento que
auditoria não aceita. Muitas linguagens modernas só oferecem esse tipo por biblioteca, e muita
migração descobre isso tarde.

A lição generaliza, e é uma das mais importantes do livro. O que mantém um sistema vivo não é a
qualidade da tecnologia, é o custo de substituí-lo comparado ao benefício. Todo software que hoje
se escreve em linguagem moderna e da moda será, se der certo, o legado de alguém em vinte anos —
sustentado por profissionais que não escolheram aquela linguagem e que a aprenderão porque o
sistema importa. Ensinar isso muda a relação do aluno com o legado: ele deixa de ser um castigo e
vira uma categoria previsível de trabalho, frequentemente bem paga e mal ensinada.

### 2.4.4 Ecossistema e gerenciador de pacotes decidem mais que sintaxe

Comparações de linguagem quase sempre discutem sintaxe e sistema de tipos, que são a parte
visível e a menos determinante. Na prática, o que decide produtividade e risco é o que vem em
volta: a biblioteca padrão, o gerenciador de pacotes, a ferramenta de build, o depurador, o
formatador, o servidor de linguagem, a qualidade das mensagens de erro do compilador e o tamanho
do conjunto de pessoas que se pode contratar.

O gerenciador de pacotes merece destaque porque mudou a natureza do trabalho. Ele resolveu um
problema real — reúso — e criou outro, que é a dependência transitiva. Um projeto declara vinte
dependências e instala mil e duzentas, das quais conhece vinte. Cada uma dessas mil e duzentas é
código de terceiro executando com os mesmos privilégios do seu, mantido por pessoas que você não
conhece, sob governança que você não verificou. O incidente do pacote de onze linhas removido do
npm em 2016, que quebrou a construção de milhares de projetos, é o exemplo didático: não porque o
pacote fosse importante, mas porque expôs que ninguém sabia que dependia dele.

Isso transforma escolha de linguagem em decisão de cadeia de suprimentos, e é a ponte para o
capítulo 4.1. As perguntas que separam ecossistemas maduros dos imaturos são operacionais: existe
arquivo de trava com verificação de integridade? Há como auditar o que foi instalado? A publicação
de pacote exige segundo fator? Existe caminho para fixar uma versão sem congelar a segurança? A
biblioteca padrão cobre o suficiente para que a árvore de dependências seja rasa?

A última pergunta é a mais subestimada. Uma biblioteca padrão abrangente não é conforto: é redução
de superfície de ataque e de trabalho de manutenção. Ecossistemas que cultivam bibliotecas padrão
pequenas transferem para cada projeto a responsabilidade de montar e manter a sua — e a maioria
dos projetos monta mal.

### 2.4.5 Runtimes e interoperabilidade — JVM, CLR, WASM

Há uma camada abaixo da linguagem que envelhece ainda mais devagar do que ela, e que raramente
recebe atenção no ensino: o ambiente de execução. A observação central é que o runtime costuma
sobreviver à linguagem que o originou, e que apostar no runtime é frequentemente mais seguro do
que apostar na linguagem.

A **JVM** foi construída para Java e hoje hospeda Kotlin, Scala e Clojure — linguagens com
filosofias incompatíveis entre si, compartilhando coletor de lixo, modelo de memória, formato de
biblioteca e ferramental de observação. Uma equipe que migrou de Java para Kotlin não trocou de
plataforma: trocou de sintaxe sobre a mesma plataforma, o que explica por que a migração é
incremental e barata. A **CLR** repetiu o padrão com C#, F# e VB.NET, com a interoperabilidade
como objetivo declarado desde o início.

O **WebAssembly** é a aposta mais recente e a mais interessante do ponto de vista deste livro. Não
é uma linguagem: é um alvo de compilação portável, com execução em caixa de areia e modelo de
segurança explícito por capacidades. Nasceu no navegador para permitir que código escrito em C,
Rust e outras linguagens rodasse ali com desempenho previsível, e saiu do navegador para servidor,
borda e plugins. Se cumprir a promessa, será a segunda vez que a indústria constrói uma camada de
portabilidade abaixo da linguagem — e a primeira em que ela nasce com o isolamento como requisito,
e não como remendo.

Uma ressalva de honestidade, porque este é o parágrafo mais perecível do capítulo: WASM está entre
emergência e consolidação. Há adoção real fora de quem o criou e casos documentados em produção, o
que são bons sinais pelo critério da seção 0.5. Não há ainda a evidência de longo prazo que só o
tempo produz, e um capítulo escrito em 2026 não pode fingir que há. A ficha registra isto como
gatilho de revisão.

A lição transferível: quando avaliar longevidade, olhe uma camada abaixo do que está sendo
vendido. A linguagem é a parte visível; o runtime, o formato de bytecode e o modelo de memória são
o que determina se haverá caminho de saída daqui a dez anos.

### 2.4.6 Como escolher uma linguagem sem escolher uma moda

A escolha de linguagem é uma decisão de arquitetura com prazo de vida longo e custo de reversão
alto, e merece o mesmo rigor que a seção 3.1.8 vai exigir para ADRs. O que segue são critérios,
não uma resposta.

**Existe evidência de uso em produção, na sua escala e no seu domínio?** Não em conferência, não em
postagem de blog de quem criou a linguagem — em produção, contada por quem operou e teve problemas.
É o mesmo critério da seção 0.5 para distinguir emergência de barulho.

**Quem mantém, sob qual governança, e o que acontece se essa parte perder o interesse?** Linguagem
mantida por uma única empresa sem fundação independente tem um risco que linguagem com governança
distribuída não tem. Não é impedimento; é um fator a declarar.

**Qual é o histórico de compatibilidade?** Este é o critério mais previsível e o menos usado. A
transição de Python 2 para 3 levou mais de uma década e dividiu o ecossistema, e foi feita por um
projeto sério com boas intenções; a promessa explícita de compatibilidade de Go e o compromisso
histórico da plataforma Java são o contraexemplo. O histórico passado de quebra é o melhor
previsor do custo de manutenção futuro.

**Você consegue contratar, e consegue formar?** Um ecossistema pequeno pode ser tecnicamente
superior e ainda assim ser a escolha errada para uma equipe que precisa crescer. Vale o inverso: a
linguagem popular pode trazer um conjunto de candidatos grande e raso.

**Qual é o custo de saída?** Se em cinco anos a decisão se mostrar errada, o que é preciso reescrever?
Sistemas que confinam a linguagem atrás de fronteiras claras — processos separados, contratos de
API, formatos de dados neutros — pagam menos por um erro de escolha. É a mesma lógica da seção
1.2.4: esconder a decisão que pode mudar.

Duas conclusões desconfortáveis fecham o capítulo. A primeira é que, para a maioria das equipes, a
resposta certa é a linguagem que a equipe já domina, e a justificativa técnica para trocar precisa
ser maior do que costuma ser. A segunda é que índices de popularidade — os que contam menções,
buscas ou repositórios — medem atenção, não adequação, e não respondem a nenhuma das cinco
perguntas acima. Usá-los como critério de decisão é terceirizar arquitetura para uma métrica que
ninguém auditou.

**Fontes primárias do capítulo.** Backus, J. W. et al., [*The FORTRAN Automatic Coding
System*](https://archive.computerhistory.org/resources/text/Fortran/102663113.05.01.acc.pdf),
1957 · CODASYL, *COBOL Report*, 1960 · Naur, P. (ed.), [*Revised Report on ALGOL
60*](https://archive.computerhistory.org/resources/text/algol/algol_bulletin/EX/RR60/INDEX.HTM),
1963 · Ritchie, D., *The Development of the C Language*, HOPL-II, 1993 · Sammet, J.,
*Programming Languages: History and Fundamentals*, 1969 · Codd, E. F., *A Relational Model of
Data for Large Shared Data Banks*, 1970, para a linhagem declarativa do SQL · Lindholm, T. e
Yellin, F., *The Java Virtual Machine Specification*, 1996 · Haas, A. et al., [*Bringing the Web
up to Speed with WebAssembly*](https://dl.acm.org/doi/10.1145/3062341.3062363), PLDI, 2017 ·
[*The Go 1 Compatibility Promise*](https://go.dev/doc/go1compat), 2012 · Python Software
Foundation, [*PEP 373 — Python 2.7 Release Schedule*](https://peps.python.org/pep-0373/), sobre o
encerramento do suporte em 2020.

---

## 2.5 · Requisitos, produto e IHC

Este é o capítulo que a maioria dos currículos de computação trata como acessório e que a prática
trata como decisivo. A estatística que sustenta a afirmação é antiga e incômoda: desde os relatórios
de fracasso de projeto dos anos 1990, a causa dominante nunca foi incompetência técnica — foi
construir a coisa errada, ou construir a coisa certa para um entendimento errado do problema.
Software que funciona perfeitamente e resolve o problema errado é uma falha de engenharia, não um
mal-entendido de negócio.

O capítulo está na camada geracional porque seu conteúdo é sobre pessoas e sobre a estrutura do
problema, não sobre ferramentas. O vocabulário mudou várias vezes — especificação, caso de uso,
história, tarefa a ser feita, descoberta contínua — e as questões por baixo do vocabulário são as
mesmas desde que existe encomenda de software.

### 2.5.1 Levantamento e descoberta — o problema atrás do pedido

A distinção que organiza a seção é entre o pedido e o problema. Um pedido é uma solução já
escolhida por quem tem o problema, e vem embrulhada como requisito: "quero um botão de exportar
para Excel". O problema atrás dele pode ser outro completamente — a pessoa precisa conferir números
com um colega que não tem acesso ao sistema, e a exportação é a única via que ela conhece. Atender
ao pedido resolve o sintoma e cria manutenção permanente; entender o problema pode revelar que a
resposta é acesso de leitura para o colega.

Isso não autoriza ignorar o que o usuário pede. O erro simétrico, e mais comum entre pessoas
técnicas, é presumir que se entende o problema melhor do que quem convive com ele. A postura
correta é investigativa e não substitutiva: perguntar o que a pessoa faz hoje, quando fez pela
última vez, quanto tempo levou, o que deu errado da última vez, e o que ela faria se o sistema não
existisse. Perguntas sobre o passado observável produzem informação; perguntas sobre preferência
futura produzem especulação educada.

Duas armadilhas recorrentes merecem nome. A primeira é entrevistar apenas quem contratou — a
pessoa que assina raramente é a que usa, e as duas descrevem o mesmo processo de formas
irreconciliáveis. A segunda é aceitar a descrição oficial do processo sem observar o processo real:
toda organização tem um fluxo documentado e um fluxo praticado, e a distância entre os dois é onde
mora o requisito de verdade — planilhas paralelas, combinados informais, campos usados para
finalidade diferente da declarada.

O produto do levantamento não é uma lista de funcionalidades. É um enunciado do problema que
sobrevive à mudança de solução: quem tem a dor, com que frequência, qual é o custo atual de conviver
com ela, e como saberemos que ela diminuiu. Se essas quatro respostas não existem, o que se tem é
um pedido, e a equipe vai descobrir isso depois de construir.

### 2.5.2 Requisito funcional, não funcional e atributo de qualidade

Requisito funcional é o que o sistema faz; não funcional é como ele precisa se comportar enquanto
faz. A nomenclatura é ruim e vale dizer por quê: "não funcional" sugere secundário, e são
justamente esses os requisitos que determinam a arquitetura. Nenhuma decisão da seção 3.1 é tomada
por causa de um requisito funcional — cadastrar cliente se faz em qualquer arquitetura. Elas são
tomadas por causa de latência, volume, disponibilidade, tolerância a perda, janela de manutenção e
requisito regulatório. Por isso a literatura de arquitetura prefere chamá-los de atributos de
qualidade, e é a nomenclatura que este livro adota.

O problema prático não é classificá-los, é torná-los verificáveis. "O sistema deve ser rápido" não
é requisito; é uma intenção. Um atributo de qualidade só existe quando tem um cenário: sob qual
carga, medido em qual percentil, em qual caminho de código, com qual valor-limite, e o que
acontece quando o limite é ultrapassado. "O percentil 95 da consulta de saldo deve ficar abaixo de
300 ms com 2.000 requisições por segundo, e acima disso a resposta é degradar para saldo em cache
com aviso" é um requisito — porque é falsificável, e porque diz o que fazer quando falha. É a mesma
exigência que a seção 0.3 faz aos objetivos de aprendizagem: verbo verificável em vez de intenção.

Vale registrar a hierarquia de custo, porque ela orienta a ordem da conversa. Atributos de
qualidade que precisam ser projetados desde o início — segurança, auditabilidade, capacidade de
particionar dados por cliente ou por região, rastreabilidade — custam pouco quando assumidos cedo e
muito quando adicionados depois, porque atravessam todas as camadas. Requisitos funcionais, em
geral, se acrescentam de forma incremental. A conversa sobre atributos de qualidade, portanto, é a
que não pode ser adiada, e é quase sempre a que é.

### 2.5.3 Histórias, critérios de aceite e a fronteira com teste

A história de usuário nasceu como um dispositivo de conversa, não como formato de documento. A
formulação original de Kent Beck, no contexto do XP, era deliberadamente insuficiente: um cartão
com poucas palavras, cuja função era garantir que a conversa acontecesse antes da implementação. A
degradação previsível transformou o cartão em especificação em miniatura, escrita por uma pessoa,
lida por outra, sem conversa nenhuma — e o formato "como X, quero Y, para Z" virou cerimônia. Ron
Jeffries reagiu a isso com a formulação das três dimensões: cartão, conversa e confirmação, sendo
o cartão a menos importante das três.

O critério de aceite é a confirmação, e é onde o requisito encosta no teste. Ele responde a uma
pergunta binária: como saberemos, sem discussão, que isto está pronto? Um bom critério é observável
do lado de fora, não menciona implementação, e inclui os casos de erro — que é onde a maioria falha.
Critérios que descrevem só o caminho feliz produzem software que funciona na demonstração.

A fronteira com o teste é sutil e vale nomeá-la, porque o capítulo 3.3 vai depender dela. O
critério de aceite é uma afirmação sobre comportamento externo acordada antes de construir; o teste
é o mecanismo que verifica essa afirmação de forma repetível. Quando se escreve o critério em
formato executável — a família de práticas de BDD e especificação por exemplo —, os dois coincidem,
e o ganho real não é a automação: é ter forçado a conversa sobre exemplos concretos antes do
código. O ganho se perde por completo quando a especificação executável é escrita depois, por quem
já implementou, sem quem tem o problema na sala. Nesse caso o que se produz é um teste com sintaxe
mais verbosa.

Uma consequência para o ensino: a habilidade escassa aqui não é escrever histórias, é fazer boas
perguntas sobre exemplos. "Me dê um caso em que isso não vale" e "o que acontece se chegarem dois
ao mesmo tempo" descobrem mais requisito do que qualquer gabarito de formatação.

### 2.5.4 Fundamentos de IHC e usabilidade

Interação humano-computador é uma disciplina com literatura própria e resultados replicados, e a
formação em computação costuma reduzi-la a uma aula sobre cores. O núcleo que todo desenvolvedor
deveria carregar é pequeno e estável há décadas.

As dez heurísticas de Jakob Nielsen, de 1994, continuam sendo o melhor instrumento de custo-benefício
da área: visibilidade do estado do sistema; correspondência com o mundo real; controle e liberdade
do usuário; consistência e padrões; prevenção de erro; reconhecer em vez de lembrar; flexibilidade
e eficiência; estética e design minimalista; ajuda para reconhecer, diagnosticar e recuperar-se de
erros; e documentação. São heurísticas e não regras: servem para inspecionar uma interface e
encontrar problemas baratos, não para provar que ela é boa.

Três delas merecem destaque por serem as mais violadas por software corporativo. **Visibilidade do
estado**: uma operação que demora sem informar o que está acontecendo transfere ao usuário a
incerteza da seção 2.3.3 — ele não distingue lento de quebrado, e clica de novo, gerando a
duplicata que a aplicação não trata. **Prevenção de erro** é sempre mais barata que boa mensagem
de erro, e desenhar o campo para que o valor inválido não seja expressável vence qualquer
validação. **Recuperação de erro**: a mensagem precisa dizer o que aconteceu, por que, e qual é o
próximo passo — três coisas que "erro inesperado" não faz nenhuma.

O conceito que amarra tudo é o de modelo mental: o usuário constrói uma teoria de como o sistema
funciona a partir do que ele mostra, e age com base nessa teoria. Norman chamou de golfos de
execução e avaliação a distância entre o que a pessoa quer fazer e o que a interface oferece, e
entre o que o sistema faz e o que ela consegue perceber. Quase todo problema de usabilidade é um
desses dois golfos. Como a seção 1.4.5 argumenta para quem programa, o custo real está no modelo
mental errado — e a interface é o que o forma.

### 2.5.5 Acessibilidade e internacionalização como requisito, não retrofit

As duas andam juntas neste capítulo porque compartilham a mesma economia: custam pouco quando
assumidas no início e muito quando adicionadas depois, exatamente como os atributos de qualidade da
seção 2.5.2.

Acessibilidade tem norma pública e verificável — as WCAG, do W3C, organizadas em quatro princípios:
perceptível, operável, compreensível e robusto. O erro conceitual mais comum é tratá-la como
atendimento a uma minoria. Ela é, na prática, qualidade de interface para todo mundo: contraste
suficiente serve a quem tem baixa visão e a quem está no sol; navegação por teclado serve a quem
não usa mouse e a quem opera rápido; legenda serve a quem não ouve e a quem está em ambiente
barulhento. E há um argumento que independe de convicção: no Brasil, acessibilidade digital é
exigência legal para serviços públicos e tem base na Lei Brasileira de Inclusão — o que a coloca
como requisito, e o capítulo 3.4 retoma o assunto pelo lado jurídico.

O motivo de não ser possível adicioná-la depois é estrutural. Acessibilidade depende de semântica:
um botão precisa ser um botão para que a tecnologia assistiva saiba anunciá-lo, o foco precisa
seguir uma ordem que faça sentido, o estado precisa ser exposto de forma programática. Uma interface
construída com elementos genéricos e comportamento montado à mão precisa ser reconstruída, não
ajustada.

Internacionalização segue o mesmo padrão com outras causas. Traduzir texto é a parte fácil e a
menos importante. O que quebra é o resto: formato de data e número, ordenação alfabética
dependente de idioma, plurais que não seguem a regra do inglês, nomes que não se separam em nome e
sobrenome, endereços com estrutura diferente, moedas com número de casas decimais diferente, fusos
horários e horário de verão, e texto que muda de direção. Cada um desses vira uma suposição
espalhada pelo código quando não é assumido no início — e o exemplo mais didático é o de guardar
data e hora sem fuso, decisão que parece inofensiva e que reaparece como bug irreproduzível na
seção 2.3.4.

### 2.5.6 Pesquisa com usuário para quem não é designer

Não é preciso ser pesquisador para obter informação melhor do que palpite, e vale delimitar o que
uma equipe de desenvolvimento consegue fazer bem com pouco treino.

O **teste de usabilidade** é o instrumento com melhor retorno. Consiste em dar uma tarefa real a
alguém que não construiu o sistema e observar em silêncio. A regra que quase todo iniciante quebra
é intervir: no instante em que se explica, o dado é perdido, porque a pergunta é justamente se a
pessoa consegue sozinha. Nielsen argumentou que cinco participantes revelam a maior parte dos
problemas de usabilidade — número que é uma heurística de custo, não uma lei, e que vale como
autorização para começar pequeno em vez de não começar.

A **entrevista** serve para entender contexto e comportamento passado, e não para validar ideia.
Perguntar "você usaria isso?" produz gentileza; perguntar "me conte a última vez que você precisou
fazer isso" produz dado. O viés de agradar o entrevistador é forte e não se elimina com boa
intenção — apenas com perguntas sobre o que já aconteceu.

A **análise de uso do sistema** é a fonte mais barata e a mais desperdiçada. Onde as pessoas
abandonam o fluxo, quais campos são preenchidos com valor inválido, qual funcionalidade tem uso
próximo de zero, quais telas concentram tempo. Isso costuma estar disponível antes de qualquer
pesquisa formal, e responde a perguntas que a entrevista não responde.

Duas ressalvas de honestidade. Métrica de uso diz o que acontece e não diz por quê — inferir
motivo a partir de comportamento agregado é o erro mais comum de equipe técnica com acesso a dados.
E qualquer coleta desse tipo é tratamento de dado pessoal quando permite identificar alguém, o que
traz a LGPD para dentro da decisão de instrumentação, assunto do capítulo 3.4.

### 2.5.7 Por que quem entende o negócio envelhece mais devagar

Esta seção existe para explicar por que um capítulo sobre requisitos aparece num livro sobre
envelhecimento de conhecimento técnico.

O conhecimento de domínio é o ativo profissional que envelhece mais devagar de todos. As regras de
liquidação de um sistema financeiro, a lógica de apuração de um tributo, o fluxo de uma
concessão de crédito e as restrições de uma operação logística mudam em ritmo de legislação e de
prática de mercado, não em ritmo de tecnologia. Alguém que entende esse domínio permanece útil
depois de duas trocas completas de stack — e a recíproca não é verdadeira.

Há uma consequência de carreira que o capítulo 2.6 vai desenvolver. Profissionais que se definem
apenas pela tecnologia recomeçam do zero a cada ciclo, e competem sempre com quem acabou de
aprender a mesma ferramenta. Profissionais que acumulam domínio somam: cada ciclo tecnológico é
uma ferramenta nova aplicada ao mesmo entendimento, que continua valendo. O par mais valioso e mais
raro no mercado brasileiro é exatamente esse — quem sabe programar e entende o negócio o bastante
para discutir a regra com quem a define.

E há uma consequência de projeto, que fecha o argumento. A capacidade de traduzir entre o
vocabulário do negócio e o do sistema é o que impede a deriva entre o que foi pedido e o que foi
construído. Quando essa tradução não existe em ninguém da equipe, ela é feita por documento, e
documento não faz pergunta.

**Fontes primárias do capítulo.** Nielsen, J., [*10 Usability Heuristics for User Interface
Design*](https://www.nngroup.com/articles/ten-usability-heuristics/), 1994 · Nielsen, J. e
Landauer, T., *A Mathematical Model of the Finding of Usability Problems*, INTERCHI, 1993, para o
argumento dos cinco participantes · Norman, D., *The Design of Everyday Things*, 1988, edição
revista de 2013 · Beck, K., *Extreme Programming Explained*, 1999, para a origem das histórias ·
Jeffries, R., [*Essential XP: Card, Conversation,
Confirmation*](https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/), 2001 ·
Cockburn, A., *Writing Effective Use Cases*, 2000 · Wiegers, K. e Beatty, J., *Software
Requirements*, 3ª ed., 2013 · Bass, L., Clements, P. e Kazman, R., *Software Architecture in
Practice*, para cenários de atributo de qualidade · W3C, [*Web Content Accessibility
Guidelines (WCAG) 2.2*](https://www.w3.org/TR/WCAG22/), 2023 · Brasil, [*Lei nº 13.146/2015 — Lei
Brasileira de Inclusão*](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm) ·
Adzic, G., *Specification by Example*, 2011.

---

## 2.6 · Comportamento e carreira

Este é o capítulo mais fácil de escrever mal, e vale declarar as duas formas de errar antes de
começar. A primeira é o conselho motivacional, que soa verdadeiro e não é verificável. A segunda é
o oposto: fingir que existe evidência forte onde há apenas prática acumulada. O que segue tenta
ficar entre as duas — descrever mecanismos observáveis, dizer quando a base é experiência e não
estudo, e evitar prescrição onde a resposta depende de contexto.

O capítulo está na camada geracional porque o objeto é a relação entre pessoas em torno de trabalho
técnico, e essa relação muda em escala de geração, não de ciclo de ferramenta. O que muda mais
rápido — remoto, assíncrono, o efeito da automação sobre a porta de entrada — está concentrado na
seção 2.6.7, que é a mais perecível e traz gatilho de revisão próprio.

### 2.6.1 Por que comportamento é infraestrutura

A palavra "comportamental" carrega a sugestão de que se trata de um complemento agradável à
competência real. A tese desta seção é o contrário: em trabalho de software, comportamento é
infraestrutura, no sentido literal de que o sistema construído depende dele.

O argumento não é moral, é estrutural, e já foi estabelecido na seção 1.2.1. A Lei de Conway diz
que a arquitetura de um sistema reproduz a estrutura de comunicação de quem o constrói. Se duas
equipes não conversam, o acoplamento entre seus módulos será feito por contorno — um campo
sobrecarregado, uma tabela compartilhada em segredo, um processo manual entre as duas. A
consequência incômoda é que problemas de comunicação viram dívida técnica com endereço no código, e
não podem ser resolvidos apenas refatorando.

Um segundo mecanismo é a segurança psicológica, e é onde a base empírica é mais sólida. O trabalho
de Amy Edmondson mostra que equipes em que as pessoas se sentem seguras para apontar erro relatam
*mais* incidentes, e não menos — e que essa contagem maior corresponde a menos dano, não a mais.
A leitura ingênua do dado inverte a conclusão: uma equipe com poucos incidentes reportados pode ser
excelente ou pode ser silenciosa, e as duas se parecem no painel. Isso conecta diretamente ao
post-mortem sem culpados do capítulo 3.3: a prática não é generosidade, é a única forma de obter
o dado verdadeiro sobre a falha.

O terceiro mecanismo é o custo de coordenação, que Brooks descreveu em 1975 e que a seção 1.2.3 já
tratou: os canais de comunicação crescem com o quadrado das pessoas. A implicação prática é que
toda decisão de organização é também decisão de arquitetura, e vice-versa — assunto que a seção
3.1.9 retoma.

### 2.6.2 Competências — colaboração, conflito produtivo, feedback

Três competências concentram a maior parte da diferença observável entre profissionais de mesmo
nível técnico, e nenhuma delas costuma ser ensinada.

A primeira é **revisar código sem transformar a revisão em disputa**. Uma revisão útil separa
quatro coisas que a maioria mistura: defeito, risco, preferência de estilo e sugestão opcional.
Marcar explicitamente qual é qual reduce a fricção mais do que qualquer regra de tom, porque o
custo real não é a rispidez — é a ambiguidade sobre o que é obrigatório. A revisão que só aponta
problema, sem dizer o que a mudança faz bem, também deforma: ensina a esconder trabalho.

A segunda é **discordar sobre a decisão sem disputar a pessoa**. Conflito técnico é produtivo e sua
ausência é sinal ruim — uma equipe em que ninguém discorda ou pensa igual demais ou não se sente
segura. O que o torna produtivo é a disciplina de tornar explícito o critério: quando duas pessoas
discordam sobre uma escolha de arquitetura, quase sempre estão otimizando atributos de qualidade
diferentes e nenhuma das duas disse qual. Nomear o critério converte disputa de opinião em escolha
de trade-off, que é decidível — e é para isso que serve o ADR da seção 3.1.8.

A terceira é **dar e receber devolutiva sobre trabalho**. O padrão que funciona é banal e
raramente seguido: falar sobre comportamento observável e efeito, não sobre traço de
personalidade; ser específico quanto ao episódio; e separar a devolutiva da avaliação formal, que
tem outra função e outra dinâmica de poder. Do lado de quem recebe, a habilidade escassa é ouvir
até o fim antes de explicar o contexto — a explicação quase sempre é legítima e quase sempre
encerra a conversa antes que a informação apareça.

Uma observação sobre ensino, para não fingir que isto se resolve em aula: essas competências se
aprendem por prática com devolutiva, como qualquer outra. O que a formação pode fazer é criar
situações em que elas sejam exercidas e comentadas — revisão de código entre pares avaliada pela
qualidade da revisão, e não só do código, é o exemplo mais direto.

### 2.6.3 Autonomia, propriedade e senioridade

Existe uma confusão persistente entre senioridade e tempo de casa, e outra entre senioridade e
profundidade técnica. Nenhuma das duas sobrevive ao contato com o que as organizações de fato
compram.

O que distingue níveis, na prática, é o tamanho e a ambiguidade do problema que a pessoa consegue
absorver. Alguém em início de carreira executa bem uma tarefa definida. O nível seguinte resolve
um problema definido, escolhendo o caminho. O seguinte pega um problema mal definido, delimita o
escopo, negocia o que fica de fora e entrega. E o nível acima disso identifica qual problema vale
a pena resolver, o que envolve dizer não a trabalho que parece legítimo. A progressão não é sobre
saber mais tecnologia; é sobre operar com menos definição e mais consequência.

**Propriedade** é o segundo eixo, e é o mais mal compreendido. Não significa exclusividade sobre um
código, que é um antipadrão organizacional — significa considerar-se responsável pelo resultado
depois da entrega: se funcionou, se está sendo usado, se quebrou de madrugada, se alguém consegue
manter. A diferença entre "minha parte está pronta" e "o problema está resolvido" é a fronteira que
mais separa níveis.

**Autonomia** é consequência das duas anteriores, e é concedida, não declarada. Ela cresce quando
a pessoa demonstra julgamento repetidamente: pediu ajuda na hora certa, escalou o que precisava ser
escalado, decidiu sozinha o que era decidível. Nenhuma dessas três é sobre capacidade técnica, e é
por isso que profissionais tecnicamente fortes às vezes estacionam sem entender por quê.

Vale um recorte brasileiro, que o capítulo 3.6 desenvolve: a inflação de títulos no mercado
nacional tornou o rótulo pouco informativo. É comum encontrar "sênior" com três anos e "pleno" com
doze, e a variação é maior entre empresas do que dentro delas. A implicação para quem está
avaliando a própria carreira é usar os critérios acima em vez do crachá.

### 2.6.4 Trilha técnica vs. gestão, e o mito da escada única

Por décadas, a única progressão disponível terminava em gestão, o que produziu duas perdas
simultâneas: bons engenheiros virando gestores medianos e infelizes, e equipes perdendo a
competência técnica sênior que mais precisavam. A trilha técnica paralela — engenheiro sênior,
staff, principal — existe para corrigir isso, e vale entender o que ela é de fato.

O erro comum é imaginar a trilha técnica como "gestão sem reuniões", ou como o lugar de quem não
quer lidar com pessoas. Não é. Nos níveis altos, ela é majoritariamente trabalho de influência sem
autoridade formal: alinhar equipes que não se reportam a você, escrever documentos que convencem,
escolher quais decisões técnicas merecem briga. Will Larson descreve os arquétipos recorrentes —
resolver o problema mais difícil, sustentar a espinha técnica de uma área, viajar entre equipes
para desbloqueá-las. Nenhum deles dispensa a habilidade de trabalhar com gente; todos dispensam a
responsabilidade formal por carreira alheia, que é a diferença real.

Três observações práticas. A primeira é que a mudança entre trilhas é possível nos dois sentidos, e
a organização que trata a volta como fracasso está apenas garantindo que ninguém experimente. A
segunda é que gestão é uma mudança de profissão, não uma promoção: o trabalho, a medida de sucesso
e a fonte de satisfação passam a ser outros, e a competência técnica anterior vira contexto, não
ferramenta. A terceira é que muitas empresas anunciam a trilha técnica e não a sustentam — o teste
é olhar quem de fato chegou aos níveis altos por ela, e se essas pessoas têm influência
comparável à dos gestores do mesmo nível.

### 2.6.5 A transição de carreira e a reinvenção por década

Uma carreira longa em tecnologia não é uma carreira; são várias, e a transição entre elas é a
habilidade central. Quem entrou na área nos anos 1990 já viveu, no mínimo, a passagem do
cliente-servidor para a web, da web para o móvel e a nuvem, e do desenvolvimento local para o
distribuído — e cada passagem exigiu recomeçar em algum grau.

O que a experiência de campo sugere, e aqui é experiência e não estudo, é que a transição bem
sucedida raramente é uma troca completa. Ela costuma ser lateral: parte do que se sabe é
transferível, e a transição se apoia nessa parte enquanto o resto é reconstruído. Quem migra de
sustentação de sistema bancário para engenharia de plataforma leva junto o entendimento de
criticidade, janela de manutenção, auditoria e reversão — que é justamente o que falta a quem
chegou pelo caminho oposto. Descartar esse capital por vergonha do legado é o erro mais comum e o
mais caro.

O mapa que a seção 0.6 desenha para o leitor em transição vale como método: as lacunas prováveis
estão nas camadas 1 e 2, não na 4. A ansiedade empurra para a ferramenta da moda, que é o item mais
fácil de aprender e o que menos diferencia. A lacuna real costuma ser sistemas distribuídos, dados
sob concorrência ou escrita técnica.

Uma nota sobre idade, porque o assunto é evitado e é real no Brasil. O mercado tem preferência
observável por profissionais mais jovens em algumas faixas, e negar isso não ajuda ninguém. O que
se pode dizer com honestidade é que a assimetria diminui onde o domínio pesa mais que a
familiaridade com ferramenta — sistemas críticos, regulação, arquitetura, integração com legado —
e que essa é uma razão estratégica, e não apenas confortável, para investir em profundidade de
domínio, como a seção 2.5.7 argumentou.

### 2.6.6 Síndrome do impostor e obsolescência percebida

Dois desconfortos são frequentes o suficiente na profissão para merecerem tratamento técnico em vez
de consolo.

O primeiro é a sensação persistente de não ser competente o bastante apesar de evidência em
contrário. A área tem duas características que a alimentam de forma estrutural. A primeira é a
assimetria de visibilidade: você vê o próprio processo — as tentativas, o que não entendeu, o que
buscou — e vê dos outros apenas o resultado publicado. A comparação é entre o seu bastidor e a
vitrine alheia, e ela é sempre desfavorável. A segunda é que o volume do que existe para saber
cresce mais rápido que a capacidade de qualquer pessoa, de modo que a fração conhecida diminui com
o tempo mesmo quando o conhecimento absoluto aumenta. Sentir que se sabe proporcionalmente menos a
cada ano é uma leitura correta de uma métrica errada.

O segundo desconforto é a obsolescência percebida: a impressão de estar ficando para trás a cada
anúncio. Aqui o livro tem uma resposta estrutural, e é o argumento da seção 0.2. Dos vinte e um
capítulos de conteúdo, três estão na camada sazonal. A ansiedade que o mercado produz se concentra
em algo próximo de quinze por cento do currículo, e os outros oitenta e cinco por cento envelhecem
devagar o bastante para que aprendê-los seja investimento. Quem sente que precisa correr atrás de
tudo está reagindo à camada 4 como se ela fosse o todo.

Duas ressalvas de honestidade. A primeira: nada disso é aconselhamento clínico, e sofrimento
persistente que atrapalha a vida pede ajuda profissional, não capítulo de livro técnico. A segunda:
existe obsolescência real, e distingui-la da percebida é justamente para isso que serve o mapa por
camadas. Quem não sabe o que é uma transação, o que acontece na falha parcial ou como escrever um
documento que convence tem uma lacuna concreta — e ela não se resolve aprendendo a ferramenta do
mês.

### 2.6.7 O envelhecimento do comportamento — de 1990 a 2026

Esta é a seção mais perecível do capítulo, e é a razão de ele ter gatilho de revisão próprio.

O que mudou de substância nas últimas três décadas é o meio em que a colaboração acontece. Nos
anos 1990, a coordenação era presencial e síncrona por padrão, e a documentação existia porque a
memória não escalava. A comunicação por texto assíncrono, dominante hoje em boa parte da indústria,
inverteu isso: a escrita deixou de ser registro e virou o principal instrumento de coordenação. É a
razão pela qual a escrita técnica subiu para a camada permanente neste livro, na seção 1.5 — ela
deixou de ser um diferencial e virou a interface primária de trabalho.

O trabalho remoto e assíncrono trouxe ganhos verificáveis em acesso e autonomia, e custos que
levaram tempo para aparecer: a formação de gente em início de carreira, que dependia de observação
informal e de perguntas de baixo custo; a transmissão de contexto tácito, que não estava em
documento nenhum; e a diferença entre estar disponível e estar presente. As soluções que
funcionam são deliberadas e chatas — escrever mais do que parece necessário, tornar o
acompanhamento explícito em vez de emergente, criar ocasiões de contato que não dependem de
alguém sentir falta.

A mudança em curso que merece registro, com toda a cautela que a seção 0.5 recomenda para
prospecção, é o efeito da assistência por modelos de linguagem sobre a porta de entrada da
profissão. A hipótese que circula é que a automação de tarefas de baixa complexidade reduz o
espaço onde iniciantes historicamente aprendiam. É plausível e ainda não está estabelecida — a
evidência disponível em 2026 é curta, parcial e frequentemente produzida por parte interessada. O
livro registra a hipótese, recusa-se a afirmá-la, e coloca a discussão de frente no capítulo 4.3,
que se declara volátil justamente por isto.

O que não mudou merece a última palavra, porque é o argumento do capítulo. A necessidade de
confiança para que alguém admita um erro; o custo de coordenação que cresce com o número de
pessoas; a diferença entre uma equipe que discorda e uma que se cala; a diferença entre entregar
sua parte e resolver o problema. Nada disso é diferente de 1975, quando Brooks escreveu, e não há
sinal de que seja diferente na próxima década.

**Fontes primárias do capítulo.** Brooks, F., *The Mythical Man-Month*, 1975 · Conway, M., *How Do
Committees Invent?*, Datamation, 1968 · Edmondson, A., [*Psychological Safety and Learning Behavior
in Work Teams*](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Performance/Edmondson%20Psychological%20safety.pdf),
Administrative Science Quarterly, 1999, e *The Fearless Organization*, 2018 · Larson, W., *Staff
Engineer: Leadership Beyond the Management Track*, 2021 · DeMarco, T. e Lister, T., *Peopleware*,
1987 · Skelton, M. e Pais, M., *Team Topologies*, 2019 · Clance, P. e Imes, S., *The Impostor
Phenomenon in High Achieving Women*, 1978, para a origem do termo · Dekker, S., *The Field Guide to
Understanding Human Error*, 2002, para a base do post-mortem sem culpados.

*As afirmações desta seção sobre trabalho remoto e sobre o efeito da assistência por modelos de
linguagem na formação de iniciantes são hipóteses de campo com evidência parcial, e estão marcadas
como gatilho de revisão na ficha do capítulo.*

---

# CAMADA 3 — CÍCLICO
*Meia-vida de 5 a 15 anos · onde mora a maior parte do que se ensina hoje no Brasil*

## 3.1 · Arquitetura de software

A camada 2 tratou de fundamentos que não mudam de substância. Esta trata do que oscila — e
arquitetura é o exemplo mais claro, porque suas mudanças não são progresso linear: são idas e
voltas. O mesmo desenho é abandonado e retomado com outro nome a cada década, e quem não viu a
volta anterior confunde retorno com novidade.

Isso não desqualifica a disciplina. Significa que o conteúdo transferível de arquitetura não é o
estilo — é o critério de escolha entre estilos, e a capacidade de nomear o que cada um cobra. Um
aluno que sai sabendo desenhar microsserviços aprendeu algo com meia-vida de dez anos. Um aluno que
sai sabendo perguntar quanto acoplamento o desenho cria, onde está a falha parcial e qual é o custo
operacional aprendeu algo que sobrevive ao próximo pêndulo.

Este capítulo depende do 2.3. Toda arquitetura distribuída é uma aposta sobre falha parcial,
latência e consistência, e discuti-la sem esses fundamentos produz a conversa que a seção 2.3.7
descreve como cara.

### 3.1.1 Monolito — e a redescoberta do monolito modular

Monolito é o desenho em que a aplicação é implantada como uma unidade. Foi o padrão por décadas,
virou pejorativo por volta de 2014, e voltou com adjetivo. Vale separar o que a palavra passou a
carregar indevidamente.

O que se criticava não era a unidade de implantação: era a ausência de fronteiras internas. Uma
base em que qualquer parte chama qualquer outra, em que o esquema de banco é compartilhado sem
dono e em que uma mudança exige entender o todo — essa é a bola de lama, e ela é ruim
independentemente de como é implantada. O erro do período foi tratar as duas propriedades como a
mesma: concluir que, para ter fronteiras, era preciso separar processos.

O **monolito modular** é o reconhecimento de que a fronteira pode ser lógica. Módulos com interface
explícita, dependências declaradas e proibição de acesso ao interior alheio — verificada por
ferramenta de build, não por combinação verbal — entregam a maior parte do benefício de
modularidade sem custo de rede, sem falha parcial e sem consistência eventual. É a aplicação direta
de Parnas, da seção 1.2.4: o critério de decomposição é esconder decisões que podem mudar, e isso
independe de topologia de implantação.

As vantagens que o monolito conserva são subestimadas porque são invisíveis quando funcionam:
transação local com garantia real, refatoração entre módulos com apoio do compilador, um único
artefato para depurar, rastreamento de pilha que atravessa a chamada inteira, e ausência de versões
incompatíveis coexistindo. Cada uma delas é abandonada explicitamente ao distribuir, e a decisão de
abandoná-las deveria ser declarada como custo, não descoberta depois.

O limite real do monolito é organizacional antes de ser técnico. Ele aparece quando o número de
pessoas que precisam mudar a mesma base ao mesmo tempo torna a coordenação de implantação mais cara
que a coordenação de contratos — e essa fronteira chega bem depois do que a literatura de
microsserviços sugere.

### 3.1.2 Camadas, hexagonal, ports & adapters, Clean Architecture

Esta família de estilos responde sempre à mesma pergunta: como impedir que a regra de negócio se
misture com a tecnologia que a cerca. As respostas diferem em vocabulário e em rigor, e é útil ver
o que compartilham antes do que as distingue.

A **arquitetura em camadas** é a formulação mais antiga: apresentação, aplicação, domínio,
infraestrutura, com dependências apontando para baixo. O problema clássico é que a camada de
domínio acaba dependendo da de persistência, porque é ali que os dados estão — e a dependência
invertida corrói a separação que motivava o desenho.

A **arquitetura hexagonal**, de Alistair Cockburn, resolve isso com uma inversão explícita: o
domínio define portas — interfaces em seus próprios termos — e a infraestrutura fornece adaptadores
que as implementam. A direção da dependência passa a apontar sempre para dentro. **Clean
Architecture**, de Robert Martin, e a *onion* de Jeffrey Palermo são reformulações do mesmo
princípio com outro diagrama, e a discussão sobre qual é superior costuma render mais do que
merece.

O ganho real é testabilidade e adiamento: a regra de negócio pode ser exercitada sem banco, sem
rede e sem framework, e a escolha de tecnologia pode ser trocada sem reescrever o que importa. O
custo é indireção, e ele é real — cada porta é uma interface a mais, cada adaptador é um arquivo a
mais, e navegar do controlador ao efeito exige saltos. Em sistema pequeno, com regra de negócio
fina, essa indireção custa mais do que entrega, e aplicar o estilo por completude é o excesso mais
comum entre equipes que acabaram de aprendê-lo.

O critério prático: o estilo se paga onde a regra de negócio é o ativo e a tecnologia é
intercambiável. Onde o sistema é essencialmente um adaptador entre um formulário e uma tabela, a
camada de domínio não tem o que proteger, e a estrutura vira cerimônia — exatamente a crítica que
a seção 2.1.2 faz à orientação a objetos que virou ortodoxia.

### 3.1.3 SOA e o legado do ESB

Arquitetura orientada a serviços dominou o discurso corporativo entre o fim dos anos 1990 e a
primeira década dos 2000, e é hoje o exemplo mais didático de estilo em arqueologia — o que a torna
mais útil para ensinar do que a moda atual.

A premissa era boa e continua válida: expor capacidades de negócio como serviços com contrato
explícito, reutilizáveis entre sistemas, para acabar com a integração ponto a ponto que crescia de
forma quadrática. O problema não estava na premissa; estava na implementação dominante, que
concentrou orquestração, transformação de mensagem, roteamento e às vezes regra de negócio dentro
de um barramento — o ESB.

O mecanismo da falha vale ser nomeado porque se repete com outros nomes. O barramento virou um
ponto único de acoplamento e de disputa: toda mudança passava por ele, a equipe que o mantinha
virou gargalo organizacional, e a lógica que morava ali não pertencia a nenhum time de negócio.
É a Lei de Conway com sinal invertido — uma estrutura técnica impondo uma estrutura organizacional
que ninguém escolheu. Somado a isso, o peso da pilha de padrões WS-* e de ferramentas caras
tornou o ciclo de mudança lento o bastante para que a promessa de agilidade se invertesse.

O que sobreviveu de SOA é mais do que a caricatura sugere: contrato explícito, versionamento de
interface, catálogo de serviços, pensar capacidade de negócio como unidade. Microsserviços
herdaram tudo isso e mudaram a resposta para uma única pergunta — onde mora a inteligência.
A formulação que ficou é a de pontos de extremidade inteligentes e canos burros: mover
orquestração e transformação para os serviços, deixando o transporte simples. Vale reparar que
essa não é uma correção definitiva, e sim uma escolha de onde concentrar complexidade. A malha de
serviços, dez anos depois, moveu parte dela de volta para a infraestrutura.

### 3.1.4 Microsserviços — promessa, custo real, e quando não usar

A promessa foi bem formulada: serviços pequenos, com fronteira de negócio, implantáveis de forma
independente, permitindo que equipes autônomas entreguem sem coordenação global, com escala e
tecnologia escolhidas por serviço. A parte importante da promessa — e a mais esquecida — é a
independência de implantação. Todo o resto é consequência dela.

O custo real aparece porque a fronteira de processo transforma toda chamada em chamada de rede, e
com isso importa o capítulo 2.3 inteiro. Uma consulta que era uma junção passa a ser N chamadas
sujeitas a latência, falha parcial e timeout. Uma operação que era uma transação passa a exigir
coordenação entre serviços, e a resposta honesta a "como faço transação distribuída?" quase sempre
é "não faça" — modele com consistência eventual e compensação, ou mantenha a operação dentro de um
serviço. Testar deixa de ser executar um binário; depurar exige rastreamento distribuído; o
ferramental operacional deixa de ser opcional.

Há também um custo silencioso e frequentemente fatal: o monólito distribuído. Serviços separados
que precisam ser implantados juntos, porque compartilham banco ou porque seus contratos mudam em
conjunto, pagam todos os custos da distribuição e não entregam o único benefício que a justificava.
É o resultado mais comum de uma decomposição feita por camada técnica em vez de por capacidade de
negócio.

Quando **não** usar é a pergunta mais útil, e há sinais claros. Quando a equipe é pequena o
bastante para coordenar implantação sem dor — abaixo de alguma dezena de pessoas, a coordenação
não é o gargalo. Quando as fronteiras de domínio ainda não são conhecidas, porque fronteira errada
em processo separado é muito mais cara de mover do que fronteira errada dentro de um módulo.
Quando não existe maturidade operacional: automação de implantação, observabilidade, plantão. E
quando o problema real é acoplamento interno, que a separação em processos não resolve — apenas
transforma em acoplamento de rede, agora com latência.

A recomendação que a prática consolidou, e que Fowler formulou como monolito primeiro, é começar
modular e extrair serviços quando houver motivo nomeado: uma parte com perfil de escala muito
diferente, um domínio com ciclo de mudança próprio, uma fronteira de equipe estabilizada, um
requisito de isolamento. Extrair por motivo é reversível; adotar por estilo, não.

### 3.1.5 Serverless e computação de borda

Serverless nomeia mal o que oferece: há servidores, o que muda é quem os opera e como se paga. O
modelo de função como serviço leva a granularidade de implantação ao limite e transfere ao provedor
o provisionamento, a escala e boa parte da resiliência, cobrando por execução em vez de por tempo
ligado.

Onde ele ganha é previsível: carga irregular ou imprevisível, em que máquinas ociosas dominam o
custo; tarefas orientadas a evento e de curta duração; equipes pequenas sem capacidade operacional
para manter infraestrutura. O ganho é real e frequentemente grande.

Os custos também são conhecidos e devem entrar na decisão. A partida a frio impõe latência de
cauda difícil de eliminar, com impacto exatamente no percentil que a seção 2.3.2 diz importar. O
modelo é sem estado por construção, o que empurra todo estado para serviços externos e multiplica
chamadas de rede. Limites de tempo de execução e de tamanho tornam certos trabalhos inviáveis. O
custo por execução, excelente em carga baixa, inverte-se em carga alta e constante — há um ponto
de cruzamento, e ele deve ser calculado, não presumido. E o acoplamento ao provedor é mais forte
do que em qualquer outro estilo, porque não está apenas no tempo de execução: está no
encadeamento de eventos, no modelo de identidade e nos serviços gerenciados ao redor.

A computação de borda é a resposta ao único problema que dinheiro não resolve: a velocidade da luz.
Executar perto de quem consome elimina a viagem intercontinental da seção 2.3.2, e é por isso que
faz sentido para entrega de conteúdo, personalização leve, autenticação e decisões de roteamento. O
que ela não elimina é a necessidade de coordenar estado — e distribuir estado geograficamente
reintroduz, com força total, a escolha da seção 2.2.5 entre coordenar e esperar ou não coordenar e
conviver com divergência.

Um registro de honestidade sobre perecibilidade: esta é a seção do capítulo mais próxima da camada
4. Os limites concretos de tempo, memória e latência de partida mudam a cada ciclo de produto, e
qualquer número específico aqui envelhece em meses. O que permanece é a estrutura da decisão —
quem opera, como se paga, o que se perde em controle, onde está o ponto de cruzamento de custo.

### 3.1.6 Event-driven, CQRS e Event Sourcing

Os três termos aparecem juntos e são independentes, e essa confusão custa caro. Vale separá-los.

**Arquitetura orientada a eventos** é uma escolha de acoplamento: em vez de A chamar B, A publica
um fato e quem se interessa reage. O ganho é que o produtor não conhece os consumidores, o que
permite acrescentar comportamento sem tocar em quem publica. O custo é que o fluxo deixa de ser
legível no código — para saber o que acontece quando um pedido é criado, é preciso descobrir quem
assina, e nenhuma ferramenta de navegação responde isso sozinha. Depuração passa a exigir
correlação, e a ordem entre eventos vira preocupação de projeto, com tudo que a seção 2.3.4 diz
sobre ordenação.

**CQRS** separa o modelo de escrita do modelo de leitura. Faz sentido quando os dois têm
requisitos genuinamente diferentes — escrita com invariante forte e volume baixo, leitura com
consultas variadas e volume alto. O custo é que os dois modelos precisam ser sincronizados, e essa
sincronização é assíncrona na prática: a leitura fica atrás da escrita por uma janela. Isso é uma
mudança de contrato com o usuário, não um detalhe interno — o clássico "gravei e não apareceu" é
consequência direta, e precisa ser tratado no desenho da interface, não escondido.

**Event Sourcing** é a decisão mais radical: guardar a sequência de eventos como fonte da verdade e
derivar o estado atual por reprodução. Entrega auditoria completa, capacidade de reconstruir o
estado em qualquer ponto do tempo e de responder perguntas que não haviam sido feitas quando o dado
foi gravado — o que é valioso em domínios regulados. Cobra caro: o esquema dos eventos é imutável e
precisa ser versionado para sempre, porque eventos antigos continuarão sendo lidos; consultas
exigem projeções mantidas à parte; e corrigir um erro passado significa acrescentar um evento
compensatório, nunca alterar o histórico. É um estilo excelente para uma parte pequena de um
sistema e desastroso como decisão global.

A regra que fecha a seção: adotar os três juntos por parecerem um pacote é o erro característico
aqui. Cada um resolve um problema distinto, cada um cobra separadamente, e a maioria dos sistemas
precisa de zero ou um deles.

### 3.1.7 Estrangulamento de legado e migração incremental

A reescrita completa é a decisão mais tentadora e a mais frequentemente errada da profissão, e vale
entender por que ela falha em vez de repetir a advertência.

Falha por três razões. O sistema antigo continua mudando enquanto o novo é construído, e o alvo se
move. O comportamento a ser replicado não está documentado — está no código, incluindo os defeitos
dos quais alguém já depende. E o novo sistema não entrega valor nenhum até estar completo, o que
significa um período longo de custo sem retorno, período em que a decisão fica vulnerável a
qualquer mudança de prioridade. Joel Spolsky chamou a reescrita do zero de o pior erro estratégico
possível, e a formulação é forte demais para todos os casos, mas o mecanismo que ele descreve é
real.

A **figueira estranguladora**, nome que Martin Fowler tomou emprestado da botânica, é a alternativa
que funciona: construir o novo em volta do antigo, desviar tráfego funcionalidade por
funcionalidade, e remover a parte antiga só depois que a nova está em uso. A propriedade essencial
é que cada passo é pequeno, entrega valor e é reversível — o sistema está sempre inteiro, nunca em
estado de transição irreversível.

Na prática, três mecanismos sustentam isso. Uma fachada na frente do sistema antigo, que decide o
que vai para onde e é o ponto onde a migração é controlada. Escrita dupla ou sincronização durante
a transição, com a mesma disciplina de expansão e contração da seção 2.2.7 — inclusive o passo do
meio, que aqui também é o pulado. E um critério explícito de conclusão por fatia, porque a falha
mais comum não é técnica: é a migração que fica pela metade por anos, com os dois sistemas vivos,
dobrando o custo de manutenção e a superfície de erro.

Michael Feathers acrescenta a peça que falta quando o legado não tem testes: costurar pontos de
articulação para conseguir testar antes de mudar. A ordem importa e é contraintuitiva — o teste de
caracterização não verifica se o comportamento está certo, verifica qual é. Congelar o
comportamento atual, inclusive o errado, é o que torna a mudança segura.

### 3.1.8 ADR — decisão arquitetural como documento versionado

Um registro de decisão de arquitetura é um documento curto que captura uma decisão, o contexto em
que foi tomada e as consequências aceitas. Fica versionado junto do código, é imutável depois de
aceito, e quando a decisão muda escreve-se um novo que substitui o anterior — o histórico
permanece.

O formato que Michael Nygard propôs em 2011 tem quatro seções e ganha por ser pequeno o bastante
para ser escrito: **título**, **status** (proposto, aceito, substituído), **contexto** — as forças
em jogo, incluindo restrições organizacionais e prazos, não só técnicas —, **decisão**, e
**consequências**, que devem incluir as ruins. Um ADR que só lista vantagens não registrou uma
decisão; registrou uma justificativa depois do fato.

O valor não está em documentar, está em preservar o contexto. Código mostra o que foi decidido e
nunca por quê; quando o porquê se perde, a equipe seguinte enfrenta duas opções igualmente ruins —
manter uma restrição cuja razão desapareceu, ou removê-la e redescobrir o motivo em produção. O ADR
é o antídoto barato para isso, e é o instrumento que transforma a discordância da seção 2.6.2 em
escolha de trade-off registrada.

Duas condições práticas separam ADR vivo de teatro documental. A primeira é o escopo: registra-se o
que é caro de reverter e o que uma pessoa nova questionaria — escolha de banco, fronteira de
serviço, formato de integração, adoção de um estilo. Registrar tudo mata a prática pelo volume. A
segunda é a imutabilidade: editar um ADR aceito para refletir o presente destrói exatamente o valor
que ele tinha, que é mostrar o que se sabia na época. Substituir, nunca reescrever.

O teste da seção é operacional, e é o marco que a Fase 3 do plano cobra: alguém que não conhece o
sistema deve conseguir reconstruir a decisão lendo apenas os ADRs.

### 3.1.9 Team Topologies — a arquitetura da organização é a do sistema

Se a Lei de Conway está certa, e a evidência acumulada sugere que está, então desenhar arquitetura
sem desenhar organização é desenhar metade. Team Topologies, de Matthew Skelton e Manuel Pais,
oferece o vocabulário que faltava para tratar as duas juntas.

O modelo propõe quatro tipos de equipe. A **alinhada a fluxo** é a unidade primária: responsável por
uma fatia de valor de ponta a ponta, com autonomia para entregar sem depender de outras. As
demais existem para reduzir a carga cognitiva dessa. A **plataforma** oferece serviços internos
consumidos como produto — com contrato e documentação, não como favor. A **capacitadora** ajuda
equipes de fluxo a adquirir uma competência e depois se retira, o que é a parte mais frequentemente
ignorada. E o **subsistema complicado** concentra uma competência rara demais para ser distribuída.

O conceito operacional mais útil do livro é a **carga cognitiva como critério de fronteira**. Uma
equipe tem limite de quanto domínio consegue manter na cabeça, e quando o escopo excede esse
limite a qualidade cai de formas que nenhuma cobrança corrige. Isso dá um critério verificável para
dimensionar responsabilidade, em vez de dividir por conveniência de organograma — e conecta
diretamente à seção 1.4.1, que trata carga cognitiva no nível individual.

O terceiro elemento são os **modos de interação**: colaboração, que é cara e deve ser temporária;
serviço, que é barato e deve ser o estado estável; e facilitação, que é transitória por definição.
Nomear o modo evita a situação mais comum em organizações grandes, que é colaboração permanente
entre equipes que deveriam ter um contrato.

A **manobra inversa de Conway** — mudar a estrutura das equipes para induzir a arquitetura
desejada — é a consequência prática, e é também a mais difícil de executar, porque exige autoridade
sobre organização que a maioria dos arquitetos não tem. Vale a ressalva de honestidade: o modelo é
recente, amplamente adotado e ainda sem corpo de evidência independente comparável ao das leis da
seção 1.2. É vocabulário útil e hipótese razoável, não resultado estabelecido.

### 3.1.10 O pêndulo centralizar ↔ distribuir

A seção 0.1 anunciou que o arco de quatro fases não é irreversível e que a oscilação entre
centralizar e distribuir merecia nome próprio. É aqui.

A sequência é reconhecível e cobre setenta anos. Mainframe centralizado, com terminal burro. Depois
cliente-servidor, distribuindo processamento para a estação. Depois a web, recentralizando no
servidor com o navegador como terminal. Depois cliente rico e aplicação de página única,
distribuindo de novo para o cliente. Serviços monolíticos, depois microsserviços, depois monolito
modular. Renderização no servidor, no cliente, e de volta ao servidor com hidratação. Cada volta
foi anunciada como avanço, e cada uma resolveu um problema real criado pela anterior.

O mecanismo por trás da oscilação não é moda, embora moda participe. É que centralizar e distribuir
otimizam coisas diferentes e ambas importam. Centralizar dá consistência, simplicidade operacional
e um lugar único para raciocinar; cobra escalabilidade, disponibilidade e autonomia de quem
depende do centro. Distribuir dá autonomia, isolamento de falha e escala independente; cobra
coordenação, latência, complexidade operacional e tudo o que a seção 2.3 descreve. Quando uma
geração acumula dor suficiente de um lado, a indústria migra para o outro — e acumula a dor
oposta.

Duas implicações para quem ensina e para quem decide. A primeira: o estilo dominante hoje não é o
correto, é o que corresponde às restrições predominantes hoje — custo de hardware, tamanho das
equipes, expectativa de disponibilidade, maturidade das ferramentas. Quando essas restrições
mudam, o estilo muda, e quem aprendeu o estilo como princípio confunde a mudança com traição. A
segunda: reconhecer o pêndulo é a defesa mais barata contra o argumento de autoridade da novidade.
Perguntar "de que lado do pêndulo isto está, e qual dor da volta anterior está resolvendo?" faz o
argumento de moda desmontar sozinho.

É por isso que este capítulo está na camada cíclica e o 2.3 na geracional. O pêndulo se move; a
falha parcial, não.

**Fontes primárias do capítulo.** Parnas, D., *On the Criteria To Be Used in Decomposing Systems
into Modules*, CACM, 1972 · Cockburn, A., [*Hexagonal
Architecture*](https://alistair.cockburn.us/hexagonal-architecture/), 2005 · Martin, R. C., *Clean
Architecture*, 2017 · Evans, E., *Domain-Driven Design*, 2003 · Fowler, M. e Lewis, J.,
[*Microservices*](https://martinfowler.com/articles/microservices.html), 2014, e
[*MonolithFirst*](https://martinfowler.com/bliki/MonolithFirst.html), 2015 · Fowler, M.,
[*StranglerFigApplication*](https://martinfowler.com/bliki/StranglerFigApplication.html), 2004 ·
Newman, S., *Building Microservices*, 2ª ed., 2021, e *Monolith to Microservices*, 2019 ·
Feathers, M., *Working Effectively with Legacy Code*, 2004 · Nygard, M., [*Documenting Architecture
Decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011 ·
Skelton, M. e Pais, M., *Team Topologies*, 2019 · Young, G., sobre CQRS e Event Sourcing, e
Fowler, M., [*Event Sourcing*](https://martinfowler.com/eaaDev/EventSourcing.html), 2005 ·
Spolsky, J., [*Things You Should Never Do, Part
I*](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/), 2000.

---

## 3.2 · Processos e metodologias

Este é o único capítulo do livro cuja ficha declara o estado **erosão**, e a declaração é o ponto
de partida. O consenso ágil que se formou nos anos 2000 rachou: não foi substituído por um sucessor
nomeado, mas as práticas se diluíram, o vocabulário se descolou da prática, e a literatura recente
é majoritariamente crítica. Reconhecer isso é diferente de anunciar a morte do ágil — anúncio de
morte é o gênero menos confiável da área.

O capítulo é o mais brasileiro dos técnicos, porque a trajetória local teve marcos próprios — o
MPS.BR, a adoção tardia e a convivência com estruturas de governança que nenhum manifesto previu.
A seção 3.2.8 trata disso de frente.

Uma advertência de leitura vale desde já: processo é o assunto em que a distância entre o que se
diz e o que se faz é maior em toda a engenharia de software. Qualquer afirmação sobre o que uma
organização "usa" deve ser lida como declaração de intenção.

### 3.2.1 A era pré-metodológica — code and fix

Antes de haver metodologia havia trabalho, e vale entender o que se fazia, porque o padrão nunca
desapareceu.

O modo original era escrever e corrigir: programar direto a partir de um entendimento informal do
problema, testar manualmente, ajustar, repetir. Funcionava — e ainda funciona — enquanto o sistema
é pequeno, o autor é o usuário e a memória de uma pessoa dá conta do todo. O que falha é a
escala: sem registro do porquê, sem separação entre decidir e construir, e sem forma de coordenar
mais de meia dúzia de pessoas, o custo de mudança cresce mais rápido que o sistema.

A conferência da OTAN de 1968, que a seção 1.1.5 tratou, é a data em que essa insuficiência virou
diagnóstico público. O termo "engenharia de software" foi escolhido como provocação deliberada:
propunha que a construção de programas precisava de disciplina de engenharia, e o relatório registra
que os participantes não concordavam sobre o que isso significava.

O ponto que interessa ao livro é que escrever-e-corrigir continua sendo o processo real de boa parte
do software escrito hoje, inclusive dentro de organizações que declaram usar outra coisa. Não é
falha moral: é o comportamento padrão quando a estrutura não sustenta nada mais elaborado. Todo
processo descrito adiante compete com ele.

### 3.2.2 Waterfall — o que Royce realmente escreveu

O caso do Waterfall é o exemplo mais citado de ironia histórica da área, e a versão popular está
errada o bastante para merecer correção cuidadosa.

Winston Royce publicou em 1970 um artigo sobre desenvolvimento de grandes sistemas de software. Nele
apresenta um diagrama sequencial — requisitos, projeto, implementação, teste, operação — e o
descreve explicitamente como arriscado e sujeito a falhar. O restante do artigo propõe correções:
fazer o projeto duas vezes, envolver o cliente, documentar, e sobretudo iterar entre fases
adjacentes, com realimentação. A recomendação central de Royce era construir um protótipo
descartável antes do sistema real.

O que a indústria absorveu foi o primeiro diagrama, sem as ressalvas. O modelo virou padrão
contratual e regulatório, especialmente em contexto de defesa e governo, onde a sequência com
marcos documentais servia a necessidades de fiscalização que nada tinham a ver com eficácia técnica.
Royce ficou conhecido como autor do modelo que criticava.

Duas lições que valem mais do que a curiosidade. A primeira é sobre como conhecimento envelhece de
forma deformada: a simplificação sobrevive ao original, e a simplificação é o que chega à sala de
aula. É o mecanismo que a seção 1.2.7 descreve para a curva de custo da mudança e que a seção 2.2.5
descreve para o CAP — em todos os casos, uma imagem venceu o texto que a acompanhava.

A segunda é que o modelo sequencial não é irracional em todo contexto. Onde o custo de errar é
catastrófico e irreversível, onde o requisito é imposto por norma e não descoberto, e onde a
integração física impede entrega incremental, planejar longamente antes de construir é o
comportamento correto. Ensinar Waterfall como erro de época impede o aluno de reconhecer os casos
em que a estrutura ainda se aplica.

### 3.2.3 Processos pesados — RUP, CMMI e o MPS.BR

Os anos 1990 responderam à crise de previsibilidade com processo formal, e a resposta foi
consistente: definir papéis, artefatos, fases e critérios de passagem, e avaliar a maturidade da
organização que os executa.

O **RUP** organizava o desenvolvimento em quatro fases — concepção, elaboração, construção,
transição — com disciplinas atravessando todas e iterações dentro de cada uma. É importante
registrar, contra a caricatura, que o RUP era iterativo e incremental por projeto, e que foi
concebido para ser adaptado. O que se implantou majoritariamente foi a versão completa, com dezenas
de artefatos obrigatórios, e o custo do processo passou a competir com o custo do trabalho.

O **CMMI**, herdeiro do CMM do SEI, não é um processo mas um modelo de maturidade: cinco níveis,
do inicial ao em otimização, avaliando se a organização define, mede e melhora seus processos. Sua
contribuição duradoura é a ideia de que processo pode ser medido e comparado. Seu efeito colateral
conhecido é a certificação como objetivo — organizações otimizando para a avaliação, produzindo
evidência documental sem mudança de prática.

O **MPS.BR** é o capítulo brasileiro dessa história e merece ser ensinado no país. Criado a partir
de 2003 pela Softex com apoio governamental, propunha um modelo de maturidade compatível com CMMI
mas adaptado à realidade nacional: níveis mais granulares, da letra G à A, para que empresas
pequenas pudessem progredir em passos financiáveis, e custo de avaliação compatível com o porte
das empresas brasileiras. O problema que ele endereçava era concreto — o custo de uma avaliação
CMMI era proibitivo para a maior parte do parque nacional, e a exigência de maturidade aparecia em
licitações públicas e em exportação de serviços.

O balanço honesto é misto e depende de qual pergunta se faz. Como política industrial de
qualificação, o MPS.BR alcançou centenas de avaliações e produziu vocabulário e prática de processo
em empresas que não tinham nenhum. Como resposta à pergunta "isso produz software melhor?", a
evidência é mais fraca e sofre do mesmo viés de seleção que afeta o CMMI: organizações que se
candidatam a avaliação já são diferentes das que não se candidatam. O capítulo 3.6 retoma o
assunto pelo lado do ecossistema.

### 3.2.4 A era ágil — manifesto, XP, Scrum, Kanban

O Manifesto Ágil, de 2001, é um documento de dezessete pessoas com quatro valores e doze
princípios, e sua característica mais relevante é a forma: cada valor é comparativo, não absoluto.
"Indivíduos e interações **mais que** processos e ferramentas" — a segunda metade tem valor, apenas
menos. Praticamente toda distorção posterior vem de ler a primeira metade e apagar a segunda.

**XP**, formulado por Kent Beck no fim dos anos 1990, é a proposta mais radical e a mais técnica.
Suas práticas — programação em par, TDD, integração contínua, propriedade coletiva do código,
refatoração constante, cliente presente — formam um sistema em que uma sustenta a outra. Vale
notar o que a história fez com ele: XP foi a metodologia ágil com práticas de engenharia mais
fortes e a que menos sobreviveu como pacote, enquanto suas práticas individuais — integração
contínua, TDD, refatoração — se tornaram universais fora do rótulo.

**Scrum** venceu em adoção, e é útil entender por quê. Ele é um arcabouço de gestão, não de
engenharia: define papéis, eventos e artefatos, e é deliberadamente silencioso sobre como se
escreve software. Isso o torna adotável por qualquer organização sem mudar nada de técnico — o que
explica simultaneamente sua difusão e a queixa mais comum contra ele, que é entregar cerimônia sem
melhorar a engenharia. A adoção de Scrum sem as práticas técnicas de XP produz iterações regulares
sobre uma base que continua difícil de mudar, e o resultado previsível é velocidade decrescente
com cerimônia constante.

**Kanban**, trazido do sistema Toyota por David Anderson, muda o eixo: em vez de iterações de
duração fixa, foco em fluxo contínuo, visualização do trabalho, limite de trabalho em progresso e
medição de tempo de ciclo. O limite de WIP é a ideia mais subestimada do conjunto e a mais bem
fundamentada — é a Lei de Little da seção 2.3.2 aplicada a pessoas: reduzir trabalho simultâneo
reduz tempo de entrega, e a intuição contrária custa caro em quase toda organização.

### 3.2.5 Escala — SAFe, LeSS e o mito do modelo Spotify

Assim que o ágil chegou a organizações grandes, apareceu a pergunta de como coordenar dezenas de
equipes, e as respostas se dividiram em duas famílias com filosofias opostas.

**SAFe** é a resposta por adição: camadas de planejamento, papéis de coordenação, cadências
sincronizadas, e um evento de planejamento conjunto. É de longe o mais adotado em empresas grandes,
e a razão é honesta — ele oferece a estrutura de gestão que uma organização hierárquica reconhece,
permitindo adotar vocabulário ágil sem alterar a estrutura de poder. A crítica, feita inclusive por
signatários do manifesto, é que isso reconstrói o processo pesado que o ágil pretendia substituir,
agora com nomes novos.

**LeSS** é a resposta por subtração: manter um Scrum, um backlog e um dono de produto, e escalar
por mais equipes no mesmo processo, removendo estrutura em vez de acrescentar. É intelectualmente
mais coerente com o manifesto e muito menos adotado, porque exige mudar a organização de verdade —
o que é precisamente o custo que a maioria não quer pagar.

O **modelo Spotify** é o caso mais instrutivo dos três, e não é um modelo. Origina-se de um artigo
de 2012 de Henrik Kniberg e Anders Ivarsson descrevendo como a empresa estava organizada naquele
momento, com o aviso explícito de que era um retrato e não uma receita. O vocabulário de squads,
tribes, chapters e guilds foi copiado por centenas de organizações como se fosse um método, e o
próprio Spotify depois publicou que havia abandonado partes daquilo. O mecanismo é o mesmo que a
seção 3.2.2 descreve para Royce: um artefato descritivo, lido como prescritivo, sobrevivendo às
ressalvas de quem o escreveu.

A lição transferível é sobre transplante de estrutura. Copiar a organização de outra empresa
importa a solução sem o contexto — o produto, a escala, a cultura, o momento e os problemas que
aquela estrutura resolvia. Pela Lei de Conway, a estrutura copiada vai produzir a arquitetura dela,
não a que você precisa.

### 3.2.6 Pós-ágil — fluxo, produto, descoberta contínua, agile washing

O termo pós-ágil não nomeia um método; nomeia o período em que o rótulo perdeu valor
discriminante. Três movimentos ocupam esse espaço, e nenhum deles se apresenta como sucessor.

O primeiro é o deslocamento da **iteração para o fluxo**. A pergunta deixa de ser quanto cabe no
sprint e passa a ser quanto tempo leva uma mudança da ideia à produção. As métricas DORA — frequência
de implantação, tempo de espera, taxa de falha de mudança, tempo de restauração — deram a esse
deslocamento uma base empírica que o ágil original não tinha, e o capítulo 3.3 as retoma. A
contribuição relevante do trabalho de Forsgren, Humble e Kim é mostrar que velocidade e estabilidade
não são opostas: as organizações que entregam mais rápido também falham menos, o que desmonta o
trade-off que boa parte da governança assume.

O segundo é o deslocamento do **projeto para o produto**. Equipes estáveis responsáveis por um
resultado continuado, em vez de equipes montadas por projeto e dissolvidas na entrega. É a mesma
ideia de propriedade da seção 2.6.3, no nível organizacional, e casa com o modelo de equipe
alinhada a fluxo da seção 3.1.9.

O terceiro é a **descoberta contínua**: reconhecer que o problema não vem pronto e que a equipe
precisa investigar demanda continuamente, e não apenas construir o que foi pedido. É o capítulo 2.5
como atividade permanente em vez de fase inicial.

E há o fenômeno que dá nome à erosão: **agile washing**. Organizações que adotaram o vocabulário e
os eventos sem transferir decisão para quem faz o trabalho. O sintoma diagnóstico não é a
cerimônia — é a ausência de mudança na estrutura de decisão. Se a equipe não pode alterar escopo,
não pode dizer não a trabalho, não pode escolher como construir e não pode parar a linha, então
retrospectiva é conversa sem consequência, e o processo é Waterfall com reuniões diárias. Quem já
viveu os dois reconhece a diferença rapidamente, e é o que faz um profissional que atravessou a
transição ler o pós-ágil melhor do que quem chegou já dentro dele — o argumento da seção 0.2 sobre
por que a camada cíclica premia quem viu a volta anterior.

### 3.2.7 Estimativa, #NoEstimates e a política das estimativas

Poucos assuntos produzem tanto atrito com tão pouca clareza sobre o que está em disputa. Vale
separar três questões que costumam ser tratadas como uma.

A primeira é **cognitiva**: pessoas estimam mal tarefas de software, de forma sistemática e na mesma
direção. A falácia do planejamento, descrita por Kahneman e Tversky, prevê subestimação persistente
mesmo com experiência prévia contrária, e software tem um agravante — boa parte do trabalho é
descoberta, e não se estima bem o tempo de descobrir o que não se sabe.

A segunda é **estatística**: uma estimativa é uma distribuição, e reportá-la como número único
descarta a informação que importa. "Duas semanas" não distingue algo com variância baixa de algo
que pode levar dois meses. Práticas que preservam a incerteza — faixas, níveis de confiança,
previsão a partir de dados históricos de fluxo — dão respostas mais úteis do que a soma de palpites,
e a previsão baseada em tempo de ciclo medido supera a estimativa em pontos na maioria dos
contextos em que ambos foram comparados.

A terceira é **política**, e é a que raramente se admite. Estimativas frequentemente não são pedidas
para planejar: são pedidas para criar compromisso, distribuir responsabilidade por atraso ou
sustentar uma data já decidida em outro lugar. Nesse uso, nenhuma melhoria de técnica ajuda,
porque o problema não é de precisão. O sintoma clássico é a estimativa questionada até baixar — o
que transforma o exercício em negociação com aparência de análise.

**#NoEstimates** é mais bem compreendido como provocação do que como método. A pergunta que ele
faz é legítima: qual decisão será tomada de forma diferente em função desta estimativa? Quando não
há resposta, o esforço é desperdício. Quando há — investimento, contrato, coordenação com terceiros,
obrigação regulatória —, a estimativa é necessária, e o caminho é fazê-la com honestidade
estatística. Fatiar o trabalho em unidades pequenas e semelhantes e medir vazão real costuma
entregar previsibilidade melhor do que estimar cada item, e é a resposta que sobrevive à discussão
ideológica.

### 3.2.8 Do campo: ágil dentro de janela de GMUD em ambiente bancário

*Esta seção é relato de campo. As afirmações abaixo são o argumento; os episódios concretos que as
sustentam entram na revisão, pela mesma regra da seção 2.2.8.*

O manifesto pressupõe uma coisa que ambientes bancários brasileiros não oferecem por padrão: que a
equipe controla quando o software chega à produção. Onde existe gestão formal de mudança — comitê
de aprovação, janela definida, congelamento em fechamento contábil, segregação de funções exigida
por auditoria —, entrega contínua não é uma escolha de engenharia. É uma negociação com governança
que responde a regulador, e o regulador não é parte do time.

A primeira observação é que o conflito costuma ser mal diagnosticado. A leitura fácil é que a
governança é burocracia atrasada; a leitura correta é que ela existe para responder a uma pergunta
legítima — quem autorizou, o que exatamente mudou, como se reverte e quem responde. O ágil não
tem, no manifesto, resposta para essas quatro perguntas. Tem nas práticas: controle de versão como
registro de autoria, implantação automatizada como descrição exata do que mudou, reversão testada
como plano de contingência, e teste automatizado como evidência. O caminho que funciona é
substituir controle manual por controle automatizado auditável — não pedir dispensa de controle.

A segunda é sobre o efeito da janela no tamanho do lote. Quando a implantação só pode acontecer em
datas fixas e espaçadas, o lote cresce, e lote grande é a causa mecânica de risco: mais mudanças
por implantação, mais interação entre elas, diagnóstico mais difícil quando falha, reversão que
desfaz o que estava certo junto com o que estava errado. É um resultado bem estabelecido, e produz
um argumento que a governança aceita melhor do que o argumento de agilidade: janelas raras não
reduzem risco, concentram risco. Separar implantação de liberação — subir código desativado por
chave de funcionalidade, liberar depois — é a técnica que permite frequência alta de implantação
mantendo o controle formal sobre a liberação, e é o meio-termo que costuma passar.

A terceira é sobre o que sobrevive quando o ambiente não permite o pacote completo. Não se
consegue implantar dez vezes por dia dentro de janela de GMUD; consegue-se integrar continuamente,
manter a base sempre implantável, automatizar teste e reversão, reduzir o lote, e ter
retrospectiva com consequência. Essas são práticas de engenharia, e a maior parte delas não pede
autorização de comitê nenhum. É a diferença entre adotar ágil como identidade — que trava no
primeiro conflito com a governança — e adotá-lo como conjunto de práticas com valor independente,
que é o que atravessa.

**Fontes primárias do capítulo.** Naur, P. e Randell, B. (eds.), *Software Engineering: NATO
Conference Report*, Garmisch, 1968 · Royce, W., [*Managing the Development of Large Software
Systems*](https://www.praxisframework.org/files/royce1970.pdf), IEEE WESCON, 1970 · Beck, K. et
al., [*Manifesto for Agile Software Development*](https://agilemanifesto.org/), 2001 · Beck, K.,
*Extreme Programming Explained*, 1999 · Schwaber, K. e Sutherland, J., [*The Scrum
Guide*](https://scrumguides.org/) · Anderson, D., *Kanban*, 2010 · Larman, C. e Vodde, B.,
*Large-Scale Scrum (LeSS)*, 2016 · Kniberg, H. e Ivarsson, A., [*Scaling Agile @
Spotify*](https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf), 2012 · Forsgren,
N., Humble, J. e Kim, G., *Accelerate*, 2018 · Humble, J. e Farley, D., *Continuous Delivery*,
2010 · Kahneman, D. e Tversky, A., *Intuitive Prediction: Biases and Corrective Procedures*, 1979 ·
SEI, *CMMI for Development*, v1.3, 2010 · Softex, [*MPS.BR — Guia
Geral*](https://softex.br/mpsbr/), a partir de 2003.

body = open('_body.html').read()

HEAD = """<title>Currículo Vivo</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,500;1,6..72,300&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --ground:#F2F4F0; --surface:#FAFBF8; --ink:#1B201D; --muted:#5C645E; --faint:#88908A;
  --rule:#DCE1D8; --rule-soft:#E8EBE4; --accent:#33604F; --accent-soft:#E2ECE5;
  --s1:#22403A; --s2:#3E6B5B; --s3:#6F9481; --s4:#A9C0B0; --alert:#9A6B22;
  --maxw:38rem;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0F1312; --surface:#161B19; --ink:#DCE3DB; --muted:#98A19A; --faint:#79827C;
    --rule:#28302C; --rule-soft:#1E2522; --accent:#7FBCA1; --accent-soft:#1C2A24;
    --s1:#9FC9B5; --s2:#79AE95; --s3:#54836E; --s4:#3A5B4C; --alert:#C79B4E;
  }
}
:root[data-theme="dark"]{
  --ground:#0F1312; --surface:#161B19; --ink:#DCE3DB; --muted:#98A19A; --faint:#79827C;
  --rule:#28302C; --rule-soft:#1E2522; --accent:#7FBCA1; --accent-soft:#1C2A24;
  --s1:#9FC9B5; --s2:#79AE95; --s3:#54836E; --s4:#3A5B4C; --alert:#C79B4E;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{background:var(--ground);color:var(--ink);margin:0;
  font-family:"Source Serif 4",Georgia,"Times New Roman",serif;
  font-size:16.5px;line-height:1.68;-webkit-font-smoothing:antialiased;overflow-x:hidden}
@media(min-width:40rem){body{font-size:17.5px;line-height:1.72}}
@media(min-width:90rem){body{font-size:18px}}
img,svg{max-width:100%;height:auto}
article p,article li,article h4{overflow-wrap:break-word}
article table{width:100%;border-collapse:collapse}
.wrap{max-width:76rem;margin:0 auto;padding:0 1.1rem}
@media(min-width:40rem){.wrap{padding:0 1.5rem}}
h1,h2,h3,h4{text-wrap:balance;font-family:"Newsreader",Georgia,serif;font-weight:500;margin:0}
code,.mono,.ficha,.snum,.num,.cnum,.eyebrow,.strata,.rm-meta{font-family:"IBM Plex Mono",ui-monospace,monospace}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}

/* ---------- cabeçalho ---------- */
header.masthead{border-bottom:1px solid var(--rule);background:var(--surface)}
.mast-in{display:grid;grid-template-columns:1fr;gap:2rem;padding:2.4rem 1.1rem 2.2rem;max-width:76rem;margin:0 auto}
@media(min-width:40rem){.mast-in{gap:2.5rem;padding:3.5rem 1.5rem 3rem}}
@media(min-width:62rem){.mast-in{grid-template-columns:1.15fr .85fr;align-items:start;gap:4rem}}
.eyebrow{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin-bottom:1.1rem}
.eyebrow a{color:var(--accent);text-decoration:none}
.eyebrow a:hover{text-decoration:underline}
h1.book{font-size:clamp(2.4rem,5.5vw,3.9rem);line-height:1.02;letter-spacing:-.02em;font-weight:300}
h1.book em{font-style:italic;color:var(--accent)}
.dek{margin-top:1.4rem;color:var(--muted);font-size:1.05rem;max-width:34rem}
.status{margin-top:1.8rem;display:flex;flex-wrap:wrap;gap:.5rem}
.chip{font-family:"IBM Plex Mono",monospace;font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;
  padding:.32rem .6rem;border:1px solid var(--rule);border-radius:2px;color:var(--muted)}
.chip.on{background:var(--accent-soft);border-color:transparent;color:var(--accent)}

/* ---------- controles ---------- */
.ctrls{display:flex;flex-wrap:wrap;gap:1.1rem;margin-top:1.6rem}
.ctrl{display:flex;align-items:center;gap:.5rem}
.ctrl>span{font-family:"IBM Plex Mono",monospace;font-size:.6rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--faint)}
.seg{display:flex;border:1px solid var(--rule);border-radius:2px;overflow:hidden}
.seg button{font-family:"IBM Plex Mono",monospace;font-size:.66rem;letter-spacing:.04em;
  padding:.3rem .55rem;background:none;border:0;border-right:1px solid var(--rule);
  color:var(--muted);cursor:pointer;line-height:1.4}
.seg button:last-child{border-right:0}
.seg button:hover{color:var(--ink)}
.seg button[aria-pressed="true"]{background:var(--accent-soft);color:var(--accent)}
body.sem-ficha .ficha{display:none}
body.largo{--maxw:45rem}

/* ---------- coluna estratigráfica ---------- */
.strata{border:1px solid var(--rule);background:var(--ground);padding:1.1rem}
.strata h2{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);
  font-family:"IBM Plex Mono",monospace;font-weight:400;margin-bottom:.9rem}
.band{display:grid;grid-template-columns:4.6rem minmax(0,1fr) auto;align-items:center;gap:.6rem;padding:.3rem 0}
@media(min-width:40rem){.band{grid-template-columns:5.5rem minmax(0,1fr) auto;gap:.75rem}}
.band .lab{font-size:.72rem;color:var(--ink);line-height:1.25}
.band .lab em{display:block;font-style:normal;font-size:.62rem;color:var(--faint)}
.band .bar{height:100%;min-height:1.5rem;border-radius:1px}
.band .hv{font-size:.62rem;color:var(--faint);white-space:nowrap}
@media(min-width:40rem){.band .hv{font-size:.66rem}}
.strata .note{margin-top:.9rem;padding-top:.8rem;border-top:1px solid var(--rule-soft);
  font-family:"Source Serif 4",serif;font-size:.85rem;color:var(--muted);line-height:1.5}
.strata .note b{color:var(--ink);font-weight:600}

/* ---------- corpo ---------- */
.layout{display:grid;grid-template-columns:minmax(0,1fr);gap:2rem;padding:2.4rem 0 3.5rem}
@media(min-width:40rem){.layout{padding:3.5rem 0 5rem;gap:3rem}}
@media(min-width:62rem){
  .layout{grid-template-columns:13.5rem minmax(0,var(--maxw));justify-content:center;
    column-gap:4.5rem;padding:4rem 0 6rem}
}
@media(min-width:100rem){.layout{column-gap:6rem}}
details.toc{border:1px solid var(--rule);background:var(--surface);border-radius:2px;padding:.7rem .9rem;margin-bottom:.5rem}
details.toc summary{cursor:pointer;font-family:"IBM Plex Mono",monospace;font-size:.7rem;
  letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
details.toc a{display:block;color:var(--muted);text-decoration:none;font-size:.9rem;padding:.28rem 0}
details.toc a:first-of-type{margin-top:.7rem;border-top:1px solid var(--rule-soft);padding-top:.7rem}
@media(min-width:62rem){details.toc{display:none}}
nav.rail{display:none}
@media(min-width:62rem){
  nav.rail{display:block;position:sticky;top:2rem;align-self:start;max-height:calc(100vh - 4rem);overflow:auto}
}
nav.rail h2{font-family:"IBM Plex Mono",monospace;font-size:.66rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--faint);font-weight:400;margin-bottom:.7rem}
nav.rail a{display:block;text-decoration:none;color:var(--muted);font-size:.85rem;padding:.22rem 0;
  border-left:2px solid transparent;padding-left:.7rem;margin-left:-.7rem}
nav.rail a:hover{color:var(--ink)}
nav.rail a.at{color:var(--ink);border-left-color:var(--accent)}
nav.rail .grp{margin-bottom:1.3rem}
nav.rail .grp>span{font-family:"IBM Plex Mono",monospace;font-size:.66rem;color:var(--faint);
  letter-spacing:.08em;display:block;margin-bottom:.3rem}

article{min-width:0}
h2.camada,section.chapter h3,h4,#roteiro{scroll-margin-top:2.5rem}
article p+h4{margin-top:2.7rem}
h2.camada{margin:5rem 0 .4rem;display:flex;flex-direction:column;gap:.15rem;
  padding-top:1.6rem;border-top:2px solid var(--ink)}
h2.camada:first-child{margin-top:0}
.cnum{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.cname{font-size:clamp(1.6rem,1.1rem + 2.2vw,2rem);font-weight:300;letter-spacing:-.01em}
h2.camada + p em{color:var(--muted);font-size:.92rem;font-style:italic}

section.chapter{margin-top:3.8rem}
section.chapter h3{display:flex;gap:.85rem;align-items:baseline;margin-bottom:.9rem}
section.chapter h3 .num{font-size:.82rem;color:var(--accent);flex:none;padding-top:.2rem}
section.chapter h3 .ttl{font-size:clamp(1.28rem,1rem + 1.4vw,1.55rem);font-weight:500;letter-spacing:-.01em;line-height:1.2}
h4{margin:2.4rem 0 .7rem;font-size:1.08rem;font-weight:600;color:var(--ink);
  font-family:"Source Serif 4",serif}
h4 .snum{color:var(--faint);font-size:.78rem;margin-right:.45rem;font-weight:400}
article p{margin:0 0 1.15rem}
article p strong{font-weight:600}
article em{font-style:italic}

.ficha{display:flex;flex-wrap:wrap;gap:.35rem 1.7rem;margin:0 0 2.2rem;padding:.6rem 0;
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.ficha>div{display:flex;gap:.45rem;align-items:baseline;min-width:0}
.ficha dt{font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);flex:none}
.ficha dd{margin:0;font-size:.74rem;color:var(--muted);overflow-wrap:break-word}
.ficha code{font-size:.72rem;color:var(--accent)}

/* ---------- roteiro ---------- */
.roadmap{border-top:2px solid var(--ink);margin-top:5rem;padding-top:1.6rem}
.rm-cam{margin-top:2.2rem}
.rm-cam>summary{cursor:pointer;list-style:none;margin-bottom:.9rem}
.rm-cam>summary::-webkit-details-marker{display:none}
.rm-cam>summary::before{content:"–";color:var(--faint);margin-right:.5rem;
  font-family:"IBM Plex Mono",monospace;font-size:.8rem}
.rm-cam:not([open])>summary::before{content:"+"}
.rm-cam h4{display:inline-flex;align-items:baseline;gap:.7rem;margin:0;
  font-family:"Newsreader",serif;font-size:1.25rem;font-weight:500}
.rm-cam>h4 .hv{font-family:"IBM Plex Mono",monospace;font-size:.68rem;color:var(--faint);letter-spacing:.04em}
.rm-list{display:grid;gap:0;border-top:1px solid var(--rule-soft)}
.rm-item{display:grid;grid-template-columns:2.4rem minmax(0,1fr);gap:.2rem .7rem;align-items:baseline;
  padding:.6rem .2rem;border-bottom:1px solid var(--rule-soft)}
.rm-item .rm-meta{grid-column:2}
@media(min-width:34rem){
  .rm-item{grid-template-columns:2.6rem minmax(0,1fr) auto;gap:.8rem}
  .rm-item .rm-meta{grid-column:auto}
}
.rm-item .n{font-family:"IBM Plex Mono",monospace;font-size:.76rem;color:var(--accent)}
.rm-item .t{font-size:.98rem}
.rm-meta{font-size:.66rem;color:var(--faint);letter-spacing:.04em;white-space:nowrap}
.rm-item.vol .n,.rm-item.vol .rm-meta{color:var(--alert)}

footer{border-top:1px solid var(--rule);color:var(--muted);font-size:.85rem;
  padding:2.2rem 1.1rem 3.5rem;max-width:76rem;margin:0 auto}
@media(min-width:40rem){footer{padding:2.5rem 1.5rem 4rem}}
footer p{margin:0 0 .6rem;max-width:44rem}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>"""

BANDS = [
 ("Camada 1","Permanente","var(--s1)",5,"sem erosão observada"),
 ("Camada 2","Geracional","var(--s2)",6,"15–20 anos"),
 ("Camada 3","Cíclico","var(--s3)",7,"5–15 anos"),
 ("Camada 4","Sazonal","var(--s4)",3,"1–5 anos"),
]
bands=""
for cam,nome,cor,n,hv in BANDS:
    h = 1.5 + n*0.62
    bands += (f'<div class="band"><div class="lab">{nome}</div>'
              f'<div class="bar" style="background:{cor};height:{h}rem"><span>{n} capítulos</span></div>'
              f'<div class="hv">{hv}</div></div>')

ROADMAP = [
 ("2","Geracional","15–20 anos",[
   ("2.1","Paradigmas de programação","7 seções",0),
   ("2.2","Dados e persistência","8 seções",0),
   ("2.3","Sistemas distribuídos: fundamentos","7 seções",0),
   ("2.4","Linguagens de programação","6 seções",0),
   ("2.5","Requisitos, produto e IHC","7 seções",0),
   ("2.6","Comportamento e carreira","7 seções",0)]),
 ("3","Cíclico","5–15 anos",[
   ("3.1","Arquitetura de software","10 seções",0),
   ("3.2","Processos e metodologias","erosão · 8 seções",0),
   ("3.3","Qualidade, testes e débito técnico","9 seções",0),
   ("3.4","Ética, legislação e impacto","7 seções",0),
   ("3.5","O ensino formal","7 seções",0),
   ("3.6","Contexto brasileiro","8 seções",0),
   ("3.7","Economia da decisão","6 seções",0)]),
 ("4","Sazonal","1–5 anos",[
   ("4.1","Segurança e cadeia de suprimentos","~4 anos · 8 seções",0),
   ("4.2","Ferramentas e infraestrutura","2–5 anos · 10 seções",0),
   ("4.3","IA no ciclo de desenvolvimento","volátil · 1–2 anos",1)]),
]
rm=""
for num,nome,hv,itens in ROADMAP:
    rm += (f'<details class="rm-cam" open><summary><h4>Camada {num} · {nome} '
           f'<span class="hv">{hv}</span></h4></summary><div class="rm-list">')
    for n,t,meta,vol in itens:
        rm += (f'<div class="rm-item{" vol" if vol else ""}"><span class="n">{n}</span>'
               f'<span class="t">{t}</span><span class="rm-meta">{meta}</span></div>')
    rm += '</div></details>'

RAIL = """<nav class="rail" aria-label="Sumário">
<div class="grp"><span>Camada 0 · A Lente</span>
<a href="#c0">0 Como ler este livro</a></div>
<div class="grp"><span>Camada 1 · Permanente</span>
<a href="#c1-1">1.1 Fundação conceitual</a>
<a href="#c1-2">1.2 Os invariantes nomeados</a>
<a href="#c1-3">1.3 O teste de perenidade</a>
<a href="#cFontes">Fontes</a></div>
<div class="grp"><span>A escrever</span>
<a href="#roteiro">Camadas 2 a 4</a></div>
</nav>"""

HTML = HEAD + f"""
<header class="masthead">
  <div class="mast-in">
    <div>
      <div class="eyebrow"><a href="index.html">&larr; Portal</a> &nbsp;·&nbsp; volume um &nbsp;·&nbsp; <a href="estudos.html">Plano de estudos &rarr;</a></div>
      <h1 class="book">Engenharia de Software:<br><em>Envelhecimento Macro</em></h1>
      <p class="dek">Um currículo organizado por uma pergunta só — em quanto tempo cada
      conhecimento envelhece. Vinte e um capítulos distribuídos em quatro camadas de
      velocidade, cada seção com data de revisão e gatilho declarados.</p>
      <div class="ctrls">
        <div class="ctrl"><span>Tema</span>
          <div class="seg" role="group" aria-label="Tema">
            <button type="button" data-tema="auto">Auto</button>
            <button type="button" data-tema="light">Claro</button>
            <button type="button" data-tema="dark">Escuro</button>
          </div></div>
        <div class="ctrl"><span>Coluna</span>
          <div class="seg" role="group" aria-label="Largura da coluna">
            <button type="button" data-larg="normal">Normal</button>
            <button type="button" data-larg="largo">Larga</button>
          </div></div>
        <div class="ctrl"><span>Fichas</span>
          <div class="seg" role="group" aria-label="Fichas de envelhecimento">
            <button type="button" data-ficha="on">Mostrar</button>
            <button type="button" data-ficha="off">Ocultar</button>
          </div></div>
      </div>
      <div class="status">
        <span class="chip on">Camadas 0 e 1 escritas</span>
        <span class="chip">~5.800 palavras</span>
        <span class="chip">Índice v3</span>
        <span class="chip">01·09·2026</span>
      </div>
    </div>
    <div class="strata">
      <h2>Coluna estratigráfica</h2>
      {bands}
      <p class="note">A espessura de cada faixa é o número de capítulos. Três dos vinte e
      um estão na camada sazonal: <b>a ansiedade que o mercado produz se concentra em 14%
      do currículo.</b></p>
    </div>
  </div>
</header>

<div class="wrap">
 <div class="layout">
  {RAIL}
  <article>
   <details class="toc"><summary>Sumário</summary>
     <a href="#c0">0 · Como ler este livro</a>
     <a href="#c1-1">1.1 · Fundação conceitual</a>
     <a href="#c1-2">1.2 · Os invariantes nomeados</a>
     <a href="#c1-3">1.3 · O teste de perenidade</a>
     <a href="#cFontes">Fontes</a>
     <a href="#roteiro">Camadas 2 a 4 · a escrever</a>
   </details>
   {body}
   <div class="roadmap" id="roteiro">
     <h2 class="camada" style="border:0;padding:0;margin:0 0 .5rem">
       <span class="cnum">A escrever</span><span class="cname">Camadas 2 a 4</span></h2>
     <p style="color:var(--muted);font-size:.95rem">Dezesseis capítulos com a ficha definida
     e o texto pendente. A ordem de escrita segue a regra do plano: fichas antes de prosa.</p>
     {rm}
   </div>
  </article>
 </div>
</div>

<footer>
  <p><strong>Estado desta publicação.</strong> Texto integral das camadas 0 e 1; índice
  completo das camadas 2 a 4. As datas e atribuições das fontes primárias ainda não foram
  conferidas contra as edições originais.</p>
  <p>Classificação por eixo único de velocidade (índice v3). O assunto de cada capítulo é
  etiqueta na ficha, não divisão estrutural. Cada capítulo tem slug estável — a numeração
  é apenas exibição, para que renumerações futuras não quebrem links.</p>
</footer>
"""
CTRL = """
<script>
(function(){
  var raiz=document.documentElement, corpo=document.body;
  function ler(k,p){ try{ return localStorage.getItem(k)||p; }catch(e){ return p; } }
  function salvar(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  function marcar(attr,valor){
    [].forEach.call(document.querySelectorAll('[data-'+attr+']'),function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-'+attr)===valor ? 'true':'false');
    });
  }
  function tema(v){
    if(v==='auto'){ raiz.removeAttribute('data-theme'); } else { raiz.setAttribute('data-theme',v); }
    marcar('tema',v); salvar('cv-tema',v);
  }
  function largura(v){ corpo.classList.toggle('largo', v==='largo'); marcar('larg',v); salvar('cv-larg',v); }
  function fichas(v){ corpo.classList.toggle('sem-ficha', v==='off'); marcar('ficha',v); salvar('cv-ficha',v); }

  tema(ler('cv-tema','auto'));
  largura(ler('cv-larg','normal'));
  fichas(ler('cv-ficha','on'));

  document.addEventListener('click',function(e){
    var b=e.target.closest && e.target.closest('button[data-tema],button[data-larg],button[data-ficha]');
    if(!b)return;
    if(b.hasAttribute('data-tema'))  tema(b.getAttribute('data-tema'));
    if(b.hasAttribute('data-larg'))  largura(b.getAttribute('data-larg'));
    if(b.hasAttribute('data-ficha')) fichas(b.getAttribute('data-ficha'));
  });
})();
</script>
"""

SPY = """
<script>
(function(){
  var links=[].slice.call(document.querySelectorAll('nav.rail a'));
  var alvos=links.map(function(a){return document.querySelector(a.getAttribute('href'));}).filter(Boolean);
  if(!alvos.length||!('IntersectionObserver' in window))return;
  var vistos=new Map();
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){vistos.set(e.target, e.isIntersecting?e.intersectionRatio:0);});
    var melhor=null,r=-1;
    vistos.forEach(function(v,k){ if(v>r){r=v;melhor=k;} });
    if(!melhor||r<=0)return;
    links.forEach(function(a){a.classList.toggle('at', a.getAttribute('href')==='#'+melhor.id);});
  },{rootMargin:'-8% 0px -72% 0px',threshold:[0,0.5,1]});
  alvos.forEach(function(t){io.observe(t);});
})();
</script>
"""
HTML += SPY + CTRL
open('_head.html','w').write(HEAD)
open('curriculo-vivo.html','w').write(HTML)
print(len(HTML))

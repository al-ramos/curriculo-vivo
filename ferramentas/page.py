import re
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
.wrap{max-width:88rem;margin:0 auto;padding:0 1.1rem}
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

/* seções recolhíveis */
details.sec{margin:0}
details.sec>summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:.5rem;
  margin:2.7rem 0 .7rem}
details.sec>summary::-webkit-details-marker{display:none}
details.sec>summary::before{content:"−";font-family:"IBM Plex Mono",monospace;font-size:.8rem;
  color:var(--faint);flex:none;width:.9rem;line-height:1.7}
details.sec:not([open])>summary::before{content:"+"}
details.sec>summary:hover::before{color:var(--accent)}
details.sec>summary h4{margin:0;flex:1}
details.sec:not([open])>summary{margin-bottom:.3rem}
.sec-corpo{padding-left:1.4rem;border-left:1px solid var(--rule-soft)}
.copiar{flex:none;align-self:center;font-family:"IBM Plex Mono",monospace;font-size:.6rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--surface);
  border:1px solid var(--rule);border-radius:2px;padding:.18rem .45rem;cursor:pointer;
  transition:color .15s,border-color .15s,background .15s;white-space:nowrap}
.copiar:hover{color:var(--accent);border-color:var(--accent)}
.copiar.ok{color:var(--ground);background:var(--accent);border-color:var(--accent)}
.marcar{flex:none;align-self:center;width:1.05rem;height:1.05rem;border-radius:50%;
  border:1.5px solid var(--rule);background:none;cursor:pointer;padding:0;position:relative}
.marcar:hover{border-color:var(--accent)}
.marcar[aria-pressed="true"]{background:var(--accent);border-color:var(--accent)}
.marcar[aria-pressed="true"]::after{content:"";position:absolute;left:.28rem;top:.12rem;
  width:.2rem;height:.42rem;border:solid var(--ground);border-width:0 1.5px 1.5px 0;
  transform:rotate(45deg)}
details.sec.lida>summary h4{color:var(--faint)}

/* trilho com subtópicos — só o capítulo ativo se abre */
nav.rail a.cap{font-size:.84rem;line-height:1.35;padding:.26rem 0 .26rem .7rem}
nav.rail a.cap.at{color:var(--ink);border-left-color:var(--accent);font-weight:600}
nav.rail .sub{display:none;margin:.05rem 0 .45rem}
nav.rail .sub.aberta{display:block}
nav.rail a.sub-a{font-size:.76rem;padding:.16rem 0 .16rem 1.5rem;color:var(--faint);line-height:1.3}
nav.rail a.sub-a:hover{color:var(--ink)}
nav.rail a.sub-a.at{color:var(--accent);border-left-color:var(--accent)}
nav.rail a.sub-a.lida{color:var(--rule);text-decoration:line-through;text-decoration-color:var(--rule)}

/* coluna de apoio */
aside.lado{display:none}
@media(min-width:82rem){
  aside.lado{display:block;position:sticky;top:2.5rem;align-self:start;
    max-height:calc(100vh - 5rem);overflow-y:auto;scrollbar-width:thin;
    scrollbar-color:var(--rule) transparent}
}
aside.lado h2{font-family:"IBM Plex Mono",monospace;font-size:.62rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--faint);font-weight:400;margin:0 0 .7rem}
aside.lado .cx{border-left:1px solid var(--rule);padding:0 0 0 1rem;margin-bottom:1.8rem}
aside.lado .lin{display:flex;justify-content:space-between;gap:.6rem;padding:.22rem 0;
  font-size:.78rem;color:var(--muted)}
aside.lado .lin b{font-family:"IBM Plex Mono",monospace;font-size:.74rem;
  font-weight:500;color:var(--ink);font-variant-numeric:tabular-nums}
aside.lado button.acao{width:100%;text-align:left;font-family:"IBM Plex Mono",monospace;
  font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);
  background:none;border:1px solid var(--rule);border-radius:2px;padding:.35rem .5rem;
  cursor:pointer;margin-top:.5rem}
aside.lado button.acao:hover{color:var(--accent);border-color:var(--accent)}
aside.lado button.acao[aria-pressed="true"]{background:var(--accent-soft);color:var(--accent);
  border-color:transparent}
body.so-nao-lidas details.sec.lida{display:none}

/* tempo de leitura e notas */
.tempo{flex:none;align-self:center;font-family:"IBM Plex Mono",monospace;font-size:.6rem;
  color:var(--faint);letter-spacing:.04em;white-space:nowrap}
.dobrar{flex:none;align-self:center;font-family:"IBM Plex Mono",monospace;font-size:.6rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--surface);
  border:1px solid var(--rule);border-radius:2px;padding:.18rem .45rem;cursor:pointer;
  white-space:nowrap;min-width:5.2rem;text-align:center}
.dobrar:hover{color:var(--accent);border-color:var(--accent)}
.nota-btn{flex:none;align-self:center;font-family:"IBM Plex Mono",monospace;font-size:.6rem;
  letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--surface);
  border:1px solid var(--rule);border-radius:2px;padding:.18rem .45rem;cursor:pointer}
.nota-btn:hover{color:var(--accent);border-color:var(--accent)}
.nota-btn.tem{color:var(--accent);border-color:var(--accent)}
.nota{display:none;margin:.9rem 0 0}
.nota.aberta{display:block}
.nota textarea{width:100%;min-height:5.5rem;resize:vertical;background:var(--surface);
  color:var(--ink);border:1px solid var(--rule);border-radius:2px;padding:.6rem .7rem;
  font-family:"Source Serif 4",serif;font-size:.92rem;line-height:1.5}
.nota textarea:focus{outline:none;border-color:var(--accent)}
.nota .dica{font-family:"IBM Plex Mono",monospace;font-size:.58rem;color:var(--faint);
  letter-spacing:.06em;margin-top:.25rem}

/* progresso */
.prog{margin-bottom:1.1rem;padding-bottom:.8rem;border-bottom:1px solid var(--rule-soft)}
.prog .barra{height:3px;background:var(--rule-soft);border-radius:2px;overflow:hidden;margin-bottom:.4rem}
.prog .barra i{display:block;height:100%;background:var(--accent);width:0;transition:width .3s}
.prog .txt{font-family:"IBM Plex Mono",monospace;font-size:.62rem;color:var(--faint);letter-spacing:.06em}
.chip.voltar{border-color:var(--accent);color:var(--accent);text-decoration:none;cursor:pointer}

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
  .layout{grid-template-columns:14rem minmax(0,var(--maxw));justify-content:start;
    column-gap:3.5rem;padding:3.5rem 0 6rem}
}
@media(min-width:82rem){
  .layout{grid-template-columns:15rem minmax(0,var(--maxw)) minmax(0,16rem);column-gap:4rem}
}
@media(min-width:104rem){.layout{--maxw:42rem;column-gap:5rem}}
details.toc{border:1px solid var(--rule);background:var(--surface);border-radius:2px;padding:.7rem .9rem;margin-bottom:.5rem}
details.toc summary{cursor:pointer;font-family:"IBM Plex Mono",monospace;font-size:.7rem;
  letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
details.toc a{display:block;color:var(--muted);text-decoration:none;font-size:.9rem;padding:.28rem 0}
details.toc a:first-of-type{margin-top:.7rem;border-top:1px solid var(--rule-soft);padding-top:.7rem}
@media(min-width:62rem){details.toc{display:none}}
nav.rail{display:none}
@media(min-width:62rem){
  nav.rail{display:block;position:sticky;top:2.5rem;align-self:start;
    max-height:calc(100vh - 5rem);overflow-y:auto;overscroll-behavior:contain;
    scrollbar-width:thin;scrollbar-color:var(--rule) transparent;
    padding-right:.4rem}
  nav.rail::-webkit-scrollbar{width:6px}
  nav.rail::-webkit-scrollbar-thumb{background:var(--rule);border-radius:3px}
  nav.rail::-webkit-scrollbar-track{background:transparent}
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

marcas = []
for mm in re.finditer(r'<h2 class="camada" id="([^"]+)"><span class="cnum">([^<]*)</span><span class="cname">([^<]*)</span>', body):
    marcas.append((mm.start(), 0, mm.group(1), mm.group(2), mm.group(3)))
for mm in re.finditer(r'<h3 id="([^"]+)"><span class="num">([^<]*)</span><span class="ttl">([^<]*)</span>', body):
    marcas.append((mm.start(), 1, mm.group(1), mm.group(2), mm.group(3)))
for mm in re.finditer(r'<details class="sec" open id="([^"]+)" data-num="([^"]*)" data-tit="([^"]*)"', body):
    marcas.append((mm.start(), 2, mm.group(1), mm.group(2), mm.group(3)))
marcas.sort()

partes = ['<nav class="rail" aria-label="Sum\u00e1rio">',
          '<div class="prog"><div class="barra"><i></i></div><div class="txt">0 de 0 se\u00e7\u00f5es</div></div>']
em_grupo = em_sub = False
for _, tipo, idd, a, b in marcas:
    if tipo == 0:
        if em_sub: partes.append('</div>'); em_sub = False
        if em_grupo: partes.append('</div>')
        partes.append('<div class="grp"><span>' + a + ' \u00b7 ' + b + '</span>')
        em_grupo = True
    elif tipo == 1:
        if em_sub: partes.append('</div>'); em_sub = False
        partes.append('<a class="cap" id="rail-' + idd + '" href="#' + idd + '">' + a + ' ' + b + '</a>')
        partes.append('<div class="sub" data-cap="' + idd + '">'); em_sub = True
    else:
        partes.append('<a class="sub-a" href="#' + idd + '">' + a + ' ' + b + '</a>')
if em_sub: partes.append('</div>')
if em_grupo: partes.append('</div>')
partes.append('<div class="grp"><span>A escrever</span>'
              '<a class="cap" href="#roteiro">Camadas 2 a 4</a></div></nav>')
RAIL = ''.join(partes)

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
        <div class="ctrl"><span>Seções</span>
          <div class="seg" role="group" aria-label="Seções do texto">
            <button type="button" data-secs="abertas">Abertas</button>
            <button type="button" data-secs="fechadas">Recolhidas</button>
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
  <aside class="lado" aria-label="Apoio ao estudo">
    <h2>Nesta leitura</h2>
    <div class="cx">
      <div class="lin"><span>Seções lidas</span><b id="ap-lidas">0 / 0</b></div>
      <div class="lin"><span>Tempo restante</span><b id="ap-tempo">—</b></div>
      <div class="lin"><span>Notas</span><b id="ap-notas">0</b></div>
      <button class="acao" type="button" id="ap-filtro" aria-pressed="false">Mostrar só as não lidas</button>
      <button class="acao" type="button" id="ap-exportar">Exportar notas</button>
      <button class="acao" type="button" id="ap-zerar">Zerar progresso</button>
    </div>
    <h2>Atalhos</h2>
    <div class="cx">
      <div class="lin"><span>Próxima seção</span><b>J</b></div>
      <div class="lin"><span>Seção anterior</span><b>K</b></div>
      <div class="lin"><span>Marcar como lida</span><b>M</b></div>
      <div class="lin"><span>Copiar a seção</span><b>C</b></div>
    </div>
  </aside>
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
    var ativo = document.querySelector('nav.rail a.at');
    var bloco = ativo && ativo.closest('.sub');
    var cap = bloco ? bloco.getAttribute('data-cap') : (ativo ? ativo.getAttribute('href').slice(1) : null);
    [].forEach.call(document.querySelectorAll('nav.rail .sub'), function(d){
      d.classList.toggle('aberta', d.getAttribute('data-cap') === cap);
    });
    [].forEach.call(document.querySelectorAll('nav.rail a.cap'), function(a){
      a.classList.toggle('at', a.getAttribute('href') === '#' + cap);
    });
  },{rootMargin:'-8% 0px -72% 0px',threshold:[0,0.5,1]});
  alvos.forEach(function(t){io.observe(t);});
})();
</script>
"""
PROG = r"""
<script>
(function(){
  var chave = 'cv-' + (location.pathname.split('/').pop() || 'index');
  function ler(k,p){ try{ var v=localStorage.getItem(chave+'-'+k); return v===null?p:v; }catch(e){ return p; } }
  function salvar(k,v){ try{ localStorage.setItem(chave+'-'+k, v); }catch(e){} }

  var secs = [].slice.call(document.querySelectorAll('details.sec'));
  if(!secs.length) return;
  var lidas = new Set((ler('lidas','')||'').split(',').filter(Boolean));
  var barra = document.querySelector('.prog .barra i');
  var txt = document.querySelector('.prog .txt');

  function pintar(){
    secs.forEach(function(d){
      var m = d.querySelector('.marcar');
      var on = lidas.has(d.id);
      d.classList.toggle('lida', on);
      if(m) m.setAttribute('aria-pressed', on ? 'true' : 'false');
      var link = document.querySelector('nav.rail a[href="#'+d.id+'"]');
      if(link) link.classList.toggle('lida', on);
    });
    var n = 0;
    secs.forEach(function(d){ if(lidas.has(d.id)) n++; });
    if(barra) barra.style.width = (n / secs.length * 100) + '%';
    if(txt) txt.textContent = n + ' de ' + secs.length + ' seções lidas';
    salvar('lidas', Array.from(lidas).join(','));
  }

  // converte o corpo da seção em texto com marcação leve
  function paraTexto(el){
    var out = [];
    [].forEach.call(el.children, function(n){
      var t = n.tagName;
      if(t === 'P' || t === 'BLOCKQUOTE'){
        var s = '';
        [].forEach.call(n.childNodes, function(c){
          if(c.nodeType === 3) s += c.nodeValue;
          else if(c.tagName === 'STRONG' || c.tagName === 'B') s += '**' + c.textContent + '**';
          else if(c.tagName === 'EM' || c.tagName === 'I') s += '*' + c.textContent + '*';
          else if(c.tagName === 'CODE') s += '`' + c.textContent + '`';
          else s += c.textContent;
        });
        s = s.replace(/\s+/g, ' ').trim();
        out.push(t === 'BLOCKQUOTE' ? '> ' + s : s);
      } else if(t === 'UL' || t === 'OL'){
        [].forEach.call(n.children, function(li){
          out.push('- ' + li.textContent.replace(/\s+/g,' ').trim());
        });
      } else {
        var s2 = n.textContent.replace(/\s+/g,' ').trim();
        if(s2) out.push(s2);
      }
    });
    return out.join('\n\n');
  }

  function copiar(txt, botao){
    function feito(){
      var antes = botao.textContent;
      botao.textContent = 'copiado';
      botao.classList.add('ok');
      setTimeout(function(){ botao.textContent = antes; botao.classList.remove('ok'); }, 1600);
    }
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(txt).then(feito, function(){ velho(txt, feito); });
    } else { velho(txt, feito); }
  }
  function velho(txt, feito){
    try{
      var ta = document.createElement('textarea');
      ta.value = txt; ta.setAttribute('readonly','');
      ta.style.position = 'fixed'; ta.style.top = '-1000px';
      document.body.appendChild(ta); ta.select();
      document.execCommand('copy'); document.body.removeChild(ta);
      feito();
    }catch(e){}
  }

  secs.forEach(function(d){
    var sum = d.querySelector('summary');
    if(!sum || sum.querySelector('.marcar')) return;

    var c = document.createElement('button');
    c.type = 'button'; c.className = 'copiar'; c.textContent = 'copiar';
    c.title = 'Copiar o texto desta seção';
    c.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      var corpo = d.querySelector('.sec-corpo');
      var cab = '## ' + d.getAttribute('data-num') + ' ' + d.getAttribute('data-tit');
      var txt = cab + '\n\n' + (corpo ? paraTexto(corpo) : '');
      var nt = '';
      try{ nt = localStorage.getItem(chave + '-nota-' + d.id) || ''; }catch(e){}
      if(nt.trim()) txt += '\n\n> **Nota:** ' + nt.trim().replace(/\n+/g, ' ');
      copiar(txt, c);
    });
    // dobrar / desdobrar a seção
    var db = document.createElement('button');
    db.type = 'button'; db.className = 'dobrar';
    function rotulo(){
      db.textContent = d.open ? 'recolher' : 'expandir';
      db.setAttribute('aria-expanded', d.open ? 'true' : 'false');
      db.title = d.open ? 'Recolher esta seção' : 'Expandir esta seção';
    }
    rotulo();
    db.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      d.open = !d.open;
    });
    d.addEventListener('toggle', rotulo);
    sum.appendChild(db);

    // tempo estimado de leitura
    var corpoEl = d.querySelector('.sec-corpo');
    var palavras = corpoEl ? corpoEl.textContent.trim().split(/\s+/).length : 0;
    var min = Math.max(1, Math.round(palavras / 200));
    d.setAttribute('data-min', min);
    var t = document.createElement('span');
    t.className = 'tempo'; t.textContent = min + ' min';
    sum.appendChild(t);

    // nota pessoal
    var nb = document.createElement('button');
    nb.type = 'button'; nb.className = 'nota-btn'; nb.textContent = 'nota';
    nb.title = 'Anotar sobre esta seção';
    var cx = document.createElement('div');
    cx.className = 'nota';
    var ta = document.createElement('textarea');
    ta.placeholder = 'Sua anotação sobre ' + d.getAttribute('data-num') + '…';
    var dica = document.createElement('div');
    dica.className = 'dica'; dica.textContent = 'salvo neste navegador · entra junto no copiar';
    cx.appendChild(ta); cx.appendChild(dica);
    if(corpoEl) corpoEl.appendChild(cx);
    try{ ta.value = localStorage.getItem(chave + '-nota-' + d.id) || ''; }catch(e){}
    if(ta.value) nb.classList.add('tem');
    ta.addEventListener('input', function(){
      try{
        if(ta.value.trim()) localStorage.setItem(chave + '-nota-' + d.id, ta.value);
        else localStorage.removeItem(chave + '-nota-' + d.id);
      }catch(e){}
      nb.classList.toggle('tem', !!ta.value.trim());
      resumo();
    });
    nb.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      d.open = true;
      cx.classList.toggle('aberta');
      if(cx.classList.contains('aberta')) ta.focus();
    });
    sum.appendChild(nb);
    sum.appendChild(c);
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'marcar';
    b.setAttribute('aria-pressed','false');
    b.title = 'Marcar como lida';
    b.setAttribute('aria-label','Marcar seção como lida');
    b.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      if(lidas.has(d.id)) lidas.delete(d.id); else lidas.add(d.id);
      pintar();
    });
    sum.appendChild(b);
  });
  pintar();

  // recolher / expandir tudo
  function secoes(v){
    secs.forEach(function(d){ d.open = (v !== 'fechadas'); });
    [].forEach.call(document.querySelectorAll('[data-secs]'), function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-secs') === v ? 'true' : 'false');
    });
    salvar('secs', v);
  }
  secoes(ler('secs','abertas'));
  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('button[data-secs]');
    if(b) secoes(b.getAttribute('data-secs'));
  });

  // painel de apoio
  function resumo(){
    var lidasN = 0, restante = 0, notas = 0;
    secs.forEach(function(d){
      var m = parseInt(d.getAttribute('data-min') || '0', 10);
      if(lidas.has(d.id)) lidasN++; else restante += m;
      try{ if((localStorage.getItem(chave + '-nota-' + d.id) || '').trim()) notas++; }catch(e){}
    });
    var el;
    if(el = document.getElementById('ap-lidas')) el.textContent = lidasN + ' / ' + secs.length;
    if(el = document.getElementById('ap-tempo'))
      el.textContent = restante >= 60
        ? Math.floor(restante/60) + ' h ' + (restante%60) + ' min'
        : restante + ' min';
    if(el = document.getElementById('ap-notas')) el.textContent = String(notas);
  }
  var pintarAntes = pintar;
  pintar = function(){ pintarAntes(); resumo(); };
  pintar();

  var filtro = document.getElementById('ap-filtro');
  if(filtro) filtro.addEventListener('click', function(){
    var on = document.body.classList.toggle('so-nao-lidas');
    filtro.setAttribute('aria-pressed', on ? 'true' : 'false');
    filtro.textContent = on ? 'Mostrar todas as seções' : 'Mostrar só as não lidas';
  });

  var exportar = document.getElementById('ap-exportar');
  if(exportar) exportar.addEventListener('click', function(){
    var linhas = [];
    secs.forEach(function(d){
      var n = '';
      try{ n = localStorage.getItem(chave + '-nota-' + d.id) || ''; }catch(e){}
      if(n.trim()) linhas.push('## ' + d.getAttribute('data-num') + ' ' +
        d.getAttribute('data-tit') + '\n\n' + n.trim());
    });
    copiar(linhas.length ? linhas.join('\n\n---\n\n') : 'Nenhuma nota ainda.', exportar);
  });

  var zerar = document.getElementById('ap-zerar');
  if(zerar) zerar.addEventListener('click', function(){
    if(!lidas.size) return;
    lidas.clear(); pintar();
  });

  // atalhos de teclado
  document.addEventListener('keydown', function(e){
    if(e.metaKey || e.ctrlKey || e.altKey) return;
    var alvo = e.target;
    if(alvo && (alvo.tagName === 'TEXTAREA' || alvo.tagName === 'INPUT')) return;
    var k = e.key.toLowerCase();
    if(['j','k','m','c'].indexOf(k) === -1) return;
    var visiveis = secs.filter(function(d){ return d.offsetParent !== null; });
    var atualIdx = 0;
    for(var i = 0; i < visiveis.length; i++){
      if(visiveis[i].getBoundingClientRect().top <= 120) atualIdx = i;
    }
    var atual = visiveis[atualIdx];
    if(!atual) return;
    if(k === 'j' || k === 'k'){
      e.preventDefault();
      var alvoSec = visiveis[Math.min(visiveis.length - 1, Math.max(0, atualIdx + (k === 'j' ? 1 : -1)))];
      if(alvoSec) alvoSec.scrollIntoView({behavior: 'smooth', block: 'start'});
    } else if(k === 'm'){
      e.preventDefault();
      if(lidas.has(atual.id)) lidas.delete(atual.id); else lidas.add(atual.id);
      pintar();
    } else if(k === 'c'){
      e.preventDefault();
      var b = atual.querySelector('.copiar');
      if(b) b.click();
    }
  });

  // marcador de página: guarda a última seção vista e oferece o retorno
  var ultima = ler('ultima','');
  var t = null;
  function anotar(){
    var alvo = null;
    for(var i=0;i<secs.length;i++){
      var r = secs[i].getBoundingClientRect();
      if(r.top <= 120) alvo = secs[i]; else break;
    }
    if(alvo && alvo.id !== ultima){ ultima = alvo.id; salvar('ultima', ultima); }
  }
  window.addEventListener('scroll', function(){
    if(t) return;
    t = setTimeout(function(){ t = null; anotar(); }, 400);
  }, {passive:true});

  if(ultima && !location.hash){
    var d = document.getElementById(ultima);
    if(d){
      var rot = d.getAttribute('data-num') + ' ' + d.getAttribute('data-tit');
      var a = document.createElement('a');
      a.className = 'chip voltar';
      a.href = '#' + ultima;
      a.textContent = '↩ Retomar em ' + rot;
      var st = document.querySelector('.status');
      if(st) st.insertBefore(a, st.firstChild);
    }
  }
})();
</script>
"""
def validar_js(html):
    """Um \\n mal escapado já quebrou os três scripts de uma vez, em silêncio.
    Verifica a sintaxe com node quando ele estiver disponível."""
    import re, shutil, subprocess, tempfile, os
    if not shutil.which('node'): return html
    for i, b in enumerate(re.findall(r'<script>(.*?)</script>', html, re.S)):
        f = os.path.join(tempfile.gettempdir(), '_cv%d.js' % i)
        open(f, 'w').write(b)
        r = subprocess.run(['node', '--check', f], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit('JavaScript inválido no bloco %d:\\n%s' % (i, r.stderr[:400]))
    return html

HTML += SPY + CTRL + PROG
HTML = validar_js(HTML)
open('_head.html','w').write(HEAD)
open('curriculo-vivo.html','w').write(HTML)
print(len(HTML))

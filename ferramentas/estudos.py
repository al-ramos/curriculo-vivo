import markdown, re

HEAD = open('_head.html').read().replace('<title>Currículo Vivo</title>',
    '<title>Plano Mestre de Estudos</title>')

EXTRA = """<style>
.plano h3{font-size:.72rem}
.trilha{margin-top:3.4rem;padding-top:1.6rem;border-top:1px solid var(--rule)}
.trilha:first-of-type{border-top:0}
.tnum{font-family:"IBM Plex Mono",monospace;font-size:.7rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--accent);display:block;margin-bottom:.25rem}
article ul{margin:0 0 1.2rem;padding-left:1.15rem}
article li{margin-bottom:.5rem}
article ol{margin:0 0 1.2rem;padding-left:1.35rem}
article blockquote{margin:1.4rem 0;padding-left:1rem;border-left:2px solid var(--accent);
  color:var(--muted);font-style:italic}
.tabelinha{overflow-x:auto;margin:0 0 1.6rem}
article table{width:100%;border-collapse:collapse;font-size:.9rem}
article th{text-align:left;font-family:"IBM Plex Mono",monospace;font-size:.62rem;
  letter-spacing:.1em;text-transform:uppercase;color:var(--faint);font-weight:400;
  padding:.5rem .7rem .5rem 0;border-bottom:1px solid var(--rule)}
article td{padding:.5rem .7rem .5rem 0;border-bottom:1px solid var(--rule-soft);
  vertical-align:top}
article td:first-child{font-family:"IBM Plex Mono",monospace;font-size:.8rem;color:var(--accent);white-space:nowrap}
</style>"""

md = open('plano-estudos.md').read()
md = md.split('---', 1)[1].strip()
body = markdown.markdown(md, extensions=['tables','smarty'])

# h2 -> trilha ; h3 -> subtítulo
def h2(m):
    t = m.group(1)
    mm = re.match(r'(Trilha \d+)\s*·\s*(.+)', t)
    idd = re.sub(r'[^a-z0-9]+','-', t.lower()).strip('-')[:40]
    if mm:
        return (f'<section class="trilha"><h3 id="{idd}"><span class="tnum">{mm.group(1)}</span>'
                f'<span class="ttl">{mm.group(2)}</span></h3>')
    return f'<section class="trilha"><h3 id="{idd}"><span class="ttl">{t}</span></h3>'
body = re.sub(r'<h2>(.*?)</h2>', h2, body)
body = re.sub(r'<h3>(.*?)</h3>', r'<h4>\1</h4>', body)
body = body.replace('<hr />','</section>') + '</section>'
body = body.replace('<table>','<div class="tabelinha"><table>').replace('</table>','</table></div>')

RAIL = """<nav class="rail" aria-label="Sumário">
<div class="grp"><span>Antes de começar</span>
<a href="#antes-do-mapa-onde-voc-come-a">Onde você começa</a>
<a href="#como-o-plano-organizado">Como o plano é organizado</a></div>
<div class="grp"><span>Trilhas</span>
<a href="#trilha-0-diagn-stico">0 · Diagnóstico</a>
<a href="#trilha-1-a-funda-o-que-falta">1 · A fundação que falta</a>
<a href="#trilha-2-dados-e-sistemas-distribu-dos">2 · Dados e distribuídos</a>
<a href="#trilha-3-projeto-e-arquitetura">3 · Projeto e arquitetura</a>
<a href="#trilha-4-qualidade-testes-e-refatora-o">4 · Qualidade e testes</a>
<a href="#trilha-5-plataforma-confiabilidade-e-seg">5 · Plataforma e segurança</a>
<a href="#trilha-6-escrita-influ-ncia-e-carreira">6 · Escrita e carreira</a></div>
<div class="grp"><span>Referência</span>
<a href="#os-dez-atemporais">Os dez atemporais</a>
<a href="#seis-regras-que-decidem-se-o-plano-funci">Seis regras</a>
<a href="#o-que-ficou-deliberadamente-de-fora">O que ficou de fora</a>
<a href="#correspond-ncia-com-o-livro">Correspondência com o livro</a></div>
</nav>"""

TRILHAS = [("1","A fundação que falta","5–6 meses","var(--s1)",6),
           ("2","Dados e distribuídos","6 meses","var(--s2)",6),
           ("3","Projeto e arquitetura","6 meses","var(--s2)",6),
           ("4","Qualidade e testes","4 meses","var(--s3)",4),
           ("5","Plataforma e segurança","3–4 meses","var(--s3)",4),
           ("6","Escrita e carreira","contínua","var(--s4)",3)]
bands = ""
for n,nome,dur,cor,meses in TRILHAS:
    bands += (f'<div class="band"><div class="lab">{nome}<em>trilha {n}</em></div>'
              f'<div class="bar" style="background:{cor};height:{1.4+meses*0.42}rem"></div>'
              f'<div class="hv">{dur}</div></div>')

HTML = HEAD + EXTRA + f"""
<header class="masthead">
  <div class="mast-in">
    <div>
      <div class="eyebrow"><a href="index.html">&larr; Portal</a> &nbsp;·&nbsp; <a href="livro.html">O livro</a></div>
      <h1 class="book">Plano mestre<br><em>de estudos</em></h1>
      <p class="dek">Um currículo autodirigido de Engenharia de Software, calibrado para
      quem já tem estrada: seis trilhas, um livro-espinha por trilha, um projeto obrigatório
      e um marco que se pode provar falso.</p>
      <div class="status">
        <span class="chip on">6 trilhas</span>
        <span class="chip">~2,5 a 3 anos</span>
        <span class="chip">6–8 h / semana</span>
        <span class="chip">40+ livros</span>
      </div>
    </div>
    <div class="strata">
      <h2>Arco do plano</h2>
      {bands}
      <p class="note">A espessura é a duração. As trilhas 1, 2 e 6 são as lacunas reais do
      perfil; a 5 é curta porque <b>a experiência já cobre a maior parte dela.</b></p>
    </div>
  </div>
</header>

<div class="wrap">
 <div class="layout">
  {RAIL}
  <article class="plano">
   <details class="toc"><summary>Sumário</summary>
     <a href="#antes-do-mapa-onde-voc-come-a">Onde você começa</a>
     <a href="#trilha-0-diagn-stico">Trilha 0 · Diagnóstico</a>
     <a href="#trilha-1-a-funda-o-que-falta">Trilha 1 · A fundação que falta</a>
     <a href="#trilha-2-dados-e-sistemas-distribu-dos">Trilha 2 · Dados e distribuídos</a>
     <a href="#trilha-3-projeto-e-arquitetura">Trilha 3 · Projeto e arquitetura</a>
     <a href="#trilha-4-qualidade-testes-e-refatora-o">Trilha 4 · Qualidade e testes</a>
     <a href="#trilha-5-plataforma-confiabilidade-e-seg">Trilha 5 · Plataforma e segurança</a>
     <a href="#trilha-6-escrita-influ-ncia-e-carreira">Trilha 6 · Escrita e carreira</a>
     <a href="#os-dez-atemporais">Os dez atemporais</a>
   </details>
   {body}
  </article>
 </div>
</div>

<footer>
  <p><strong>Como este plano foi calibrado.</strong> Ele parte de um perfil concreto —
  mais de uma década em missão crítica no mercado financeiro, sustentação de legado,
  infraestrutura e entrega contínua — e por isso omite fundamentos que a experiência já
  cobriu. Um leitor com outro ponto de partida deve refazer a trilha 0 antes de seguir a
  ordem proposta.</p>
  <p>Companheiro de <a href="livro.html">Engenharia de Software: Envelhecimento Macro</a>.
  O livro descreve o território; este plano descreve o percurso.</p>
</footer>
"""

SPY = open('_spy.html').read() if False else ""
open('estudos.html','w').write(HTML)
print(len(HTML))

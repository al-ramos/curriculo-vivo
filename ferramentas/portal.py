import markdown, re

HEAD = open('_head.html').read().replace('<title>Currículo Vivo</title>',
    '<title>Currículo Vivo</title>')

EXTRA = """<style>
.portas{display:grid;grid-template-columns:1fr;gap:1px;background:var(--rule);
  border:1px solid var(--rule);border-radius:2px;overflow:hidden;margin:0 0 3rem}
@media(min-width:44rem){.portas{grid-template-columns:1fr 1fr}}
.porta{background:var(--surface);padding:1.5rem 1.4rem;text-decoration:none;display:block;color:inherit}
.porta:hover{background:var(--accent-soft)}
.porta .k{font-family:"IBM Plex Mono",monospace;font-size:.62rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent);display:block;margin-bottom:.6rem}
.porta h3{font-family:"Newsreader",serif;font-size:1.4rem;font-weight:500;margin:0 0 .5rem}
.porta p{margin:0;font-size:.92rem;color:var(--muted);line-height:1.5}
.porta .st{display:block;margin-top:.9rem;font-family:"IBM Plex Mono",monospace;
  font-size:.64rem;color:var(--faint);letter-spacing:.04em}
.fase{position:relative;padding-left:2.2rem;padding-bottom:2.4rem}
.fase::before{content:"";position:absolute;left:.42rem;top:1.5rem;bottom:0;width:1px;background:var(--rule)}
.fase:last-of-type::before{display:none}
.fase::after{content:"";position:absolute;left:0;top:.75rem;width:.9rem;height:.9rem;
  border-radius:50%;border:2px solid var(--accent);background:var(--ground)}
.fase.feita::after{background:var(--accent)}
.fase>h3{display:flex;flex-wrap:wrap;align-items:baseline;gap:.6rem;margin:0 0 .2rem;
  font-family:"Newsreader",serif;font-size:1.3rem;font-weight:500}
.fase>h3 .quando{font-family:"IBM Plex Mono",monospace;font-size:.66rem;color:var(--faint);
  letter-spacing:.06em;text-transform:uppercase}
article table{width:100%;border-collapse:collapse;font-size:.88rem}
article th{text-align:left;font-family:"IBM Plex Mono",monospace;font-size:.6rem;
  letter-spacing:.1em;text-transform:uppercase;color:var(--faint);font-weight:400;
  padding:.45rem .7rem .45rem 0;border-bottom:1px solid var(--rule)}
article td{padding:.5rem .7rem .5rem 0;border-bottom:1px solid var(--rule-soft);vertical-align:top}
.tabelinha{overflow-x:auto;margin:.6rem 0 1.3rem}
article ul{margin:0 0 1.2rem;padding-left:1.15rem}
article li{margin-bottom:.5rem}
article blockquote{margin:1.5rem 0;padding:.2rem 0 .2rem 1.1rem;border-left:2px solid var(--accent);
  color:var(--ink);font-style:italic;font-size:1.02rem}
</style>"""

def fechar_secoes(html):
    """Fecha cada <section> imediatamente antes da próxima abrir, e no fim.
    Substitui o fechamento por <hr />, que quebrava quando as contagens
    divergiam e derrubava o layout silenciosamente."""
    html = html.replace('<hr />', '')
    pedacos = html.split('<section class=')
    fora = pedacos[0]
    corpo = ''
    for i, p in enumerate(pedacos[1:]):
        if i: corpo += '</section>'
        corpo += '<section class=' + p
    if corpo: corpo += '</section>'
    return fora + corpo

def validar(html):
    from html.parser import HTMLParser
    class V(HTMLParser):
        VAZIAS = {'br','img','hr','input','meta','link'}
        def __init__(self):
            super().__init__(); self.pilha=[]; self.erros=[]
        def handle_starttag(self, t, a):
            if t not in self.VAZIAS: self.pilha.append(t)
        def handle_endtag(self, t):
            if not self.pilha: self.erros.append('fecha sem abrir </%s>' % t); return
            if self.pilha[-1] != t: self.erros.append('esperava </%s>, veio </%s>' % (self.pilha[-1], t))
            else: self.pilha.pop()
    v = V(); v.feed(html)
    if v.erros or v.pilha:
        raise SystemExit('HTML mal aninhado: %s | abertas: %s' % (v.erros[:3], v.pilha[:3]))
    return html

md = open('linha-do-tempo.md').read()
md = md.split('\n', 1)[1]
body = markdown.markdown(md, extensions=['tables','smarty'])

FEITAS = {"Fase 0"}
def h2(m):
    t = m.group(1)
    idd = re.sub(r'[^a-z0-9]+','-', t.lower()).strip('-')
    mm = re.match(r'(Fase \d+)\s*·\s*(.+)', t)
    cls = "fase feita" if (mm and mm.group(1) in FEITAS) else ("fase" if mm else "bloco")
    nome = mm.group(2) if mm else t
    pref = f'<span class="quando">{mm.group(1)}</span>' if mm else ''
    return f'<section class="{cls}"><h3 id="{idd}">{pref}<span>{nome}</span></h3>'
body = re.sub(r'<h2>(.*?)</h2>', h2, body)
body = validar(fechar_secoes(body))
body = body.replace('<table>','<div class="tabelinha"><table>').replace('</table>','</table></div>')
# a linha "Duas semanas · agora" vira etiqueta
body = re.sub(r'<p><strong>(Meses [^<]*|Duas semanas[^<]*)</strong></p>',
              r'<p class="quandoP"><em>\1</em></p>', body)

PORTAS = """
<div class="portas">
  <a class="porta" href="livro.html">
    <span class="k">O território</span>
    <h3>Engenharia de Software: Envelhecimento Macro</h3>
    <p>O livro. Vinte e dois capítulos organizados por velocidade de envelhecimento, cada
    seção com meia-vida, estado e data de revisão declarados.</p>
    <span class="st">Camada 0, 1.1 a 1.4, 2.1 a 2.6, 3.1 e 3.2 · 13 de 22 capítulos</span>
  </a>
  <a class="porta" href="estudos.html">
    <span class="k">O percurso</span>
    <h3>Plano mestre de estudos</h3>
    <p>O currículo autodirigido. Seis trilhas, um livro-espinha por trilha, projeto
    obrigatório e um marco que se pode provar falso.</p>
    <span class="st">6 trilhas · 40+ livros · 6–8 h por semana</span>
  </a>
</div>
"""

HTML = HEAD + EXTRA + f"""
<header class="masthead">
  <div class="mast-in">
    <div>
      <div class="eyebrow">Currículo vivo · o portal</div>
      <h1 class="book">Uma formação<br><em>com data de validade</em></h1>
      <p class="dek">Um livro sobre como o conhecimento de Engenharia de Software envelhece,
      um plano de estudos calibrado para quem já tem estrada, e uma linha do tempo que
      costura os dois: cada capítulo é escrito depois da trilha que o sustenta.</p>
      <div class="status">
        <span class="chip on">39 meses</span>
        <span class="chip">8 fases</span>
        <span class="chip">22 capítulos</span>
        <span class="chip">6 trilhas</span>
        <span class="chip data" id="chip-data">—</span>
      </div>
    </div>
    <div class="strata">
      <h2>Onde o plano está</h2>
      <div class="band"><div class="lab">Escrito<em>capítulos</em></div>
        <div class="bar" style="background:var(--s1);height:3.6rem"></div><div class="hv">13 de 22</div></div>
      <div class="band"><div class="lab">Com ficha<em>capítulos</em></div>
        <div class="bar" style="background:var(--s2);height:1.6rem"></div><div class="hv">22 de 22</div></div>
      <div class="band"><div class="lab">Trilhas<em>concluídas</em></div>
        <div class="bar" style="background:var(--s4);height:1.5rem"></div><div class="hv">0 de 6</div></div>
      <p class="note">O portal está na <b>Fase 0</b>. A próxima entrega é o diagnóstico de
      duas semanas e as fichas dos 22 capítulos.</p>
    </div>
  </div>
</header>

<div class="wrap">
 <div class="layout">
  <nav class="rail" aria-label="Sumário">
    <div class="grp"><span>O portal</span>
      <a href="livro.html">O livro</a>
      <a href="estudos.html">Plano de estudos</a></div>
    <div class="grp"><span>Linha do tempo</span>
      <a href="#a-regra-que-costura-tudo">A regra que costura tudo</a>
      <a href="#fase-0-funda-o">0 · Fundação</a>
      <a href="#fase-1-a-funda-o-que-falta">1 · A fundação que falta</a>
      <a href="#fase-2-dados-e-sistemas-distribu-dos">2 · Dados e distribuídos</a>
      <a href="#fase-3-projeto-e-arquitetura">3 · Projeto e arquitetura</a>
      <a href="#fase-4-qualidade-e-testes">4 · Qualidade e testes</a>
      <a href="#fase-5-plataforma-confiabilidade-e-seguran-a">5 · Plataforma e segurança</a>
      <a href="#fase-6-os-cap-tulos-sem-trilha">6 · Capítulos sem trilha</a>
      <a href="#fase-7-a-camada-contextual">7 · A camada contextual</a>
      <a href="#fase-8-o-cap-tulo-perec-vel-e-o-fechamento">8 · Fechamento</a>
      <a href="#conceito-e-pr-tica-lado-a-lado">Conceito e prática</a>
      <a href="#o-quadro-completo">O quadro completo</a>
      <a href="#o-que-fazer-se-atrasar">Se atrasar</a></div>
  </nav>
  <article>
   {PORTAS}
   {body}
  </article>
 </div>
</div>

<section class="bloco" id="publicacoes">
  <h3 id="publicacoes-t"><span>Publicações</span></h3>
  <p>Cada mudança no portal é um commit datado. Esta lista vem do histórico do repositório,
  ao vivo — se ela estiver desatualizada, o portal também está.</p>
  <div class="pubs" id="lista-pubs"><span class="aviso">Carregando o histórico…</span></div>
</section>

<footer>
  <p><strong>Como ler este portal.</strong> O livro descreve o território; o plano de
  estudos descreve o percurso; esta página diz em que ordem as duas coisas acontecem. A
  regra que as une é simples: nenhum capítulo é escrito antes da trilha que o sustenta.</p>
  <p>Conteúdo sob CC BY-SA 4.0, código sob MIT.
  Fonte em <a href="https://github.com/al-ramos/curriculo-vivo">github.com/al-ramos/curriculo-vivo</a>.</p>
</footer>
"""
open('portal.html','w').write(HTML)
print(len(HTML))

import markdown, re, json, html

md = open('livro/camadas-0-1.md').read()
md = md.split('---',1)[1].strip()   # drop the two title lines
md = md.replace('## 0.', '### 0.')
md = md.replace('*Sem meia-vida: é o instrumento de leitura das camadas 1 a 4*',
                '*Sem meia-vida: é o instrumento de leitura das camadas 1 a 4*\n\n## 0 · Como ler este livro')
md = md.replace('## Fontes desta camada', '## Fontes · referências primárias')
body = markdown.markdown(md, extensions=['tables','smarty'])

# fichas: chapter number -> (meia-vida, estado, etiquetas, slug)
fichas = {
 '0':   ('sem meia-vida','instrumento','meta','/como-ler'),
 '1.1': ('sem erosão observada','permanente','técnico · teórico','/fundacao'),
 '1.2': ('sem erosão observada','permanente','técnico · teórico','/invariantes'),
 '1.3': ('sem erosão observada','permanente','teórico · meta','/perenidade'),
}
def ficha(num):
    if num not in fichas: return ''
    mv, est, tags, slug = fichas[num]
    return (f'<dl class="ficha"><div><dt>meia-vida</dt><dd>{mv}</dd></div>'
            f'<div><dt>estado</dt><dd>{est}</dd></div>'
            f'<div><dt>etiquetas</dt><dd>{tags}</dd></div>'
            f'<div><dt>slug</dt><dd><code>{slug}</code></dd></div></dl>')

# h1 -> camada banner ; h2 -> chapter with ficha ; h3 -> section with margin number
def h1(m):
    t = m.group(1)
    n = t.split('—')[0].replace('CAMADA','').strip()
    name = t.split('—')[1].strip().title() if '—' in t else ''
    return f'<h2 class="camada" id="camada-{n}"><span class="cnum">Camada {n}</span><span class="cname">{name}</span></h2>'
body = re.sub(r'<h1>(.*?)</h1>', h1, body)

def h2(m):
    t = m.group(1)
    num = t.split('·')[0].strip() if '·' in t else t.split(' ')[0]
    title = t.split('·',1)[1].strip() if '·' in t else t
    idd = 'c'+num.replace('.','-')
    return (f'<section class="chapter"><h3 id="{idd}"><span class="num">{num}</span>'
            f'<span class="ttl">{title}</span></h3>{ficha(num)}')
body = re.sub(r'<h2>(.*?)</h2>', h2, body)

def h3(m):
    t = m.group(1); parts = t.split(' ',1)
    num = parts[0]; tit = parts[1] if len(parts)>1 else ''
    idd = 's' + num.replace('.','-')
    return (f'@@SEC@@<details class="sec" open id="{idd}" data-num="{num}" data-tit="{tit}">'
            f'<summary><h4><span class="snum">{num}</span> {tit}</h4></summary><div class="sec-corpo">')
body = re.sub(r'<h3>(.*?)</h3>', h3, body)

# fechar cada details antes do próximo marcador de seção/capítulo/camada e no fim
partes = body.split('@@SEC@@')
saida = [partes[0]]
for p in partes[1:]:
    corte = len(p)
    for marca in ('<section class="chapter">', '<h2 class="camada"', '</section>'):
        k = p.find(marca)
        if k != -1: corte = min(corte, k)
    saida.append(p[:corte] + '</div></details>' + p[corte:])
body = ''.join(saida)

body = body.replace('<hr />','</section>')
body += '</section>'
open('_body.html','w').write(body)
print(body[:400])

# Genera las pantallas de Liquidaciones (CRM-MotoT) en formato .dc.html
import json, os, sys, datetime

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

# ---------- Iconos Lucide (línea, 24 px) ----------
I = {
 'receipt': '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"></path><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"></path><path d="M12 17.5v-11"></path>',
 'bike': '<circle cx="18.5" cy="17.5" r="3.5"></circle><circle cx="5.5" cy="17.5" r="3.5"></circle><circle cx="15" cy="5" r="1"></circle><path d="M12 17.5V14l-3-3 4-3 2 3h2"></path>',
 'user': '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>',
 'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
 'search': '<circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.3-4.3"></path>',
 'plus': '<path d="M5 12h14"></path><path d="M12 5v14"></path>',
 'pencil': '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"></path><path d="m15 5 4 4"></path>',
 'arrow-left': '<path d="m12 19-7-7 7-7"></path><path d="M19 12H5"></path>',
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
 'log-out': '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><path d="m16 17 5-5-5-5"></path><path d="M21 12H9"></path>',
 'x': '<path d="M18 6 6 18"></path><path d="m6 6 12 12"></path>',
 'chev-r': '<path d="m9 18 6-6-6-6"></path>',
 'chev-l': '<path d="m15 18-6-6 6-6"></path>',
 'chev-d': '<path d="m6 9 6 6 6-6"></path>',
 'calendar': '<path d="M8 2v4"></path><path d="M16 2v4"></path><rect width="18" height="18" x="3" y="4" rx="2"></rect><path d="M3 10h18"></path>',
 'check-circle': '<circle cx="12" cy="12" r="10"></circle><path d="m9 12 2 2 4-4"></path>',
 'alert': '<circle cx="12" cy="12" r="10"></circle><line x1="12" x2="12" y1="8" y2="12"></line><line x1="12" x2="12.01" y1="16" y2="16"></line>',
 'check': '<path d="M20 6 9 17l-5-5"></path>',
 'delete': '<path d="M10 5a2 2 0 0 0-1.344.519l-6.328 5.74a1 1 0 0 0 0 1.481l6.328 5.741A2 2 0 0 0 10 19h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2z"></path><path d="m12 9 6 6"></path><path d="m18 9-6 6"></path>',
}

def ic(name, cls='', style=''):
    c = 'ic' + (' ' + cls if cls else '')
    st = f' style="{style}"' if style else ''
    return f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true"{st}>{I[name]}</svg>'

# ---------- Estilos (solo tokens del design system) ----------
CSS = r"""
body{margin:0}
.app,.app *{box-sizing:border-box}
.app{font-family:'Inter',system-ui,-apple-system,sans-serif;color:#1A202C;background:#F7F8FA;font-size:16px;line-height:24px;-webkit-font-smoothing:antialiased;position:relative;overflow:hidden}
.app h1,.app h2,.app h3,.app p,.app dl,.app dd{margin:0}
.app ul{margin:0;padding:0;list-style:none}
.app input::placeholder{color:#5A6475;opacity:1}
.app a{color:#C25A12}
.app a:hover{color:#A84B0C}
.ic{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0}
.ic-s{width:20px;height:20px}
.ic-xs{width:16px;height:16px}
.num{font-variant-numeric:tabular-nums}
.placa{text-transform:uppercase;font-weight:600;letter-spacing:.5px;white-space:nowrap}
.t-scr{font-size:24px;line-height:32px;font-weight:600}
.t-scr-pc{font-size:28px;line-height:36px;font-weight:600}
.t-sub{font-size:18px;line-height:26px;font-weight:600}
.t-sec{font-size:14px;line-height:20px;color:#5A6475}
.t-lab{font-size:12px;line-height:16px;font-weight:500}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.card{background:#FFFFFF;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 1px 2px rgba(0,0,0,.06)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:10px 16px;border-radius:8px;border:1px solid transparent;font-family:inherit;font-size:16px;line-height:24px;font-weight:600;text-decoration:none;cursor:pointer;white-space:nowrap}
.app .btn-pri{background:#C25A12;color:#FFFFFF}
.app .btn-pri:hover{background:#A84B0C;color:#FFFFFF}
.app .btn-sec{background:#FFFFFF;color:#C25A12;border-color:#E2E8F0}
.app .btn-sec:hover{background:#FDF3EA;color:#C25A12}
.app .btn-ico{width:44px;padding:0;background:transparent;color:#1A202C}
.app .btn-ico:hover{background:#F7F8FA;color:#1A202C}
.btn-lg{min-height:48px}
.tag{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px;border-radius:999px;font-size:12px;line-height:16px;font-weight:500;white-space:nowrap}
.tag-ayu{color:#5A6475;background:#EEF0F3}
.tag-aviso{color:#B26A00;background:#FFF4E5}
.tag-nueva{color:#C25A12;background:#FDF3EA}
.dot{width:8px;height:8px;border-radius:999px;background:#F26B1D;flex-shrink:0}
/* buscador */
.search{position:relative}
.search > .ic{position:absolute;left:12px;top:14px;color:#5A6475;pointer-events:none}
.search input{width:100%;height:48px;padding:0 48px 0 44px;border:1px solid #E2E8F0;border-radius:8px;background:#FFFFFF;font-family:inherit;font-size:16px;line-height:24px;color:#1A202C;-webkit-appearance:none;appearance:none}
.search input:focus,.search input.foco{outline:none;border-color:#C25A12;box-shadow:0 0 0 3px #FDF3EA}
.search input::-webkit-search-cancel-button{display:none}
.search .clr{position:absolute;right:2px;top:2px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:8px;color:#5A6475;text-decoration:none}
.app .search .clr:hover{background:#F7F8FA;color:#1A202C}
/* celular */
.top{height:56px;flex-shrink:0;display:flex;align-items:center;justify-content:space-between;gap:8px;padding:0 16px;background:#FFFFFF;border-bottom:1px solid #E2E8F0}
.top-f{padding:0 16px 0 4px;justify-content:flex-start}
.app .back{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 12px 0 8px;margin-left:-8px;border-radius:8px;color:#C25A12;font-weight:600;text-decoration:none}
.day{font-size:14px;line-height:20px;font-weight:600;color:#5A6475}
.app .lcard{display:flex;align-items:center;gap:12px;min-height:72px;padding:12px 12px 12px 16px;color:#1A202C;text-decoration:none}
.app .lcard:hover{border-color:#C25A12;color:#1A202C}
.lc-body{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.monto{font-weight:600;font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap}
.chev{color:#5A6475}
.app .fab{position:absolute;right:16px;bottom:88px;height:56px;padding:0 24px 0 20px;border-radius:999px;display:flex;align-items:center;gap:8px;background:#C25A12;color:#FFFFFF;font-size:16px;line-height:24px;font-weight:600;text-decoration:none;box-shadow:0 4px 12px rgba(194,90,18,.32)}
.app .fab:hover{background:#A84B0C;color:#FFFFFF}
.bnav{height:72px;flex-shrink:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));padding:0 4px;background:#FFFFFF;border-top:1px solid #E2E8F0}
.app .bnav a{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;margin:8px 2px;border-radius:8px;color:#5A6475;font-size:12px;line-height:16px;font-weight:500;text-decoration:none}
.app .bnav a.on{color:#C25A12;background:#FDF3EA;font-weight:600}
.app .bnav a.on::before{content:"";position:absolute;top:-9px;left:50%;margin-left:-16px;width:32px;height:3px;border-radius:0 0 3px 3px;background:#F26B1D}
.toast{position:absolute;display:flex;align-items:center;gap:12px;padding:8px 4px 8px 16px;border-radius:12px;background:#E6F4EA;border:1px solid #CDE9D6;box-shadow:0 4px 12px rgba(0,0,0,.12);color:#1A202C;font-weight:600}
.toast > .ic{color:#1E8E3E}
.nuevo{background:#FDF3EA}
/* formularios */
.app .lbl{display:block;margin:0 0 8px;font-size:14px;line-height:20px;font-weight:500;color:#1A202C}
.inp{display:flex;align-items:center;gap:8px;width:100%;height:48px;margin:0;padding:0 12px;border:1px solid #E2E8F0;border-radius:8px;background:#FFFFFF;color:#1A202C;font-family:inherit;font-size:16px;line-height:24px;text-align:left;text-decoration:none;cursor:pointer}
.app a.inp{color:#1A202C}
.app a.inp:hover{border-color:#C25A12;color:#1A202C}
.inp .val{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.inp > .ic{color:#5A6475}
input.inp{cursor:text}
.inp:focus{outline:none;border-color:#C25A12;box-shadow:0 0 0 3px #FDF3EA}
.inp.foco{border-color:#C25A12;box-shadow:0 0 0 3px #FDF3EA}
.inp.err{border-color:#C5221F;box-shadow:0 0 0 1px #C5221F}
.inp.off{background:#F7F8FA;cursor:default}
.ph{color:#5A6475}
.money{position:relative}
.money .pre{position:absolute;left:12px;top:12px;font-weight:600;pointer-events:none}
.money .inp{padding-left:28px;font-variant-numeric:tabular-nums}
.app .hint{margin:8px 0 0;font-size:14px;line-height:20px;color:#5A6475}
.app .msg-err{display:flex;align-items:center;gap:6px;margin:8px 0 0;font-size:14px;line-height:20px;font-weight:500;color:#C5221F}
.caret{display:inline-block;width:2px;height:22px;margin-left:1px;background:#C25A12;vertical-align:-5px}
.scrim{position:absolute;inset:0;background:rgba(26,32,44,.48)}
.sheet{position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-radius:12px 12px 0 0;box-shadow:0 -4px 16px rgba(0,0,0,.12)}
.grab{display:flex;justify-content:center;padding-top:8px}
.grab span{width:40px;height:4px;border-radius:999px;background:#E2E8F0}
.app .opt{display:flex;align-items:center;gap:12px;min-height:64px;padding:8px 16px;border-bottom:1px solid #E2E8F0;color:#1A202C;text-decoration:none}
.app .opt:hover{background:#F7F8FA;color:#1A202C}
.app .opt.sel{background:#FDF3EA}
.avatar{width:40px;height:40px;border-radius:999px;display:flex;align-items:center;justify-content:center;background:#FDF3EA;color:#C25A12;flex-shrink:0}
/* calendario */
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:4px;text-align:center}
.cal .wd{height:32px;display:flex;align-items:center;justify-content:center;font-size:12px;line-height:16px;font-weight:500;color:#5A6475}
.app .cal a,.cal span.d{height:44px;display:flex;align-items:center;justify-content:center;border-radius:8px;color:#1A202C;text-decoration:none;font-variant-numeric:tabular-nums}
.app .cal a:hover{background:#FDF3EA;color:#1A202C}
.app .cal a.sel{background:#C25A12;color:#FFFFFF;font-weight:600}
.cal span.fut{color:#5A6475;opacity:.6}
/* teclado numérico */
.kbd{position:absolute;left:0;right:0;bottom:0;padding:8px 8px 24px;background:#EEF0F3;border-top:1px solid #E2E8F0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.kbd span{height:48px;display:flex;align-items:center;justify-content:center;border-radius:8px;background:#FFFFFF;box-shadow:0 1px 2px rgba(0,0,0,.06);font-size:22px;line-height:28px;font-weight:500}
.kbd span.fn{background:transparent;box-shadow:none}
/* computadora */
.side{width:240px;flex-shrink:0;display:flex;flex-direction:column;padding:24px 16px;background:#FFFFFF;border-right:1px solid #E2E8F0}
.logo{display:flex;align-items:center;gap:8px;padding:0 12px;min-height:44px;font-size:18px;line-height:26px;font-weight:600}
.app .nav-t{padding:0 12px;margin:24px 0 8px;font-size:12px;line-height:16px;font-weight:500;color:#5A6475}
.app .nav-i{position:relative;display:flex;align-items:center;gap:12px;min-height:44px;padding:0 12px;border-radius:8px;color:#1A202C;font-size:16px;line-height:24px;font-weight:500;text-decoration:none}
.app .nav-i:hover{background:#F7F8FA;color:#1A202C}
.nav-i .ic{color:#5A6475}
.app .nav-i.on{background:#FDF3EA;color:#C25A12;font-weight:600}
.nav-i.on .ic{color:#C25A12}
.nav-i.on::before{content:"";position:absolute;left:0;top:10px;bottom:10px;width:3px;border-radius:0 3px 3px 0;background:#F26B1D}
.tbl{overflow:hidden}
.trow{display:grid;grid-template-columns:160px 240px minmax(0,1fr) 160px 24px;gap:24px;align-items:center;min-height:56px;padding:0 24px;border-top:1px solid #E2E8F0;color:#1A202C;text-decoration:none}
.app a.trow{color:#1A202C}
.app a.trow:hover{background:#F7F8FA;color:#1A202C}
.thead{min-height:44px;border-top:0;font-size:12px;line-height:16px;font-weight:500;color:#5A6475}
.tgrp{padding:8px 24px;border-top:1px solid #E2E8F0;background:#F7F8FA;font-size:14px;line-height:20px;font-weight:600;color:#5A6475}
.panel{position:absolute;top:0;right:0;bottom:0;width:480px;background:#FFFFFF;box-shadow:-8px 0 24px rgba(0,0,0,.12);display:flex;flex-direction:column}
.pop{position:absolute;left:0;right:0;top:100%;margin-top:4px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.12);z-index:2;overflow:hidden}
.app .lk{display:flex;align-items:center;gap:16px;padding:16px;color:#1A202C;text-decoration:none}
.app a.lk:hover{border-color:#C25A12;color:#1A202C}
"""

HEAD = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>{css}</style>
</helmet>
'''
TAIL = '''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

BOARDS = {}
ORDER = []

def save(fname, title, body, w, h, inter=True):
    html = HEAD.format(title=title, css=CSS.strip()) + body + '\n' + TAIL.format(w=w, h=h)
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f:
        f.write(html)
    ORDER.append(fname)
    BOARDS[fname] = {'w': w, 'h': h, 'title': title}
    if inter:
        BOARDS[fname]['is_interactive'] = True

def A(href, cls, inner, live=True, extra=''):
    """Enlace real si la pantalla está activa; span si está detrás de un velo."""
    if live:
        return f'<a class="{cls}" href="{href}"{extra}>{inner}</a>'
    return f'<span class="{cls}">{inner}</span>'

# ---------- Datos de ejemplo ----------
LIQ = [
    ('hoy', '13 oct 2026', '27-ABC-4', 'Juan Pérez López', '$350.00'),
    ('hoy', '13 oct 2026', '31-XKT-8', 'María González Ruiz', '$350.00'),
    ('ayer', '12 oct 2026', '12-MNO-5', 'Luis Hernández Soto', '$300.00'),
    ('ayer', '12 oct 2026', '27-ABC-4', 'Juan Pérez López', '$350.00'),
]
GRUPOS = {'hoy': 'Hoy · 13 oct 2026', 'ayer': 'Ayer · 12 oct 2026'}
MOTOS = [('27-ABC-4', 'Italika FT150', 'Juan Pérez López'), ('31-XKT-8', 'Honda CGL 125', 'María González Ruiz'),
         ('12-MNO-5', 'Yamaha YBR 125', 'Luis Hernández Soto'), ('45-PQR-2', 'Italika DM150', None)]

# ---------- Celular ----------
def bnav(live=True):
    items = [('receipt', 'Liquidaciones', 'Main.dc.html', True), ('bike', 'Motos', '#', False),
             ('user', 'Choferes', '#', False), ('users', 'Administración', '#', False)]
    out = []
    for icn, lab, href, on in items:
        if live:
            cur = ' class="on" aria-current="page"' if on else ''
            out.append(f'<a href="{href}"{cur}>{ic(icn)}{lab}</a>')
        else:
            out.append(f'<span{" class=\"on\"" if on else ""} style="position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; margin: 8px 2px; border-radius: 8px; font-size: 12px; line-height: 16px; font-weight: {600 if on else 500}; color: {"#C25A12" if on else "#5A6475"}; background: {"#FDF3EA" if on else "transparent"}">{ic(icn)}{lab}</span>')
    attrs = ' aria-label="Menú principal"' if live else ' aria-hidden="true"'
    return f'<nav class="bnav"{attrs}>' + ''.join(out) + '</nav>'

def search_cel(value='', live=True, foco=False):
    clr = ''
    if value:
        clr = A('Main.dc.html', 'clr', ic('x', 'ic-s'), live, ' aria-label="Borrar búsqueda"')
    val = f' value="{value}"' if value else ''
    fc = ' class="foco"' if foco else ''
    return f'''<div class="search">
<label class="sr" for="q">Buscar liquidaciones</label>
{ic('search', 'ic-s')}
<input id="q" type="search"{fc} placeholder="Buscar por placa, chofer o fecha"{val} autocomplete="off">
{clr}
</div>'''

def lcard(l, live=True, nueva=False):
    _, fecha, placa, chofer, monto = l
    extra = ''
    if nueva:
        extra = '<span class="tag tag-nueva"><span class="dot"></span>Nueva</span>'
    cls = 'card lcard' + (' nuevo' if nueva else '')
    inner = (f'<span class="lc-body"><span style="display: flex; align-items: center; gap: 8px"><span class="placa">{placa}</span>{extra}</span>'
             f'<span class="t-sec">{chofer}</span></span><span class="monto">{monto}</span>{ic("chev-r", "chev ic-s")}')
    return A('DetalleCel.dc.html', cls, inner, live)

def lista_cel(rows, live=True, nueva_idx=None):
    out = []
    for g in ('hoy', 'ayer'):
        rs = [(i, r) for i, r in enumerate(rows) if r[0] == g]
        if not rs:
            continue
        out.append(f'<section aria-labelledby="d-{g}" style="display: flex; flex-direction: column; gap: 8px">')
        out.append(f'<h2 id="d-{g}" class="day num">{GRUPOS[g]}</h2>')
        for i, r in rs:
            out.append(lcard(r, live, nueva=(i == nueva_idx)))
        out.append('</section>')
    return '\n'.join(out)

def fab(live=True, bottom=88):
    st = f' style="bottom: {bottom}px"' if bottom != 88 else ''
    if live:
        return f'<a class="fab" href="RegistrarCel.dc.html"{st}>{ic("plus")}Registrar liquidación</a>'
    return f'<span class="fab" aria-hidden="true"{st}>{ic("plus")}Registrar liquidación</span>'

def cel_lista(fname, title, contenido, con_fab=True, overlay='', fab_bottom=88):
    body = f'''<div class="app" style="width: 390px; height: 844px; display: flex; flex-direction: column">
<header class="top">
<h1 class="t-scr">Liquidaciones</h1>
</header>
<main style="flex: 1; min-height: 0; overflow: hidden; padding: 16px 16px 160px; display: flex; flex-direction: column; gap: 24px">
{contenido}
</main>
{fab(True, fab_bottom) if con_fab else ''}
{overlay}
{bnav()}
</div>'''
    save(fname, title, body, 390, 844)

# ---------- Computadora ----------
def side(live=True):
    def item(icn, lab, on=False, href='#'):
        cls = 'nav-i on' if on else 'nav-i'
        cur = ' aria-current="page"' if (on and live) else ''
        return A(href, cls, ic(icn) + lab, live, cur)
    attrs = ' aria-label="Menú"' if live else ' aria-hidden="true"'
    return f'''<aside class="side">
<div class="logo">{ic('bike', style='color: #F26B1D')}CRM-MotoT</div>
<nav{attrs} style="display: flex; flex-direction: column; gap: 4px">
<p class="nav-t">Operación</p>
{item('receipt', 'Liquidaciones', True, 'HistorialPC.dc.html')}
{item('bike', 'Motos')}
{item('user', 'Choferes')}
<p class="nav-t">Administración</p>
{item('users', 'Usuarios')}
</nav>
<div style="margin-top: auto; padding-top: 16px; border-top: 1px solid #E2E8F0; display: flex; flex-direction: column; gap: 8px">
<div style="padding: 0 12px; display: flex; flex-direction: column; align-items: flex-start; gap: 4px">
<span style="font-weight: 600">Pedro Martínez</span>
<span class="tag tag-ayu">Ayudante</span>
</div>
{A('../login/Main.dc.html' if False else '#', 'nav-i', ic('log-out') + 'Cerrar sesión', live)}
</div>
</aside>'''

def search_pc(value='', live=True, href_clear='HistorialPC.dc.html'):
    clr = ''
    if value:
        clr = A(href_clear, 'clr', ic('x', 'ic-s'), live, ' aria-label="Borrar búsqueda"')
    val = f' value="{value}"' if value else ''
    return f'''<div class="search" style="width: 440px">
<label class="sr" for="q">Buscar liquidaciones</label>
{ic('search', 'ic-s')}
<input id="q" type="search" placeholder="Buscar por placa, chofer o fecha"{val} autocomplete="off"{'' if live else ' tabindex="-1"'}>
{clr}
</div>'''

def tabla(rows, live=True, nueva_idx=None):
    out = ['<div class="card tbl" role="table" aria-label="Liquidaciones">',
           '<div class="trow thead" role="row"><span role="columnheader">Fecha</span><span role="columnheader">Moto</span><span role="columnheader">Chofer</span><span role="columnheader" style="text-align: right">Monto</span><span></span></div>']
    for g in ('hoy', 'ayer'):
        rs = [(i, r) for i, r in enumerate(rows) if r[0] == g]
        if not rs:
            continue
        out.append(f'<p class="tgrp num" role="row"><span role="cell">{GRUPOS[g]}</span></p>')
        for i, r in rs:
            _, fecha, placa, chofer, monto = r
            nueva = i == nueva_idx
            tag = '<span class="tag tag-nueva"><span class="dot"></span>Nueva</span>' if nueva else ''
            inner = (f'<span class="num" role="cell">{fecha}</span>'
                     f'<span role="cell" style="display: flex; align-items: center; gap: 8px"><span class="placa">{placa}</span>{tag}</span>'
                     f'<span role="cell">{chofer}</span><span class="monto" role="cell">{monto}</span>{ic("chev-r", "chev ic-s")}')
            cls = 'trow' + (' nuevo' if nueva else '')
            out.append(A('DetallePC.dc.html', cls, inner, live, ' role="row"'))
    out.append('</div>')
    return '\n'.join(out)

def pc_head(live=True):
    btn = A('RegistrarPC.dc.html', 'btn btn-pri', ic('plus', 'ic-s') + 'Registrar liquidación', live)
    h = '<h1 class="t-scr-pc">Liquidaciones</h1>' if live else '<p class="t-scr-pc">Liquidaciones</p>'
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; gap: 24px">
{h}
{btn}
</div>'''

def pc_lista(fname, title, contenido, overlay='', live=True):
    main_attr = '' if live else ' aria-hidden="true"'
    body = f'''<div class="app" style="width: 1440px; height: 900px; display: flex">
{side(live)}
<main{main_attr} style="flex: 1; min-width: 0; padding: 32px; display: flex; flex-direction: column; gap: 24px">
{pc_head(live)}
{contenido}
</main>
{overlay}
</div>'''
    save(fname, title, body, 1440, 900)

# ---------- Formulario ----------
def campo_moto(estado, live=True, pc=False):
    """estado: 'lleno' | 'vacio' | 'err' | 'abierto'"""
    target = 'ElegirMotoPC.dc.html' if pc else 'ElegirMotoCel.dc.html'
    if estado in ('lleno',):
        val = '<span class="val"><span class="placa">27-ABC-4</span><span class="ph"> · Italika FT150</span></span>'
    else:
        val = '<span class="val ph">Elige la moto</span>'
    cls = 'inp' + (' err' if estado == 'err' else '') + (' foco' if estado == 'abierto' else '')
    extra = ' id="moto" aria-labelledby="l-moto moto"' + (' aria-describedby="e-moto"' if estado == 'err' else '')
    fld = A(target, cls, val + ic('chev-d', 'ic-s'), live, extra)
    err = f'<p class="msg-err" id="e-moto">{ic("alert", "ic-xs")}Elige la moto</p>' if estado == 'err' else ''
    return f'<p class="lbl" id="l-moto">Moto</p>\n{fld}\n{err}'

def campo_chofer(lleno=True, live=True):
    if lleno:
        b = f'<button class="inp" id="chofer" type="button" aria-haspopup="listbox" aria-describedby="h-chofer"{"" if live else " tabindex=\"-1\""}><span class="val">Juan Pérez López</span>{ic("chev-d", "ic-s")}</button>'
        h = '<p class="hint" id="h-chofer">Es el chofer de 27-ABC-4. Puedes cambiarlo.</p>'
    else:
        b = f'<button class="inp off" id="chofer" type="button" disabled><span class="val ph">Se llena al elegir la moto</span>{ic("chev-d", "ic-s")}</button>'
        h = ''
    return f'<label class="lbl" for="chofer">Chofer</label>\n{b}\n{h}'

def campo_fecha(live=True, pc=False, foco=False):
    target = 'FechaPC.dc.html' if pc else 'FechaCel.dc.html'
    inner = f'<span class="val num">Hoy · 13 oct 2026</span>{ic("calendar", "ic-s", "color: #C25A12")}'
    return f'<p class="lbl" id="l-fecha">Fecha</p>\n' + A(target, 'inp' + (' foco' if foco else ''), inner, live, ' id="fecha" aria-labelledby="l-fecha fecha"')

def campo_monto(estado, live=True, valor=''):
    """estado: 'vacio' | 'err' | 'lleno' | 'foco'"""
    cls = 'inp' + (' err' if estado == 'err' else '') + (' foco' if estado == 'foco' else '')
    val = f' value="{valor}"' if valor else ''
    desc = ' aria-describedby="e-monto"' if estado == 'err' else ''
    ti = '' if live else ' tabindex="-1"'
    err = f'<p class="msg-err" id="e-monto">{ic("alert", "ic-xs")}Escribe el monto en pesos</p>' if estado == 'err' else ''
    return f'''<label class="lbl" for="monto">Monto</label>
<div class="money">
<span class="pre" aria-hidden="true">$</span>
<input class="{cls}" id="monto" type="text" inputmode="decimal" placeholder="0.00"{val}{desc}{ti} autocomplete="off">
</div>
{err}'''

def campo_nombre(lleno=True, live=True):
    ti = '' if live else ' tabindex="-1"'
    if lleno:
        return f'''<label class="lbl" for="nombre">Nombre</label>
<input class="inp" id="nombre" type="text" value="27-ABC-4 · 13 oct 2026" aria-describedby="h-nombre"{ti}>
<p class="hint" id="h-nombre">Se llena solo. Puedes cambiarlo.</p>'''
    return f'''<label class="lbl" for="nombre">Nombre</label>
<input class="inp" id="nombre" type="text" placeholder="Se llena al elegir la moto" aria-describedby="h-nombre"{ti}>
<p class="hint" id="h-nombre">Se llena solo. Puedes cambiarlo.</p>'''

def campos(modo, live=True, pc=False):
    """modo: registrar | errores | corregir | elegir | fecha | teclado"""
    if modo == 'errores':
        m, ch, mo, no = campo_moto('err', live, pc), campo_chofer(False, live), campo_monto('err', live), campo_nombre(False, live)
    elif modo == 'corregir':
        m, ch, mo, no = campo_moto('lleno', live, pc), campo_chofer(True, live), campo_monto('lleno', live, '350.00'), campo_nombre(True, live)
    elif modo == 'elegir':
        m, ch, mo, no = campo_moto('abierto', live, pc), campo_chofer(False, live), campo_monto('vacio', live), campo_nombre(False, live)
    elif modo == 'teclado':
        m, ch, mo, no = campo_moto('lleno', live, pc), campo_chofer(True, live), None, campo_nombre(True, live)
        mo = f'''<label class="lbl" for="monto">Monto</label>
<div class="money"><span class="pre" aria-hidden="true">$</span><span class="inp foco num" id="monto" role="textbox" aria-label="Monto"><span>350<span class="caret"></span></span></span></div>'''
    else:  # registrar (moto ya elegida)
        m, ch, mo, no = campo_moto('lleno', live, pc), campo_chofer(True, live), campo_monto('foco' if live else 'vacio', live), campo_nombre(True, live)
    fe = campo_fecha(live, pc, foco=(modo == 'fecha'))
    return [m, ch, fe, mo, no]

def form_cel(fname, title, modo, titulo, guardar, cancelar_href, guardar_href, overlay=''):
    live = overlay == '' and modo != 'teclado'
    cs = campos(modo, live)
    blocks = '\n'.join(f'<div>\n{c}\n</div>' for c in cs)
    if live:
        cerrar = f'<a class="btn btn-ico" href="{cancelar_href}" aria-label="Cerrar sin guardar">{ic("x")}</a>'
        guardar_b = f'<a class="btn btn-pri btn-lg" href="{guardar_href}" style="width: 100%">{guardar}</a>'
        cancel_b = f'<a class="btn btn-sec btn-lg" href="{cancelar_href}" style="width: 100%">Cancelar</a>'
        h = f'<h1 class="t-scr">{titulo}</h1>'
        hid = ''
    else:
        cerrar = f'<span class="btn btn-ico">{ic("x")}</span>'
        guardar_b = f'<span class="btn btn-pri btn-lg" style="width: 100%">{guardar}</span>'
        cancel_b = '<span class="btn btn-sec btn-lg" style="width: 100%">Cancelar</span>'
        h = f'<p class="t-scr">{titulo}</p>'
        hid = ' aria-hidden="true"' if modo != 'teclado' else ''
    body = f'''<div class="app" style="width: 390px; height: 844px; display: flex; flex-direction: column; background: #FFFFFF">
<header class="top top-f"{hid}>
{cerrar}
{h}
</header>
<form{hid} style="flex: 1; min-height: 0; overflow: hidden; padding: 24px 16px; display: flex; flex-direction: column; gap: 24px">
{blocks}
</form>
<div{hid} style="flex-shrink: 0; display: flex; flex-direction: column; gap: 8px; padding: 16px; border-top: 1px solid #E2E8F0; background: #FFFFFF">
{guardar_b}
{cancel_b}
</div>
{overlay}
</div>'''
    save(fname, title, body, 390, 844)

def form_panel(modo, titulo, guardar, cancelar_href, guardar_href, popover=None):
    live = popover is None
    cs = campos(modo, True, pc=True)
    blocks = []
    for i, c in enumerate(cs):
        pop = popover[1] if (popover and popover[0] == i) else ''
        blocks.append(f'<div style="position: relative">\n{c}\n{pop}\n</div>')
    blocks = '\n'.join(blocks)
    return f'''<div class="scrim"></div>
<section class="panel" role="dialog" aria-modal="true" aria-labelledby="t-panel">
<div style="display: flex; align-items: center; justify-content: space-between; padding: 16px 12px 16px 24px; border-bottom: 1px solid #E2E8F0">
<h2 id="t-panel" class="t-scr">{titulo}</h2>
<a class="btn btn-ico" href="{cancelar_href}" aria-label="Cerrar sin guardar">{ic("x")}</a>
</div>
<form style="flex: 1; min-height: 0; overflow: visible; padding: 24px; display: flex; flex-direction: column; gap: 24px">
{blocks}
</form>
<div style="display: flex; justify-content: flex-end; gap: 12px; padding: 16px 24px; border-top: 1px solid #E2E8F0">
<a class="btn btn-sec" href="{cancelar_href}">Cancelar</a>
<a class="btn btn-pri" href="{guardar_href}">{guardar}</a>
</div>
</section>'''

# ---------- Selectores ----------
def lista_motos(target, sel=None):
    out = []
    for placa, modelo, chofer in MOTOS:
        tag = '<span class="tag tag-aviso">Sin chofer</span>' if not chofer else ''
        s = ' sel' if placa == sel else ''
        out.append(f'<li><a class="opt{s}" href="{target}"><span class="avatar">{ic("bike", "ic-s")}</span>'
                   f'<span style="flex: 1; display: flex; flex-direction: column"><span class="placa">{placa}</span><span class="t-sec">{modelo}</span></span>{tag}</a></li>')
    return '<ul aria-label="Motos">' + ''.join(out) + '</ul>'

def calendario(target, compact=False):
    dias = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
    cells = [f'<span class="wd" aria-hidden="true">{d}</span>' for d in dias]
    cells += ['<span></span>'] * 3
    for d in range(1, 32):
        if d == 13:
            cells.append(f'<a class="sel" href="{target}" aria-current="date" aria-label="13 de octubre de 2026, hoy">{d}</a>')
        elif d > 13:
            cells.append(f'<span class="d fut" aria-hidden="true">{d}</span>')
        else:
            cells.append(f'<a href="{target}" aria-label="{d} de octubre de 2026">{d}</a>')
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px">
<a class="btn btn-ico" href="#" aria-label="Mes anterior">{ic("chev-l")}</a>
<p style="font-weight: 600">octubre 2026</p>
<span class="btn btn-ico" aria-hidden="true" style="color: #5A6475; opacity: .5">{ic("chev-r")}</span>
</div>
<div class="cal">{''.join(cells)}</div>'''

# =====================================================================
# 1 · Historial
cel_lista('Main.dc.html', 'Liquidaciones · Historial · Celular',
          search_cel() + '\n' + lista_cel(LIQ))
pc_lista('HistorialPC.dc.html', 'Liquidaciones · Historial · Computadora',
         search_pc() + '\n' + tabla(LIQ))

# 2 · Buscando
JUAN = [l for l in LIQ if 'Juan' in l[3]]
cel_lista('BuscandoCel.dc.html', 'Liquidaciones · Buscando · Celular',
          search_cel('Juan', foco=True) + '\n' + lista_cel(JUAN))
pc_lista('BuscandoPC.dc.html', 'Liquidaciones · Buscando · Computadora',
         search_pc('Juan') + '\n' + tabla(JUAN))

# 3 · Sin resultados
def vacio(icono, texto, boton, cel=True):
    return f'''<div style="flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; padding: {'32px 16px 96px' if cel else '48px 32px'}; text-align: center">
<span style="width: 64px; height: 64px; border-radius: 999px; display: flex; align-items: center; justify-content: center; background: #FDF3EA; color: #C25A12">{ic(icono, style='width: 32px; height: 32px')}</span>
<p style="max-width: 300px">{texto}</p>
{boton}
</div>'''

cel_lista('SinResultadosCel.dc.html', 'Liquidaciones · Sin resultados · Celular',
          search_cel('Roberto') + '\n' + vacio('search', 'No encontramos liquidaciones con "Roberto"',
          f'<a class="btn btn-sec" href="Main.dc.html">Borrar búsqueda</a>'))
pc_lista('SinResultadosPC.dc.html', 'Liquidaciones · Sin resultados · Computadora',
         search_pc('Roberto') + '\n<div class="card" style="display: flex">' + vacio('search', 'No encontramos liquidaciones con "Roberto"',
         '<a class="btn btn-sec" href="HistorialPC.dc.html">Borrar búsqueda</a>', cel=False) + '</div>')

# 4 · Lista vacía (sin buscador ni botón flotante: no hay nada que buscar y el botón ya está al centro)
txt_vacio = 'Todavía no hay liquidaciones.<br>Registra el primer pago.'
cel_lista('VaciaCel.dc.html', 'Liquidaciones · Lista vacía · Celular',
          vacio('receipt', txt_vacio, f'<a class="btn btn-pri btn-lg" href="RegistrarCel.dc.html">{ic("plus", "ic-s")}Registrar liquidación</a>'),
          con_fab=False)
body_vacia_pc = f'''<div class="app" style="width: 1440px; height: 900px; display: flex">
{side()}
<main style="flex: 1; min-width: 0; padding: 32px; display: flex; flex-direction: column; gap: 24px">
<h1 class="t-scr-pc">Liquidaciones</h1>
<div class="card" style="flex: 1; display: flex">{vacio('receipt', txt_vacio, f'<a class="btn btn-pri" href="RegistrarPC.dc.html">{ic("plus", "ic-s")}Registrar liquidación</a>', cel=False)}</div>
</main>
</div>'''
save('VaciaPC.dc.html', 'Liquidaciones · Lista vacía · Computadora', body_vacia_pc, 1440, 900)

# 5 · Registrar
form_cel('RegistrarCel.dc.html', 'Liquidaciones · Registrar · Celular', 'registrar', 'Registrar liquidación',
         'Guardar liquidación', 'Main.dc.html', 'RegistradaCel.dc.html')
pc_lista('RegistrarPC.dc.html', 'Liquidaciones · Registrar · Computadora', search_pc(live=False) + '\n' + tabla(LIQ, live=False),
         overlay=form_panel('registrar', 'Registrar liquidación', 'Guardar liquidación', 'HistorialPC.dc.html', 'RegistradaPC.dc.html'), live=False)

# 5a · Elegir moto
sheet_moto = f'''<div class="scrim"></div>
<section class="sheet" role="dialog" aria-modal="true" aria-labelledby="t-moto">
<div class="grab"><span></span></div>
<div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 8px 8px 16px">
<h2 id="t-moto" class="t-sub">Elige la moto</h2>
<a class="btn btn-ico" href="RegistrarCel.dc.html" aria-label="Cerrar">{ic("x")}</a>
</div>
<div class="search" style="margin: 0 16px 16px">
{ic("search", "ic-s")}
<input type="search" class="foco" placeholder="Buscar por placa" aria-label="Buscar moto por placa" autocapitalize="characters" autocomplete="off">
</div>
<div style="border-top: 1px solid #E2E8F0; padding-bottom: 16px">{lista_motos("RegistrarCel.dc.html")}</div>
</section>'''
form_cel('ElegirMotoCel.dc.html', 'Liquidaciones · Registrar · Elegir moto · Celular', 'elegir', 'Registrar liquidación',
         'Guardar liquidación', 'Main.dc.html', 'RegistradaCel.dc.html', overlay=sheet_moto)
pop_moto = f'''<div class="pop" role="dialog" aria-label="Elige la moto">
<div class="search" style="margin: 12px">
{ic("search", "ic-s")}
<input type="search" class="foco" placeholder="Buscar por placa" aria-label="Buscar moto por placa" autocomplete="off">
</div>
<div style="border-top: 1px solid #E2E8F0">{lista_motos("RegistrarPC.dc.html").replace('<li><a class="opt" href="RegistrarPC.dc.html"><span class="avatar">', '<li><a class="opt" href="RegistrarPC.dc.html"><span class="avatar">', 1)}</div>
</div>'''
pc_lista('ElegirMotoPC.dc.html', 'Liquidaciones · Registrar · Elegir moto · Computadora', search_pc(live=False) + '\n' + tabla(LIQ, live=False),
         overlay=form_panel('elegir', 'Registrar liquidación', 'Guardar liquidación', 'HistorialPC.dc.html', 'RegistradaPC.dc.html', popover=(0, pop_moto)), live=False)

# 5b · Fecha
sheet_fecha = f'''<div class="scrim"></div>
<section class="sheet" role="dialog" aria-modal="true" aria-labelledby="t-fecha" style="padding-bottom: 24px">
<div class="grab"><span></span></div>
<div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 8px 8px 16px">
<h2 id="t-fecha" class="t-sub">Elige la fecha</h2>
<a class="btn btn-ico" href="RegistrarCel.dc.html" aria-label="Cerrar">{ic("x")}</a>
</div>
<div style="padding: 0 16px">{calendario("RegistrarCel.dc.html")}</div>
</section>'''
form_cel('FechaCel.dc.html', 'Liquidaciones · Registrar · Fecha · Celular', 'fecha', 'Registrar liquidación',
         'Guardar liquidación', 'Main.dc.html', 'RegistradaCel.dc.html', overlay=sheet_fecha)
pop_fecha = f'<div class="pop" role="dialog" aria-label="Elige la fecha" style="padding: 12px 16px 16px">{calendario("RegistrarPC.dc.html")}</div>'
pc_lista('FechaPC.dc.html', 'Liquidaciones · Registrar · Fecha · Computadora', search_pc(live=False) + '\n' + tabla(LIQ, live=False),
         overlay=form_panel('fecha', 'Registrar liquidación', 'Guardar liquidación', 'HistorialPC.dc.html', 'RegistradaPC.dc.html', popover=(2, pop_fecha)), live=False)

# 5c · Monto con teclado numérico (solo celular)
teclas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0']
kbd = '<div class="kbd" aria-hidden="true">' + ''.join(f'<span>{t}</span>' for t in teclas) + f'<span class="fn">{ic("delete")}</span></div>'
form_cel('TecladoCel.dc.html', 'Liquidaciones · Registrar · Monto con teclado numérico · Celular', 'teclado', 'Registrar liquidación',
         'Guardar liquidación', 'Main.dc.html', 'RegistradaCel.dc.html', overlay=kbd)

# 6 · Errores
form_cel('ErroresCel.dc.html', 'Liquidaciones · Registrar con errores · Celular', 'errores', 'Registrar liquidación',
         'Guardar liquidación', 'Main.dc.html', 'RegistrarCel.dc.html')
pc_lista('ErroresPC.dc.html', 'Liquidaciones · Registrar con errores · Computadora', search_pc(live=False) + '\n' + tabla(LIQ, live=False),
         overlay=form_panel('errores', 'Registrar liquidación', 'Guardar liquidación', 'HistorialPC.dc.html', 'RegistrarPC.dc.html'), live=False)

# 7 · Aviso de éxito (la nueva arriba)
NUEVA = [('hoy', '13 oct 2026', '27-ABC-4', 'Juan Pérez López', '$350.00')] + LIQ
def toast(cel=True):
    pos = 'left: 16px; right: 16px; bottom: 88px; min-height: 56px; padding-right: 16px' if cel else 'top: 24px; right: 32px; width: 400px'
    return f'''<div class="toast" role="status" style="{pos}">
{ic("check-circle")}
<span class="num" style="flex: 1">Liquidación registrada · $350.00</span>
{'' if cel else '<a class="btn btn-ico" href="HistorialPC.dc.html" aria-label="Cerrar aviso">' + ic("x", "ic-s") + '</a>'}
</div>'''
cel_lista('RegistradaCel.dc.html', 'Liquidaciones · Liquidación registrada · Celular',
          search_cel() + '\n' + lista_cel(LIQ, nueva_idx=0), overlay=toast(True), fab_bottom=164)
pc_lista('RegistradaPC.dc.html', 'Liquidaciones · Liquidación registrada · Computadora',
         search_pc() + '\n' + tabla(LIQ, nueva_idx=0), overlay=toast(False))

# 8 · Detalle
def tarjetas_detalle(live=True):
    moto = A('#', 'card lk', f'<span class="avatar">{ic("bike")}</span><span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span class="t-lab" style="color: #5A6475">Moto</span><span class="placa">27-ABC-4</span><span class="t-sec">Italika FT150</span></span>{ic("chev-r", "chev")}', live, ' aria-label="Moto 27-ABC-4, Italika FT150. Abrir la moto"')
    chof = A('#', 'card lk', f'<span class="avatar">{ic("user")}</span><span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span class="t-lab" style="color: #5A6475">Chofer</span><span style="font-weight: 600">Juan Pérez López</span><span class="t-sec num">55 1234 5678</span></span>{ic("chev-r", "chev")}', live, ' aria-label="Chofer Juan Pérez López. Abrir el chofer"')
    return moto, chof

def datos_detalle(pc=False):
    t = 't-scr-pc' if pc else 't-scr'
    return f'''<div style="display: flex; flex-direction: column; gap: 8px">
<p class="t-sec">Liquidación</p>
<h1 class="{t} num">$350.00</h1>
</div>
<dl style="display: flex; flex-direction: column; gap: 12px">
<div style="display: flex; align-items: center; gap: 12px">{ic("calendar", "ic-s", "color: #5A6475")}<dt class="sr">Fecha</dt><dd class="num">13 oct 2026</dd></div>
<div style="display: flex; align-items: center; gap: 12px">{ic("receipt", "ic-s", "color: #5A6475")}<dt class="sr">Nombre</dt><dd>27-ABC-4 · 13 oct 2026</dd></div>
</dl>'''

moto_c, chof_c = tarjetas_detalle()
det_cel = f'''<div class="app" style="width: 390px; height: 844px; display: flex; flex-direction: column">
<header class="top">
<a class="back" href="Main.dc.html">{ic("arrow-left")}Liquidaciones</a>
<a class="btn btn-sec" href="CorregirCel.dc.html">{ic("pencil", "ic-s")}Corregir</a>
</header>
<main style="flex: 1; min-height: 0; overflow: hidden; padding: 24px 16px; display: flex; flex-direction: column; gap: 24px">
<div class="card" style="padding: 16px; display: flex; flex-direction: column; gap: 16px">
{datos_detalle()}
</div>
<div style="display: flex; flex-direction: column; gap: 12px">
{moto_c}
{chof_c}
</div>
</main>
{bnav()}
</div>'''
save('DetalleCel.dc.html', 'Liquidaciones · Detalle · Celular', det_cel, 390, 844)

def det_pc_main(live=True):
    m, c = tarjetas_detalle(live)
    back = A('HistorialPC.dc.html', 'back', ic('arrow-left') + 'Liquidaciones', live)
    corr = A('CorregirPC.dc.html', 'btn btn-sec', ic('pencil', 'ic-s') + 'Corregir', live)
    dd = datos_detalle(True)
    if not live:
        dd = dd.replace('<h1 ', '<p ').replace('</h1>', '</p>')
    return f'''<main{'' if live else ' aria-hidden="true"'} style="flex: 1; min-width: 0; padding: 32px; display: flex; flex-direction: column; gap: 24px">
<div>{back}</div>
<div style="max-width: 800px; display: flex; flex-direction: column; gap: 24px">
<div class="card" style="padding: 24px; display: flex; align-items: flex-start; justify-content: space-between; gap: 24px">
<div style="display: flex; flex-direction: column; gap: 16px">
{dd}
</div>
{corr}
</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px">
{m}
{c}
</div>
</div>
</main>'''

save('DetallePC.dc.html', 'Liquidaciones · Detalle · Computadora', f'''<div class="app" style="width: 1440px; height: 900px; display: flex">
{side()}
{det_pc_main()}
</div>''', 1440, 900)

# 9 · Corregir
form_cel('CorregirCel.dc.html', 'Liquidaciones · Corregir · Celular', 'corregir', 'Corregir liquidación',
         'Guardar cambios', 'DetalleCel.dc.html', 'DetalleCel.dc.html')
save('CorregirPC.dc.html', 'Liquidaciones · Corregir · Computadora', f'''<div class="app" style="width: 1440px; height: 900px; display: flex">
{side(False)}
{det_pc_main(False)}
{form_panel('corregir', 'Corregir liquidación', 'Guardar cambios', 'DetallePC.dc.html', 'DetallePC.dc.html')}
</div>''', 1440, 900)

# ---------- Lienzo ----------
NUM = {'Main.dc.html': '1', 'BuscandoCel.dc.html': '2', 'SinResultadosCel.dc.html': '3', 'VaciaCel.dc.html': '4',
       'RegistrarCel.dc.html': '5', 'ElegirMotoCel.dc.html': '5a', 'FechaCel.dc.html': '5b', 'TecladoCel.dc.html': '5c',
       'ErroresCel.dc.html': '6', 'RegistradaCel.dc.html': '7', 'DetalleCel.dc.html': '8', 'CorregirCel.dc.html': '9'}
FILAS = [('Main.dc.html', 'HistorialPC.dc.html'), ('BuscandoCel.dc.html', 'BuscandoPC.dc.html'),
         ('SinResultadosCel.dc.html', 'SinResultadosPC.dc.html'), ('VaciaCel.dc.html', 'VaciaPC.dc.html'),
         ('RegistrarCel.dc.html', 'RegistrarPC.dc.html'), ('ElegirMotoCel.dc.html', 'ElegirMotoPC.dc.html'),
         ('FechaCel.dc.html', 'FechaPC.dc.html'), ('TecladoCel.dc.html', None),
         ('ErroresCel.dc.html', 'ErroresPC.dc.html'), ('RegistradaCel.dc.html', 'RegistradaPC.dc.html'),
         ('DetalleCel.dc.html', 'DetallePC.dc.html'), ('CorregirCel.dc.html', 'CorregirPC.dc.html')]
boards, order = {}, []
y = 0
for cel, pc in FILAS:
    n = NUM[cel]
    for f, x in ((cel, 0), (pc, 470)):
        if not f:
            continue
        b = BOARDS[f]
        e = {'x': x, 'y': y, 'w': b['w'], 'h': b['h'], 'title': f"{n} · {b['title']}"}
        if b.get('is_interactive'):
            e['is_interactive'] = True
        boards[f] = e
        order.append(f)
    y += 900 + 120
canvas = {'v': 3, 'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},
          'title': 'Liquidaciones', 'launch': {'view': 'canvas'}, 'pages': [], 'boards': boards, 'order': order,
          'notes': {}, 'designSystems': []}
with open(os.path.join(OUT, 'canvas.json'), 'w', encoding='utf-8') as f:
    json.dump(canvas, f, ensure_ascii=False, indent=2)
print(len(order), 'pantallas')

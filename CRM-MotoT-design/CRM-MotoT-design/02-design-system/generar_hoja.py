#!/usr/bin/env python3
"""Genera la hoja del design system de CRM-MotoT (HTML estático, 1440 px)."""
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "hoja-design-system.html"

# ---------- Iconos Lucide (trazo 1.5, 20 px) · mismos trazos que la hoja de componentes ----------
ICONS = {
    "bike": '<circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="15" cy="5" r="1"/><path d="M12 17.5V14l-3-3 4-3 2 3h2"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "receipt": '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/>',
    "landmark": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
    "pencil": '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/>',
    "arrow-left": '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "log-out": '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "circle-check": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
}


def ic(name, cls=""):
    return f'<svg class="ic {cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + "</svg>"

CSS = """
/* Hoja de referencia de 1440 px: columna de título a la izquierda, ejemplos a la derecha. Solo modo claro. */
:root{
  --acc:#C25A12; --acc-h:#A84B0C; --acc-s:#FDF3EA;
  --bg:#FAFAF9; --sf:#FFFFFF; --side:#F5F5F4; --bd:#E7E5E4; --bd-f:#D6D3D1; --hov:#F5F5F4; --sb-hov:#EEEDEC;
  --t1:#1C1917; --t2:#57534E; --t3:#78716C;
  --ok:#15803D; --ok-s:#F0FDF4; --err:#B91C1C; --err-s:#FEF2F2; --warn:#854D0E; --warn-s:#FEF9C3;
  --dark:#1C1917; --on-dark:#FAFAF9;
  --sh:0 4px 16px rgba(28,25,23,0.08);
  --font:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  color-scheme:light;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--t1);font-family:var(--font);font-size:14px;line-height:20px;-webkit-font-smoothing:antialiased;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0}
h1,h2,h3,h4,p,ul,dl,dd{margin:0;padding:0}
ul{list-style:none}
button,input{font-family:inherit}
.ic{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0}
.num{font-variant-numeric:tabular-nums}
.placa{text-transform:uppercase;font-weight:500;letter-spacing:.04em;font-variant-numeric:tabular-nums}
:focus-visible{outline:none;box-shadow:0 0 0 2px var(--sf),0 0 0 4px var(--acc)}

.scroll{overflow-x:auto;margin-inline:calc(-1 * max(16px,env(safe-area-inset-left,0px)))}
.sheet{width:1440px;margin:0 auto;padding:48px}

/* Portada */
.top{display:grid;grid-template-columns:1fr 440px;gap:48px;padding-bottom:32px;border-bottom:1px solid var(--bd)}
.top h1{font-size:32px;line-height:40px;font-weight:600;letter-spacing:-0.01em;text-wrap:balance}
.top .lead{margin-top:8px;font-size:16px;line-height:24px;color:var(--t2);max-width:620px}
.meta{display:flex;gap:24px;margin-top:24px;font-size:13px;line-height:18px;color:var(--t3)}
.meta b{display:block;font-weight:500;color:var(--t1);font-size:14px;line-height:20px}
.notes{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:16px 20px}
.cap{font-size:12px;line-height:16px;font-weight:500;color:var(--t2);text-transform:uppercase;letter-spacing:.04em}
.notes ul{margin-top:8px;display:flex;flex-direction:column;gap:6px;font-size:13px;line-height:18px;color:var(--t2)}
.notes li{padding-left:12px;position:relative}
.notes li::before{content:"";position:absolute;left:0;top:8px;width:4px;height:4px;border-radius:2px;background:var(--bd-f)}
.index{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;flex-wrap:wrap;gap:4px;padding:12px 0;background:var(--bg);border-bottom:1px solid var(--bd)}
.index a{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 10px;border-radius:6px;color:var(--t2);text-decoration:none;font-size:13px;line-height:18px;font-weight:500}
.index a:hover{background:var(--sb-hov);color:var(--t1)}
.index a span{color:var(--t3);font-variant-numeric:tabular-nums}

/* Secciones */
.sec{display:grid;grid-template-columns:280px 1fr;gap:48px;padding:48px 0;border-bottom:1px solid var(--bd);scroll-margin-top:64px}
.sec:last-child{border-bottom:0}
.sec-n{font-size:13px;line-height:18px;color:var(--t3);font-variant-numeric:tabular-nums}
.sec h2{margin-top:4px;font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em}
.sec-d{margin-top:8px;color:var(--t2);font-size:14px;line-height:20px}
.sec-l{position:sticky;top:72px;align-self:start}
.body{min-width:0;display:flex;flex-direction:column;gap:32px}
.grp h3{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em;margin-bottom:12px}
.grp h3 small{font-size:13px;line-height:18px;font-weight:400;color:var(--t3);margin-left:8px}
.anno{font-size:12px;line-height:16px;color:var(--t3);font-variant-numeric:tabular-nums}

/* 1 · Logotipo */
.logos{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.lbox{border:1px solid var(--bd);border-radius:8px;overflow:hidden}
.lstage{height:200px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:24px}
.lstage.w{background:var(--sf)}
.lstage.d{background:var(--dark);color:var(--on-dark)}
.lfoot{display:flex;justify-content:space-between;gap:16px;padding:12px 16px;border-top:1px solid var(--bd);background:var(--sf);font-size:13px;line-height:18px;color:var(--t2)}
.lfoot code,.hex{font-family:var(--font);font-variant-numeric:tabular-nums;color:var(--t1);font-weight:500}
.logo{display:inline-flex;align-items:center;gap:8px;font-weight:600;letter-spacing:-0.01em;white-space:nowrap}
.logo .ic{color:var(--acc)}
.logo.xl{font-size:32px;line-height:40px;gap:12px}
.logo.xl .ic{width:36px;height:36px;stroke-width:1.5}
.logo.md{font-size:16px;line-height:24px}
.lsizes{display:flex;align-items:center;gap:32px}
.lrules{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:16px}
.rule{display:flex;flex-direction:column;gap:8px;padding:16px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;font-size:13px;line-height:18px;color:var(--t2)}
.rule b{font-size:14px;line-height:20px;font-weight:500;color:var(--t1)}
.rule .demo{height:64px;display:flex;align-items:center;justify-content:center;border-radius:6px;background:var(--bg)}
.ok-t{color:var(--ok)} .no-t{color:var(--err)}

/* 2 · Paleta */
.sw-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.sw-grid.c3{grid-template-columns:repeat(3,1fr)}
.sw{background:var(--sf);border:1px solid var(--bd);border-radius:8px;overflow:hidden;display:flex;flex-direction:column}
.chip{height:88px;border-bottom:1px solid var(--bd);display:flex;align-items:flex-end;padding:12px}
.sw-b{padding:12px 16px 16px;display:flex;flex-direction:column;gap:2px}
.sw-n{font-weight:500}
.sw-h{font-size:13px;line-height:18px;color:var(--t2);font-variant-numeric:tabular-nums}
.sw-u{margin-top:6px;font-size:13px;line-height:18px;color:var(--t3)}
.pair .chip{align-items:center;justify-content:center;font-weight:500;gap:8px}

/* Etiquetas */
.tag{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 8px;border-radius:6px;font-size:12px;line-height:16px;font-weight:500;white-space:nowrap}
.tag .dot{width:6px;height:6px;border-radius:3px;background:currentColor}
.tag.alta{color:var(--ok);background:var(--ok-s)}
.tag.baja{color:var(--err);background:var(--err-s)}
.tag.aviso{color:var(--warn);background:var(--warn-s)}
.tag.ger{color:var(--acc-h);background:var(--acc-s)}
.tag.ayu{color:var(--t2);background:var(--side)}

/* 3 · Tipografía */
.ty{background:var(--sf);border:1px solid var(--bd);border-radius:8px}
.ty-r{display:grid;grid-template-columns:220px 1fr 200px;gap:24px;align-items:center;padding:20px 24px;border-bottom:1px solid var(--bd)}
.ty-r:last-child{border-bottom:0}
.ty-n{font-weight:500}
.ty-n small{display:block;font-size:13px;line-height:18px;font-weight:400;color:var(--t3)}
.ty-s{min-width:0}
.ty-m{font-size:13px;line-height:18px;color:var(--t2);font-variant-numeric:tabular-nums;text-align:right}
.data{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.dbox{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:12px}
.dbox .big{font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em}
.dbox .row{display:flex;justify-content:space-between;gap:8px;font-size:13px;line-height:18px;color:var(--t3);border-top:1px solid var(--bd);padding-top:8px}
.dbox .row span:last-child{color:var(--t2);text-align:right}
.cols{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.mini{background:var(--sf);border:1px solid var(--bd);border-radius:8px;overflow:hidden}
.mini table{width:100%;border-collapse:collapse}
.mini th{height:40px;padding:0 16px;text-align:left;font-size:12px;line-height:16px;font-weight:500;color:var(--t2);border-bottom:1px solid var(--bd);background:var(--sf)}
.mini td{height:44px;padding:0 16px;font-size:14px;line-height:20px;border-bottom:1px solid var(--bd)}
.mini tr:last-child td{border-bottom:0}
.mini .r{text-align:right}

/* 4 · Espacios */
.sp{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:24px;display:flex;align-items:flex-end;gap:40px}
.sp-i{display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.sp-blk{background:var(--acc-s);border:1px solid #F3D3B8;border-radius:2px}
.sp-l{display:flex;flex-direction:column;gap:2px}
.sp-l b{font-weight:600;font-variant-numeric:tabular-nums}
.sp-l span{font-size:12px;line-height:16px;color:var(--t3)}
.rules3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.mrule{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:12px}
.mrule b{font-weight:500}
.mrule p{font-size:13px;line-height:18px;color:var(--t2)}
.gut{position:relative;height:72px;border:1px solid var(--bd);border-radius:6px;background:var(--bg);overflow:hidden}
.gut i{position:absolute;top:0;bottom:0;background:var(--acc-s);border-color:#F3D3B8;border-style:solid;border-width:0}
.gut .c{position:absolute;top:12px;bottom:12px;border:1px solid var(--bd);border-radius:4px;background:var(--sf)}

/* 5 · Bordes y sombras */
.bs{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.bs-c{background:var(--bg);border:1px solid var(--bd);border-radius:8px;padding:24px;display:flex;flex-direction:column;gap:16px}
.bs-c .anno{display:flex;flex-wrap:wrap;gap:4px 16px}
.card{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:12px}
.card-h{display:flex;align-items:center;justify-content:space-between;gap:12px}
.card-t{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em}
.dl{display:grid;grid-template-columns:120px 1fr;font-size:14px;line-height:20px}
.dl dt{color:var(--t2);padding:8px 0;border-top:1px solid var(--bd)}
.dl dd{padding:8px 0;border-top:1px solid var(--bd)}
.btns{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.b{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:44px;padding:0 16px;border-radius:6px;border:1px solid var(--bd-f);background:var(--sf);color:var(--t1);font-size:14px;line-height:20px;font-weight:500;cursor:pointer;white-space:nowrap}
.b:hover{background:var(--hov)}
.b.pri{background:var(--acc);border-color:var(--acc);color:#FFFFFF;font-weight:600}
.b.pri:hover,.b.pri.h{background:var(--acc-h);border-color:var(--acc-h)}
.b.dng{background:var(--err);border-color:var(--err);color:#FFFFFF;font-weight:600}
.b.ghost{border-color:transparent;background:transparent;color:var(--acc);padding:0 12px}
.fld{display:flex;flex-direction:column;gap:8px}
.fld label{font-weight:500}
.inp{display:flex;align-items:center;gap:8px;height:44px;padding:0 12px;border:1px solid var(--bd-f);border-radius:6px;background:var(--sf);color:var(--t1);font-size:14px;line-height:20px}
.inp.ph{color:var(--t3)}
.inp.f{border-color:var(--acc);box-shadow:0 0 0 3px var(--acc-s)}
.inp.e{border-color:var(--err)}
.help{font-size:13px;line-height:18px;color:var(--t3)}
.help.e{color:var(--err)}
.tags{display:flex;flex-wrap:wrap;gap:8px}
.menu{width:260px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;box-shadow:var(--sh);padding:4px}
.menu div{display:flex;align-items:center;gap:12px;height:40px;padding:0 12px;border-radius:6px;color:var(--t1)}
.menu div .ic{color:var(--t2)}
.menu div.h{background:var(--hov)}
.modal{background:var(--sf);border:1px solid var(--bd);border-radius:8px;box-shadow:var(--sh);padding:24px;display:flex;flex-direction:column;gap:8px;max-width:420px}
.modal h4{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em}
.modal p{color:var(--t2)}
.modal .btns{justify-content:flex-end;margin-top:16px}
.radii{display:flex;gap:24px;align-items:flex-end}
.rd{display:flex;flex-direction:column;gap:8px;align-items:flex-start}
.rd i{display:block;width:72px;height:72px;border:1px solid var(--t2);border-right:0;border-bottom:0;background:var(--sf)}

/* 6 · Iconos */
.icg{display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
.icc{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:20px 16px 16px;display:flex;flex-direction:column;gap:16px}
.icc .ib{width:44px;height:44px;display:flex;align-items:center;justify-content:center;border-radius:6px;background:var(--bg);border:1px solid var(--bd);color:var(--t1)}
.icc b{font-weight:500;display:block}
.icc span{font-size:12px;line-height:16px;color:var(--t3)}
.icc.extra .ib{border-style:dashed}
.icstates{display:flex;gap:24px;align-items:center;padding:16px 20px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;font-size:13px;line-height:18px;color:var(--t2)}
.icstates div{display:flex;align-items:center;gap:8px}

/* 7 · Tono */
.princ{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.pr{padding:16px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;display:flex;flex-direction:column;gap:4px}
.pr b{font-weight:500}
.pr p{font-size:13px;line-height:18px;color:var(--t2)}
.tone{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.tc{background:var(--sf);border:1px solid var(--bd);border-radius:8px;overflow:hidden;display:flex;flex-direction:column}
.tc-h{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 16px;border-bottom:1px solid var(--bd)}
.tc-h .cap{text-transform:none;letter-spacing:0;font-size:13px;line-height:18px}
.verd{display:inline-flex;align-items:center;gap:6px;font-size:12px;line-height:16px;font-weight:500}
.verd.y{color:var(--ok)} .verd.n{color:var(--err)}
.verd .ic{width:16px;height:16px}
.tc-s{padding:24px;background:var(--bg);flex:1;display:flex;align-items:center;justify-content:center}
.tc-w{padding:12px 16px;border-top:1px solid var(--bd);font-size:13px;line-height:18px;color:var(--t2)}
.toast{display:flex;align-items:center;gap:12px;min-width:320px;padding:12px 16px;border-radius:8px;background:var(--dark);color:var(--on-dark);font-weight:500;box-shadow:var(--sh)}
.toast .ic{color:#4ADE80}
.empty{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;width:100%}
.empty .bub{display:flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:8px;background:var(--side);color:var(--t2);margin-bottom:4px}
.empty b{font-size:16px;line-height:24px;font-weight:600}
.empty p{color:var(--t2);font-size:14px}
.bad{display:flex;align-items:center;gap:12px;padding:12px 16px;border:1px solid var(--bd);border-radius:8px;background:var(--sf);min-width:320px}
.bad .ic{color:var(--t2)}
.strike{text-decoration:line-through;text-decoration-color:var(--err);text-decoration-thickness:1.5px}
.alt{display:flex;flex-direction:column;gap:2px;padding:12px 16px;border-top:1px solid var(--bd)}
.alt span{font-size:12px;line-height:16px;color:var(--t3)}
.alt b{font-weight:500}

/* 8 · Marco */
.frames{display:grid;grid-template-columns:392px 1fr;gap:32px;align-items:end}
.fcap{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px}
.fcap b{font-weight:600}
.dev{position:relative;border:1px solid var(--bd-f);border-radius:8px;overflow:hidden;background:var(--bg)}
.phone{width:392px;height:846px;display:flex;flex-direction:column}
.status{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 24px;background:var(--sf);font-size:15px;line-height:20px;font-weight:600}
.status i{display:flex;gap:4px}
.status i u{display:block;width:16px;height:10px;border-radius:2px;background:var(--t1);text-decoration:none}
.tbar{display:flex;align-items:center;gap:8px;height:56px;padding:0 16px;background:var(--sf);border-bottom:1px solid var(--bd)}
.tbar h4{flex:1;font-size:22px;line-height:28px;font-weight:600;letter-spacing:-0.01em}
.tbar .logo .ic{width:20px;height:20px}
.content{flex:1;position:relative}
.guide{position:absolute;border:1px dashed var(--bd-f);border-radius:6px;display:flex;align-items:center;justify-content:center;color:var(--t3);font-size:12px;line-height:16px;text-align:center;padding:8px}
.mtag{position:absolute;font-size:11px;line-height:14px;font-weight:500;color:var(--acc-h);background:var(--acc-s);border-radius:4px;padding:1px 4px;font-variant-numeric:tabular-nums}
.bnav{display:flex;background:var(--sf);border-top:1px solid var(--bd);padding:0 4px 8px}
.bn{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;min-height:64px;padding-top:8px;color:var(--t2);font-size:12px;line-height:16px;font-weight:500;text-decoration:none;border-radius:6px}
.bn .pill{display:flex;align-items:center;justify-content:center;width:56px;height:28px;border-radius:6px}
.bn.on{color:var(--t1);font-weight:600}
.bn.on .pill{background:var(--bd)}
.bn.on .ic{color:var(--acc)}
.home{height:20px;background:var(--sf);display:flex;align-items:flex-start;justify-content:center}
.home i{width:134px;height:5px;border-radius:3px;background:var(--t1)}
.pcwrap{width:100%;}
.pcscale{width:1440px;height:900px;transform:scale(.7042);transform-origin:0 0}
.pcbox{width:1016px;height:636px}
.pc{width:1440px;height:900px;display:flex;background:var(--bg)}
.side{width:240px;flex-shrink:0;display:flex;flex-direction:column;background:var(--side);border-right:1px solid var(--bd)}
.side .logo{height:64px;padding:0 20px;font-size:16px;line-height:24px}
.sgrp{padding:8px 8px 0}
.sgrp+.sgrp{padding-top:16px}
.slbl{padding:0 12px 4px;font-size:12px;line-height:16px;font-weight:500;color:var(--t3)}
.si{display:flex;align-items:center;gap:12px;height:40px;padding:0 12px;border-radius:6px;color:var(--t2);text-decoration:none;font-size:14px;line-height:20px}
.si.on{background:var(--bd);color:var(--t1);font-weight:600}
.si.on .ic{color:var(--acc)}
.sfoot{margin-top:auto;border-top:1px solid var(--bd);padding:12px 8px 8px}
.who{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:4px 12px 8px}
.who b{font-weight:500}
.main{flex:1;position:relative}
.specs{display:flex;flex-direction:column;gap:16px}
.spec{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:16px}
.spec dl{display:grid;grid-template-columns:150px 1fr;gap:6px 12px;margin-top:8px;font-size:13px;line-height:18px}
.spec dt{color:var(--t3)}
.spec dd{color:var(--t1);font-variant-numeric:tabular-nums}
"""


def sec(n, sid, title, desc, body):
    return (f'<section class="sec" id="{sid}"><div class="sec-l"><div class="sec-n">{n} de 8</div>'
            f'<h2>{title}</h2><p class="sec-d">{desc}</p></div><div class="body">{body}</div></section>')


def grp(title, body, small=""):
    s = f"<small>{small}</small>" if small else ""
    return f'<div class="grp"><h3>{title}{s}</h3>{body}</div>'


def logo(cls=""):
    return f'<span class="logo {cls}">{ic("bike")}CRM-MotoT</span>'


# ---------- 1 · Logotipo ----------
s1 = grp("Versiones", f"""
<div class="logos">
  <div class="lbox"><div class="lstage w"><div class="lsizes">{logo("xl")}</div><div class="lsizes">{logo("md")}</div></div>
    <div class="lfoot"><span>Sobre blanco · texto <code>#1C1917</code>, icono <code>#C25A12</code></span><span>32 px y 16 px</span></div></div>
  <div class="lbox"><div class="lstage d"><div class="lsizes">{logo("xl")}</div><div class="lsizes">{logo("md")}</div></div>
    <div class="lfoot"><span>Sobre oscuro <code>#1C1917</code> · texto <code>#FAFAF9</code>, icono <code>#C25A12</code></span><span>32 px y 16 px</span></div></div>
</div>""", "Inter semibold, -0.01em · icono bike con trazo 1.5")
s1 += grp("Uso", f"""
<div class="lrules">
  <div class="rule"><div class="demo">{logo("md")}</div><b>Tamaño en la app</b><p>16/24 con icono de 20 px y 8 px de separación. Va arriba del menú lateral y en el inicio de sesión.</p></div>
  <div class="rule"><div class="demo" style="padding:0 16px;justify-content:flex-start"><span style="display:inline-flex;padding:16px;border:1px dashed var(--bd-f);border-radius:4px">{logo("md")}</span></div><b>Espacio libre</b><p>Deja al menos 16 px vacíos alrededor. No lo pongas dentro de cajas ni sobre fotos.</p></div>
  <div class="rule"><div class="demo"><span class="logo md" style="color:var(--acc)">{ic("bike")}CRM-MotoT</span></div><b class="no-t">Evita</b><p>Pintar el texto de ocre, cambiar el icono, deformarlo o ponerle sombra. Solo el icono va en ocre.</p></div>
</div>""")

# ---------- 2 · Paleta ----------
def sw(name, hx, use, fg=None, text=None, border=False):
    style = f"background:{hx}" + (f";color:{fg}" if fg else "")
    inner = text or ""
    return (f'<div class="sw"><div class="chip" style="{style}">{inner}</div>'
            f'<div class="sw-b"><span class="sw-n">{name}</span><span class="sw-h">{hx}</span><span class="sw-u">{use}</span></div></div>')


def pair(name, fg, bg, use, label, icon=None):
    i = ic(icon) if icon else ""
    return (f'<div class="sw pair"><div class="chip" style="background:{bg};color:{fg}">{i}{label}</div>'
            f'<div class="sw-b"><span class="sw-n">{name}</span><span class="sw-h">{fg} sobre {bg}</span><span class="sw-u">{use}</span></div></div>')


s2 = grp("Acento ocre-naranja", '<div class="sw-grid c3">'
         + sw("Ocre", "#C25A12", "Botón principal con texto blanco, enlaces, anillo de foco, icono de la opción activa y logo. Úsalo poco.", "#FFFFFF", '<span style="font-weight:600">Guardar</span>')
         + sw("Ocre hover", "#A84B0C", "Botón principal y enlaces al pasar el mouse. Texto de la etiqueta Gerente.", "#FFFFFF")
         + sw("Ocre suave", "#FDF3EA", "Halo del foco en campos y fondo de la etiqueta Gerente.")
         + "</div>", "una sola marca de color en cada pantalla")
s2 += grp("Neutros", '<div class="sw-grid c3">'
          + sw("Fondo de la app", "#FAFAF9", "Detrás de todo el contenido.")
          + sw("Superficie", "#FFFFFF", "Tarjetas, ventanas, barras superior e inferior, campos.")
          + sw("Menú lateral", "#F5F5F4", "Fondo del menú lateral en computadora.")
          + sw("Borde", "#E7E5E4", "Bordes de 1 px de tarjetas y divisiones. También fondo de la opción activa del menú.")
          + sw("Borde de campos", "#D6D3D1", "Contorno de campos y botones secundarios.")
          + sw("Fila al pasar el mouse", "#F5F5F4", "Fondo de filas y opciones al pasar el mouse.")
          + "</div>")
s2 += grp("Texto", '<div class="sw-grid c3">'
          + sw("Texto principal", "#1C1917", "Títulos, cuerpo, montos y datos.", "#FFFFFF", '<span style="font-weight:600;font-size:16px">Aa</span>')
          + sw("Texto secundario", "#57534E", "Descripciones, nombres de campo en fichas, opciones inactivas.", "#FFFFFF", '<span style="font-weight:600;font-size:16px">Aa</span>')
          + sw("Texto de ayuda", "#78716C", "Ayuda bajo los campos, marcadores y notas.", "#FFFFFF", '<span style="font-weight:600;font-size:16px">Aa</span>')
          + "</div>")
s2 += grp("Estados", '<div class="sw-grid c3">'
          + pair("Éxito · Alta", "#15803D", "#F0FDF4", "Confirmaciones y estado Alta de choferes, motos y usuarios.", '<span class="tag alta"><span class="dot"></span>Alta</span>')
          + pair("Error · Baja · Peligro", "#B91C1C", "#FEF2F2", "Errores de campos, estado Baja y acciones que borran o dan de baja.", '<span class="tag baja"><span class="dot"></span>Baja</span>')
          + pair("Aviso", "#854D0E", "#FEF9C3", "Algo incompleto que no es error: «Sin chofer», «Sin moto».", '<span class="tag aviso">Sin chofer</span>')
          + "</div>", "texto de color sobre fondo suave")
s2 += grp("Etiquetas de rol", '<div class="sw-grid c3">'
          + pair("Gerente", "#A84B0C", "#FDF3EA", "Rol con todos los permisos.", '<span class="tag ger">Gerente</span>')
          + pair("Ayudante", "#57534E", "#F5F5F4", "Rol que registra y consulta, sin altas, bajas ni Financiamiento.", '<span class="tag ayu">Ayudante</span>')
          + "</div>")

# ---------- 3 · Tipografía ----------
def tyr(name, dev, sample, style, meta):
    return (f'<div class="ty-r"><div class="ty-n">{name}<small>{dev}</small></div>'
            f'<div class="ty-s" style="{style}">{sample}</div><div class="ty-m">{meta}</div></div>')


s3 = grp("Estilos", '<div class="ty">'
         + tyr("Título de pantalla", "Celular", "Liquidaciones", "font-size:22px;line-height:28px;font-weight:600;letter-spacing:-0.01em", "22 / 28 · semibold<br>-0.01em")
         + tyr("Título de pantalla", "Computadora", "Liquidaciones", "font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em", "24 / 32 · semibold<br>-0.01em")
         + tyr("Subtítulo", "Ambos", "Pagos de esta semana", "font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em", "16 / 24 · semibold<br>-0.01em")
         + tyr("Cuerpo", "Celular", "Juan Pérez entregó su liquidación del lunes.", "font-size:15px;line-height:22px", "15 / 22 · regular")
         + tyr("Cuerpo", "Computadora", "Juan Pérez entregó su liquidación del lunes.", "font-size:14px;line-height:20px", "14 / 20 · regular")
         + tyr("Secundario", "Ambos", "Registrada por Laura Méndez a las 9:40", "font-size:13px;line-height:18px;color:var(--t2)", "13 / 18 · regular")
         + tyr("Etiqueta y encabezado de tabla", "Ambos", "Monto", "font-size:12px;line-height:16px;font-weight:500;color:var(--t2)", "12 / 16 · medium")
         + "</div>", "Inter · los títulos y subtítulos llevan -0.01em")
s3 += grp("Datos", """
<div class="data">
  <div class="dbox"><span class="anno">Monto</span><span class="big num">$1,500.00</span>
    <div class="row"><span>Formato</span><span>$ con comas y 2 decimales</span></div><div class="row"><span>Estilo</span><span>Números tabulares</span></div></div>
  <div class="dbox"><span class="anno">Fecha</span><span class="big num">13 oct 2026</span>
    <div class="row"><span>Formato</span><span>día, mes corto, año</span></div><div class="row"><span>Estilo</span><span>Números tabulares</span></div></div>
  <div class="dbox"><span class="anno">Placa</span><span class="big placa">27-ABC-4</span>
    <div class="row"><span>Formato</span><span>MAYÚSCULAS</span></div><div class="row"><span>Estilo</span><span>Medium · 0.04em</span></div></div>
  <div class="dbox"><span class="anno">Teléfono</span><span class="big num">55 1234 5678</span>
    <div class="row"><span>Formato</span><span>2 · 4 · 4 dígitos</span></div><div class="row"><span>Estilo</span><span>Números tabulares</span></div></div>
</div>""", "en la app van al tamaño del texto que los rodea")
s3 += grp("Números alineados en tabla", """
<div class="cols">
  <div class="mini"><table><thead><tr><th>Fecha</th><th>Placa</th><th class="r">Monto</th></tr></thead><tbody>
    <tr><td class="num">13 oct 2026</td><td class="placa">27-ABC-4</td><td class="num r">$1,500.00</td></tr>
    <tr><td class="num">12 oct 2026</td><td class="placa">14-MNR-2</td><td class="num r">$850.00</td></tr>
    <tr><td class="num">11 oct 2026</td><td class="placa">09-PLQ-5</td><td class="num r">$12,300.50</td></tr>
  </tbody></table></div>
  <div class="mini" style="padding:16px;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:18px;color:var(--t2)">
    <b style="font-size:14px;line-height:20px;color:var(--t1);font-weight:500">Reglas</b>
    <p>Los montos se alinean a la derecha para comparar pesos con pesos.</p>
    <p>Filas de 44 px y encabezado de 12/16 medium en texto secundario.</p>
    <p>La jerarquía sale del tamaño y el peso. El color queda para estados y para la acción principal.</p>
  </div>
</div>""")

# ---------- 4 · Espacios ----------
scale = [(4, "Entre icono y texto pequeño"), (8, "Entre icono y texto, etiqueta y campo"), (12, "Dentro de filas y tarjetas"),
         (16, "Margen lateral en celular, relleno de tarjetas"), (24, "Entre grupos de una pantalla"),
         (32, "Margen lateral en computadora"), (48, "Entre secciones grandes")]
s4 = grp("Escala", '<div class="sp">' + "".join(
    f'<div class="sp-i"><div class="sp-blk" style="width:{v}px;height:{v}px"></div><div class="sp-l"><b>{v} px</b><span>{u}</span></div></div>'
    for v, u in scale) + "</div>", "solo estos siete valores")
s4 += grp("Medidas fijas", """
<div class="rules3">
  <div class="mrule"><div class="gut"><i style="left:0;width:16px;border-right-width:1px"></i><i style="right:0;width:16px;border-left-width:1px"></i><div class="c" style="left:16px;right:16px"></div></div>
    <b>Margen lateral en celular · 16 px</b><p>El contenido nunca toca el borde de la pantalla.</p></div>
  <div class="mrule"><div class="gut"><i style="left:0;width:32px;border-right-width:1px"></i><i style="right:0;width:32px;border-left-width:1px"></i><div class="c" style="left:32px;right:32px"></div></div>
    <b>Margen lateral en computadora · 32 px</b><p>Se mide desde el borde del menú lateral.</p></div>
  <div class="mrule"><div class="gut" style="display:flex;align-items:center;padding:0 12px;gap:12px"><span class="sp-blk" style="width:44px;height:44px;flex-shrink:0"></span><span class="anno">Filas de tabla 44 px<br>Áreas táctiles mínimo 44 × 44 px</span></div>
    <b>Alto mínimo · 44 px</b><p>Botones, campos, filas y cualquier cosa que se toque.</p></div>
</div>""")

# ---------- 5 · Bordes y sombras ----------
s5 = grp("Radios", """
<div class="radii">
  <div class="rd"><i style="border-top-left-radius:6px"></i><span class="anno">6 px · botones, campos y etiquetas</span></div>
  <div class="rd"><i style="border-top-left-radius:8px"></i><span class="anno">8 px · tarjetas y ventanas</span></div>
</div>""")
s5 += grp("Ejemplos", f"""
<div class="bs">
  <div class="bs-c"><span class="cap">Tarjeta</span>
    <div class="card"><div class="card-h"><span class="card-t placa">27-ABC-4</span><span class="tag alta"><span class="dot"></span>Alta</span></div>
      <dl class="dl"><dt>Chofer</dt><dd>Juan Pérez</dd><dt>Teléfono</dt><dd class="num">55 1234 5678</dd><dt>Última liquidación</dt><dd class="num">$1,500.00 · 13 oct 2026</dd></dl></div>
    <div class="anno"><span>Fondo #FFFFFF</span><span>Borde 1 px #E7E5E4</span><span>Radio 8</span><span>Sin sombra</span><span>Relleno 16</span></div></div>
  <div class="bs-c"><span class="cap">Botones</span>
    <div class="btns"><button class="b pri">{ic("plus")}Registrar liquidación</button><button class="b pri h">Hover</button></div>
    <div class="btns"><button class="b">{ic("pencil")}Corregir</button><button class="b dng">Dar de baja</button><button class="b ghost">Olvidé mi contraseña</button></div>
    <div class="anno"><span>Alto 44</span><span>Radio 6</span><span>Principal ocre con texto blanco semibold</span><span>Secundario blanco con borde #D6D3D1</span><span>Peligro #B91C1C</span></div></div>
  <div class="bs-c"><span class="cap">Campo</span>
    <div class="fld"><label>Monto</label><div class="inp ph">$0.00</div><span class="help">Escribe el monto en pesos</span></div>
    <div class="fld"><label>Placa</label><div class="inp f"><span class="placa">27-ABC-4</span></div></div>
    <div class="fld"><label>Teléfono</label><div class="inp e"><span class="num">55 1234</span></div><span class="help e">Escribe los 10 dígitos del teléfono</span></div>
    <div class="anno"><span>Alto 44</span><span>Radio 6</span><span>Borde #D6D3D1</span><span>Foco: borde ocre + halo 3 px #FDF3EA</span><span>Error: borde #B91C1C</span></div></div>
  <div class="bs-c"><span class="cap">Etiquetas</span>
    <div class="tags"><span class="tag alta"><span class="dot"></span>Alta</span><span class="tag baja"><span class="dot"></span>Baja</span><span class="tag aviso">Sin chofer</span><span class="tag aviso">Sin moto</span><span class="tag ger">Gerente</span><span class="tag ayu">Ayudante</span></div>
    <div class="anno"><span>Alto 24</span><span>Radio 6</span><span>12/16 medium</span><span>Relleno 8 a los lados</span><span>Sin borde</span></div></div>
</div>""")
s5 += grp("Sombra", f"""
<div class="bs">
  <div class="bs-c" style="align-items:flex-start"><span class="cap">Menú desplegable</span>
    <div class="menu"><div class="h">{ic("pencil")}Corregir datos</div><div>{ic("phone")}Llamar al chofer</div></div>
    <div class="anno"><span>0 4px 16px rgba(28,25,23,0.08)</span><span>Radio 8</span><span>Borde 1 px</span></div></div>
  <div class="bs-c"><span class="cap">Ventana</span>
    <div class="modal"><h4>¿Dar de baja a Sofía Torres?</h4><p>Ya no podrá entrar al CRM.</p><div class="btns"><button class="b">Cancelar</button><button class="b dng">Dar de baja</button></div></div>
    <div class="anno"><span>Misma sombra</span><span>Radio 8</span><span>Relleno 24</span><span>Solo menús y ventanas llevan sombra</span></div></div>
</div>""")

# ---------- 6 · Iconos ----------
icons = [("bike", "Moto"), ("user", "Chofer"), ("users", "Usuarios"), ("receipt", "Liquidación"), ("landmark", "Financiamiento"),
         ("search", "Buscar"), ("plus", "Agregar"), ("pencil", "Corregir"), ("arrow-left", "Regresar"), ("phone", "Teléfono"),
         ("log-out", "Cerrar sesión")]
s6 = grp("Los 11 iconos", '<div class="icg">' + "".join(
    f'<div class="icc"><span class="ib">{ic(k)}</span><div><b>{n}</b><span>{k}</span></div></div>' for k, n in icons)
    + f'<div class="icc extra"><span class="ib">{ic("settings")}</span><div><b>Administración</b><span>settings · solo barra inferior</span></div></div>'
    + "</div>", "Lucide · 20 px · trazo 1.5")
s6 += grp("Color", f"""
<div class="icstates">
  <div>{ic("bike")}<span>Normal · color del texto</span></div>
  <div style="color:var(--t2)">{ic("bike")}<span>Inactivo · #57534E</span></div>
  <div><span style="color:var(--acc);display:flex">{ic("bike")}</span><span>Opción activa · ocre</span></div>
  <div><span style="color:var(--err);display:flex">{ic("log-out")}</span><span>Acción peligrosa · #B91C1C</span></div>
</div>""")

# ---------- 7 · Tono ----------
s7 = grp("Cómo escribimos", """
<div class="princ">
  <div class="pr"><b>Claro y corto</b><p>Una idea por frase. Si cabe en cinco palabras, no uses diez.</p></div>
  <div class="pr"><b>Palabras de la flotilla</b><p>Moto, chofer, liquidación, placa. Nada de «registro», «entidad» o «usuario final».</p></div>
  <div class="pr"><b>Di qué pasó y qué hacer</b><p>En errores, explica el problema y el siguiente paso. Sin códigos.</p></div>
  <div class="pr"><b>De tú y sin culpar</b><p>«Escribe el monto», no «El usuario ingresó un monto inválido».</p></div>
</div>""")


def tcard(ok, ctx, scene, why):
    v = (f'<span class="verd y">{ic("check")}Así sí</span>' if ok else f'<span class="verd n">{ic("x")}Evita</span>')
    return f'<div class="tc"><div class="tc-h"><span class="cap">{ctx}</span>{v}</div><div class="tc-s">{scene}</div><div class="tc-w">{why}</div></div>'


s7 += grp("Ejemplos correctos", '<div class="tone">'
          + tcard(True, "Aviso al guardar", f'<div class="toast">{ic("circle-check")}Liquidación registrada</div>',
                  "Nombra lo que se guardó con la palabra que el equipo usa.")
          + tcard(True, "Búsqueda sin resultados", f'<div class="empty"><span class="bub">{ic("search")}</span><b>No encontramos motos con esa placa</b><p>Revisa la placa o busca por chofer.</p></div>',
                  "Dice qué se buscó y qué intentar después.")
          + tcard(True, "Confirmar una baja", '<div class="modal" style="box-shadow:none"><h4>¿Dar de baja a Sofía Torres?</h4><p>Ya no podrá entrar al CRM.</p><div class="btns"><button class="b">Cancelar</button><button class="b dng">Dar de baja</button></div></div>',
                  "Pregunta con el nombre de la persona y explica la consecuencia. El botón repite la acción.")
          + tcard(True, "Ayuda bajo un campo", '<div class="fld" style="width:100%;max-width:320px"><label>Monto</label><div class="inp ph">$0.00</div><span class="help">Escribe el monto en pesos</span></div>',
                  "Instrucción directa, de tú, en una línea.")
          + "</div>")
s7 += grp("Ejemplos a evitar", '<div class="tone">'
          + '<div class="tc"><div class="tc-h"><span class="cap">Error del sistema</span><span class="verd n">' + ic("x") + 'Evita</span></div>'
          + f'<div class="tc-s"><div class="bad">{ic("x")}<span class="strike">Error 500</span></div></div>'
          + '<div class="alt"><span>Mejor</span><b>No pudimos guardar la liquidación. Revisa tu internet e intenta de nuevo.</b></div>'
          + '<div class="tc-w">Un código no le dice a nadie qué pasó ni qué hacer.</div></div>'
          + '<div class="tc"><div class="tc-h"><span class="cap">Aviso al guardar</span><span class="verd n">' + ic("x") + 'Evita</span></div>'
          + f'<div class="tc-s"><div class="bad">{ic("x")}<span class="strike">Registro insertado correctamente</span></div></div>'
          + '<div class="alt"><span>Mejor</span><b>Liquidación registrada</b></div>'
          + '<div class="tc-w">«Registro» e «insertado» son palabras de base de datos. Di qué se guardó.</div></div>'
          + "</div>")

# ---------- 8 · Marco de la app ----------
def bnav(active):
    items = [("Liquidaciones", "receipt"), ("Motos", "bike"), ("Choferes", "user"), ("Administración", "settings")]
    out = '<nav class="bnav" aria-label="Navegación principal">'
    for lab, icn in items:
        on = lab == active
        out += f'<a class="bn{" on" if on else ""}" href="#marco"{" aria-current=\"page\"" if on else ""}><span class="pill">{ic(icn)}</span>{lab}</a>'
    return out + "</nav>"


def si(lab, icn, on=False):
    return f'<a class="si{" on" if on else ""}" href="#marco">{ic(icn)}{lab}</a>'


phone = f"""
<div class="dev phone">
  <div class="status"><span class="num">9:41</span><i><u></u><u></u><u style="width:24px"></u></i></div>
  <header class="tbar"><h4>Liquidaciones</h4></header>
  <div class="content">
    <div class="guide" style="left:16px;right:16px;top:16px;bottom:16px">Contenido</div>
    <span class="mtag" style="left:1px;top:50%">16</span><span class="mtag" style="right:1px;top:50%">16</span>
  </div>
  {bnav("Liquidaciones")}
  <div class="home"><i></i></div>
</div>"""

pc = f"""
<div class="dev pcbox"><div class="pcscale"><div class="pc">
  <aside class="side">
    <div class="logo" style="display:flex">{ic("bike")}CRM-MotoT</div>
    <div class="sgrp"><div class="slbl">Operación</div>{si("Liquidaciones","receipt",True)}{si("Motos","bike")}{si("Choferes","user")}</div>
    <div class="sgrp"><div class="slbl">Administración</div>{si("Usuarios","users")}{si("Financiamiento","landmark")}</div>
    <div class="sfoot"><div class="who"><b>Laura Méndez</b><span class="tag ger">Gerente</span></div>{si("Cerrar sesión","log-out")}</div>
  </aside>
  <main class="main">
    <div class="guide" style="left:32px;right:32px;top:32px;bottom:32px;font-size:16px;line-height:24px">Contenido · 1200 px de ancho sin el menú</div>
    <span class="mtag" style="left:6px;top:50%;font-size:16px;line-height:20px">32</span><span class="mtag" style="right:6px;top:50%;font-size:16px;line-height:20px">32</span>
  </main>
</div></div></div>"""

spec_cel = """<div class="spec"><span class="cap">Celular</span><dl>
        <dt>Barra de estado</dt><dd>Del teléfono, no se diseña</dd>
        <dt>Barra superior</dt><dd>56 px · blanco · borde inferior 1 px · título 22/28 semibold</dd>
        <dt>Barra inferior</dt><dd>64 px + 8 px · 4 opciones de 1/4 del ancho · texto 12/16</dd>
        <dt>Opción activa</dt><dd>Icono ocre sobre pastilla #E7E5E4 de 56 × 28 · texto #1C1917 semibold</dd>
        <dt>Opción inactiva</dt><dd>Icono y texto #57534E</dd>
        <dt>Administración</dt><dd>Abre una hoja con Usuarios y, para el Gerente, Financiamiento</dd>
        <dt>Margen</dt><dd>16 px a los lados</dd></dl></div>"""
spec_pc = """<div class="spec"><span class="cap">Computadora</span><dl>
        <dt>Menú lateral</dt><dd>240 px fijo · #F5F5F4 · borde derecho 1 px · logo en 64 px</dd>
        <dt>Secciones</dt><dd>Operación: Liquidaciones, Motos, Choferes · Administración: Usuarios, Financiamiento</dd>
        <dt>Opciones</dt><dd>40 px de alto · radio 6 · títulos de sección 12/16 medium #78716C</dd>
        <dt>Opción activa</dt><dd>Fondo #E7E5E4 · texto #1C1917 semibold · icono ocre</dd>
        <dt>Pie</dt><dd>Nombre, etiqueta de rol y Cerrar sesión</dd>
        <dt>Ayudante</dt><dd>No ve Financiamiento</dd>
        <dt>Margen</dt><dd>32 px a los lados del contenido</dd></dl></div>"""
s8 = (grp("Celular", f'<div class="frames"><div>{phone}</div>{spec_cel}</div>', "390 × 844 px · se diseña primero")
      + grp("Computadora", f'{pc}', "1440 × 900 px · mostrado al 70 %")
      + f'<div style="max-width:620px">{spec_pc}</div>')

SECS = [
    ("logo", "Logotipo", "Texto «CRM-MotoT» con el icono bike en ocre. Es el único lugar donde el ocre es decorativo.", s1),
    ("paleta", "Paleta", "Base neutra y cálida. El ocre marca la acción principal, el foco y la opción activa; los estados usan texto de color sobre fondo suave.", s2),
    ("tipografia", "Tipografía", "Inter en cuatro tamaños y tres pesos. La jerarquía sale del tamaño y del peso, no del color.", s3),
    ("espacios", "Espacios", "Escala de 4 a 48 px. Todo margen, relleno y separación sale de aquí.", s4),
    ("bordes", "Bordes y sombras", "Bordes de 1 px en lugar de sombras. La sombra se reserva para lo que flota: menús y ventanas.", s5),
    ("iconos", "Iconos", "Lucide de línea fina. Siempre acompañados de texto, salvo en botones con nombre para lectores de pantalla.", s6),
    ("tono", "Tono de los textos", "Para personas no técnicas: claro, corto y con las palabras de la flotilla.", s7),
    ("marco", "Marco de la app", "Estructura vacía que comparten todas las pantallas. Se muestra la vista del Gerente con Liquidaciones activa.", s8),
]

index = '<nav class="index" aria-label="Secciones">' + "".join(
    f'<a href="#{sid}"><span>{i}</span>{t}</a>' for i, (sid, t, _, _) in enumerate(SECS, 1)) + "</nav>"

head = f"""
<header class="top">
  <div>
    {logo("md")}
    <h1 style="margin-top:24px">Design system de CRM-MotoT</h1>
    <p class="lead">Referencia para diseñar las pantallas de la flotilla: colores, letras, espacios, bordes, iconos, tono y el marco de la app en celular y computadora.</p>
    <div class="meta"><div><b>Celular</b>390 × 844 · primero</div><div><b>Computadora</b>1440 × 900</div><div><b>Tema</b>Solo modo claro</div><div><b>Versión</b>14 oct 2026</div></div>
  </div>
  <div class="notes"><span class="cap">Supuestos de esta hoja</span><ul>
    <li>Logo sobre oscuro: texto #FAFAF9 (el fondo de la app), icono en el mismo ocre.</li>
    <li>Administración en la barra inferior usa el icono settings, como en la hoja de componentes.</li>
    <li>El aviso flotante «Liquidación registrada» es oscuro #1C1917 con icono verde claro, para que se lea sobre cualquier pantalla.</li>
    <li>Etiquetas de 24 px de alto; botones, campos y filas de 44 px.</li>
    <li>Texto blanco sobre #C25A12 da 4.4:1; se usa solo en semibold de 14 px o más.</li>
  </ul></div>
</header>"""

html = f"""<title>Design system CRM-MotoT</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap">
<style>{CSS}</style>
{SPRITE}
<div class="scroll"><div class="sheet">
{head}
{index}
{"".join(sec(i, sid, t, d, b) for i, (sid, t, d, b) in enumerate(SECS, 1))}
</div></div>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("ok", OUT, len(html))

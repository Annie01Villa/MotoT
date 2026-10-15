#!/usr/bin/env python3
"""Genera la hoja de componentes de CRM-MotoT (HTML estático)."""
import sys

OUT = sys.argv[1]

# ---------- Iconos Lucide (trazo 1.5, 20 px) ----------
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
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "circle-x": '<circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/>',
    "eye": '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    "eye-off": '<path d="M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49"/><path d="M14.084 14.158a3 3 0 0 1-4.242-4.242"/><path d="M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143"/><path d="m2 2 20 20"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "calendar": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    "chevron-right": '<path d="m9 18 6-6-6-6"/>',
    "chevron-left": '<path d="m15 18-6-6 6-6"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "circle-check": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "circle-alert": '<circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "triangle-alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "loader": '<path d="M21 12a9 9 0 1 1-6.219-8.56"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
    "map-pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
}


def ic(name, cls="", label=None):
    a = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<svg class="ic {cls}"{a}><use href="#i-{name}"/></svg>'


SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + "</svg>"

CSS = r"""
/* Hoja de 1440 px. Retícula de 4 px. Cada componente: nombre, ficha técnica y sus estados en fila. */
:root{
  --acc:#C25A12; --acc-h:#A84B0C; --acc-p:#8F3F0A; --acc-s:#FDF3EA;
  --bg:#FAFAF9; --sf:#FFFFFF; --side:#F5F5F4; --bd:#E7E5E4; --bd-f:#D6D3D1; --hov:#F5F5F4; --sb-hov:#EEEDEC;
  --t1:#1C1917; --t2:#57534E; --t3:#78716C;
  --ok:#15803D; --ok-s:#F0FDF4; --err:#B91C1C; --err-h:#991B1B; --err-p:#7F1D1D; --err-s:#FEF2F2;
  --warn:#854D0E; --warn-s:#FEF9C3;
  --scrim:rgba(28,25,23,.40); --shadow:0 4px 16px rgba(28,25,23,.08);
  --font:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--t1);font-family:var(--font);font-size:14px;line-height:20px;-webkit-font-smoothing:antialiased;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0}
h1,h2,h3,h4,p,dl,dd,ul{margin:0;padding:0}
ul{list-style:none}
button,input{font-family:inherit}
.ic{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0}
.ic.s16{width:16px;height:16px}
.num{font-variant-numeric:tabular-nums}
.placa{text-transform:uppercase;font-weight:500;letter-spacing:.04em;font-variant-numeric:tabular-nums}
.spin{animation:girar .8s linear infinite}
@keyframes girar{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.spin{animation:none}}
:focus-visible{outline:none;box-shadow:0 0 0 2px var(--sf),0 0 0 4px var(--acc)}

/* ---------- Hoja ---------- */
.scroll{overflow-x:auto;margin-inline:calc(-1 * max(16px,env(safe-area-inset-left,0px)))}
.sheet{width:1440px;margin:0 auto;padding:48px}
.top{display:grid;grid-template-columns:1fr 420px;gap:48px;padding-bottom:32px}
.top h1{font-size:32px;line-height:40px;font-weight:600;letter-spacing:-0.01em}
.top .lead{margin-top:8px;color:var(--t2);font-size:15px;line-height:22px;max-width:640px}
.swatches{display:flex;flex-wrap:wrap;gap:8px;margin-top:24px}
.sw{display:flex;align-items:center;gap:8px;padding:4px 8px 4px 4px;border:1px solid var(--bd);border-radius:6px;background:var(--sf);font-size:12px;line-height:16px;color:var(--t2)}
.sw i{width:20px;height:20px;border-radius:4px;border:1px solid rgba(28,25,23,.08)}
.sw b{font-weight:500;color:var(--t1)}
.notes{background:var(--sf);border:1px solid var(--bd);border-radius:8px;padding:16px}
.notes h2{font-size:12px;line-height:16px;font-weight:500;color:var(--t2);text-transform:uppercase;letter-spacing:.04em;margin-bottom:8px}
.notes li{font-size:13px;line-height:18px;color:var(--t2);padding-left:12px;position:relative}
.notes li+li{margin-top:6px}
.notes li::before{content:"";position:absolute;left:0;top:8px;width:4px;height:4px;border-radius:2px;background:var(--bd-f)}
.index{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;flex-wrap:wrap;gap:4px;padding:12px 0;background:var(--bg);border-bottom:1px solid var(--bd)}
.index a{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 10px;border-radius:6px;color:var(--t2);text-decoration:none;font-size:13px;line-height:18px}
.index a:hover{background:var(--hov);color:var(--t1)}
.index a span{color:var(--t3);font-variant-numeric:tabular-nums}
.sec{padding-top:48px;scroll-margin-top:64px}
.sec+.sec{margin-top:16px;border-top:1px solid var(--bd)}
.sec-h{display:flex;align-items:baseline;gap:12px;margin-bottom:8px}
.sec-h .n{font-size:13px;line-height:18px;color:var(--t3);font-variant-numeric:tabular-nums;width:24px}
.sec-h h2{font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em}
.sec-d{margin-left:36px;margin-bottom:32px;color:var(--t2);max-width:760px}
.comp{margin-left:36px;margin-bottom:48px}
.comp-h{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 12px;margin-bottom:4px}
.comp-h h3{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em}
.cid{font-size:12px;line-height:16px;color:var(--t3);border:1px solid var(--bd);border-radius:4px;padding:1px 6px;background:var(--sf)}
.dev{font-size:12px;line-height:16px;font-weight:500;color:var(--t2);background:var(--side);border-radius:4px;padding:2px 6px}
.spec{font-size:13px;line-height:18px;color:var(--t3);margin-bottom:16px}
.states{display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start}
.st{display:flex;flex-direction:column;align-items:flex-start;gap:8px;min-width:0}
.cap{font-size:12px;line-height:16px;font-weight:500;color:var(--t2)}
.cap em{font-style:normal;color:var(--t3);font-weight:400}
.frame{position:relative;background:var(--sf);border:1px solid var(--bd);border-radius:8px;overflow:hidden}
.frame.app{background:var(--bg)}
.w390{width:390px}

/* ---------- Botones ---------- */
.b{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:44px;padding:0 16px;border:1px solid transparent;border-radius:6px;font-size:14px;line-height:20px;font-weight:600;cursor:pointer;white-space:nowrap;text-decoration:none}
.b.cel{height:48px;font-size:15px;line-height:22px}
.b.full{width:100%}
.b-pri{background:var(--acc);color:#FFFFFF}
.b-pri:hover,.b-pri.h{background:var(--acc-h)}
.b-pri:active,.b-pri.p{background:var(--acc-p)}
.b-sec{background:var(--sf);border-color:var(--bd-f);color:var(--t1)}
.b-sec:hover,.b-sec.h{background:var(--hov)}
.b-sec:active,.b-sec.p{background:var(--bd)}
.b-dan{background:var(--err);color:#FFFFFF}
.b-dan:hover,.b-dan.h{background:var(--err-h)}
.b-dan:active,.b-dan.p{background:var(--err-p)}
.b-ico{width:44px;padding:0;background:transparent;color:var(--t2)}
.b-ico:hover,.b-ico.h{background:var(--hov);color:var(--t1)}
.b-ico:active,.b-ico.p{background:var(--bd);color:var(--t1)}
.b.f{box-shadow:0 0 0 2px var(--sf),0 0 0 4px var(--acc)}
.b:disabled{background:var(--side);border-color:var(--bd);color:var(--t3);cursor:not-allowed}
.b-ico:disabled{background:transparent;border-color:transparent;color:var(--bd-f)}
.b.load{cursor:progress}
.fab{display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:0;border-radius:6px;background:var(--acc);color:#FFFFFF;box-shadow:var(--shadow);cursor:pointer}
.fab .ic{width:24px;height:24px}
.fab:hover,.fab.h{background:var(--acc-h)}
.fab:active,.fab.p{background:var(--acc-p)}
.lnk{color:var(--acc);font-weight:500;text-decoration:none}
.lnk:hover{color:var(--acc-h);text-decoration:underline}
.bgrid{display:grid;grid-template-columns:120px repeat(6,160px);gap:16px 24px;align-items:center}
.bgrid .rh{font-size:13px;line-height:18px;font-weight:500;color:var(--t1)}
.bgrid .ch{font-size:12px;line-height:16px;font-weight:500;color:var(--t2)}

/* ---------- Etiquetas ---------- */
.tag{display:inline-flex;align-items:center;height:24px;padding:0 8px;border-radius:6px;font-size:12px;line-height:16px;font-weight:500;white-space:nowrap}
.tag.ger{color:var(--acc-h);background:var(--acc-s)}
.tag.ayu{color:var(--t2);background:var(--side)}
.tag.alta{color:var(--ok);background:var(--ok-s)}
.tag.baja{color:var(--err);background:var(--err-s)}
.tag.warn{color:var(--warn);background:var(--warn-s)}

/* ---------- Campos ---------- */
.fld{display:flex;flex-direction:column;gap:8px;min-width:0}
.fld label,.fld .fl{font-size:14px;line-height:20px;font-weight:500;color:var(--t1)}
.inb{display:flex;align-items:center;gap:8px;height:44px;padding:0 12px;border:1px solid var(--bd-f);border-radius:6px;background:var(--sf);color:var(--t1)}
.inb input{flex:1;min-width:0;height:100%;border:0;padding:0;background:transparent;color:inherit;font-size:14px;line-height:20px;outline:none}
.inb input::placeholder{color:var(--t3)}
.inb .pre{color:var(--t2);font-variant-numeric:tabular-nums}
.inb .lead{color:var(--t3)}
.inb .tb{display:inline-flex;align-items:center;justify-content:center;width:44px;height:42px;margin-right:-12px;border:0;border-radius:0 6px 6px 0;background:transparent;color:var(--t2);cursor:pointer}
.inb .tb:hover{color:var(--t1)}
.inb:focus-within,.inb.f{border-color:var(--acc);box-shadow:0 0 0 3px var(--acc-s)}
.inb.e{border-color:var(--err)}
.inb.e:focus-within{box-shadow:0 0 0 3px var(--err-s)}
.inb.d{background:var(--bg);border-color:var(--bd);color:var(--t2)}
.inb.d .tb,.inb.d .pre,.inb.d .lead{color:var(--t3)}
.fld.dis label{color:var(--t2)}
.help{font-size:13px;line-height:18px;color:var(--t3)}
.ferr{display:flex;gap:6px;align-items:flex-start;font-size:13px;line-height:18px;color:var(--err)}
.ferr .ic{margin-top:1px}
.cel .inb{height:48px}
.cel .inb input{font-size:15px;line-height:22px}
.cel .inb .tb{height:46px;width:48px}
.fgrid{display:grid;grid-template-columns:150px repeat(5,200px);gap:24px;align-items:start}
.fgrid .rh{font-size:13px;line-height:18px;font-weight:500;padding-top:30px}
.fgrid .ch{font-size:12px;line-height:16px;font-weight:500;color:var(--t2)}

/* ---------- Buscador ---------- */
.srch{display:flex;align-items:center;gap:8px;height:44px;padding:0 0 0 12px;border:1px solid var(--bd-f);border-radius:6px;background:var(--sf);color:var(--t3)}
.srch input{flex:1;min-width:0;height:100%;border:0;background:transparent;color:var(--t1);font-size:14px;outline:none;padding:0}
.srch input::placeholder{color:var(--t3)}
.srch .clr{display:inline-flex;align-items:center;justify-content:center;width:44px;height:42px;border:0;border-radius:0 6px 6px 0;background:transparent;color:var(--t3);cursor:pointer}
.srch .clr:hover,.srch .clr.h{color:var(--t1)}
.srch .clr.h .ic{background:var(--hov);border-radius:10px}
.srch:focus-within,.srch.f{border-color:var(--acc);box-shadow:0 0 0 3px var(--acc-s)}
.srch.f .ic:first-child{color:var(--t2)}
.srch.cel{height:48px}
.srch.cel input{font-size:15px}
.srch.cel .clr{width:48px;height:46px}

/* ---------- Navegación ---------- */
.bnav{display:flex;background:var(--sf);border-top:1px solid var(--bd);padding:0 4px 8px}
.bn{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;min-height:64px;padding-top:8px;color:var(--t2);font-size:12px;line-height:16px;font-weight:500;text-decoration:none;border-radius:6px}
.bn .pill{display:flex;align-items:center;justify-content:center;width:56px;height:28px;border-radius:6px}
.bn.on{color:var(--t1);font-weight:600}
.bn.on .pill{background:var(--bd)}
.bn.on .ic{color:var(--acc)}
.bn.p .pill{background:var(--hov)}
.tbar{display:flex;align-items:center;gap:4px;height:56px;padding:0 16px;background:var(--sf);border-bottom:1px solid var(--bd)}
.tbar.back{padding-left:4px}
.tbar h4{flex:1;min-width:0;font-size:22px;line-height:28px;font-weight:600;letter-spacing:-0.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tbar .b-ico{width:44px;height:44px}
.sheetbox{background:var(--sf);border-radius:8px 8px 0 0;border-top:1px solid var(--bd)}
.handle{width:32px;height:4px;border-radius:2px;background:var(--bd-f);margin:8px auto 4px}
.sh-t{display:flex;align-items:center;justify-content:space-between;padding:4px 4px 4px 16px}
.sh-t h4{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em}
.sh-i{display:flex;align-items:center;gap:12px;min-height:56px;padding:0 16px;font-size:15px;line-height:22px;color:var(--t1);border-top:1px solid var(--bd)}
.sh-i .ic:first-child{color:var(--t2)}
.sh-i .grow{flex:1;min-width:0}
.sh-i small{display:block;font-size:13px;line-height:18px;color:var(--t3)}
.sh-i>.ic:last-child{color:var(--t3)}
.scrim{position:absolute;inset:0;background:var(--scrim)}
.stub{padding:16px;display:flex;flex-direction:column;gap:12px}
.stub i{display:block;height:64px;border:1px solid var(--bd);border-radius:8px;background:var(--sf)}
.side{width:240px;height:600px;display:flex;flex-direction:column;background:var(--side);border-right:1px solid var(--bd)}
.logo{display:flex;align-items:center;gap:8px;height:64px;padding:0 20px;font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em}
.logo .ic{color:var(--acc)}
.sgrp{padding:8px 8px 0}
.sgrp+.sgrp{padding-top:16px}
.slbl{padding:0 12px 4px;font-size:12px;line-height:16px;font-weight:500;color:var(--t3)}
.si{display:flex;align-items:center;gap:12px;height:40px;padding:0 12px;border-radius:6px;color:var(--t2);text-decoration:none;font-size:14px;line-height:20px}
.si:hover,.si.h{background:var(--sb-hov);color:var(--t1)}
.si.on{background:var(--bd);color:var(--t1);font-weight:600}
.si.on .ic{color:var(--acc)}
.sfoot{margin-top:auto;border-top:1px solid var(--bd);padding:12px 8px 8px}
.who{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:4px 12px 8px}
.who b{font-weight:500;font-size:14px;line-height:20px}

/* ---------- Listas ---------- */
.lc{display:flex;align-items:center;gap:12px;width:358px;min-height:72px;padding:12px 12px 12px 16px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;cursor:pointer}
.lc:hover,.lc.h{background:var(--hov)}
.lc:active,.lc.p{background:var(--bd);border-color:var(--bd-f)}
.lc .grow{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.lc .t{font-size:15px;line-height:22px;font-weight:500}
.lc .s{font-size:13px;line-height:18px;color:var(--t2);display:flex;align-items:center;gap:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lc>.ic{color:var(--t3)}
.lc .amt{font-size:15px;line-height:22px;font-weight:600;font-variant-numeric:tabular-nums}
.lc .tags{display:flex;gap:4px}
.lgrid{display:grid;grid-template-columns:96px repeat(3,358px);gap:16px 24px;align-items:center}
.lgrid .rh{font-size:13px;line-height:18px;font-weight:500}
.lgrid .ch{font-size:12px;line-height:16px;font-weight:500;color:var(--t2)}
.trow{display:flex;gap:16px;align-items:stretch}
.tlab{width:112px;flex-shrink:0;display:flex;flex-direction:column}
.tlab span{display:flex;align-items:center;height:44px;font-size:12px;line-height:16px;font-weight:500;color:var(--t2)}
.tlab span:first-child{height:41px}
.tbl{width:1136px;border:1px solid var(--bd);border-radius:8px;background:var(--sf);overflow:hidden}
.tbl table{width:100%;border-collapse:collapse;table-layout:fixed}
.tbl th{height:40px;padding:0 16px;text-align:left;font-size:12px;line-height:16px;font-weight:500;color:var(--t2);border-bottom:1px solid var(--bd)}
.tbl td{height:44px;padding:0 16px;font-size:14px;line-height:20px;border-bottom:1px solid var(--bd);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tbl tr:last-child td{border-bottom:0}
.tbl tbody tr{cursor:pointer}
.tbl tbody tr:hover,.tbl tr.h{background:var(--hov)}
.tbl tbody tr:active,.tbl tr.p{background:var(--bd)}
.tbl .r{text-align:right}
.tbl .sec2{color:var(--t2)}
.tbl td.go{color:var(--t3);text-align:right;padding-right:12px}
.tbl td.go .ic{vertical-align:middle}

/* ---------- Vacío ---------- */
.empty{display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px;padding:48px 24px}
.empty .bub{display:flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:8px;background:var(--side);color:var(--t2);margin-bottom:8px}
.empty h4{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em;text-wrap:balance}
.empty p{color:var(--t2);max-width:300px}
.empty .b{margin-top:16px}

/* ---------- Selector ---------- */
.menu{background:var(--sf);border:1px solid var(--bd);border-radius:8px;box-shadow:var(--shadow);overflow:hidden}
.menu .msr{padding:8px;border-bottom:1px solid var(--bd)}
.opt{display:flex;align-items:center;gap:12px;min-height:52px;padding:8px 12px;cursor:pointer}
.opt .grow{flex:1;min-width:0}
.opt .t{font-size:14px;line-height:20px}
.opt .s{font-size:13px;line-height:18px;color:var(--t2)}
.opt:hover,.opt.h{background:var(--hov)}
.opt.sel .t{font-weight:600}
.opt .ck{width:20px;color:var(--acc)}
.opts{padding:4px}
.opts .opt{border-radius:6px}
.cel .opt{min-height:60px;padding:8px 16px}
.cel .opt .t{font-size:15px;line-height:22px}
.selbox .inb{cursor:pointer}
.selbox .val{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.selbox .ph{flex:1;color:var(--t3)}
.selbox .chev{color:var(--t2)}

/* ---------- Rol ---------- */
.rol{display:flex;gap:12px;align-items:flex-start;padding:16px;border:1px solid var(--bd-f);border-radius:8px;background:var(--sf);cursor:pointer;width:280px}
.rol .rd{flex-shrink:0;width:20px;height:20px;border-radius:10px;border:1.5px solid var(--bd-f);background:var(--sf);display:flex;align-items:center;justify-content:center;margin-top:0}
.rol .t{font-size:14px;line-height:20px;font-weight:600}
.rol .s{font-size:13px;line-height:18px;color:var(--t2);margin-top:2px}
.rol:hover,.rol.h{background:var(--hov)}
.rol.on{border-color:var(--acc);box-shadow:inset 0 0 0 1px var(--acc)}
.rol.on:hover{background:var(--sf)}
.rol.on .rd{border-color:var(--acc)}
.rol.on .rd::after{content:"";width:10px;height:10px;border-radius:5px;background:var(--acc)}
.rol.f{box-shadow:0 0 0 2px var(--sf),0 0 0 4px var(--acc)}
.rol.d{background:var(--bg);border-color:var(--bd);cursor:not-allowed}
.rol.d .t,.rol.d .s{color:var(--t3)}
.rol.d .rd{border-color:var(--bd);background:var(--side)}

/* ---------- Detalle ---------- */
.det{background:var(--sf);border:1px solid var(--bd);border-radius:8px}
.det-h{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;padding:24px}
.det-h h4{font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em}
.det-h h4.placa{letter-spacing:.04em}
.det-h p{color:var(--t2);margin-top:4px;display:flex;align-items:center;gap:8px}
.dl{display:grid;grid-template-columns:200px 1fr;border-top:1px solid var(--bd);padding:8px 24px}
.dl dt,.dl dd{padding:10px 0;border-bottom:1px solid var(--bd);font-size:14px;line-height:20px}
.dl dt{color:var(--t2)}
.dl dt:nth-last-child(2),.dl dd:last-child{border-bottom:0}
.rel{border-top:1px solid var(--bd);padding:24px;display:flex;flex-direction:column;gap:12px}
.rel h5{font-size:12px;line-height:16px;font-weight:500;color:var(--t2);margin:0}
.rels{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.lk{display:flex;align-items:center;gap:12px;min-height:64px;padding:12px 12px 12px 16px;border:1px solid var(--bd);border-radius:8px;background:var(--sf);color:var(--t1);text-decoration:none}
.lk:hover,.lk.h{background:var(--hov)}
.lk:active,.lk.p{background:var(--bd)}
.lk .bub{display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:6px;background:var(--side);color:var(--t2)}
.lk .grow{flex:1;min-width:0}
.lk .t,.lk .s{display:block}
.lk .t{font-size:14px;line-height:20px;font-weight:500}
.lk .s{font-size:13px;line-height:18px;color:var(--t2)}
.lk>.ic{color:var(--t3)}
.det.cel .det-h{padding:16px}
.det.cel .det-h h4{font-size:22px;line-height:28px}
.det.cel .dl{display:block;padding:0 16px}
.det.cel .dl dt{padding:12px 0 0;border:0;font-size:13px;line-height:18px}
.det.cel .dl dd{padding:2px 0 12px;font-size:15px;line-height:22px}
.det.cel .dl dd:last-child{border-bottom:0}
.det.cel .rel{padding:16px}
.det.cel .rels{grid-template-columns:1fr}
.det.cel .lk .t{font-size:15px;line-height:22px}

/* ---------- Mensajes ---------- */
.toast{display:flex;align-items:center;gap:12px;padding:8px 8px 8px 16px;min-height:52px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;box-shadow:var(--shadow)}
.toast>.ic{color:var(--ok)}
.toast .t{flex:1;font-weight:500}
.toast .b-ico{width:36px;height:36px}
.bn-msg{display:flex;align-items:flex-start;gap:12px;padding:12px 16px;border-radius:6px;border:1px solid transparent}
.bn-msg .grow{flex:1;min-width:0}
.bn-msg .t{font-weight:600}
.bn-msg .act{margin-top:4px;display:inline-block;font-weight:600;text-decoration:underline;color:inherit}
.bn-msg.err{background:var(--err-s);color:var(--err)}
.bn-msg.warn{background:var(--warn-s);color:var(--warn)}
.bn-msg.info{background:var(--sf);border-color:var(--bd);color:var(--t2)}
.bn-msg.info>.ic{color:var(--t2)}
.bn-msg.info .t{color:var(--t1)}
.dlg{background:var(--sf);border:1px solid var(--bd);border-radius:8px;box-shadow:var(--shadow);padding:24px}
.dlg h4{font-size:16px;line-height:24px;font-weight:600;letter-spacing:-0.01em;text-wrap:balance}
.dlg p{color:var(--t2);margin-top:8px}
.dlg .acts{display:flex;justify-content:flex-end;gap:8px;margin-top:24px}
.dlg.cel{padding:20px}
.dlg.cel p{font-size:15px;line-height:22px}
.dlg.cel .acts{flex-direction:column-reverse}

/* ---------- Encabezado ---------- */
.ph{display:flex;align-items:flex-end;justify-content:space-between;gap:16px}
.ph h4{font-size:24px;line-height:32px;font-weight:600;letter-spacing:-0.01em}
.ph p{font-size:13px;line-height:18px;color:var(--t2);font-variant-numeric:tabular-nums;margin-top:2px}
.ph.cel h4{font-size:22px;line-height:28px}

/* ---------- Calendario ---------- */
.cal{width:296px;padding:12px;background:var(--sf);border:1px solid var(--bd);border-radius:8px;box-shadow:var(--shadow)}
.cal-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}
.cal-h b{font-weight:600}
.cal-h .b-ico{width:36px;height:36px}
.cal-g{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;text-align:center}
.cal-g .dw{font-size:12px;line-height:16px;font-weight:500;color:var(--t3);height:28px;display:flex;align-items:center;justify-content:center}
.cal-g button{height:36px;border:0;border-radius:6px;background:transparent;color:var(--t1);font-size:14px;font-variant-numeric:tabular-nums;cursor:pointer}
.cal-g button:hover{background:var(--hov)}
.cal-g button.today{box-shadow:inset 0 0 0 1px var(--bd-f)}
.cal-g button.sel{background:var(--acc);color:#FFFFFF;font-weight:600}
.cal-g button.fut{color:var(--t3)}
"""

# ---------- helpers ----------
def comp(title, cid, spec, body, dev=None):
    d = f'<span class="dev">{dev}</span>' if dev else ""
    return (f'<div class="comp"><div class="comp-h"><h3>{title}</h3>{d}<span class="cid">{cid}</span></div>'
            f'<p class="spec">{spec}</p>{body}</div>')


def st(cap, inner, style=""):
    return f'<div class="st" style="{style}"><span class="cap">{cap}</span>{inner}</div>'


def sec(n, sid, title, desc, body):
    return (f'<section class="sec" id="{sid}"><div class="sec-h"><span class="n">{n:02d}</span><h2>{title}</h2></div>'
            f'<p class="sec-d">{desc}</p>{body}</section>')


uid = [0]
def nid(p):
    uid[0] += 1
    return f"{p}-{uid[0]}"


# ======================= 1. Navegación =======================
def bnav(active, pressed=None):
    items = [("Liquidaciones", "receipt"), ("Motos", "bike"), ("Choferes", "user"), ("Administración", "settings")]
    out = '<nav class="bnav" aria-label="Navegación principal">'
    for lab, icn in items:
        cls = " on" if lab == active else (" p" if lab == pressed else "")
        cur = ' aria-current="page"' if lab == active else ""
        out += f'<a class="bn{cls}" href="#nav"{cur}><span class="pill">{ic(icn)}</span>{lab}</a>'
    return out + "</nav>"


def admin_sheet(gerente):
    items = f'<div class="sh-i">{ic("users")}<span class="grow">Usuarios<small>{"Altas, bajas y roles" if gerente else "Consulta quién usa el CRM"}</small></span>{ic("chevron-right")}</div>'
    if gerente:
        items += f'<div class="sh-i">{ic("landmark")}<span class="grow">Financiamiento<small>Pagos de las motos a crédito</small></span>{ic("chevron-right")}</div>'
    h = 420 if gerente else 364
    return (f'<div class="frame app w390" style="height:{h}px">'
            '<div class="stub"><i></i><i></i><i></i><i></i></div><div class="scrim"></div>'
            '<div style="position:absolute;left:0;right:0;bottom:0">'
            f'<div class="sheetbox"><div class="handle"></div><div class="sh-t"><h4>Administración</h4>'
            f'<button class="b b-ico" aria-label="Cerrar">{ic("x")}</button></div>{items}</div>'
            f'{bnav("Administración")}</div></div>')


def sidebar(gerente, active, hover=None):
    def si(lab, icn):
        cls = " on" if lab == active else (" h" if lab == hover else "")
        return f'<a class="si{cls}" href="#nav">{ic(icn)}{lab}</a>'
    adm = si("Usuarios", "users") + (si("Financiamiento", "landmark") if gerente else "")
    name, tag = ("Laura Méndez", '<span class="tag ger">Gerente</span>') if gerente else ("Carlos Ramírez", '<span class="tag ayu">Ayudante</span>')
    return (f'<div class="frame" style="width:242px"><aside class="side">'
            f'<div class="logo">{ic("bike")}CRM-MotoT</div>'
            f'<div class="sgrp"><div class="slbl">Operación</div>{si("Liquidaciones","receipt")}{si("Motos","bike")}{si("Choferes","user")}</div>'
            f'<div class="sgrp"><div class="slbl">Administración</div>{adm}</div>'
            f'<div class="sfoot"><div class="who"><b>{name}</b>{tag}</div>'
            f'<a class="si" href="#nav">{ic("log-out")}Cerrar sesión</a></div></aside></div>')


def tbar(title, back=False, action=None, pressed=False):
    b = f'<button class="b b-ico{" p" if pressed else ""}" aria-label="Regresar">{ic("arrow-left")}</button>' if back else ""
    a = f'<button class="b b-ico" aria-label="{action[1]}">{ic(action[0])}</button>' if action else ""
    return f'<div class="frame w390"><header class="tbar{" back" if back else ""}">{b}<h4>{title}</h4>{a}</header></div>'


nav = (
    comp("Barra de navegación inferior", "Nav/BarraInferior", "64 px + 8 px de margen inferior · 4 opciones de 1/4 de ancho · activa: icono ocre sobre pastilla #E7E5E4 y texto #1C1917 semibold · resto #57534E",
         '<div class="states">'
         + st("Motos activa", f'<div class="frame w390">{bnav("Motos")}</div>')
         + st("Presionando Choferes", f'<div class="frame w390">{bnav("Motos", "Choferes")}</div>')
         + st("Liquidaciones activa", f'<div class="frame w390">{bnav("Liquidaciones")}</div>')
         + "</div>", "Celular")
    + comp("Hoja «Administración»", "Nav/HojaAdministracion", "Se abre al tocar Administración · hoja desde abajo, radio 8 arriba, fondo oscurecido rgba(28,25,23,0.4) · filas de 56 px · Financiamiento solo para el Gerente",
           '<div class="states">' + st("Gerente", admin_sheet(True)) + st("Ayudante <em>(sin Financiamiento)</em>", admin_sheet(False)) + "</div>", "Celular")
    + comp("Barra superior", "Nav/BarraSuperior", "56 px · fondo blanco con borde inferior de 1 px · título 22/28 semibold · botón regresar de 44 × 44 px",
           '<div class="states">'
           + st("Pantalla principal", tbar("Motos"))
           + st("Con regresar", tbar("Detalle de moto", back=True))
           + st("Con regresar y acción", tbar("Detalle de moto", back=True, action=("pencil", "Corregir")))
           + st("Regresar presionado", tbar("Detalle de moto", back=True, pressed=True))
           + "</div>", "Celular")
    + comp("Menú lateral", "Nav/MenuLateral", "240 px fijo · fondo #F5F5F4 con borde derecho · opciones de 40 px, radio 6 · activa: #E7E5E4, texto #1C1917 semibold, icono ocre · hover #EEEDEC · pie con usuario, rol y Cerrar sesión",
           '<div class="states">'
           + st("Gerente <em>· Motos activa, hover en Choferes</em>", sidebar(True, "Motos", "Choferes"))
           + st("Ayudante <em>· sin Financiamiento</em>", sidebar(False, "Liquidaciones"))
           + st("Gerente <em>· Financiamiento activa</em>", sidebar(True, "Financiamiento"))
           + "</div>", "Computadora")
)

# ======================= 2. Buscador =======================
def srch(cel, state):
    i = nid("buscar")
    cls = " cel" if cel else ""
    val, clr = "", ""
    if state in ("texto", "borrar"):
        val = ' value="27-ABC"'
        clr = f'<button class="clr{" h" if state == "borrar" else ""}" aria-label="Borrar búsqueda">{ic("circle-x")}</button>'
    f = " f" if state in ("foco", "texto", "borrar") else ""
    w = 358 if cel else 320
    return (f'<div class="srch{cls}{f}" style="width:{w}px">{ic("search")}'
            f'<input id="{i}" type="search" placeholder="Buscar por placa, modelo o chofer" aria-label="Buscar"{val}>{clr}</div>')


def srow(cel):
    return ('<div class="states">' + st("Vacío", srch(cel, "vacio")) + st("Enfocado", srch(cel, "foco"))
            + st("Con texto y botón borrar", srch(cel, "texto")) + st("Hover en borrar", srch(cel, "borrar")) + "</div>")


buscador = (
    comp("Buscador", "Buscador", "48 px · cuerpo 15/22 · icono buscar #78716C a la izquierda · el botón borrar (círculo con x, 48 × 48) aparece solo con texto", srow(True), "Celular")
    + comp("Buscador", "Buscador", "44 px · cuerpo 14/20 · ancho 320 px sobre la tabla · foco: borde ocre y anillo #FDF3EA de 3 px", srow(False), "Computadora")
)

# ======================= 3. Elementos de lista =======================
def card(kind, state):
    s = {"n": "", "h": " h", "p": " p"}[state]
    if kind == "moto":
        g = f'<span class="t placa">27-ABC-4</span><span class="s">Italika FT150 · Juan Pérez López</span>'
        return f'<div class="lc{s}"><div class="grow">{g}</div>{ic("chevron-right")}</div>'
    if kind == "chofer":
        g = f'<span class="t">María González Ruiz</span><span class="s num">55 2345 6789 · Moto <span class="placa">31-XKT-8</span></span>'
        return f'<div class="lc{s}"><div class="grow">{g}</div>{ic("chevron-right")}</div>'
    if kind == "liq":
        g = f'<span class="t">Juan Pérez López</span><span class="s num"><span class="placa">27-ABC-4</span> · 13 oct 2026</span>'
        return f'<div class="lc{s}"><div class="grow">{g}</div><span class="amt">$350.00</span>{ic("chevron-right")}</div>'
    g = f'<span class="t">Laura Méndez</span><span class="s">laura@ejemplo.com</span>'
    return f'<div class="lc{s}"><div class="grow">{g}</div><span class="tags"><span class="tag ger">Gerente</span><span class="tag alta">Alta</span></span>{ic("chevron-right")}</div>'


lg = '<div class="lgrid"><span></span><span class="ch">Normal</span><span class="ch">Al pasar el mouse</span><span class="ch">Presionado</span>'
for kind, lab in [("moto", "Moto"), ("chofer", "Chofer"), ("liq", "Liquidación"), ("usr", "Usuario")]:
    lg += f'<span class="rh">{lab}</span>' + "".join(card(kind, s) for s in "nhp")
lg += "</div>"


def table(cols, widths, rows):
    cg = "".join(f'<col style="width:{w}">' for w in widths)
    th = "".join(f'<th{" class=\"r\"" if c.startswith(">") else ""}>{c.lstrip(">")}</th>' for c in cols)
    body = ""
    for cls, cells in zip(["", "h", "p"], rows):
        body += f'<tr class="{cls}">' + "".join(cells) + f'<td class="go">{ic("chevron-right")}</td></tr>'
    labs = '<div class="tlab"><span></span><span>Normal</span><span>Al pasar el mouse</span><span>Presionado</span></div>'
    return f'<div class="trow">{labs}<div class="tbl"><table><colgroup>{cg}</colgroup><thead><tr>{th}<th></th></tr></thead><tbody>{body}</tbody></table></div></div>'


def td(x, cls=""):
    return f'<td class="{cls}">{x}</td>'


P = lambda x: f'<span class="placa">{x}</span>'
t_motos = table(["Placa", "Modelo", "Chofer"], ["180px", "260px", "auto", "52px"], [
    [td(P("27-ABC-4")), td("Italika FT150"), td("Juan Pérez López")],
    [td(P("31-XKT-8")), td("Italika DT150"), td("María González Ruiz")],
    [td(P("14-MNR-2")), td("Honda Cargo 150"), td('<span class="tag warn">Sin chofer</span>')]])
t_chof = table(["Nombre", "Teléfono", "Dirección", "Moto"], ["260px", "160px", "auto", "160px", "52px"], [
    [td("María González Ruiz"), td("55 2345 6789", "num"), td("Av. Juárez 120, Col. Moderna", "sec2"), td(P("31-XKT-8"))],
    [td("Juan Pérez López"), td("55 1234 5678", "num"), td("Calle Hidalgo 45, Col. Centro", "sec2"), td(P("27-ABC-4"))],
    [td("Pedro Sánchez Vega"), td("55 3456 7890", "num"), td("Av. Reforma 310, Col. Juárez", "sec2"), td('<span class="tag warn">Sin moto</span>')]])
t_liq = table(["Fecha", "Placa", "Chofer", ">Monto"], ["180px", "180px", "auto", "180px", "52px"], [
    [td("13 oct 2026", "num"), td(P("27-ABC-4")), td("Juan Pérez López"), td("$350.00", "num r")],
    [td("13 oct 2026", "num"), td(P("31-XKT-8")), td("María González Ruiz"), td("$1,500.00", "num r")],
    [td("12 oct 2026", "num"), td(P("27-ABC-4")), td("Juan Pérez López"), td("$350.00", "num r")]])
t_usr = table(["Nombre", "Correo", "Rol", "Estado"], ["260px", "auto", "160px", "160px", "52px"], [
    [td("Laura Méndez"), td("laura@ejemplo.com", "sec2"), td('<span class="tag ger">Gerente</span>'), td('<span class="tag alta">Alta</span>')],
    [td("Sofía Torres"), td("sofia@ejemplo.com", "sec2"), td('<span class="tag ayu">Ayudante</span>'), td('<span class="tag baja">Baja</span>')],
    [td("Carlos Ramírez"), td("carlos@ejemplo.com", "sec2"), td('<span class="tag ayu">Ayudante</span>'), td('<span class="tag alta">Alta</span>')]])

listas = (
    comp("Tarjeta de lista", "Lista/Tarjeta", "358 px (pantalla menos 16 px por lado) · alto mínimo 72 px · borde 1 px, radio 8, sin sombra · al pasar #F5F5F4 · presionado #E7E5E4 · toda la tarjeta es tocable", lg, "Celular")
    + comp("Fila de tabla · Motos", "Lista/Fila/Moto", "Filas de 44 px · encabezado 40 px, 12/16 medium #57534E · ancho del área de contenido (1440 − 240 − 64 = 1136 px) · al pasar #F5F5F4 · presionado #E7E5E4", t_motos, "Computadora")
    + comp("Fila de tabla · Choferes", "Lista/Fila/Chofer", "Teléfono con números tabulares · dirección en texto secundario", t_chof, "Computadora")
    + comp("Fila de tabla · Liquidaciones", "Lista/Fila/Liquidacion", "Monto alineado a la derecha con números tabulares", t_liq, "Computadora")
    + comp("Fila de tabla · Usuarios", "Lista/Fila/Usuario", "Rol y estado como etiquetas", t_usr, "Computadora")
)

# ======================= 4. Vacío y sin resultados =======================
def empty(cel, kind):
    b = " cel" if cel else ""
    if kind == "vacia":
        return (f'<div class="empty"><span class="bub">{ic("bike")}</span><h4>Aún no hay motos</h4>'
                f'<p>Registra la primera moto para poder asignarle un chofer.</p>'
                f'<button class="b b-pri{b}">{ic("plus")}Registrar moto</button></div>')
    return (f'<div class="empty"><span class="bub">{ic("search")}</span><h4>No encontramos motos con "XYZ"</h4>'
            f'<p>Revisa la placa o busca por el modelo o el nombre del chofer.</p>'
            f'<button class="b b-sec{b}">Borrar búsqueda</button></div>')


def srch_xyz(cel):
    i = nid("buscar")
    c = " cel" if cel else ""
    w = "100%" if cel else "320px"
    return (f'<div class="srch{c}" style="width:{w}">{ic("search")}<input id="{i}" type="search" aria-label="Buscar" value="XYZ">'
            f'<button class="clr" aria-label="Borrar búsqueda">{ic("circle-x")}</button></div>')


vac_cel = (f'<div class="frame app w390" style="height:560px;display:flex;flex-direction:column">'
           f'<header class="tbar"><h4>Motos</h4></header><div style="flex:1;display:flex;align-items:center">{empty(True,"vacia")}</div>{bnav("Motos")}</div>')
sin_cel = (f'<div class="frame app w390" style="height:560px;display:flex;flex-direction:column">'
           f'<header class="tbar"><h4>Motos</h4></header><div style="padding:16px 16px 0">{srch_xyz(True)}</div>'
           f'<div style="flex:1;display:flex;align-items:center">{empty(True,"sin")}</div>{bnav("Motos")}</div>')
vac_pc = (f'<div class="frame app" style="width:640px;padding:24px"><div class="tbl" style="width:100%">{empty(False,"vacia")}</div></div>')
sin_pc = (f'<div class="frame app" style="width:640px;padding:24px;display:flex;flex-direction:column;gap:16px">{srch_xyz(False)}'
          f'<div class="tbl" style="width:100%"><table><thead><tr><th>Placa</th><th>Modelo</th><th>Chofer</th></tr></thead></table>{empty(False,"sin")}</div></div>')

vacios = (
    comp("Estado vacío y sin resultados", "Lista/Vacia · Lista/SinResultados", "Icono de 20 px en cuadro de 48 px #F5F5F4 · título 16/24 semibold · explicación en texto secundario · vacío lleva botón principal; sin resultados, botón secundario «Borrar búsqueda»",
         '<div class="states">' + st("Lista vacía", vac_cel) + st("Sin resultados", sin_cel) + "</div>", "Celular")
    + comp("Estado vacío y sin resultados", "Lista/Vacia · Lista/SinResultados", "Va dentro de la tarjeta de la tabla; en sin resultados se conserva el encabezado para que se entienda qué se buscaba",
           '<div class="states">' + st("Lista vacía", vac_pc) + st("Sin resultados", sin_pc) + "</div>", "Computadora")
)

# ======================= 5. Botones =======================
def btn(kind, state):
    k = {"pri": "b-pri", "sec": "b-sec", "dan": "b-dan", "ico": "b-ico"}[kind]
    text = {"pri": "Guardar", "sec": "Cancelar", "dan": "Dar de baja", "ico": ""}[kind]
    load = {"pri": "Guardando…", "sec": "Cargando…", "dan": "Dando de baja…", "ico": ""}[kind]
    cls = {"n": "", "h": " h", "p": " p", "f": " f", "d": "", "l": " load"}[state]
    dis = " disabled" if state == "d" else ""
    aria = ' aria-label="Corregir"' if kind == "ico" else ""
    if state == "l":
        inner = ic("loader", "spin") + load
        return f'<button class="b {k}{cls}" aria-busy="true"{aria}>{inner}</button>'
    inner = ic("pencil") if kind == "ico" else text
    return f'<button class="b {k}{cls}"{dis}{aria}>{inner}</button>'


bg = '<div class="bgrid"><span></span>' + "".join(f'<span class="ch">{c}</span>' for c in ["Normal", "Hover", "Presionado", "Enfocado (teclado)", "Deshabilitado", "Cargando"])
for kind, lab in [("pri", "Principal"), ("sec", "Secundario"), ("dan", "Peligro"), ("ico", "Solo icono")]:
    bg += f'<span class="rh">{lab}</span>' + "".join(f'<div>{btn(kind, s)}</div>' for s in "nhpfdl")
bg += "</div>"

sizes = ('<div class="states" style="align-items:flex-end">'
         + st("Computadora <em>· 44 px, ancho al texto</em>", f'<div style="display:flex;gap:8px"><button class="b b-sec">Cancelar</button><button class="b b-pri">{ic("plus")}Registrar moto</button></div>')
         + st("Celular <em>· 48 px, ancho completo</em>", f'<div style="width:358px;display:flex;flex-direction:column;gap:8px"><button class="b b-pri cel full">Registrar liquidación</button><button class="b b-sec cel full">Cancelar</button></div>')
         + st("Con icono", f'<div style="display:flex;gap:8px"><button class="b b-sec">{ic("pencil")}Corregir</button><button class="b b-dan">Dar de baja</button></div>')
         + "</div>")

fab_ctx = (f'<div class="frame app w390" style="height:260px">'
           '<div class="stub"><i></i><i></i></div>'
           f'<div style="position:absolute;left:0;right:0;bottom:0"><div style="display:flex;justify-content:flex-end;padding:0 16px 16px">'
           f'<button class="fab" aria-label="Registrar moto">{ic("plus")}</button></div>{bnav("Motos")}</div></div>')

botones = (
    comp("Botón", "Boton/Principal · Boton/Secundario · Boton/Peligro · Boton/Icono", "44 px en computadora (48 px en celular) · radio 6 · 14/20 semibold · principal ocre con hover #A84B0C · peligro #B91C1C · foco: anillo ocre de 2 px separado 2 px · cargando: icono girando y texto en gerundio, no se puede volver a tocar", bg)
    + comp("Tamaños y combinaciones", "Boton/Tamanos", "La acción principal va a la derecha en computadora y arriba en celular; nunca más de un botón principal por zona", sizes)
    + comp("Botón flotante «+»", "Boton/Flotante", "56 × 56 px, radio 6, icono plus de 24 px · 16 px sobre la barra inferior y del borde derecho · única excepción con sombra (flota sobre la lista) · lleva el nombre de la acción para lectores de pantalla",
           '<div class="states" style="align-items:flex-end">'
           + st("Normal", f'<button class="fab" aria-label="Registrar moto">{ic("plus")}</button>')
           + st("Presionado", f'<button class="fab p" aria-label="Registrar moto">{ic("plus")}</button>')
           + st("En contexto", fab_ctx)
           + "</div>", "Celular")
)

# ======================= 6. Campos =======================
FIELDS = [
    ("texto", "Nombre completo", "María González Ruiz", "Escribe el nombre completo."),
    ("correo", "Correo", "laura@ejemplo.com", "Escribe un correo válido, como laura@ejemplo.com."),
    ("contrasena", "Contraseña", "contrasena1", "La contraseña debe tener al menos 8 caracteres."),
    ("telefono", "Teléfono", "55 2345 6789", "El teléfono debe tener 10 dígitos."),
    ("fecha", "Fecha", "13 oct 2026", "Elige la fecha de la liquidación."),
    ("monto", "Monto", "350.00", "Escribe un monto mayor a $0.00."),
]
PH = {"texto": "", "correo": "laura@ejemplo.com", "contrasena": "", "telefono": "55 1234 5678", "fecha": "13 oct 2026", "monto": "0.00"}
ERRV = {"texto": "", "correo": "laura@ejemplo", "contrasena": "abc12", "telefono": "55 2345", "fecha": "", "monto": "0.00"}


def field(kind, label, val, err, state, cel=False):
    i = nid(kind)
    wcls = {"vacio": "", "foco": " f", "lleno": "", "error": " e", "dis": " d"}[state]
    v = {"vacio": "", "foco": "", "lleno": val, "error": ERRV[kind], "dis": val}[state]
    vattr = f' value="{v}"' if v else ""
    dis = " disabled" if state == "dis" else ""
    inv = ' aria-invalid="true"' if state == "error" else ""
    ph = f' placeholder="{PH[kind]}"' if PH[kind] else ""
    typ = {"texto": "text", "correo": "email", "contrasena": "password", "telefono": "tel", "fecha": "text", "monto": "text"}[kind]
    extra = ' inputmode="decimal"' if kind == "monto" else (' inputmode="tel"' if kind == "telefono" else "")
    if kind == "contrasena" and state == "foco":
        typ, vattr = "text", ' value="contrasena1"'
    pre = '<span class="pre">$</span>' if kind == "monto" else ""
    num = ' class="num"' if kind in ("monto", "telefono", "fecha") else ""
    tail = ""
    if kind == "contrasena":
        shown = state == "foco"
        tail = f'<button class="tb" type="button" aria-label="{"Ocultar" if shown else "Mostrar"} contraseña"{dis}>{ic("eye-off" if shown else "eye")}</button>'
    elif kind == "fecha":
        tail = f'<button class="tb" type="button" aria-label="Abrir calendario"{dis}>{ic("calendar")}</button>'
    elif kind == "telefono":
        pre = f'<span class="lead">{ic("phone")}</span>'
    msg = ""
    if state == "error":
        msg = f'<p class="ferr" id="{i}-m">{ic("circle-alert","s16")}{err}</p>'
    elif kind == "contrasena" and state != "dis":
        msg = '<p class="help">Mínimo 8 caracteres.</p>'
    elif kind == "telefono" and state == "foco":
        msg = '<p class="help">10 dígitos, sin lada internacional.</p>'
    desc = f' aria-describedby="{i}-m"' if state == "error" else ""
    return (f'<div class="fld{" dis" if state == "dis" else ""}{" cel" if cel else ""}"><label for="{i}">{label}</label>'
            f'<div class="inb{wcls}">{pre}<input id="{i}" type="{typ}"{num}{vattr}{ph}{extra}{dis}{inv}{desc}>{tail}</div>{msg}</div>')


fg = '<div class="fgrid"><span></span>' + "".join(f'<span class="ch">{c}</span>' for c in ["Vacío", "Enfocado", "Lleno", "Con error", "Deshabilitado"])
for kind, label, val, err in FIELDS:
    rl = {"texto": "Texto", "correo": "Correo", "contrasena": "Contraseña <em class=\"help\" style=\"font-style:normal;display:block\">mostrar / ocultar</em>",
          "telefono": "Teléfono", "fecha": "Fecha <em class=\"help\" style=\"font-style:normal;display:block\">con calendario</em>", "monto": "Monto en pesos <em class=\"help\" style=\"font-style:normal;display:block\">prefijo $</em>"}[kind]
    fg += f'<span class="rh">{rl}</span>' + "".join(field(kind, label, val, err, s) for s in ["vacio", "foco", "lleno", "error", "dis"])
fg += "</div>"

# calendario octubre 2026 (1 de oct = jueves; semana inicia en lunes)
days = '<span class="dw">L</span><span class="dw">M</span><span class="dw">M</span><span class="dw">J</span><span class="dw">V</span><span class="dw">S</span><span class="dw">D</span>'
days += "<span></span>" * 3
for d in range(1, 32):
    cls = "sel" if d == 13 else ("today" if d == 14 else ("fut" if d > 14 else ""))
    cur = ' aria-pressed="true"' if d == 13 else ""
    days += f'<button class="{cls}"{cur} aria-label="{d} de octubre de 2026">{d}</button>'
cal = (f'<div class="cal"><div class="cal-h"><button class="b b-ico" aria-label="Mes anterior">{ic("chevron-left")}</button>'
       f'<b>Octubre 2026</b><button class="b b-ico" aria-label="Mes siguiente">{ic("chevron-right")}</button></div><div class="cal-g">{days}</div></div>')
cal_open = ('<div style="width:296px;display:flex;flex-direction:column;gap:4px">'
            + field("fecha", "Fecha", "13 oct 2026", "", "lleno").replace('class="inb"', 'class="inb f"', 1) + cal + "</div>")

cel_form = (f'<div class="frame w390" style="display:flex;flex-direction:column">'
            f'<header class="tbar back"><button class="b b-ico" aria-label="Regresar">{ic("arrow-left")}</button><h4>Registrar liquidación</h4></header>'
            '<div style="padding:24px 16px;display:flex;flex-direction:column;gap:20px">'
            + field("fecha", "Fecha", "13 oct 2026", "", "lleno", cel=True)
            + f'<div class="fld cel selbox"><span class="fl">Moto</span><div class="inb"><span class="val"><span class="placa">27-ABC-4</span> · Juan Pérez López</span>{ic("chevron-down","chev")}</div></div>'
            + field("monto", "Monto", "350.00", "", "foco", cel=True).replace('<input', '<input value="350"', 1)
            + f'<button class="b b-pri cel full" style="margin-top:8px">Registrar liquidación</button></div></div>')

campos = (
    comp("Campo de formulario", "Campo/Texto · Campo/Correo · Campo/Contrasena · Campo/Telefono · Campo/Fecha · Campo/Monto",
         "Etiqueta arriba 14/20 medium, 8 px de separación · 44 px, radio 6, borde #D6D3D1 · enfocado: borde ocre y anillo #FDF3EA de 3 px · error: borde y mensaje #B91C1C 13/18 debajo con icono · deshabilitado: fondo #FAFAF9, borde #E7E5E4, texto #57534E · teléfono, fecha y monto con números tabulares", fg, "Computadora")
    + comp("Calendario de fecha", "Campo/Fecha/Calendario", "Se abre debajo del campo como menú (radio 8 y sombra de menú) · semana inicia en lunes · día elegido en ocre · hoy con contorno · días futuros en gris porque no se registran liquidaciones adelantadas",
           '<div class="states">' + st("Abierto", cal_open) + "</div>")
    + comp("Formulario en celular", "Campo/Celular", "Mismos estados con 48 px de alto y texto 15/22 · campos a todo lo ancho, 20 px entre campos · el teclado numérico se abre en monto y teléfono",
           '<div class="states">' + st("Ejemplo: registrar liquidación", cel_form) + "</div>", "Celular")
)

# ======================= 7. Selector de lista =======================
def sel_field(state, w=320):
    i = nid("moto")
    if state == "vacio":
        inner, cls = f'<span class="ph">Elige una moto</span>', ""
    elif state == "abierto":
        inner, cls = f'<span class="val"><span class="placa">27-ABC-4</span> · Italika FT150</span>', " f"
    elif state == "error":
        inner, cls = f'<span class="ph">Elige una moto</span>', " e"
    else:
        inner, cls = f'<span class="val"><span class="placa">27-ABC-4</span> · Italika FT150</span>', ""
    msg = f'<p class="ferr">{ic("circle-alert","s16")}Elige la moto que entregó la liquidación.</p>' if state == "error" else ""
    chev = "chevron-down"
    return (f'<div class="fld selbox" style="width:{w}px"><span class="fl" id="{i}">Moto</span>'
            f'<div class="inb{cls}" role="combobox" aria-labelledby="{i}" aria-expanded="{"true" if state=="abierto" else "false"}" tabindex="0">{inner}{ic(chev,"chev")}</div>{msg}</div>')


def opt(placa, sub, sel=False, hov=False, tag=None, cel=False):
    t = f'<span class="t placa">{placa}</span>' if placa[0].isdigit() else f'<span class="t">{placa}</span>'
    tg = f'<span class="tag warn">{tag}</span>' if tag else ""
    ck = f'<span class="ck">{ic("check") if sel else ""}</span>'
    return (f'<div class="opt{" sel" if sel else ""}{" h" if hov else ""}" role="option" aria-selected="{"true" if sel else "false"}">'
            f'<div class="grow">{t}<div class="s">{sub}</div></div>{tg}{ck}</div>')


i_s = nid("buscar-moto")
dd = (f'<div style="width:400px;display:flex;flex-direction:column;gap:4px">{sel_field("abierto", 400)}'
      f'<div class="menu"><div class="msr"><div class="srch f" style="height:40px">{ic("search")}<input id="{i_s}" type="search" placeholder="Buscar placa o chofer" aria-label="Buscar moto"></div></div>'
      '<div class="opts" role="listbox">'
      + opt("27-ABC-4", "Italika FT150 · Juan Pérez López", sel=True)
      + opt("31-XKT-8", "Italika DT150 · María González Ruiz", hov=True)
      + opt("14-MNR-2", "Honda Cargo 150", tag="Sin chofer")
      + opt("09-PLQ-5", "Italika FT150 · Pedro Sánchez Vega")
      + "</div></div></div>")

i_c = nid("buscar-chofer")
sheet_ch = (f'<div class="frame app w390 cel" style="height:640px">'
            '<div class="stub"><i></i><i></i><i></i></div><div class="scrim"></div>'
            '<div class="sheetbox" style="position:absolute;left:0;right:0;bottom:0;padding-bottom:16px">'
            f'<div class="handle"></div><div class="sh-t"><h4>Elegir chofer</h4><button class="b b-ico" aria-label="Cerrar">{ic("x")}</button></div>'
            f'<div style="padding:4px 16px 8px"><div class="srch cel">{ic("search")}<input id="{i_c}" type="search" placeholder="Buscar por nombre o teléfono" aria-label="Buscar chofer"></div></div>'
            '<div role="listbox" style="border-top:1px solid var(--bd)">'
            + opt("María González Ruiz", 'Moto <span class="placa">31-XKT-8</span>', sel=True, cel=True)
            + opt("Juan Pérez López", 'Moto <span class="placa">27-ABC-4</span>', cel=True)
            + opt("Pedro Sánchez Vega", '<span class="num">55 3456 7890</span>', tag="Sin moto", cel=True)
            + opt("Rosa Hernández Díaz", 'Moto <span class="placa">09-PLQ-5</span>', hov=True, cel=True)
            + "</div></div></div>")

selector = (
    comp("Campo selector", "Selector/Campo", "Se ve como un campo con flecha hacia abajo · mismos estados que los campos de formulario",
         '<div class="states">' + st("Vacío", sel_field("vacio")) + st("Elegido", sel_field("lleno")) + st("Con error", sel_field("error")) + "</div>")
    + comp("Selector de lista", "Selector/Desplegable", "Menú bajo el campo, mismo ancho, radio 8 y sombra de menú · buscador arriba con foco automático · opciones de 52 px: placa y detalle · elegida con palomita ocre y texto semibold · hover #F5F5F4",
           '<div class="states">' + st("Abierto · eligiendo moto", dd) + "</div>", "Computadora")
    + comp("Selector de lista", "Selector/Hoja", "Hoja desde abajo con buscador · opciones de 60 px · se cierra al elegir · «Sin moto» en color de aviso",
           '<div class="states">' + st("Abierta · eligiendo chofer <em>(presionando Rosa)</em>", sheet_ch) + "</div>", "Celular")
)

# ======================= 8. Selector de rol =======================
ROL = {"Gerente": "Puede hacer todo, incluso dar de alta y de baja usuarios y ver Financiamiento.",
       "Ayudante": "Registra y consulta motos, choferes y liquidaciones. No ve Financiamiento."}


def rol(name, cls="", w=None):
    style = f' style="width:{w}"' if w else ""
    chk = "true" if "on" in cls else "false"
    dis = ' aria-disabled="true"' if " d" in f" {cls}" else ""
    return (f'<div class="rol {cls}" role="radio" aria-checked="{chk}" tabindex="0"{dis}{style}><span class="rd"></span>'
            f'<div><div class="t">{name}</div><div class="s">{ROL[name]}</div></div></div>')


roles = (
    comp("Opción de rol", "Rol/Opcion", "Tarjeta tocable completa · radio 8, borde #D6D3D1 · elegida: borde ocre de 2 px y punto ocre · la línea explica qué puede hacer en palabras simples",
         '<div class="states">' + st("Normal", rol("Ayudante")) + st("Hover", rol("Ayudante", "h")) + st("Elegida", rol("Gerente", "on"))
         + st("Enfocada (teclado)", rol("Ayudante", "f")) + st("Deshabilitada", rol("Gerente", "d")) + "</div>")
    + comp("Selector de rol", "Rol/Selector", "Dos opciones; nunca queda sin elegir (Ayudante por omisión, el rol con menos permisos)",
           '<div class="states">'
           + st("Computadora <em>· lado a lado</em>", '<div class="fld"><span class="fl">Rol</span><div role="radiogroup" style="display:flex;gap:12px">' + rol("Gerente", "on") + rol("Ayudante") + "</div></div>")
           + st("Celular <em>· una debajo de otra</em>", '<div class="fld"><span class="fl">Rol</span><div role="radiogroup" style="display:flex;flex-direction:column;gap:12px">' + rol("Gerente", "", "358px") + rol("Ayudante", "on", "358px") + "</div></div>")
           + "</div>")
)

# ======================= 9. Etiquetas =======================
tags = comp("Etiqueta", "Etiqueta/Gerente · Ayudante · Alta · Baja · SinChofer · SinMoto", "24 px de alto · 12/16 medium · 8 px a los lados · radio 6 · siempre con texto, nunca solo color · igual en celular y computadora",
            '<div class="states" style="gap:32px">'
            + st("Gerente", '<span class="tag ger">Gerente</span>') + st("Ayudante", '<span class="tag ayu">Ayudante</span>')
            + st("Alta", '<span class="tag alta">Alta</span>') + st("Baja", '<span class="tag baja">Baja</span>')
            + st("Sin chofer <em>· aviso</em>", '<span class="tag warn">Sin chofer</span>') + st("Sin moto <em>· aviso</em>", '<span class="tag warn">Sin moto</span>')
            + "</div>")

# ======================= 10. Detalle =======================
def lk(icn, t, s, state=""):
    return f'<a class="lk {state}" href="#detalle"><span class="bub">{ic(icn)}</span><span class="grow"><span class="t">{t}</span><span class="s">{s}</span></span>{ic("chevron-right")}</a>'


det_pc = (f'<div class="det" style="width:720px">'
          f'<div class="det-h"><div><h4 class="placa">27-ABC-4</h4><p>Italika FT150</p></div><button class="b b-sec">{ic("pencil")}Corregir</button></div>'
          '<dl class="dl"><dt>Placa</dt><dd class="placa">27-ABC-4</dd><dt>Modelo</dt><dd>Italika FT150</dd>'
          '<dt>Chofer</dt><dd>Juan Pérez López</dd><dt>Registrada</dt><dd class="num">2 sep 2026</dd>'
          '<dt>Última liquidación</dt><dd class="num">13 oct 2026 · $350.00</dd></dl>'
          '<div class="rel"><h5>Relacionado</h5><div class="rels">'
          + lk("user", "Juan Pérez López", '<span class="num">55 1234 5678</span>')
          + lk("receipt", "Liquidaciones", '<span class="num">12 registradas · $4,200.00</span>', "h")
          + "</div></div></div>")

det_cel = (f'<div class="frame app w390"><header class="tbar back"><button class="b b-ico" aria-label="Regresar">{ic("arrow-left")}</button><h4>Chofer</h4>'
           f'<button class="b b-ico" aria-label="Corregir">{ic("pencil")}</button></header>'
           '<div style="padding:16px"><div class="det cel">'
           '<div class="det-h"><div><h4>María González Ruiz</h4><p><span class="tag alta">Alta</span></p></div></div>'
           '<dl class="dl" style="border-top:1px solid var(--bd)"><dt>Teléfono</dt><dd class="num">55 2345 6789</dd>'
           '<dt>Dirección</dt><dd>Av. Juárez 120, Col. Moderna</dd><dt>Moto</dt><dd class="placa">31-XKT-8</dd></dl>'
           '<div class="rel"><h5>Relacionado</h5><div class="rels">'
           + lk("bike", '<span class="placa">31-XKT-8</span>', "Italika DT150")
           + lk("receipt", "Liquidaciones", '<span class="num">Última: 13 oct 2026 · $1,500.00</span>', "p")
           + "</div></div></div></div></div>")

detalle = (
    comp("Tarjeta de detalle", "Detalle/Tarjeta", "Título 24/32 semibold (placa con su espaciado) · datos en dos columnas: etiqueta #57534E 200 px y valor · enlaces relacionados de 64 px con flecha; el segundo muestra hover",
         '<div class="states">' + st("Moto", det_pc) + "</div>", "Computadora")
    + comp("Tarjeta de detalle", "Detalle/Tarjeta", "Título 22/28 · etiqueta arriba del valor · enlaces a todo lo ancho, uno debajo de otro; el segundo muestra presionado",
           '<div class="states">' + st("Chofer", det_cel) + "</div>", "Celular")
    + comp("Tarjeta de enlace", "Detalle/Enlace", "Toda la tarjeta lleva al registro relacionado",
           '<div class="states">' + st("Normal", f'<div style="width:340px">{lk("user","Juan Pérez López","<span class=\"num\">55 1234 5678</span>")}</div>')
           + st("Hover", f'<div style="width:340px">{lk("user","Juan Pérez López","<span class=\"num\">55 1234 5678</span>","h")}</div>')
           + st("Presionado", f'<div style="width:340px">{lk("user","Juan Pérez López","<span class=\"num\">55 1234 5678</span>","p")}</div>') + "</div>")
)

# ======================= 11. Mensajes =======================
toast = f'<div class="toast" role="status">{ic("circle-check")}<span class="t">Liquidación registrada</span><button class="b b-ico" aria-label="Cerrar aviso">{ic("x")}</button></div>'
toast_pc = (f'<div class="frame app" style="width:720px;height:200px">'
            f'<div style="position:absolute;left:0;top:0;bottom:0;width:120px;background:var(--side);border-right:1px solid var(--bd)"></div>'
            '<div style="position:absolute;left:152px;top:32px;right:32px" class="ph"><div><h4>Liquidaciones</h4><p>128 liquidaciones</p></div></div>'
            f'<div style="position:absolute;top:24px;right:24px;width:340px">{toast}</div></div>')
toast_cel = (f'<div class="frame app w390" style="height:300px">'
             '<div class="stub"><i></i><i></i><i></i></div>'
             f'<div style="position:absolute;left:0;right:0;bottom:0"><div style="padding:0 16px 12px">{toast}</div>{bnav("Liquidaciones")}</div></div>')

banners = ('<div style="display:flex;flex-direction:column;gap:12px;width:560px">'
           f'<div class="bn-msg err" role="alert">{ic("circle-alert")}<div class="grow"><p class="t">No pudimos guardar la liquidación.</p><p>Revisa tu conexión a internet e inténtalo de nuevo.</p><a class="act" href="#mensajes">Intentar de nuevo</a></div></div>'
           f'<div class="bn-msg info" role="status">{ic("info")}<div class="grow"><p class="t">Solo el Gerente puede dar de alta y de baja usuarios.</p><p>Puedes ver la lista, pero no cambiarla.</p></div></div>'
           f'<div class="bn-msg warn" role="status">{ic("triangle-alert")}<div class="grow"><p class="t">Esta moto no tiene chofer.</p><p>Asígnale uno para poder registrar sus liquidaciones.</p></div></div>'
           "</div>")

dlg_pc = (f'<div class="frame" style="width:640px;height:320px;background:var(--bg)"><div class="stub"><i></i><i></i><i></i></div><div class="scrim"></div>'
          '<div class="dlg" role="alertdialog" aria-labelledby="dlg-t1" style="position:absolute;left:120px;top:72px;width:400px">'
          '<h4 id="dlg-t1">¿Dar de baja a Sofía Torres?</h4><p>Ya no podrá entrar al CRM.</p>'
          '<div class="acts"><button class="b b-sec">Cancelar</button><button class="b b-dan">Dar de baja</button></div></div></div>')
dlg_cel = (f'<div class="frame w390" style="height:460px;background:var(--bg)"><div class="stub"><i></i><i></i><i></i><i></i></div><div class="scrim"></div>'
           '<div class="dlg cel" role="alertdialog" aria-labelledby="dlg-t2" style="position:absolute;left:16px;right:16px;top:110px">'
           '<h4 id="dlg-t2">¿Dar de baja a Sofía Torres?</h4><p>Ya no podrá entrar al CRM.</p>'
           '<div class="acts"><button class="b b-sec cel full">Cancelar</button><button class="b b-dan cel full">Dar de baja</button></div></div></div>')

mensajes = (
    comp("Aviso temporal de éxito", "Mensaje/AvisoExito", "Fondo blanco, borde y sombra de menú · icono verde #15803D · se va solo a los 4 s y se puede cerrar · arriba a la derecha (24 px) en computadora; abajo, sobre la barra, en celular",
         '<div class="states">' + st("Computadora", toast_pc) + st("Celular", toast_cel) + "</div>")
    + comp("Mensajes dentro de la pantalla", "Mensaje/Error · Mensaje/Info · Mensaje/Aviso", "Radio 6 · 12 × 16 px de relleno · primera línea semibold dice qué pasó, la segunda qué hacer · error #B91C1C sobre #FEF2F2 · informativo neutro con borde (sin color de acento) · aviso #854D0E sobre #FEF9C3",
           '<div class="states">' + st("Error · informativo · aviso", banners) + "</div>")
    + comp("Confirmación peligrosa", "Mensaje/ConfirmarBaja", "Ventana de 400 px, radio 8, sombra de ventana · fondo oscurecido · botón de peligro a la derecha en computadora y arriba en celular; Cancelar recibe el foco al abrir",
           '<div class="states">' + st("Computadora", dlg_pc) + st("Celular", dlg_cel) + "</div>")
)

# ======================= 12. Encabezado =======================
def ph_pc(title, count, btn_label=None, note=None):
    b = f'<button class="b b-pri">{ic("plus")}{btn_label}</button>' if btn_label else ""
    n = f'<span class="help">{note}</span>' if note else ""
    return (f'<div class="frame app" style="width:1136px;padding:32px 32px 24px"><div class="ph"><div><h4>{title}</h4><p>{count}</p></div>{b}{n}</div></div>')


def ph_cel(title, count):
    return (f'<div class="frame app w390" style="height:320px"><header class="tbar"><h4>{title}</h4></header>'
            f'<div style="padding:16px 16px 0;display:flex;flex-direction:column;gap:12px"><p class="help num" style="font-size:13px">{count}</p>'
            f'{srch(True,"vacio").replace("width:358px","width:100%")}</div><div class="stub"><i></i><i></i></div>'
            f'<div style="position:absolute;right:16px;bottom:16px"><button class="fab" aria-label="Registrar">{ic("plus")}</button></div></div>')


encabezado = (
    comp("Encabezado de pantalla", "Encabezado/Pantalla", "Título 24/32 semibold · contador 13/18 #57534E debajo, con números tabulares y en singular cuando es 1 · botón principal alineado a la derecha · 32 px de margen lateral",
         '<div style="display:flex;flex-direction:column;gap:16px">'
         + st("Motos", ph_pc("Motos", "4 motos", "Registrar moto"))
         + st("Singular", ph_pc("Choferes", "1 chofer", "Registrar chofer"))
         + st("Usuarios · Ayudante <em>(sin botón, no puede dar altas)</em>", ph_pc("Usuarios", "3 usuarios", None, "Solo el Gerente puede agregar usuarios"))
         + "</div>", "Computadora")
    + comp("Encabezado de pantalla", "Encabezado/Pantalla", "El título vive en la barra superior; el contador va arriba del buscador y la acción principal pasa al botón flotante",
           '<div class="states">' + st("Motos", ph_cel("Motos", "4 motos")) + st("Liquidaciones", ph_cel("Liquidaciones", "128 liquidaciones")) + "</div>", "Celular")
)

# ======================= Página =======================
SECS = [
    (1, "nav", "Navegación", "Celular usa barra superior + barra inferior fija; computadora, menú lateral de 240 px. La opción activa es el único lugar del menú con ocre.", nav),
    (2, "buscador", "Buscador", "Busca por placa, modelo o chofer mientras se escribe. El botón para borrar aparece solo cuando hay texto.", buscador),
    (3, "listas", "Elementos de lista", "Tarjetas en celular, filas de tabla en computadora. Todo el elemento abre el detalle.", listas),
    (4, "vacio", "Lista vacía y sin resultados", "Dicen qué pasó y ofrecen el siguiente paso.", vacios),
    (5, "botones", "Botones", "Tres variantes con texto y una solo icono. El ocre se reserva para la acción principal de cada zona.", botones),
    (6, "campos", "Campos de formulario", "Etiqueta siempre arriba, nunca dentro del campo. Los mensajes de error dicen cómo corregir.", campos),
    (7, "selector", "Selector de lista", "Para elegir una moto o un chofer entre muchos, con buscador.", selector),
    (8, "rol", "Selector de rol", "Gerente o Ayudante, explicado en una línea.", roles),
    (9, "etiquetas", "Etiquetas", "Estados y roles. El amarillo de aviso marca lo que necesita atención.", tags),
    (10, "detalle", "Tarjeta de detalle", "La ficha de un registro y los enlaces a lo que se relaciona con él.", detalle),
    (11, "mensajes", "Mensajes", "Avisos temporales, mensajes dentro de la pantalla y la confirmación antes de una acción que no se puede deshacer.", mensajes),
    (12, "encabezado", "Encabezado de pantalla", "Título, cuántos registros hay y la acción principal.", encabezado),
]

SW = [("#C25A12", "Acento"), ("#A84B0C", "Hover"), ("#FDF3EA", "Suave"), ("#FAFAF9", "Fondo"), ("#FFFFFF", "Superficie"),
      ("#F5F5F4", "Menú"), ("#E7E5E4", "Borde"), ("#D6D3D1", "Borde campo"), ("#1C1917", "Texto"), ("#57534E", "Secundario"),
      ("#78716C", "Ayuda"), ("#15803D", "Éxito"), ("#B91C1C", "Error"), ("#854D0E", "Aviso")]

NOTES = [
    "Valores derivados que el sistema no definía: ocre presionado #8F3F0A, peligro hover #991B1B y presionado #7F1D1D, hover del menú lateral #EEEDEC (el #F5F5F4 se pierde sobre el fondo del menú).",
    "Opciones del menú lateral de 40 px: en computadora se usa mouse; todo lo que se toca en celular mide 44 px o más.",
    "Botón flotante: radio 6 como el resto de botones y la sombra de menú, porque flota sobre la lista.",
    "Icono de Administración en la barra inferior: settings (el sistema no le asignaba uno).",
    "Datos extra inventados para llenar tablas: Carlos Ramírez (Ayudante), Pedro Sánchez Vega, Rosa Hernández Díaz y las motos 14-MNR-2 y 09-PLQ-5.",
]

index = "".join(f'<a href="#{sid}"><span>{n:02d}</span>{t}</a>' for n, sid, t, _, _ in SECS)
body = "".join(sec(n, sid, t, d, b) for n, sid, t, d, b in SECS)
sw = "".join(f'<span class="sw"><i style="background:{c}"></i><b>{lab}</b>{c}</span>' for c, lab in SW)
notes = "".join(f"<li>{x}</li>" for x in NOTES)

html = f"""<title>Componentes CRM-MotoT</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap">
<style>{CSS}</style>
{SPRITE}
<div class="scroll"><div class="sheet">
<header class="top">
  <div>
    <h1>Componentes CRM-MotoT</h1>
    <p class="lead">Biblioteca de componentes en el sistema ocre: 12 grupos, cada uno con su nombre, su ficha técnica y sus estados lado a lado. Celular (390 px) y computadora (1440 px) aparecen por separado cuando cambian.</p>
    <div class="swatches">{sw}</div>
  </div>
  <aside class="notes"><h2>Supuestos</h2><ul>{notes}</ul></aside>
</header>
<nav class="index" aria-label="Grupos">{index}</nav>
{body}
</div></div>
"""

open(OUT, "w", encoding="utf-8").write(html)
print(len(html))

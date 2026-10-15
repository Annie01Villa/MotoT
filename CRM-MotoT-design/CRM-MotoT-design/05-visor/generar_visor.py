#!/usr/bin/env python3
"""Arma visor.html: todas las pantallas de CRM-MotoT en una sola página.

Uso: python3 generar_visor.py   (lee ../pantallas, ../componentes y ../design-system-v2)
"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

# (carpeta, nombre en el menú, prefijo que se quita del nombre de cada pantalla)
MODULOS = [
    ("login", "Login", "Login"),
    ("motos", "Motos", "Moto"),
    ("motos-lista", "Motos lista", "Motos"),
    ("choferes-lista", "Choferes lista", "Choferes"),
    ("choferes-detalle", "Chofer detalle", "Chofer"),
    ("financiamiento", "Financiamiento", "Financiamiento"),
    ("liquidaciones", "Liquidaciones", "Liquidaciones"),
    ("usuarios", "Usuarios", "Usuarios"),
]
HOJAS = [
    ("componentes/hoja-componentes.html", "Componentes"),
    ("design-system-v2/hoja-design-system.html", "Design system"),
]

# Dentro de cada pantalla: los enlaces a otra .dc.html avisan al visor en lugar de navegar.
PUENTE = """<script>
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href');e.preventDefault();var m=h&&h.match(/([\\w-]+\\.dc\\.html)/);if(m)parent.postMessage({visor:'ir',archivo:m[1]},'*');},true);
document.addEventListener('submit',function(e){e.preventDefault();},true);
function alto(){parent.postMessage({visor:'alto',h:document.documentElement.scrollHeight},'*');}
window.addEventListener('load',alto);setTimeout(alto,600);
</script>"""

# Tema oscuro derivado del sistema ocre. Cada color se cambia según su papel:
# texto (color), relleno (background) o línea (border, box-shadow).
_T = {  # texto
    "#1A202C": "#F5F5F4", "#1C1917": "#F5F5F4", "#5A6475": "#C9C4C0", "#57534E": "#C9C4C0",
    "#78716C": "#A8A29E", "#C25A12": "#EB8F4E", "#A84B0C": "#F2A56D", "#8F3F0A": "#F2A56D",
    "#F26B1D": "#F58A4B", "#C5221F": "#F87171", "#B91C1C": "#F87171", "#A51C1A": "#FCA5A5",
    "#991B1B": "#FCA5A5", "#7F1D1D": "#FCA5A5", "#1E8E3E": "#4ADE80", "#15803D": "#4ADE80",
    "#B26A00": "#FBBF24", "#854D0E": "#FBBF24", "#E2E8F0": "#3A3532", "#E7E5E4": "#3A3532",
}
_F = {  # rellenos
    "#FFFFFF": "#24201D", "#F7F8FA": "#171412", "#FAFAF9": "#171412", "#EEF0F3": "#2E2926",
    "#F5F5F4": "#2E2926", "#EEEDEC": "#332E2B", "#E2E8F0": "#3A3532", "#E7E5E4": "#3A3532",
    "#D6D3D1": "#4A4440", "#FDF3EA": "#3A2516", "#F3D3B8": "#5A3418", "#E6F4EA": "#16301F",
    "#F0FDF4": "#16301F", "#CDE9D6": "#1F3F2A", "#FCE8E6": "#3B1A18", "#FEF2F2": "#3B1A18",
    "#FFF4E5": "#36290F", "#FEF9C3": "#36290F", "#1A202C": "#F5F5F4", "#1C1917": "#F5F5F4",
}
_L = {  # líneas y anillos de foco
    "#E2E8F0": "#3A3532", "#E7E5E4": "#3A3532", "#D6D3D1": "#4A4440", "#FFFFFF": "#24201D",
    "#C25A12": "#E07A33", "#A84B0C": "#EB8F4E", "#FDF3EA": "#4A2C15", "#CDE9D6": "#2F5A3C",
    "#F3D3B8": "#7A4520", "#C5221F": "#F87171", "#B91C1C": "#F87171", "#A51C1A": "#F87171",
    "#FCE8E6": "#5A2420", "#F26B1D": "#F58A4B", "#1E8E3E": "#4ADE80",
    "#5A6475": "#A8A29E", "#57534E": "#A8A29E", "#78716C": "#A8A29E",
}
_HEX = re.compile(r"#[0-9A-Fa-f]{6}\b")


def _papel(prop):
    prop = prop.lower()
    if prop in ("color", "caret-color", "fill", "stroke", "-webkit-text-fill-color", "text-decoration-color"):
        return _T
    if prop.startswith("border") or prop.startswith("outline") or prop == "box-shadow":
        return _L
    return _F


def a_oscuro(doc):
    def decl(m):
        mapa = _papel(m.group(1))
        return m.group(1) + m.group(2) + _HEX.sub(lambda h: mapa.get(h.group(0).upper(), h.group(0)), m.group(3))
    doc = re.sub(r"([a-zA-Z-]+)(\s*:\s*)([^;}\"<]*)", decl, doc)
    doc = re.sub(r"rgba\(26,\s*32,\s*44,\s*\.48\)", "rgba(0,0,0,.62)", doc)
    return doc.replace("</head>", "<style>:root{color-scheme:dark}</style></head>", 1)


def pantalla_a_doc(src):
    helmet = re.search(r"<helmet>(.*?)</helmet>", src, re.S).group(1)
    cuerpo = re.search(r"<x-dc>(.*?)</x-dc>", src, re.S).group(1)
    cuerpo = re.sub(r"<helmet>.*?</helmet>", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r'(\w+)="\{\{yes\}\}"', r"\1", cuerpo)
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            + helmet + "</head><body>" + cuerpo + PUENTE + "</body></html>")


def hoja_a_doc(src):
    return ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<style>body{margin:0}</style></head><body>' + src + PUENTE + "</body></html>")


def main():
    secciones, docs, docs_osc = [], {}, {}
    for carpeta, nombre, prefijo in MODULOS:
        d = os.path.join(RAIZ, "pantallas", carpeta)
        canvas = json.load(open(os.path.join(d, "canvas.json"), encoding="utf-8"))
        grupos = {}
        for archivo in canvas["order"]:
            b = canvas["boards"][archivo]
            partes = b["title"].split(" · ")
            num, disp, resto = partes[0], partes[-1], " · ".join(partes[1:-1])
            if resto.startswith(prefijo + " · "):
                resto = resto[len(prefijo) + 3:]
            clave = num + "|" + resto
            if clave not in grupos:
                grupos[clave] = {"num": num, "nombre": resto, "vistas": {}}
            id_ = carpeta + "/" + archivo
            grupos[clave]["vistas"]["cel" if disp == "Celular" else "pc"] = {
                "id": id_, "w": b["w"], "h": b["h"]}
            docs[id_] = pantalla_a_doc(open(os.path.join(d, archivo), encoding="utf-8").read())
            docs_osc[id_] = a_oscuro(docs[id_])
        secciones.append({"id": carpeta, "nombre": nombre, "pantallas": list(grupos.values())})

    hojas = []
    for ruta, nombre in HOJAS:
        docs[ruta] = hoja_a_doc(open(os.path.join(RAIZ, ruta), encoding="utf-8").read())
        hojas.append({"num": "", "nombre": nombre, "hoja": True,
                      "vistas": {"pc": {"id": ruta, "w": 1440, "h": None}}})
    secciones.append({"id": "referencia", "nombre": "Componentes y design system", "pantallas": hojas})

    datos = json.dumps({"secciones": secciones, "docs": docs, "oscuro": docs_osc}, ensure_ascii=False).replace("</", "<\\/")
    plantilla = open(os.path.join(AQUI, "plantilla.html"), encoding="utf-8").read()
    salida = plantilla.replace("/*DATOS*/", datos)
    open(os.path.join(AQUI, "visor.html"), "w", encoding="utf-8").write(salida)
    total = sum(len(s["pantallas"]) for s in secciones)
    print("visor.html:", len(salida) // 1024, "KB,", total, "pantallas,", len(docs), "archivos")


if __name__ == "__main__":
    main()

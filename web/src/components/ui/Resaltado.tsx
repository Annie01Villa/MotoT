import { segmentar } from "@/lib/busqueda";

/**
 * Pinta el texto con las coincidencias marcadas. Se arma con nodos de React,
 * así que cualquier texto (aunque traiga «<b>») se muestra como texto.
 */
export function Resaltado({
  texto,
  palabras,
  placa = false,
}: {
  texto: string;
  palabras: string[];
  placa?: boolean;
}) {
  if (palabras.length === 0) return <>{texto}</>;
  return (
    <>
      {segmentar(texto, palabras, placa).map((s, i) =>
        s.resaltado ? (
          <mark key={i} className="hl">
            {s.texto}
          </mark>
        ) : (
          <span key={i}>{s.texto}</span>
        ),
      )}
    </>
  );
}

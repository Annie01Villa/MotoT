"use client";

import { useId, useState } from "react";
import { Search } from "lucide-react";
import { normalizar, sinSeparadores } from "@/lib/texto";

export type Opcion = {
  id: string;
  principal: string;
  secundario: string;
  aviso?: string;
  esPlaca?: boolean;
  icono: React.ReactNode;
};

/**
 * Buscador + lista de opciones (patrón combobox): el foco se queda en el buscador,
 * las flechas mueven la opción activa y Enter la elige.
 */
export function ListaOpciones({
  opciones,
  valor,
  onElegir,
  etiquetaBusqueda,
  placeholder,
  etiquetaLista,
}: {
  opciones: Opcion[];
  valor: string | null;
  onElegir: (id: string) => void;
  etiquetaBusqueda: string;
  placeholder: string;
  etiquetaLista: string;
}) {
  const idLista = useId();
  const [texto, setTexto] = useState("");
  const buscado = sinSeparadores(normalizar(texto.trim()));
  const visibles = opciones.filter(
    (o) => !buscado || sinSeparadores(normalizar(`${o.principal} ${o.secundario}`)).includes(buscado),
  );
  const inicial = Math.max(0, visibles.findIndex((o) => o.id === valor));
  const [activa, setActiva] = useState(inicial);
  const indice = Math.min(activa, visibles.length - 1);

  function teclado(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActiva((i) => Math.min(i + 1, visibles.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActiva((i) => Math.max(i - 1, 0));
    } else if (e.key === "Enter") {
      e.preventDefault();
      if (visibles[indice]) onElegir(visibles[indice].id);
    }
  }

  return (
    <>
      <div className="search mx-4 mt-3 mb-3 md:mx-3">
        <Search aria-hidden="true" />
        <input
          type="search"
          role="combobox"
          aria-label={etiquetaBusqueda}
          aria-expanded="true"
          aria-controls={idLista}
          aria-activedescendant={visibles[indice] ? `${idLista}-${visibles[indice].id}` : undefined}
          placeholder={placeholder}
          autoComplete="off"
          value={texto}
          onChange={(e) => {
            setTexto(e.target.value);
            setActiva(0);
          }}
          onKeyDown={teclado}
        />
      </div>
      <div className="border-t border-borde">
        <ul id={idLista} role="listbox" aria-label={etiquetaLista}>
          {visibles.map((o, i) => (
            <li
              key={o.id}
              id={`${idLista}-${o.id}`}
              role="option"
              aria-selected={o.id === valor}
              data-activa={i === indice}
              className="opt"
              onClick={() => onElegir(o.id)}
              onMouseMove={() => setActiva(i)}
            >
              <span className="avatar" aria-hidden="true">
                {o.icono}
              </span>
              <span className="flex flex-1 flex-col">
                <span className={o.esPlaca ? "placa" : "font-semibold"}>{o.principal}</span>
                <span className="t-sec">{o.secundario}</span>
              </span>
              {o.aviso && <span className="tag tag-aviso">{o.aviso}</span>}
            </li>
          ))}
          {visibles.length === 0 && <li className="t-sec px-4 py-4">No hay resultados</li>}
        </ul>
      </div>
    </>
  );
}

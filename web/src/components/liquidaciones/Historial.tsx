"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { ChevronRight, Plus, Receipt, Search, SearchX, X } from "lucide-react";
import { useLiquidaciones } from "@/data/LiquidacionesProvider";
import { choferPorId, motoPorId } from "@/data/mock";
import { agruparPorDia } from "@/data/repo";
import type { Liquidacion } from "@/data/types";
import { coincide, palabrasDeBusqueda } from "@/lib/busqueda";
import { now } from "@/lib/clock";
import { fechaMx, formatFecha } from "@/lib/fechas";
import { formatMonto } from "@/lib/monto";
import { BarraSuperior } from "@/components/shell/BarraSuperior";
import { Aviso } from "@/components/ui/Aviso";
import { Resaltado } from "@/components/ui/Resaltado";
import { FormLiquidacion } from "./FormLiquidacion";

type Fila = Liquidacion & { placa: string; chofer: string };

function EtiquetaNueva() {
  return (
    <span className="tag tag-nueva">
      <span className="dot" aria-hidden="true" />
      Nueva
    </span>
  );
}

function Vacio({
  icono,
  children,
  accion,
}: {
  icono: React.ReactNode;
  children: React.ReactNode;
  accion: React.ReactNode;
}) {
  return (
    <div className="flex flex-1 flex-col items-center justify-center gap-4 px-4 py-12 text-center md:px-8">
      <span className="flex h-16 w-16 items-center justify-center rounded-full bg-ocre-suave text-ocre-texto" aria-hidden="true">
        {icono}
      </span>
      <p className="max-w-[300px]">{children}</p>
      {accion}
    </div>
  );
}

export function Historial() {
  const { lista, nuevaId, marcarNueva } = useLiquidaciones();
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const q = searchParams.get("q") ?? "";
  const [texto, setTexto] = useState(q);
  const [formAbierto, setFormAbierto] = useState(false);
  const [aviso, setAviso] = useState<string | null>(null);
  const buscadorRef = useRef<HTMLInputElement>(null);
  const hoy = fechaMx(now());

  // «Nueva» desaparece al salir de la pantalla (al detalle o a otra opción del menú).
  useEffect(() => () => marcarNueva(null), [marcarNueva]);

  useEffect(() => {
    if (!aviso) return;
    const t = setTimeout(() => setAviso(null), 4000);
    return () => clearTimeout(t);
  }, [aviso]);

  function buscar(valor: string) {
    setTexto(valor);
    // La búsqueda vive en la URL para conservarla al abrir un detalle y regresar.
    router.replace(valor ? `${pathname}?q=${encodeURIComponent(valor)}` : pathname, { scroll: false });
  }

  function limpiar() {
    buscar("");
    buscadorRef.current?.focus();
  }

  const filas: Fila[] = lista.map((l) => ({
    ...l,
    placa: motoPorId(l.motoId)?.placa ?? "",
    chofer: choferPorId(l.choferId)?.nombre ?? "",
  }));
  const palabras = palabrasDeBusqueda(texto);
  const visibles = palabras.length
    ? filas.filter((f) => coincide({ placa: f.placa, chofer: f.chofer, fecha: f.fecha }, texto, hoy))
    : filas;
  const grupos = agruparPorDia(visibles, hoy);
  const vacia = lista.length === 0;
  const hrefDetalle = (id: string) => `/liquidaciones/${id}${q ? `?q=${encodeURIComponent(q)}` : ""}`;

  const botonRegistrar = (clase: string) => (
    <button type="button" className={clase} onClick={() => setFormAbierto(true)}>
      <Plus size={24} aria-hidden="true" />
      Registrar liquidación
    </button>
  );

  const buscador = (
    <div className="search w-full md:w-[440px]">
      <label className="sr-only-text" htmlFor="q">
        Buscar liquidaciones
      </label>
      <Search aria-hidden="true" />
      <input
        ref={buscadorRef}
        id="q"
        type="search"
        placeholder="Buscar por placa, chofer o fecha"
        autoComplete="off"
        value={texto}
        onChange={(e) => buscar(e.target.value)}
      />
      {texto && (
        <button type="button" className="clr" aria-label="Borrar búsqueda" onClick={limpiar}>
          <X size={20} aria-hidden="true" />
        </button>
      )}
    </div>
  );

  let contenido: React.ReactNode;
  if (vacia) {
    contenido = (
      <div className="card flex flex-1 border-0 bg-transparent shadow-none md:border md:bg-white md:shadow-sm">
        <Vacio icono={<Receipt size={32} />} accion={botonRegistrar("btn btn-pri btn-lg")}>
          Todavía no hay liquidaciones.
          <br />
          Registra el primer pago.
        </Vacio>
      </div>
    );
  } else if (grupos.length === 0) {
    contenido = (
      <div className="card flex">
        <Vacio
          icono={<SearchX size={32} />}
          accion={
            <button type="button" className="btn btn-sec" onClick={limpiar}>
              Borrar búsqueda
            </button>
          }
        >
          No encontramos liquidaciones con &quot;{texto.trim()}&quot;
        </Vacio>
      </div>
    );
  } else {
    contenido = (
      <>
        {/* Celular: tarjetas por día */}
        <div className="solo-cel">
          <div className="flex flex-col gap-6">
            {grupos.map((g) => (
              <section key={g.fecha} aria-labelledby={`d-${g.fecha}`} className="flex flex-col gap-2">
                <h2 id={`d-${g.fecha}`} className="day num">
                  {g.etiqueta}
                </h2>
                <ul className="flex flex-col gap-2">
                  {g.items.map((f) => (
                    <li key={f.id}>
                      <Link
                        href={hrefDetalle(f.id)}
                        className={`card lcard ${f.id === nuevaId ? "nuevo" : ""}`}
                        data-testid="fila-liquidacion"
                      >
                        <span className="flex min-w-0 flex-1 flex-col gap-0.5">
                          <span className="flex items-center gap-2">
                            <span className="placa">
                              <Resaltado texto={f.placa} palabras={palabras} placa />
                            </span>
                            {f.id === nuevaId && <EtiquetaNueva />}
                          </span>
                          <span className="t-sec">
                            <Resaltado texto={f.chofer} palabras={palabras} />
                          </span>
                        </span>
                        <span className="monto">{formatMonto(f.montoCentavos)}</span>
                        <ChevronRight size={24} className="text-texto-2" aria-hidden="true" />
                      </Link>
                    </li>
                  ))}
                </ul>
              </section>
            ))}
          </div>
        </div>

        {/* Computadora: tabla agrupada por día */}
        <div className="solo-pc">
          <div className="card overflow-hidden">
            <div className="trow thead" aria-hidden="true">
              <span>Fecha</span>
              <span>Moto</span>
              <span>Chofer</span>
              <span className="text-right">Monto</span>
              <span />
            </div>
            {grupos.map((g) => (
              <section key={g.fecha} aria-labelledby={`t-${g.fecha}`}>
                <h2 id={`t-${g.fecha}`} className="tgrp num">
                  {g.etiqueta}
                </h2>
                <ul>
                  {g.items.map((f) => (
                    <li key={f.id}>
                      <Link
                        href={hrefDetalle(f.id)}
                        className={`trow ${f.id === nuevaId ? "nuevo" : ""}`}
                        data-testid="fila-liquidacion"
                      >
                        <span className="num">
                          <Resaltado texto={formatFecha(f.fecha)} palabras={palabras} />
                        </span>
                        <span className="flex items-center gap-2">
                          <span className="placa">
                            <Resaltado texto={f.placa} palabras={palabras} placa />
                          </span>
                          {f.id === nuevaId && <EtiquetaNueva />}
                        </span>
                        <span>
                          <Resaltado texto={f.chofer} palabras={palabras} />
                        </span>
                        <span className="monto">{formatMonto(f.montoCentavos)}</span>
                        <ChevronRight size={24} className="text-texto-2" aria-hidden="true" />
                      </Link>
                    </li>
                  ))}
                </ul>
              </section>
            ))}
          </div>
        </div>
      </>
    );
  }

  return (
    <>
      <BarraSuperior>
        <h1 className="t-scr">Liquidaciones</h1>
      </BarraSuperior>

      <main className="flex min-h-[calc(100vh-128px)] flex-col gap-6 px-4 pt-4 pb-40 md:min-h-screen md:p-8">
        <div className="solo-pc">
          <div className="flex items-center justify-between gap-6">
            <h1 className="t-scr-pc">Liquidaciones</h1>
            {!vacia && botonRegistrar("btn btn-pri")}
          </div>
        </div>
        {/* La lista vacía no lleva buscador ni botón flotante. */}
        {!vacia && buscador}
        {contenido}
      </main>

      {!vacia && <div className="solo-cel">{botonRegistrar(`fab ${aviso ? "sube" : ""}`)}</div>}

      {aviso && <Aviso mensaje={aviso} onCerrar={() => setAviso(null)} />}

      <FormLiquidacion
        abierto={formAbierto}
        onAbiertoChange={setFormAbierto}
        onGuardado={(liq) => {
          setFormAbierto(false);
          marcarNueva(liq.id);
          setAviso(`Liquidación registrada · ${formatMonto(liq.montoCentavos)}`);
        }}
      />
    </>
  );
}

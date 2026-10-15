"use client";

import { useState } from "react";
import Link from "next/link";
import { useParams, useSearchParams } from "next/navigation";
import { ArrowLeft, Bike, Calendar, ChevronRight, FileText, Pencil, User } from "lucide-react";
import { useLiquidaciones } from "@/data/LiquidacionesProvider";
import { choferPorId, motoPorId } from "@/data/mock";
import { formatFecha } from "@/lib/fechas";
import { formatMonto } from "@/lib/monto";
import { BarraSuperior } from "@/components/shell/BarraSuperior";
import { FormLiquidacion } from "./FormLiquidacion";

export function Detalle() {
  const { id } = useParams<{ id: string }>();
  const q = useSearchParams().get("q") ?? "";
  const { lista } = useLiquidaciones();
  const [corrigiendo, setCorrigiendo] = useState(false);
  const liq = lista.find((l) => l.id === id);
  // Regresar conserva la búsqueda de la lista.
  const hrefLista = `/liquidaciones${q ? `?q=${encodeURIComponent(q)}` : ""}`;

  const regresar = (
    <Link className="back" href={hrefLista}>
      <ArrowLeft size={24} aria-hidden="true" />
      Liquidaciones
    </Link>
  );

  if (!liq) {
    return (
      <>
        <BarraSuperior>{regresar}</BarraSuperior>
        <main className="flex flex-col gap-6 px-4 py-6 md:p-8">
          <div className="solo-pc">{regresar}</div>
          <h1 className="t-scr">No encontramos esta liquidación</h1>
        </main>
      </>
    );
  }

  const moto = motoPorId(liq.motoId);
  const chofer = choferPorId(liq.choferId);
  const botonCorregir = (
    <button type="button" className="btn btn-sec" onClick={() => setCorrigiendo(true)}>
      <Pencil size={20} aria-hidden="true" />
      Corregir
    </button>
  );

  return (
    <>
      <BarraSuperior>
        {regresar}
        {botonCorregir}
      </BarraSuperior>

      <main className="flex flex-col gap-6 px-4 py-6 md:p-8">
        <div className="solo-pc">{regresar}</div>
        <div className="flex max-w-[800px] flex-col gap-6">
          <div className="card flex items-start justify-between gap-6 p-4 md:p-6">
            <div className="flex flex-col gap-4">
              <div className="flex flex-col gap-2">
                <p className="t-sec">Liquidación</p>
                <h1 className="t-scr-resp num">{formatMonto(liq.montoCentavos)}</h1>
              </div>
              <dl className="flex flex-col gap-3">
                <div className="flex items-center gap-3">
                  <Calendar size={20} className="text-texto-2" aria-hidden="true" />
                  <dt className="sr-only-text">Fecha</dt>
                  <dd className="num">{formatFecha(liq.fecha)}</dd>
                </div>
                <div className="flex items-center gap-3">
                  <FileText size={20} className="text-texto-2" aria-hidden="true" />
                  <dt className="sr-only-text">Nombre</dt>
                  <dd>{liq.nombre}</dd>
                </div>
              </dl>
            </div>
            <div className="solo-pc">{botonCorregir}</div>
          </div>

          <div className="grid grid-cols-1 gap-3 md:grid-cols-2 md:gap-4">
            <Link
              className="card lk"
              href="/motos"
              aria-label={`Moto ${moto?.placa}, ${moto?.modelo}. Abrir la moto`}
            >
              <span className="avatar" aria-hidden="true">
                <Bike size={20} />
              </span>
              <span className="flex flex-1 flex-col gap-0.5">
                <span className="t-lab text-texto-2">Moto</span>
                <span className="placa">{moto?.placa}</span>
                <span className="t-sec">{moto?.modelo}</span>
              </span>
              <ChevronRight size={24} className="text-texto-2" aria-hidden="true" />
            </Link>
            <Link className="card lk" href="/choferes" aria-label={`Chofer ${chofer?.nombre}. Abrir el chofer`}>
              <span className="avatar" aria-hidden="true">
                <User size={20} />
              </span>
              <span className="flex flex-1 flex-col gap-0.5">
                <span className="t-lab text-texto-2">Chofer</span>
                <span className="font-semibold">{chofer?.nombre}</span>
                <span className="t-sec num">{chofer?.telefono}</span>
              </span>
              <ChevronRight size={24} className="text-texto-2" aria-hidden="true" />
            </Link>
          </div>
        </div>
      </main>

      <FormLiquidacion
        abierto={corrigiendo}
        onAbiertoChange={setCorrigiendo}
        liquidacion={liq}
        onGuardado={() => setCorrigiendo(false)}
      />
    </>
  );
}

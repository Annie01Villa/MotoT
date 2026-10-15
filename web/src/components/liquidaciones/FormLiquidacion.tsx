"use client";

import { useReducer, useRef, useState } from "react";
import * as Dialog from "@radix-ui/react-dialog";
import { DayPicker } from "react-day-picker";
import { es } from "react-day-picker/locale";
import { Bike, Calendar, ChevronDown, CircleAlert, User, X } from "lucide-react";
import { useLiquidaciones } from "@/data/LiquidacionesProvider";
import { choferesOrdenados, motoDeChofer, motoPorId, MOTOS } from "@/data/mock";
import type { Liquidacion } from "@/data/types";
import { now } from "@/lib/clock";
import { dateLocalDeFecha, etiquetaDia, fechaDeDateLocal, fechaMx } from "@/lib/fechas";
import { crearReducer, estadoInicial, validar } from "@/lib/formulario";
import { Desplegable } from "@/components/ui/Desplegable";
import { ListaOpciones, type Opcion } from "@/components/ui/ListaOpciones";

const reducer = crearReducer(MOTOS);

const OPCIONES_MOTO: Opcion[] = MOTOS.map((m) => ({
  id: m.id,
  principal: m.placa,
  secundario: m.modelo,
  aviso: m.choferId ? undefined : "Sin chofer",
  esPlaca: true,
  icono: <Bike size={20} />,
}));

// Todos los choferes registrados, en orden alfabético, con su placa o «Sin moto».
const OPCIONES_CHOFER: Opcion[] = choferesOrdenados().map((c) => ({
  id: c.id,
  principal: c.nombre,
  secundario: motoDeChofer(c.id)?.placa ?? "Sin moto",
  icono: <User size={20} />,
}));

function MensajeError({ id, texto }: { id: string; texto?: string }) {
  if (!texto) return null;
  return (
    <p className="msg-err" id={id}>
      <CircleAlert size={16} aria-hidden="true" />
      {texto}
    </p>
  );
}

function Cuerpo({
  liquidacion,
  onGuardado,
}: {
  liquidacion?: Liquidacion;
  onGuardado: (liq: Liquidacion) => void;
}) {
  const { repo } = useLiquidaciones();
  const hoy = fechaMx(now());
  const [estado, despachar] = useReducer(reducer, undefined, () => estadoInicial(hoy, liquidacion));
  const [intentado, setIntentado] = useState(false);
  const [guardando, setGuardando] = useState(false);
  const [abierto, setAbierto] = useState<"moto" | "chofer" | "fecha" | null>(null);
  const motoRef = useRef<HTMLButtonElement>(null);
  const choferRef = useRef<HTMLButtonElement>(null);
  const montoRef = useRef<HTMLInputElement>(null);

  const moto = motoPorId(estado.motoId);
  const chofer = OPCIONES_CHOFER.find((c) => c.id === estado.choferId);
  const validacion = validar(estado, MOTOS);
  const errores = intentado && !validacion.ok ? validacion.errores : {};
  const corrigiendo = Boolean(liquidacion);

  function guardar(e: React.FormEvent) {
    e.preventDefault();
    if (guardando) return;
    if (!validacion.ok) {
      setIntentado(true);
      const v = validacion.errores;
      (v.moto ? motoRef : v.chofer ? choferRef : montoRef).current?.focus();
      return;
    }
    setGuardando(true);
    const guardada = liquidacion
      ? repo.corregir(liquidacion.id, validacion.datos)
      : repo.registrar(validacion.datos);
    onGuardado(guardada);
  }

  const ayudaChofer = !moto
    ? undefined
    : moto.choferId && moto.choferId === estado.choferId
      ? `Es el chofer de ${moto.placa}. Puedes cambiarlo.`
      : !moto.choferId && !estado.choferId
        ? `${moto.placa} no tiene chofer. Elige quién la trae.`
        : undefined;

  return (
    <>
      <div className="flex flex-row-reverse items-center justify-end gap-2 border-b border-borde py-2 pr-4 pl-1 md:flex-row md:justify-between md:py-4 md:pr-3 md:pl-6">
        <Dialog.Title className="t-scr">{corrigiendo ? "Corregir liquidación" : "Registrar liquidación"}</Dialog.Title>
        <Dialog.Close className="btn btn-ico" aria-label="Cerrar sin guardar">
          <X size={24} aria-hidden="true" />
        </Dialog.Close>
      </div>

      <form
        id="form-liquidacion"
        noValidate
        onSubmit={guardar}
        className="flex min-h-0 flex-1 flex-col gap-6 overflow-auto px-4 py-6 md:p-6"
      >
        <div>
          <p className="lbl" id="l-moto">
            Moto
          </p>
          <Desplegable
            abierto={abierto === "moto"}
            onAbiertoChange={(v) => setAbierto(v ? "moto" : null)}
            titulo="Elige la moto"
            disparador={
              <button
                ref={motoRef}
                type="button"
                id="moto"
                className="inp"
                aria-labelledby="l-moto moto-valor"
                data-error={Boolean(errores.moto)}
                aria-describedby={errores.moto ? "e-moto" : undefined}
              >
                <span className="val" id="moto-valor">
                  {moto ? (
                    <>
                      <span className="placa">{moto.placa}</span>
                      <span className="ph"> · {moto.modelo}</span>
                    </>
                  ) : (
                    <span className="ph">Elige la moto</span>
                  )}
                </span>
                <ChevronDown aria-hidden="true" />
              </button>
            }
          >
            <ListaOpciones
              opciones={OPCIONES_MOTO}
              valor={estado.motoId}
              etiquetaBusqueda="Buscar moto por placa"
              placeholder="Buscar por placa"
              etiquetaLista="Motos"
              onElegir={(id) => {
                despachar({ tipo: "moto", motoId: id });
                setAbierto(null);
              }}
            />
          </Desplegable>
          <MensajeError id="e-moto" texto={errores.moto} />
        </div>

        <div>
          <p className="lbl" id="l-chofer">
            Chofer
          </p>
          <Desplegable
            abierto={abierto === "chofer"}
            onAbiertoChange={(v) => setAbierto(v ? "chofer" : null)}
            titulo="Elige el chofer"
            disparador={
              <button
                ref={choferRef}
                type="button"
                id="chofer"
                className="inp"
                disabled={!moto}
                aria-labelledby="l-chofer chofer-valor"
                data-error={Boolean(errores.chofer)}
                aria-describedby={errores.chofer ? "e-chofer" : ayudaChofer ? "h-chofer" : undefined}
              >
                <span className="val" id="chofer-valor">
                  {chofer ? (
                    chofer.principal
                  ) : (
                    <span className="ph">{moto ? "Elige el chofer" : "Se llena al elegir la moto"}</span>
                  )}
                </span>
                <ChevronDown aria-hidden="true" />
              </button>
            }
          >
            <ListaOpciones
              opciones={OPCIONES_CHOFER}
              valor={estado.choferId}
              etiquetaBusqueda="Buscar chofer por nombre"
              placeholder="Buscar por nombre"
              etiquetaLista="Choferes"
              onElegir={(id) => {
                despachar({ tipo: "chofer", choferId: id });
                setAbierto(null);
              }}
            />
          </Desplegable>
          {ayudaChofer && !errores.chofer && (
            <p className="hint" id="h-chofer">
              {ayudaChofer}
            </p>
          )}
          <MensajeError id="e-chofer" texto={errores.chofer} />
        </div>

        <div>
          <p className="lbl" id="l-fecha">
            Fecha
          </p>
          <Desplegable
            abierto={abierto === "fecha"}
            onAbiertoChange={(v) => setAbierto(v ? "fecha" : null)}
            titulo="Elige la fecha"
            disparador={
              <button type="button" id="fecha" className="inp" aria-labelledby="l-fecha fecha-valor">
                <span className="val num" id="fecha-valor">
                  {etiquetaDia(estado.fecha, hoy)}
                </span>
                <Calendar aria-hidden="true" />
              </button>
            }
          >
            <DayPicker
              className="cal"
              mode="single"
              required
              locale={es}
              weekStartsOn={1}
              autoFocus
              selected={dateLocalDeFecha(estado.fecha)}
              defaultMonth={dateLocalDeFecha(estado.fecha)}
              endMonth={dateLocalDeFecha(hoy)}
              disabled={{ after: dateLocalDeFecha(hoy) }}
              onSelect={(d) => {
                if (d) despachar({ tipo: "fecha", fecha: fechaDeDateLocal(d) });
                setAbierto(null);
              }}
            />
          </Desplegable>
        </div>

        <div>
          <label className="lbl" htmlFor="monto">
            Monto
          </label>
          <div className="money">
            <span className="pre" aria-hidden="true">
              $
            </span>
            <input
              ref={montoRef}
              className="inp"
              id="monto"
              type="text"
              inputMode="decimal"
              placeholder="0.00"
              autoComplete="off"
              value={estado.montoTexto}
              aria-invalid={Boolean(errores.monto)}
              aria-describedby={errores.monto ? "e-monto" : undefined}
              onChange={(e) => despachar({ tipo: "monto", texto: e.target.value })}
            />
          </div>
          <MensajeError id="e-monto" texto={errores.monto} />
        </div>

        <div>
          <label className="lbl" htmlFor="nombre">
            Nombre
          </label>
          <input
            className="inp"
            id="nombre"
            type="text"
            placeholder="Se llena al elegir la moto"
            aria-describedby="h-nombre"
            value={estado.nombre}
            onChange={(e) => despachar({ tipo: "nombre", texto: e.target.value })}
          />
          <p className="hint" id="h-nombre">
            Se llena solo. Puedes cambiarlo.
          </p>
        </div>
      </form>

      <div className="flex flex-col-reverse gap-2 border-t border-borde p-4 md:flex-row md:justify-end md:gap-3 md:px-6">
        <Dialog.Close className="btn btn-sec btn-lg w-full md:w-auto md:min-h-11">Cancelar</Dialog.Close>
        <button
          type="submit"
          form="form-liquidacion"
          className="btn btn-pri btn-lg w-full md:w-auto md:min-h-11"
          disabled={guardando}
        >
          {corrigiendo ? "Guardar cambios" : "Guardar liquidación"}
        </button>
      </div>
    </>
  );
}

/** Registrar (sin `liquidacion`) o Corregir (con `liquidacion`). */
export function FormLiquidacion({
  abierto,
  onAbiertoChange,
  liquidacion,
  onGuardado,
}: {
  abierto: boolean;
  onAbiertoChange: (v: boolean) => void;
  liquidacion?: Liquidacion;
  onGuardado: (liq: Liquidacion) => void;
}) {
  // Botón que abrió el panel: al cerrarlo, el foco regresa ahí.
  const abridor = useRef<HTMLElement | null>(null);
  return (
    <Dialog.Root open={abierto} onOpenChange={onAbiertoChange}>
      <Dialog.Portal>
        <Dialog.Overlay className="scrim" />
        <Dialog.Content
          className="panel"
          aria-describedby={undefined}
          onOpenAutoFocus={(e) => {
            // El foco va al primer campo (Moto), no al botón de cerrar.
            e.preventDefault();
            abridor.current = document.activeElement instanceof HTMLElement ? document.activeElement : null;
            document.getElementById("moto")?.focus();
          }}
          onCloseAutoFocus={(e) => {
            if (abridor.current?.isConnected) {
              e.preventDefault();
              abridor.current.focus();
            }
          }}
        >
          {/* Se monta al abrir: cada vez arranca con los datos de la liquidación (o vacío). */}
          <Cuerpo liquidacion={liquidacion} onGuardado={onGuardado} />
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}

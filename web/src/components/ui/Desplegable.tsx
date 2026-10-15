"use client";

import * as Dialog from "@radix-ui/react-dialog";
import * as Popover from "@radix-ui/react-popover";
import { X } from "lucide-react";
import { useEsEscritorio } from "./useEsEscritorio";

// Al abrir, el foco va al buscador de la lista o al día elegido del calendario,
// no al botón de cerrar.
function enfocarPrimerCampo(e: Event) {
  const contenedor = e.currentTarget as HTMLElement;
  const destino = contenedor.querySelector<HTMLElement>('input, .rdp-day_button[tabindex="0"]');
  if (destino) {
    e.preventDefault();
    destino.focus();
  }
}

/**
 * Contenedor de un selector: menú desplegable bajo el campo en computadora,
 * hoja que sube desde abajo en celular. En los dos casos es modal: Radix atrapa el foco
 * (Tab y Shift+Tab no salen), cierra con Escape y regresa el foco al campo que lo abrió.
 */
export function Desplegable({
  abierto,
  onAbiertoChange,
  titulo,
  disparador,
  children,
}: {
  abierto: boolean;
  onAbiertoChange: (v: boolean) => void;
  titulo: string;
  disparador: React.ReactElement;
  children: React.ReactNode;
}) {
  const escritorio = useEsEscritorio();

  if (escritorio) {
    return (
      // modal: el foco queda atrapado en el selector o el calendario, igual que en celular.
      <Popover.Root open={abierto} onOpenChange={onAbiertoChange} modal>
        <Popover.Trigger asChild>{disparador}</Popover.Trigger>
        <Popover.Portal>
          <Popover.Content
            className="pop"
            align="start"
            sideOffset={4}
            aria-label={titulo}
            onOpenAutoFocus={enfocarPrimerCampo}
          >
            {children}
          </Popover.Content>
        </Popover.Portal>
      </Popover.Root>
    );
  }

  return (
    <Dialog.Root open={abierto} onOpenChange={onAbiertoChange}>
      <Dialog.Trigger asChild>{disparador}</Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="scrim" />
        <Dialog.Content className="sheet" aria-describedby={undefined} onOpenAutoFocus={enfocarPrimerCampo}>
          <div className="grab" aria-hidden="true">
            <span />
          </div>
          <div className="flex items-center justify-between py-1 pr-2 pl-4">
            <Dialog.Title className="t-sub">{titulo}</Dialog.Title>
            <Dialog.Close className="btn btn-ico" aria-label="Cerrar">
              <X size={24} aria-hidden="true" />
            </Dialog.Close>
          </div>
          <div className="pb-4">{children}</div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}

"use client";

import { createContext, useCallback, useContext, useState, useSyncExternalStore } from "react";
import { LIQUIDACIONES } from "./mock";
import { crearRepoMemoria, type RepoMemoria } from "./repo";
import type { Liquidacion } from "./types";

type Valor = {
  repo: RepoMemoria;
  /** id de la última liquidación registrada (etiqueta «Nueva»). */
  nuevaId: string | null;
  marcarNueva: (id: string | null) => void;
};

const Contexto = createContext<Valor | null>(null);

export function LiquidacionesProvider({
  children,
  semilla = LIQUIDACIONES,
}: {
  children: React.ReactNode;
  semilla?: Liquidacion[];
}) {
  // Un repositorio por carga de página: las altas y correcciones viven mientras dure la sesión.
  const [repo] = useState(() => crearRepoMemoria(semilla));
  const [nuevaId, setNuevaId] = useState<string | null>(null);
  const marcarNueva = useCallback((id: string | null) => setNuevaId(id), []);
  return <Contexto.Provider value={{ repo, nuevaId, marcarNueva }}>{children}</Contexto.Provider>;
}

function useContexto(): Valor {
  const v = useContext(Contexto);
  if (!v) throw new Error("Falta LiquidacionesProvider");
  return v;
}

export function useLiquidaciones() {
  const { repo, nuevaId, marcarNueva } = useContexto();
  const lista = useSyncExternalStore(repo.subscribe, repo.listar, repo.listar);
  return { repo, lista, nuevaId, marcarNueva };
}

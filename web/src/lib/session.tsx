"use client";

// Sesión simulada: el login real queda fuera de esta maqueta.
import { createContext, useContext, useState } from "react";

export type Usuario = { nombre: string; rol: "Gerente" | "Ayudante" };

export const USUARIOS_PRUEBA: Usuario[] = [
  { nombre: "Pedro Martínez", rol: "Ayudante" },
  { nombre: "Laura Méndez", rol: "Gerente" },
];

/** El selector de sesión solo existe en desarrollo; nunca en la compilación de producción. */
export const MOSTRAR_SELECTOR_SESION = process.env.NODE_ENV === "development";

type Valor = { usuario: Usuario; cambiar: (u: Usuario) => void };

const Contexto = createContext<Valor | null>(null);

export function SesionProvider({ children }: { children: React.ReactNode }) {
  const [usuario, cambiar] = useState<Usuario>(USUARIOS_PRUEBA[0]);
  return <Contexto.Provider value={{ usuario, cambiar }}>{children}</Contexto.Provider>;
}

export function useSesion(): Valor {
  const v = useContext(Contexto);
  if (!v) throw new Error("Falta SesionProvider");
  return v;
}

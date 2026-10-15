// Datos de prueba de §8 del documento de la Fase 0 (CRM motoT.md).
import type { Chofer, Liquidacion, Moto } from "./types";

export const CHOFERES: Chofer[] = [
  { id: "cho-1", nombre: "Juan Pérez López", telefono: "55 1234 5678" },
  { id: "cho-2", nombre: "María González Ruiz", telefono: "55 2345 6789" },
  { id: "cho-3", nombre: "Luis Hernández Soto", telefono: "55 3456 7890" },
  { id: "cho-4", nombre: "Carlos Ramírez Díaz", telefono: "55 4567 8901" },
];

export const MOTOS: Moto[] = [
  { id: "mot-1", placa: "27-ABC-4", modelo: "Italika FT150", choferId: "cho-1" },
  { id: "mot-2", placa: "31-XKT-8", modelo: "Honda CGL 125", choferId: "cho-2" },
  { id: "mot-3", placa: "12-MNO-5", modelo: "Yamaha YBR 125", choferId: "cho-3" },
  { id: "mot-4", placa: "45-PQR-2", modelo: "Italika DM150", choferId: null },
];

export const LIQUIDACIONES: Liquidacion[] = [
  {
    id: "liq-001",
    fecha: "2026-10-13",
    creadaEn: "2026-10-13T18:00:00.000Z",
    motoId: "mot-1",
    choferId: "cho-1",
    montoCentavos: 35000,
    nombre: "27-ABC-4 · 13 oct 2026",
    nombrePersonalizado: false,
  },
  {
    id: "liq-002",
    fecha: "2026-10-13",
    creadaEn: "2026-10-13T17:00:00.000Z",
    motoId: "mot-2",
    choferId: "cho-2",
    montoCentavos: 35000,
    nombre: "31-XKT-8 · 13 oct 2026",
    nombrePersonalizado: false,
  },
  {
    id: "liq-003",
    fecha: "2026-10-12",
    creadaEn: "2026-10-12T18:00:00.000Z",
    motoId: "mot-3",
    choferId: "cho-3",
    montoCentavos: 30000,
    nombre: "12-MNO-5 · 12 oct 2026",
    nombrePersonalizado: false,
  },
  {
    id: "liq-004",
    fecha: "2026-10-12",
    creadaEn: "2026-10-12T17:00:00.000Z",
    motoId: "mot-1",
    choferId: "cho-1",
    montoCentavos: 35000,
    nombre: "27-ABC-4 · 12 oct 2026",
    nombrePersonalizado: false,
  },
];

export function motoPorId(id: string | null | undefined): Moto | undefined {
  return MOTOS.find((m) => m.id === id);
}

export function choferPorId(id: string | null | undefined): Chofer | undefined {
  return CHOFERES.find((c) => c.id === id);
}

/** Moto que trae un chofer (o undefined si no trae ninguna). */
export function motoDeChofer(choferId: string): Moto | undefined {
  return MOTOS.find((m) => m.choferId === choferId);
}

/** Todos los choferes registrados, en orden alfabético. */
export function choferesOrdenados(): Chofer[] {
  return [...CHOFERES].sort((a, b) => a.nombre.localeCompare(b.nombre, "es"));
}

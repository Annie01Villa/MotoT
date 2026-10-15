export type Moto = {
  id: string;
  placa: string;
  modelo: string;
  choferId: string | null;
};

export type Chofer = {
  id: string;
  nombre: string;
  telefono: string;
};

export type Liquidacion = {
  /** No cambia nunca. Es la key de React y la ruta del detalle. */
  id: string;
  /** Día de calendario en México, "YYYY-MM-DD". */
  fecha: string;
  /** Instante ISO (UTC) en que se registró. No cambia al corregir. */
  creadaEn: string;
  motoId: string;
  choferId: string;
  /** Entero. Nunca decimal flotante. */
  montoCentavos: number;
  nombre: string;
  /** true en cuanto el usuario escribe en Nombre; entonces el nombre ya no se recalcula. */
  nombrePersonalizado: boolean;
};

/** Lo que el formulario manda al registrar o corregir. id y creadaEn los pone el repositorio. */
export type DatosLiquidacion = Omit<Liquidacion, "id" | "creadaEn">;

export interface LiquidacionesRepo {
  listar(): Liquidacion[];
  obtener(id: string): Liquidacion | undefined;
  registrar(datos: DatosLiquidacion): Liquidacion;
  corregir(id: string, cambios: DatosLiquidacion): Liquidacion;
}

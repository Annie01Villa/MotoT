// Única fuente de la hora en la app. En las pruebas se fija el reloj
// (vi.useFakeTimers / page.clock), así que basta con usar Date.now().
export function now(): Date {
  return new Date(Date.now());
}

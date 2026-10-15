/** Barra superior del celular. Cada pantalla decide qué lleva. */
export function BarraSuperior({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <div className="solo-cel">
      <header className={`top ${className}`}>{children}</header>
    </div>
  );
}

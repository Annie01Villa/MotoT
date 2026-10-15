import Link from "next/link";
import { Bike } from "lucide-react";

export const metadata = { title: "Entrar · CRM-MotoT" };

// Provisional: el inicio de sesión real se construye en su propia tarea.
export default function PaginaLogin() {
  return (
    <main className="flex min-h-screen items-center justify-center p-4">
      <div className="card flex w-full max-w-[400px] flex-col gap-4 p-6 text-center">
        <p className="logo justify-center">
          <Bike size={24} aria-hidden="true" />
          CRM-MotoT
        </p>
        <h1 className="t-scr">Cerraste sesión</h1>
        <p className="t-sec">El inicio de sesión se construye en su propia tarea.</p>
        <Link href="/liquidaciones" className="btn btn-pri btn-lg">
          Volver a entrar
        </Link>
      </div>
    </main>
  );
}

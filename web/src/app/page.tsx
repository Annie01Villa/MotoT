import { redirect } from "next/navigation";

// Después del login, todos llegan a Liquidaciones.
export default function Inicio() {
  redirect("/liquidaciones");
}

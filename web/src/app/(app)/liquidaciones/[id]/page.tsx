import { Suspense } from "react";
import { Detalle } from "@/components/liquidaciones/Detalle";

export const metadata = { title: "Liquidación · CRM-MotoT" };

export default function PaginaDetalle() {
  return (
    <Suspense>
      <Detalle />
    </Suspense>
  );
}

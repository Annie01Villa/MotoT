import { Suspense } from "react";
import { Historial } from "@/components/liquidaciones/Historial";

export const metadata = { title: "Liquidaciones · CRM-MotoT" };

export default function PaginaLiquidaciones() {
  return (
    <Suspense>
      <Historial />
    </Suspense>
  );
}

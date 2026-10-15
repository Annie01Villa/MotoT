import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { LiquidacionesProvider } from "@/data/LiquidacionesProvider";
import { SesionProvider } from "@/lib/session";
import "./globals.css";

const inter = Inter({ variable: "--font-inter", subsets: ["latin"], weight: ["400", "500", "600"] });

export const metadata: Metadata = {
  title: "CRM-MotoT",
  description: "Supervisión y registro rápido de la flotilla de motos.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="es" className={inter.variable}>
      <body>
        <SesionProvider>
          <LiquidacionesProvider>{children}</LiquidacionesProvider>
        </SesionProvider>
      </body>
    </html>
  );
}

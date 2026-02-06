import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "Labour Platform",
  description: "Find work fast. Hire workers faster.",
};

type RootLayoutProps = {
  children: ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-950 text-slate-50">
        {children}
      </body>
    </html>
  );
}

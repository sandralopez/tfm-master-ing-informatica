import { Inter } from "next/font/google";
import { Header } from '../components/shared/Header';
import { Footer } from '../components/shared/Footer';

import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Explicabilidad CNN",
  description: "Genera predicciones de modelos de clasificación con redes neuronales convolucionales y añade explicabilidad",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Header />
          <div className="min-h-full">
            {children}
          </div>
        <Footer />
      </body>
    </html>
  );
}

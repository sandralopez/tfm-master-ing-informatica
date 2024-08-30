"use client"

import { Description } from "../components/shared/Description";

export default function Error() {
  return (
    <main>
      <Description header="Error 500: Ha ocurrido un error en el servidor" subheader="Ha ocurrido un error al procesar la petición." />
    </main>
  );
}

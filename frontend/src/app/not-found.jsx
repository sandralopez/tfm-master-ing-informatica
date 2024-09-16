import { Description } from "../components/shared/Description";

export default function NotFound() {
  return (
    <main>
      <Description header="Error 400: Página no encontrada" subheader="La página que has solicitado no existe" />
    </main>
  );
}

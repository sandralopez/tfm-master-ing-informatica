import { Description } from "../components/shared/Description";
import { FormServer } from "../components/home/FormServer";

export const revalidate = 60;

export default function Home() {
  return (
    <main>
      <Description header="Explicabilidad CNN" subheader="Explicabilidad aplicada a modelos de redes neuronales convolucionales" />
      <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <FormServer />
      </div>
    </main>
  );
}

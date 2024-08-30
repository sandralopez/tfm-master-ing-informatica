import { Description } from "../../components/shared/Description";

export default function About() {
  return (
    <main>
      <Description header="Acerca de Explicabilidad CNN" subheader="Proyecto Fin de Máster en Ingeniería Informática" />
      <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <p>Explicabilidad CNN: Clasificación de imágenes y explicabilidad</p>
        <p>Este proyecto Fin de Máster consiste ofrecer una forma fácil para realizar clasificación de imágenes utilizando modelos de redes neuronales convolucionales a los que aplicar librerías de interpretabilidad con el objetivo de explicar los resultados obtenidos.</p>
        <p>A través de esta página puedes seleccionar entre algunos modelos de clasificación ya entrenados y librerías de explicabilidad para aplicarlos a una imagen. La finalidad es la visualización de resultados de forma sencilla e intuitiva.</p>
        <p>Este proyecto es mi Trabajo Fin de Máster de Ingeniería Informática en la Universidad de Burgos.</p>
      </div>
    </main>
  );
}

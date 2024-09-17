import { Description } from "../../components/shared/Description";

export default function About() {
  return (
    <main>
      <Description header="Acerca de Explicabilidad CNN" subheader="Explicabilidad aplicada a modelos de redes neuronales convolucionales" />
      <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <p className="text-xl font-semibold my-4">Explicabilidad CNN: Clasificación de imágenes y explicabilidad</p>
        <p className="mb-2">Este proyecto es parte de mi Trabajo Final del Máster en Ingeniería Informática en la Universidad de Burgos.</p>
        <p className="mb-2"> El objetivo es ofrecer una forma sencilla de que los usuarios puedan ejecutar los modelos de redes neuronales disponibles a los que además se les aplica bibliotecas de explicabilidad para hacer comprensibles los resultados obtenidos.</p>
        <p className="mb-2">Este proyecto consta de varias partes creadas con distintas tecnologías. El frontend fue desarrollado con Next.js y como backend se tienen varios servicios desarrollados con FastApi. Las bibliotecas de explicabilidad incorporadas aplican la función Grad-CAM para generar un mapa de calor que muestre las partes más relevantes de la imagen para el resultado obtenido.</p>
        <p className="mb-2">La explicabilidad permite hacer más transparente el funcionamiento de los modelos, haciendo más sencilla su evaluación, su comparación o la detección de sesgos.</p>
      </div>
    </main>
  );
}

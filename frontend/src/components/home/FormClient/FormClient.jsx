"use client"

import { useState, useEffect } from 'react';
import { Message } from "../../shared/Message";

export const FormClient = ({ models, libraries }) => {
	const [selectedModel, setSelectedModel] = useState("");
	const [selectedLibrary, setSelectedLibrary] = useState("");
	const [libraryOptions, setLibraryOptions] = useState([]);
	const [file, setFile] = useState(null);
	const [isFormValid, setIsFormValid] = useState(false);
	const [resultData, setResultData] = useState([])
	const [isAccordionOpen, setIsAccordionOpen] = useState([]);
	const [dragging, setDragging] = useState(false);
	const [errors, setErrors] = useState([]);
	const [isLoading, setIsLoading] = useState(false);

	const handleModelChange = (e) => {
		const selectedModel = e.target.value;

		let modelLibrary = models?.find(model => model.id == selectedModel);
		let options = libraries?.filter(library => library.id == modelLibrary?.library);

		setErrors([]);
		setSelectedModel(selectedModel);
		setLibraryOptions(options);
	};

	const handleLibraryChange = (e) => {
		const selectedLibrary = e.target.value;

		setErrors([]);
		setSelectedLibrary(selectedLibrary);
	};

	const handleFileChange = (e) => {
		const selectedFile = e.target.files[0];

		setErrors([]);

		if (selectedFile) {
			const maxSize = 5 * 1024 * 1024;
			const allowedTypes = ['image/png', 'image/jpeg', 'image/gif'];

			if (!allowedTypes.includes(selectedFile.type)) {
				// Validar el formato de la imagen
				setErrors((prevErrors) => ([
					...prevErrors,
					'El archivo seleccionado debe ser una imagen en formato PNG, JPEG o GIF',
				]));

				return;
			}
			else if (selectedFile.size > maxSize) {
				// Validar el tamaño de la iamgen
				setErrors((prevErrors) => ([
					...prevErrors,
					'El tamaño de la imagen debe ser menor a 5MB',
				]));

				return;
			}
			else {
				setErrors([]);
				setFile(e.target.files[0]);
			}
		}
	};

	const handleDragLeave = (e) => {
		e.preventDefault();

		setDragging(false);
	};

	const handleDragOver = (e) => {
		e.preventDefault();

		setDragging(true);
	};

	const handleDrop = (e) => {
		e.preventDefault();

		setDragging(false);

		// Considerar sólo un archivo
		const droppedItem = e.dataTransfer.items[0];

		if (droppedItem) {
			if (droppedItem.kind === "file") {
				const file = droppedItem.getAsFile();
				setFile(file);
			}
		}
	};

	const handleSubmit = async (e) => {
		e.preventDefault();

	    if (!validate()) {
	      return;
	    }

		let modelName = models?.find(model => model.id == selectedModel).name;
		let libraryName = libraries?.find(library => library.id == selectedLibrary).name;

		const formData = new FormData();
		formData.append('model', modelName);
		formData.append('library', libraryName);
		formData.append('file', file);

		setIsLoading(true);

		try {
			const response = await fetch('/api/submitForm', {
				method: 'POST',
				body: formData,
			});

			const data = await response.json();

			if (response.status === 200) {
				setResultData([...resultData, data]);
				setIsAccordionOpen([...isAccordionOpen, true]);
			}
			else {
				setErrors([data.message])
			}

			setIsLoading(false);
		}
		catch(error) {
			setIsLoading(false);
			setErrors(['Ha ocurrido un error al enviar los datos: ' + error]);
		}
	};

	const toggleAcordeon = (index) => {
		setIsAccordionOpen(isAccordionOpen.map((item, i) => (i === index ? !item : item)));
	};

	const validate = () => {
		const newErrors = [];

		if (!selectedModel) {
			newErrors.push('Debe seleccionar un modelo');
		}

		if (!selectedLibrary) {
			newErrors.push('Debe seleccionar una biblioteca de explicabilidad');
		}

		if (!file) {
			newErrors.push('Debe seleccionar una imagen');
		}

		setErrors(newErrors);

		return newErrors.length > 0 ? false : true;
	};

  return (
	<>
		<form
			onSubmit={handleSubmit}
		>
			<div className="grid grid-cols-1 sm:grid-cols-2 gap-12">
				<div>
					{errors.length > 0 && (
						<Message
							type="error"
							title="Error"
							message={errors.map((error, index) => (
										<span key={index}>
											{error}
											<br />
										</span>
									))}
						/>
					)}
					<div className="sm:col-span-4">
						<label className="block">Selecciona un modelo</label>
						<select
							id="model"
							required
							name="model"
							onChange={handleModelChange}
							className="w-full bg-white rounded-md border-0 my-2.5 py-2.5 px-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-violet-600 sm:text-sm sm:leading-6"
						>
							<option key="" value="">Selecciona un modelo</option>
							{ models?.map((model) => {
								return (
									<option key={model.id} value={model.id}>
										{model.name}
									</option>
								);
							})}
						</select>
					</div>
					<div className="sm:col-span-4"> 
						<label className="block">
							Selecciona una librería de explicabilidad&nbsp;&nbsp;
							<span
								className="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10"
								title="Los resultados se muestran como un mapa de calor que indica qué partes de la imagen son más importantes para la predicción del modelo, resaltando en colores más cálidos las áreas clave."
							>
								Ver Información
							</span>
						</label>
						<select
							id="library"
							required
							name="library"
							onChange={handleLibraryChange}
							className="w-full bg-white rounded-md border-0 my-2.5 py-2.5 px-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-violet-600 sm:text-sm sm:leading-6"
						>
							<option value="">Selecciona una opción</option>
							{ selectedModel && (
								libraryOptions?.map((library) => (
									<option key={library.id} value={library.id}>
										{library.name}
									</option>
								)))
							}
						</select>
					</div>
					<div className="sm:col-span-4"> 
						<label className="block">Selecciona una imagen</label>
						<div 
							onDragLeave={handleDragLeave}
							onDragOver={handleDragOver}
							onDrop={handleDrop}
							className={`mt-2.5 flex justify-center rounded-lg border border-dashed px-6 py-10 ${dragging ? 'border-violet-700 bg-violet-50' : 'border-gray-900 bg-white'}`}
						>
							<div className="text-center">
								{file && (
									<p className="text-sm leading-6 text-gray-600">
									Archivo seleccionado: {file.name}
									</p>
								)}
								<div className="flex text-sm leading-6 text-gray-600 w-100">
									<label
										htmlFor="file-upload"
										className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
									>
										{file ? (
											<span>Sube otro archivo</span>
										) : (
											<span>Sube un archivo</span>
										)}

										<input
											id="file-upload"
											required
											name="file-upload"
											type="file"
											className="sr-only"
											onChange={handleFileChange}
										/>
									</label>
									<p className="pl-1">o arrástralo aquí</p>
								</div>
								<p className="text-xs leading-5 text-gray-600">PNG, JPG, GIF hasta 10MB</p>
							</div>
						</div>
					</div>
					<div className="text-center py-6">
					<input 
						type="submit" 
						disabled={isLoading}
						className={`rounded-2xl text-white py-2.5 px-3.5 ${isLoading ? 'bg-violet-300 cursor-not-allowed' : 'bg-violet-500 hover:bg-violet-700 cursor-pointer'}`}
						value="Aplicar"
					/>
					</div>
				</div> {/* Fin de la primera columna */}
				<div className="mt-4"> {/* Inicio de la segunda columna */}
					{
						isLoading && (
							<>
								<span className="animate-pulse delay-75 font-semibold text-xl">Cargando...</span>
							</>
						)
					}
					{
						resultData?.map((data, index) => (
							<div key={index} className="mt-4">
	          					<button
	          						type="button"
						            className="w-full rounded-2xl text-left bg-violet-500 text-white py-2 px-4 font-semibold"
						            onClick={() => toggleAcordeon(index)}
	          					>
	            					{`Resultados ${index + 1}`}
	          					</button>

	          					{isAccordionOpen[index] && (
	          						<div className="mt-4 pl-4">
          	 							<div>
											<div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
												<div>
													<span className="my-1 font-semibold">Clasificación: </span>
													<span className="pl-1">{data.prediction.label}</span>
												</div>
												<div>
													<span className="pl-1  font-semibold">Probabilidad: </span>
													<span className="pl-1">{data.prediction.confidence}</span>
												</div>
											</div>
											<div className="w-full mt-4">
												<div className="grid grid-cols-1 sm:grid-cols-2 place-items-center sm:place-items-start gap-6">
													<div>
														<img id="prevImage" src={`data:image/jpg;base64,${data.originalImage}`} />
													</div>
													<div>
														<img id="resultImage" src={`data:image/jpg;base64,${data.image}`} />
													</div>
												</div>
											</div>
										</div>
									</div>
								)}
							</div>
				    	))
					}
				</div>
			</div> {/* Fin de la grilla */}
		</form>
	</>
  )
}

"use client"

import { useState, useEffect } from 'react';

export const FormClient = ({ models, libraries }) => {
	const [selectedModel, setSelectedModel] = useState("");
	const [selectedLibrary, setSelectedLibrary] = useState("");
	const [libraryOptions, setLibraryOptions] = useState([]);
	const [file, setFile] = useState(null);
	const [isFormValid, setIsFormValid] = useState(false);
	const [resultData, setResultData] = useState([])
	const [isAccordionOpen, setIsAccordionOpen] = useState([]);

	const handleModelChange = (e) => {
		const selectedModel = e.target.value;

		let modelLibrary = models.find(model => model.id == selectedModel);
		let options = libraries.filter(library => library.id == modelLibrary?.library);

		setSelectedModel(selectedModel);
		setLibraryOptions(options);
	};

	const handleLibraryChange = (e) => {
		const selectedLibrary = e.target.value;

		setSelectedLibrary(selectedLibrary);
	};

	const handleFileChange = (e) => {
		setFile(e.target.files[0]);
	};

	const handleSubmit = async (e) => {
		e.preventDefault();

		let modelName = models.find(model => model.id == selectedModel).name;
		let libraryName = libraries.find(library => library.id == selectedLibrary).name;

		const formData = new FormData();
		formData.append('model', modelName);
		formData.append('library', libraryName);
		formData.append('file', file);

		try {
			const response = await fetch('/api/submitForm', {
				method: 'POST',
				body: formData,
			});

			const data = await response.json();

			setResultData([...resultData, data]);
			setIsAccordionOpen([...isAccordionOpen, false]);
		}
		catch(error) {
			console.log('Error: ', error);
		}
	};

	const toggleAcordeon = (index) => {
		setIsAccordionOpen(isAccordionOpen.map((item, i) => (i === index ? !item : item)));
	};

  return (
	<>
		<form
		onSubmit={handleSubmit}

		>
			<div className="grid grid-cols-1 sm:grid-cols-2 gap-12">
				<div>
					<div className="sm:col-span-4">
						<label className="block">Selecciona un modelo</label>
						<select
							id="model"
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
						<label className="block">Selecciona una librería de explicabilidad</label>
						<select
							id="library"
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
						<div className="mt-2.5 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
							<div className="text-center">
								<div className="mt-4 flex text-sm leading-6 text-gray-600">
									<label
										htmlFor="file-upload"
										className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
									>
										<span>Sube un archivo</span>
										<input 
											id="file-upload" 
											name="file-upload" 
											type="file" 
											className="sr-only"
											onChange={handleFileChange}
										/>
									</label>
									<p className="pl-1">o arrástralo</p>
								</div>
								<p className="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
							</div>
						</div>
					</div>
					<div className="text-center py-6">
					<input 
						type="submit" 
						className="rounded-2xl bg-violet-500 text-white py-2.5 px-3.5" 
						value="Aplicar"
						disabled={!(selectedModel && selectedLibrary && file)}
					/>
					</div>
				</div> {/* Fin de la primera columna */}
				<div className="mt-4"> {/* Inicio de la segunda columna */}
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
													<span className="pl-1  font-semibold">Confianza: </span>
													<span className="pl-1">{data.prediction.confidence}</span>
												</div>
											</div>
											<div className="w-full mt-4">
												<img id="prevImage" className="mx-auto" src="" />
												<img id="resultImage" className="mx-auto" src={`data:image/jpg;base64,${data.image}`} />
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

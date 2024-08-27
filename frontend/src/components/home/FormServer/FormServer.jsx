import { FormClient } from "../FormClient";

const getModels = async () => {
  const response = await fetch(`${process.env.API_HOST}/models`, {
    headers: new Headers({
      'x-api-key': process.env.API_KEY || ""
    })
  })

  const data = await response.json()

  return data
}

const getLibraries = async () => {
  const response = await fetch(`${process.env.API_HOST}/libraries`, {
    headers: new Headers({
      'x-api-key': process.env.API_KEY || ""
    })
  })

  const data = await response.json()

  return data
}

const submitData = async (formData) => {
    const response = await fetch(`${process.env.API_HOST}/predict`, {
      headers: new Headers({
        'x-api-key': process.env.API_KEY || ""
      }),
      method: 'POST',
      body: formData
    })

    const data = await response.json()

    return data
}

export async function FormServer() {
  const models = await getModels()
  const libraries = await getLibraries()

  return (
      <FormClient models={models} libraries={libraries} />
  );
}

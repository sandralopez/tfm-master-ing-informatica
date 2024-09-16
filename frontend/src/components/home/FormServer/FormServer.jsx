import { FormClient } from "../FormClient";

const getModels = async () => {
  if (process.env.SKIP_FETCH){
    return [];
  }

  const response = await fetch(`${process.env.API_HOST}/models`, {
    headers: new Headers({
      'x-api-key': process.env.API_KEY || ""
    })
  })

  const data = await response.json()

  return data
}

const getLibraries = async () => {
  if (process.env.SKIP_FETCH){
    return [];
  }

  const response = await fetch(`${process.env.API_HOST}/libraries`, {
    headers: new Headers({
      'x-api-key': process.env.API_KEY || ""
    })
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

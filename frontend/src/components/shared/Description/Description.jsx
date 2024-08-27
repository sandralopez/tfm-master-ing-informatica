export const Description = ({ header, subheader }) => {
	return (
    <header className="bg-white shadow">
      <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold tracking-tight text-gray-900">{ header }</h1>
        <h2 className="text-2xl font-medium tracking-tight text-gray-900">{ subheader }</h2>
      </div>
    </header>
	)
}

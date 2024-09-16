"use client"

export const Message = ({type="error", title, message}) => {
	const getColors = () => {
		switch (type) {
			case 'error':
				return 'bg-red-200 border-red-500 text-red-900';
			case 'success':
				return 'bg-green-200 border-green-500 text-green 900';
			case 'info':
				return 'bg-blue-200 border-blue-500 text-blue-900';
			default:
				return 'bg-gray-200 border-gray-500 text-blue-900';
		}
	};

	return (
		<div className={`${getColors()} border-t-4 rounded-b px-4 py-3 shadow-md my-2`} role="alert">
		  <div className="flex">
		    <div>
		      <p className="font-bold">{ title }</p>
		      <p className="text-sm">{ message }</p>
		    </div>
		  </div>
		</div>
	)
}


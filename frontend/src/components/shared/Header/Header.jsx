"use client"

import Link from 'next/link'
import { useState } from 'react';

export const Header = () => {
	const [isOpened, setIsOpened] = useState(false);

	return (
	  <nav className="bg-gray-50 shadow-inner">
	    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
	      <div className="flex h-16 items-center justify-between">
	        <div className="flex items-center">
	          <div className="hidden md:block">
	            <div className="ml-10 flex items-baseline space-x-4">
	              <Link href="/" className="rounded-md underline px-3 py-2 text-sm font-medium text-violet-500" aria-current="page">Inicio</Link>
	              <Link href="/about" className="rounded-md hover:underline px-3 py-2 text-sm font-medium text-gray-500 hover:text-violet-700">Acerca de</Link>
	            </div>
	          </div>
	        </div>
	        <div className="-mr-2 flex md:hidden">
	          <button
				type="button"
				className="relative inline-flex items-center justify-center rounded-md bg-violet-200 p-2 text-violet-700 hover:bg-violet-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
				aria-controls="mobile-menu"
				aria-expanded="false"
				onClick={() => setIsOpened(!isOpened)}
	          >
	            <span className="absolute -inset-0.5"></span>
	            <span className="sr-only">Abrir menú</span>
	            <svg className="block h-6 w-6" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" aria-hidden="true">
	              <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
	            </svg>
	            <svg className="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" aria-hidden="true">
	              <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
	            </svg>
	          </button>
	        </div>
	      </div>
	    </div>
	    {
			isOpened && (
			    <div className="md:hidden" id="mobile-menu">
			      <div className="space-y-1 px-2 pb-3 pt-2 sm:px-3">
			        <Link href="/" className="block rounded-md px-3 py-2 text-base font-medium text-gray-500 hover:bg-violet-500 hover:text-white" aria-current="page">Inicio</Link>
			        <Link href="/about" className="block rounded-md px-3 py-2 text-base font-medium text-gray-500 hover:bg-violet-500 hover:text-white">Acerca de</Link>
			      </div>
			    </div>
			)
	    }
	  </nav>
	)
}

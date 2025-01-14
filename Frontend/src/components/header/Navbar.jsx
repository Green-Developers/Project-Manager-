import React, { useState } from "react";

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div className="container mx-auto flex justify-between items-center relative">
      {/* عنوان */}
      <div className="text-2xl text-white font-bold flex items-center">
        مدیریت پروژه
      </div>

      {/* دکمه منوی موبایل */}
      <button
        className="text-white sm:hidden flex items-center"
        onClick={() => setMenuOpen(!menuOpen)}
      >
        <svg
          className="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M4 6h16M4 12h16m-7 6h7"
          ></path>
        </svg>
      </button>

      {/* منوی اصلی */}
      <div
        className={`${
          menuOpen ? "block" : "hidden"
        } sm:flex sm:items-center sm:gap-4 absolute sm:relative top-full sm:top-auto left-0 sm:left-auto w-full sm:w-auto bg-indigo-600 sm:bg-transparent z-10`}
      >
        <div className="flex flex-col sm:flex-row sm:items-center gap-4 p-4 sm:p-0">
          {/* فیلد جستجو */}
          <input
            type="text"
            placeholder="جستجوی پروژه..."
            className="px-3 py-2 rounded-md border border-gray-300 focus:ring focus:ring-blue-300 outline-none w-full sm:w-auto"
          />
          {/* دکمه جستجو */}
          <button className="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded-md">
            جستجو
          </button>
        </div>
      </div>
    </div>
  );
}
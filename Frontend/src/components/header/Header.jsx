import React from "react";
import Navbar from "./Navbar";

export default function Header({ test }) {
  console.log(test);
  return (
    <header className="bg-gradient-to-r from-violet-400 to-indigo-600 p-4 shadow-md">
      <Navbar />
    </header>
  );
}

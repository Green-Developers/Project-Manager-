import React from "react";
import Header from "../../header/Header";
import ProjectManager from "./ProjectManager";

const Home = () => {
  
  return (
    <div className="font-[Vazir] bg-gradient-to-br from-indigo-300 to-pink-300 min-h-screen flex flex-col">
      <Header  />
      <main className="flex-1 px-4 sm:px-6 lg:px-8">
        <ProjectManager />
      </main>
    </div>
  );
};

export default Home;

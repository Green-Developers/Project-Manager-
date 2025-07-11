import React, { useState } from "react";
import ProjectList from "./ProjectList";
import ProjectForm from "./ProjectForm";

const ProjectManager = () => {
  const [projects, setProjects] = useState([]);
  const [editingProject, setEditingProject] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);

  const addOrEditProject = (project) => {
    if (editingProject) {
      setProjects((prevProjects) =>
        prevProjects.map((p) => (p.id === project.id ? project : p))
      );
    } else {
      setProjects((prevProjects) => [
        ...prevProjects,
        { id: Date.now(), ...project },
      ]);
    }
    setEditingProject(null);
    setIsFormVisible(false);
  };

  const deleteProject = (id) => {
    setProjects((prevProjects) => prevProjects.filter((p) => p.id !== id));
  };

  const editProject = (project) => {
    setEditingProject(project);
    setIsFormVisible(true);
  };

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8">
      <button
        className="bg-green-500 text-white py-2 px-6 rounded-md mt-4 shadow-md hover:bg-green-600 transition-all"
        onClick={() => {
          setEditingProject(null);
          setIsFormVisible(true);
        }}
      >
        + ایجاد پروژه جدید
      </button>
      <ProjectList
        projects={projects}
        onDelete={deleteProject}
        onEdit={editProject}
      />
      {isFormVisible && (
        <ProjectForm
          project={editingProject}
          onSave={addOrEditProject}
          onCancel={() => setIsFormVisible(false)}
        />
      )}
    </div>
  );
};

export default ProjectManager;

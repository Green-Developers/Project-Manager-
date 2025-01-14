import React, { useState } from "react";
import { Link } from "react-router-dom";
import UserForm from "./UserForm";

const ProjectList = ({ projects, onDelete, onEdit }) => {
  const [isUserFormVisible, setIsUserFormVisible] = useState(false);
  const [selectedProject, setSelectedProject] = useState(null);

  const handleAddUser = (userName) => {
    alert(`کاربر "${userName}" به پروژه "${selectedProject.title}" اضافه شد.`);
    setIsUserFormVisible(false);
  };

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6 px-4 sm:px-6 lg:px-8">
      {projects.map((project) => (
        <div
          key={project.id}
          className="bg-gradient-to-br from-white to-gray-100 p-6 rounded-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition"
        >
          <h3 className="text-xl font-semibold mb-2 text-indigo-600">
            {project.title}
          </h3>
          <p className="text-gray-600 mb-2">تاریخ شروع: {project.startDate}</p>
          <p className="text-gray-600 mb-2">تاریخ پایان: {project.endDate}</p>
          <p className={`font-bold ${getStatusColor(project.status)}`}>
            وضعیت: {project.status}
          </p>
          <div className="mt-4 flex flex-wrap gap-2">
            <button
              className="bg-gradient-to-r from-indigo-500 to-purple-500 text-white py-2 px-4 rounded-full shadow-md hover:shadow-lg transform hover:scale-105 transition-all w-full sm:w-auto"
              onClick={() => onEdit(project)}
            >
              ویرایش
            </button>
            <button
              className="bg-gradient-to-r from-red-500 to-pink-500 text-white py-2 px-4 rounded-full shadow-md hover:shadow-lg transform hover:scale-105 transition-all w-full sm:w-auto"
              onClick={() => onDelete(project.id)}
            >
              حذف
            </button>
            <button
              className="bg-gradient-to-r from-blue-500 to-cyan-500 text-white py-2 px-4 rounded-full shadow-md hover:shadow-lg transform hover:scale-105 transition-all w-full sm:w-auto"
              onClick={() => {
                setSelectedProject(project);
                setIsUserFormVisible(true);
              }}
            >
              + کاربر
            </button>
            <Link
              to="/project_page"
              className="bg-gradient-to-r from-green-500 to-teal-500 text-white py-2 px-4 rounded-full shadow-md hover:shadow-lg transform hover:scale-105 transition-all w-full sm:w-auto"
            >
              مشاهده پروژه
            </Link>
          </div>
        </div>
      ))}
      {isUserFormVisible && (
        <UserForm
          onAddUser={handleAddUser}
          onCancel={() => setIsUserFormVisible(false)}
        />
      )}
    </div>
  );
};

const getStatusColor = (status) => {
  return status === "در حال انجام"
    ? "text-green-600"
    : status === "معلق"
    ? "text-yellow-500"
    : "text-red-600";
};

export default ProjectList;

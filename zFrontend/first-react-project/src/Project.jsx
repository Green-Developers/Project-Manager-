import React, { useState, useEffect } from "react";
import { FaXmark } from "react-icons/fa6";

function Project() {
  const [showModal, setShowModal] = useState(false);
  const [projects, setProjects] = useState([]);
  const [editingProjectId, setEditingProjectId] = useState(null);

  useEffect(() => {}, []);

  const renderProjects = () => {
    return projects.map((project) => (
      <div key={project.id} className="bg-white p-6 rounded-lg shadow-md card">
        <h3 className="text-xl font-semibold mb-2 text-blue-700">
          {project.title}
        </h3>
        <p className="text-gray-500 mb-2">تاریخ شروع: {project.startDate}</p>
        <p className="text-gray-500 mb-2">تاریخ پایان: {project.endDate}</p>
        <p className={`${getStatusColor(project.status)} font-bold`}>
          وضعیت: {project.status}
        </p>
        <div className="mt-4 flex gap-2">
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded-md btn"
            onClick={() => editProject(project.id)}
          >
            ویرایش
          </button>
          <button
            className="bg-red-500 text-white px-4 py-2 rounded-md btn"
            onClick={() => deleteProject(project.id)}
          >
            حذف
          </button>
        </div>
      </div>
    ));
  };

  const getStatusColor = (status) => {
    return status === "در حال انجام"
      ? "text-green-600"
      : status === "معلق"
        ? "text-yellow-500"
        : "text-red-600";
  };

  const showForm = (isEdit, project) => {
    setEditingProjectId(isEdit ? project.id : null);
    // $("#form-title").text(isEdit ? "ویرایش پروژه" : "ایجاد پروژه جدید");
    // $("#project-title").val(isEdit ? project.title : "");
    // $("#project-start").val(isEdit ? project.startDate : "");
    // $("#project-end").val(isEdit ? project.endDate : "");
    // $("#project-status").val(isEdit ? project.status : "در حال انجام");
    // $("#project-form").removeClass("hidden");
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    const title = $("#project-title").val();
    const startDate = $("#project-start").val();
    const endDate = $("#project-end").val();
    const status = $("#project-status").val();
    if (editingProjectId !== null) {
      const project = projects.find((p) => p.id === editingProjectId);
      Object.assign(project, { title, startDate, endDate, status });
    } else {
      setProjects([
        ...projects,
        { id: Date.now(), title, startDate, endDate, status },
      ]);
    }
    $("#project-form").addClass("hidden");
  };

  const editProject = (id) => {
    const project = projects.find((p) => p.id === id);
    showForm(true, project);
  };

  const deleteProject = (id) => {
    if (confirm("آیا مطمئن هستید که می‌خواهید این پروژه را حذف کنید؟")) {
      setProjects(projects.filter((p) => p.id !== id));
    }
  };

  return (
    <div>
      <header className="bg-gradient-to-r from-green-400 to-indigo-500 p-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center">
          <div className="text-2xl text-white font-bold flex items-center">
            مدیریت پروژه
          </div>
          <div className="hidden text-black sm:flex items-center gap-4">
            <input
              type="text"
              placeholder="جستجوی پروژه..."
              className="px-4 py-2 rounded-md border border-gray-300 focus:ring focus:ring-blue-300 outline-none"
            />
            <button className="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded-md">
              جستجو
            </button>
          </div>
        </div>
      </header>
      <main className="container mx-auto mt-8 px-4 ">
        <div className="mb-4 flex justify-start">
          <button
            id="create-project"
            className=" bg-green-500 text-white py-2 px-6 rounded-md"
            onClick={() => {
              setShowModal(true);
            }}
          >
            + ایجاد پروژه جدید
          </button>
        </div>
        <div
          id="projects"
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          {renderProjects()}
        </div>
      </main>
      <div
        id="project-form"
        className={`fixed inset-0 bg-black bg-opacity-50  items-center justify-center fade-in ${showModal ? "flex" : "hidden"}`}
      >
        <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
          <div className="flex justify-between">
            <h2 id="form-title" className="text-2xl font-bold mb-4">
              ایجاد پروژه جدید
            </h2>
            <button onClick={() => setShowModal(false)}>
              <FaXmark />
            </button>
          </div>
          <form id="project-details-form" onSubmit={handleFormSubmit}>
            <div className="mb-4">
              <label
                htmlFor="project-title"
                className="block text-sm font-medium text-gray-700"
              >
                عنوان پروژه
              </label>
              <input
                type="text"
                id="project-title"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                required
              />
            </div>
            <div className="mb-4">
              <label
                htmlFor="project-start"
                className="block text-sm font-medium text-gray-700"
              >
                تاریخ شروع
              </label>
              <input
                type="text"
                id="project-start"
                className="datepicker mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                required
              />
            </div>
            <div className="mb-4">
              <label
                htmlFor="project-end"
                className="block text-sm font-medium text-gray-700"
              >
                تاریخ پایان
              </label>
              <input
                type="text"
                id="project-end"
                className="datepicker mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                required
              />
            </div>
            <div className="mb-4">
              <label
                htmlFor="project-status"
                className="block text-sm font-medium text-gray-700"
              >
                وضعیت پروژه
              </label>
              <select
                id="project-status"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="در حال انجام">در حال انجام</option>
                <option value="معلق">معلق</option>
                <option value="تکمیل شده">تکمیل شده</option>
              </select>
            </div>
            <div className="flex justify-between">
              <button
                type="button"
                id="cancel-form"
                className="btn text-gray-700 bg-gray-200 hover:bg-gray-300 py-2 px-4 rounded-md"
                onClick={() => {}}
              >
                انصراف
              </button>
              <button
                type="submit"
                id="save-project"
                className="btn btn-blue text-white py-2 px-4 rounded-md"
              >
                ذخیره
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Project;

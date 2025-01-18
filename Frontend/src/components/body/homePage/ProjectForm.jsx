import React, { useState } from "react";
import DatePicker from "react-multi-date-picker";
import persian from "react-date-object/calendars/persian";
import persian_fa from "react-date-object/locales/persian_fa";

const ProjectForm = ({ project, onSave, onCancel }) => {
  const [formData, setFormData] = useState({
    title: project?.title || "",
    startDate: project?.startDate || null,
    endDate: project?.endDate || null,
    status: project?.status || "در حال انجام",
  });

  const handleSave = (e) => {
    e.preventDefault();
    if (!formData.startDate || !formData.endDate) {
      alert("لطفاً تاریخ‌های شروع و پایان را وارد کنید.");
      return;
    }
    onSave(formData);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-gradient-to-br from-gray-100 to-gray-200 p-8 rounded-lg shadow-2xl w-full max-w-md">
        <h2 className="text-2xl font-bold text-indigo-700 mb-4">
          {project ? "ویرایش پروژه" : "ایجاد پروژه جدید"}
        </h2>
        <form onSubmit={handleSave}>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">
              عنوان پروژه
            </label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) =>
                setFormData({ ...formData, title: e.target.value })
              }
              className="mt-1 block w-full rounded-lg border-gray-300 shadow-md focus:ring-indigo-500 focus:border-indigo-500"
              required
            />
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                تاریخ شروع
              </label>
              <DatePicker
                value={formData.startDate}
                onChange={(date) =>
                  setFormData({ ...formData, startDate: date?.format("YYYY/MM/DD") })
                }
                calendar={persian}
                locale={persian_fa}
                inputClass="mt-1 block w-full rounded-lg border-gray-300 shadow-md focus:ring-indigo-500 focus:border-indigo-500"
                format="YYYY/MM/DD"
                placeholder="تاریخ شروع را انتخاب کنید"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">
                تاریخ پایان
              </label>
              <DatePicker
                value={formData.endDate}
                onChange={(date) =>
                  setFormData({ ...formData, endDate: date?.format("YYYY/MM/DD") })
                }
                calendar={persian}
                locale={persian_fa}
                inputClass="mt-1 block w-full rounded-lg border-gray-300 shadow-md focus:ring-indigo-500 focus:border-indigo-500"
                format="YYYY/MM/DD"
                placeholder="تاریخ پایان را انتخاب کنید"
              />
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">
              وضعیت پروژه
            </label>
            <select
              value={formData.status}
              onChange={(e) =>
                setFormData({ ...formData, status: e.target.value })
              }
              className="mt-1 block w-full rounded-lg border-gray-300 shadow-md focus:ring-indigo-500 focus:border-indigo-500"
            >
              <option value="در حال انجام">در حال انجام</option>
              <option value="معلق">معلق</option>
              <option value="تکمیل شده">تکمیل شده</option>
            </select>
          </div>
          <div className="flex justify-between">
            <button
              type="button"
              onClick={onCancel}
              className="py-2 px-4 rounded-lg bg-gray-400 hover:bg-gray-500 text-white"
            >
              انصراف
            </button>
            <button
              type="submit"
              className="py-2 px-4 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white"
            >
              ذخیره
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ProjectForm;

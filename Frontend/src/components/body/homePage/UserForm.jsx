import React, { useState } from "react";

const UserForm = ({ onAddUser, onCancel }) => {
  const [userName, setUserName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!userName.trim()) {
      alert("نام کاربر را وارد کنید");
      return;
    }
    onAddUser(userName);
    setUserName("");
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-sm sm:max-w-md">
        <h2 className="text-xl font-bold mb-4">اضافه کردن کاربر</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-sm font-medium">نام کاربر</label>
            <input
              type="text"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              className="mt-1 block w-full border rounded-md p-2"
              placeholder="نام کاربر را وارد کنید"
            />
          </div>
          <div className="flex justify-between">
            <button
              type="button"
              onClick={onCancel}
              className="bg-gray-500 text-white py-2 px-4 rounded"
            >
              انصراف
            </button>
            <button
              type="submit"
              className="bg-indigo-600 text-white py-2 px-4 rounded"
            >
              اضافه کردن
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default UserForm;

import React, { useState } from "react";

const Card = ({ card, onOpenModal, onEdit, onDelete }) => {
  const [isUserModalVisible, setIsUserModalVisible] = useState(false);
  const [users, setUsers] = useState([]);

  const addUser = (userName) => {
    if (!userName.trim()) return;
    setUsers((prev) => [...prev, userName]);
    setIsUserModalVisible(false);
  };

  return (
    <div className="bg-white rounded-lg p-4 shadow-md card hover:shadow-lg transform transition-all hover:-translate-y-1">
      <h3 className="text-base font-semibold text-gray-800">{card.name}</h3>
      <p className="text-sm text-gray-600 mt-2">{card.description}</p>

      {/* نمایش لیست کاربران */}
      <div className="mt-4">
        <h4 className="text-sm font-semibold text-gray-700">کاربران:</h4>
        {users.length > 0 ? (
          <ul className="list-disc ml-4 mt-2 text-sm text-gray-600">
            {users.map((user, index) => (
              <li key={index} className="flex justify-between items-center">
                {user}
                <button
                  className="text-red-500 text-xs font-bold ml-2"
                  onClick={() => setUsers(users.filter((_, i) => i !== index))}
                >
                  ✖
                </button>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-sm text-gray-500 mt-2">کاربری اضافه نشده است.</p>
        )}
      </div>

      {/* دکمه‌ها */}
      <div className="flex flex-wrap justify-between gap-2 mt-4">
        <button
          className="bg-green-500 text-white text-xs py-2 px-4 rounded hover:bg-green-600 transition w-full sm:w-auto"
          onClick={() => onOpenModal(card)}
        >
          نظرات
        </button>
        <button
          className="bg-blue-500 text-white text-xs py-2 px-4 rounded hover:bg-blue-600 transition w-full sm:w-auto"
          onClick={() => setIsUserModalVisible(true)}
        >
          + کاربر
        </button>
        <button
          className="bg-yellow-500 text-white text-xs py-2 px-4 rounded hover:bg-yellow-600 transition w-full sm:w-auto"
          onClick={() => onEdit(card)}
        >
          ویرایش
        </button>
        <button
          className="bg-red-500 text-white text-xs py-2 px-4 rounded hover:bg-red-600 transition w-full sm:w-auto"
          onClick={() => onDelete(card.id)}
        >
          حذف
        </button>
      </div>

      {/* پنجره افزودن کاربر */}
      {isUserModalVisible && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-sm">
            <h3 className="text-lg font-bold mb-4">اضافه کردن کاربر</h3>
            <input
              type="text"
              placeholder="نام کاربر را وارد کنید"
              className="w-full border border-gray-300 rounded-lg p-2 mb-4"
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  addUser(e.target.value);
                  e.target.value = "";
                }
              }}
            />
            <div className="flex justify-end space-x-4">
              <button
                className="bg-red-500 text-white text-sm py-2 px-4 rounded hover:bg-red-600 transition"
                onClick={() => setIsUserModalVisible(false)}
              >
                انصراف
              </button>
              <button
                className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600 transition"
                onClick={() => {
                  const input = document.querySelector("input");
                  addUser(input.value);
                  input.value = "";
                }}
              >
                اضافه کردن
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Card;

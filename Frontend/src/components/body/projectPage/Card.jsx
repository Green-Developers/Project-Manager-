import React, { useState } from "react";

const Card = ({ card, onEdit }) => {
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

      {/* New section for additional details */}
      <p className="text-xs text-gray-500 mt-2">
        تاریخ شروع: {card.startDate || "نامشخص"}
      </p>
      <p className="text-xs text-gray-500 mt-2">
        تاریخ پایان: {card.endDate || "نامشخص"}
      </p>
      <p className="text-xs text-gray-500 mt-2">توسط: {card.employee}</p>
      {/* End of new section */}

      {/* دکمه‌ها */}
      <div className="flex flex-wrap justify-between gap-2 mt-4">
        <button
          className="bg-yellow-500 text-white text-xs py-2 px-4 rounded hover:bg-yellow-600 transition w-full sm:w-auto"
          onClick={() => onEdit(card)}
        >
          ویرایش
        </button>
      </div>

    </div>
  );
};

export default Card;

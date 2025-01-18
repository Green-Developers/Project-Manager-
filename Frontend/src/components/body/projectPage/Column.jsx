import React from "react";
import Card from "./Card";

const Column = ({ title, cards, onAddCard, onOpenModal, onEdit, onDelete, bgColor }) => {
  return (
    <div
      className="flex flex-col rounded-lg shadow-lg bg-gray-50 overflow-hidden"
      style={{ height: "calc(100vh - 150px)" }}
    >
      <div className={`${bgColor} text-white py-3 px-4 text-center font-bold`}>
        {title}
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {cards.map((card) => (
          <Card
            key={card.id}
            card={card}
            onOpenModal={onOpenModal}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        ))}
      </div>
      <button
        className="bg-blue-600 text-white text-sm py-2 px-4 rounded hover:bg-blue-700 m-4 transition-transform transform hover:scale-105 shadow-lg"
        onClick={onAddCard}
      >
        + افزودن کارت
      </button>
    </div>
  );
};

export default Column;

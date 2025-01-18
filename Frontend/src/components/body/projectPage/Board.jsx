import React, { useState, useEffect } from "react";
import Column from "./Column";
import Modal from "./Modal";

const Board = () => {
  const [isAccordionView, setIsAccordionView] = useState(false);
  const [expanded, setExpanded] = useState(null);
  const [columns, setColumns] = useState({
    todo: [],
    doing: [],
    done: [],
  });
  const [currentCard, setCurrentCard] = useState(null);
  const [isModalVisible, setIsModalVisible] = useState(false);

  // شناسایی حالت ریسپانسیو (آکاردئون یا سه ستونی)
  useEffect(() => {
    const handleResize = () => {
      setIsAccordionView(window.innerWidth < 1024); // عرض کمتر از 1024px
    };
    handleResize(); // برای بار اول
    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  // افزودن کارت جدید
  const addCard = (columnId) => {
    const taskName = prompt("عنوان تسک را وارد کنید:", "تسک جدید");
    if (!taskName) return;
    const taskDescription = prompt("توضیحات تسک را وارد کنید:", "جزئیات تسک...");
    if (!taskDescription) return;

    const newCard = { id: Date.now(), name: taskName, description: taskDescription };
    setColumns((prev) => ({
      ...prev,
      [columnId]: [...prev[columnId], newCard],
    }));
  };

  // ویرایش کارت
  const editCard = (columnId, card) => {
    const updatedName = prompt("عنوان جدید را وارد کنید:", card.name);
    if (!updatedName) return;

    const updatedDescription = prompt("توضیحات جدید را وارد کنید:", card.description);
    if (!updatedDescription) return;

    setColumns((prev) => ({
      ...prev,
      [columnId]: prev[columnId].map((c) =>
        c.id === card.id ? { ...c, name: updatedName, description: updatedDescription } : c
      ),
    }));
  };

  // حذف کارت
  const deleteCard = (columnId, cardId) => {
    setColumns((prev) => ({
      ...prev,
      [columnId]: prev[columnId].filter((c) => c.id !== cardId),
    }));
  };

  // نمایش مودال برای نظرات
  const openCommentModal = (card) => {
    setCurrentCard(card);
    setIsModalVisible(true);
  };

  // بستن مودال
  const closeCommentModal = () => {
    setCurrentCard(null);
    setIsModalVisible(false);
  };

  return (
    <div className="w-full max-w-7xl mx-auto p-4">
      {isAccordionView ? (
        // حالت آکاردئون برای صفحات کوچک
        <div className="space-y-4 rtl" dir="rtl">
          {Object.keys(columns).map((key) => (
            <div key={key}>
              <button
                className="w-full text-right bg-gray-200 py-2 px-4 rounded shadow"
                onClick={() => setExpanded(expanded === key ? null : key)}
              >
                {key === "todo" ? "کارها" : key === "doing" ? "در حال انجام" : "انجام شده"}
              </button>
              {expanded === key && (
                <div className="mt-2">
                  <Column
                    title={
                      key === "todo"
                        ? "کارها"
                        : key === "doing"
                        ? "در حال انجام"
                        : "انجام شده"
                    }
                    cards={columns[key]}
                    onAddCard={() => addCard(key)}
                    onEdit={(card) => editCard(key, card)}
                    onDelete={(cardId) => deleteCard(key, cardId)}
                    onOpenModal={openCommentModal}
                    bgColor={
                      key === "todo"
                        ? "bg-gradient-to-tr from-pink-400 to-pink-600"
                        : key === "doing"
                        ? "bg-gradient-to-tr from-yellow-300 to-yellow-500"
                        : "bg-gradient-to-tr from-green-400 to-green-600"
                    }
                  />
                </div>
              )}
            </div>
          ))}
        </div>
      ) : (
        // حالت سه ستونی برای صفحات بزرگ
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <Column
            title="کارها"
            cards={columns.todo}
            onAddCard={() => addCard("todo")}
            onEdit={(card) => editCard("todo", card)}
            onDelete={(cardId) => deleteCard("todo", cardId)}
            onOpenModal={openCommentModal}
            bgColor="bg-gradient-to-tr from-pink-400 to-pink-600"
          />
          <Column
            title="در حال انجام"
            cards={columns.doing}
            onAddCard={() => addCard("doing")}
            onEdit={(card) => editCard("doing", card)}
            onDelete={(cardId) => deleteCard("doing", cardId)}
            onOpenModal={openCommentModal}
            bgColor="bg-gradient-to-tr from-yellow-300 to-yellow-500"
          />
          <Column
            title="انجام شده"
            cards={columns.done}
            onAddCard={() => addCard("done")}
            onEdit={(card) => editCard("done", card)}
            onDelete={(cardId) => deleteCard("done", cardId)}
            onOpenModal={openCommentModal}
            bgColor="bg-gradient-to-tr from-green-400 to-green-600"
          />
        </div>
      )}

      {/* مودال نظرات */}
      {isModalVisible && (
        <Modal
          card={currentCard}
          onClose={closeCommentModal}
        />
      )}
    </div>
  );
};

export default Board;

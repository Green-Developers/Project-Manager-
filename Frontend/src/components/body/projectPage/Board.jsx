import React, { useState, useEffect } from "react";
import Column from "./Column";
import Modals from "./Modals";
import CommentsModal from "./CommentsModal";

const Board = () => {
  const [isAccordionView, setIsAccordionView] = useState(false);
  const [expanded, setExpanded] = useState(null);
  const [columns, setColumns] = useState({
    todo: [],
    doing: [],
    done: [],
  });
  const [currentCard, setCurrentCard] = useState(null);
  const [isAddCardModalVisible, setIsAddCardModalVisible] = useState(false);
  const [newCardInfo, setNewCardInfo] = useState({
    name: "",
    description: "",
    employee: "",
    status: "todo",
    startDate: null,
    endDate: null,
  });
  const [isEditMode, setIsEditMode] = useState(false);
  const [isCommentModalVisible, setIsCommentModalVisible] = useState(false);
  const [showEmployeeList, setShowEmployeeList] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      setIsAccordionView(window.innerWidth < 1024);
    };
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const addCard = () => {
    setNewCardInfo({
      name: "",
      description: "",
      employee: "",
      status: "todo",
      startDate: null,
      endDate: null,
    });
    setIsEditMode(false);
    setIsAddCardModalVisible(true);
  };

  const saveCard = () => {
    if (!newCardInfo.name.trim() || !newCardInfo.description.trim()) return;

    const targetColumnId = newCardInfo.status;

    if (isEditMode) {
      setColumns((prev) => {
        const updatedColumns = {
          ...prev,
          [currentCard.status]: prev[currentCard.status].filter(
            (card) => card.id !== currentCard.id
          ),
        };
        updatedColumns[targetColumnId] = [
          ...updatedColumns[targetColumnId],
          { ...currentCard, ...newCardInfo },
        ];
        return updatedColumns;
      });
    } else {
      const newCard = {
        id: Date.now(),
        ...newCardInfo,
      };
      setColumns((prev) => ({
        ...prev,
        [targetColumnId]: [...prev[targetColumnId], newCard],
      }));
    }

    setIsAddCardModalVisible(false);
  };

  const editCard = (columnId, card) => {
    setCurrentCard(card);
    setNewCardInfo({ ...card });
    setIsEditMode(true);
    setIsAddCardModalVisible(true);
  };

  const deleteCard = (columnId, cardId) => {
    setColumns((prev) => ({
      ...prev,
      [columnId]: prev[columnId].filter((c) => c.id !== cardId),
    }));
  };

  const getCardTitles = () => {
    return Object.keys(columns)
      .flatMap((key) => columns[key].map((card) => card.name));
  };

  return (
    <div className="w-full max-w-7xl mx-auto p-4">
      {isAccordionView ? (
        <div className="space-y-4 rtl" dir="rtl">
          {Object.keys(columns).map((key) => (
            <div key={key}>
              <button
                className="w-full text-right bg-gray-200 py-2 px-4 rounded shadow"
                onClick={() => setExpanded(expanded === key ? null : key)}
              >
                {key === "todo"
                  ? "کارها"
                  : key === "doing"
                  ? "در حال انجام"
                  : "انجام شده"}
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
                    onAddCard={key === "todo" ? addCard : null}
                    onEdit={(card) => editCard(key, card)}
                    onDelete={(cardId) => deleteCard(key, cardId)}
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
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {Object.keys(columns).map((key) => (
            <Column
              key={key}
              title={
                key === "todo"
                  ? "کارها"
                  : key === "doing"
                  ? "در حال انجام"
                  : "انجام شده"
              }
              cards={columns[key]}
              onAddCard={key === "todo" ? addCard : null}
              onEdit={(card) => editCard(key, card)}
              onDelete={(cardId) => deleteCard(key, cardId)}
              bgColor={
                key === "todo"
                  ? "bg-gradient-to-tr from-pink-400 to-pink-600"
                  : key === "doing"
                  ? "bg-gradient-to-tr from-yellow-300 to-yellow-500"
                  : "bg-gradient-to-tr from-green-400 to-green-600"
              }
            />
          ))}
        </div>
      )}

      {/* دکمه‌های پایین */}
      <button
        className="fixed bottom-28 left-4 bg-purple-600 text-white p-3 mb-5 rounded-full shadow-lg hover:bg-purple-700 transition"
        onClick={() => alert("این دکمه عملکرد دیگری دارد!")}
      >
        دکمه جدید
      </button>
      <button
        className="fixed bottom-16 left-4 bg-green-600 text-white p-3 mb-3 rounded-full shadow-lg hover:bg-green-700 transition"
        onClick={() => setShowEmployeeList(!showEmployeeList)}
      >
        نمایش کاربران
      </button>
      <button
        className="fixed bottom-4 left-4 bg-blue-600 text-white p-3 rounded-full shadow-lg hover:bg-blue-700 transition"
        onClick={() => setIsCommentModalVisible(true)}
      >
        نظر دهید
      </button>

      {/* نمایش لیست کاربران */}
      {showEmployeeList && (
        <div className="absolute bottom-40 left-4 bg-white p-4 rounded-lg shadow-lg w-64">
          <h3 className="text-lg font-bold mb-2">لیست کاربران</h3>
          <ul className="space-y-2">
            {/* اینجا لیست کاربرا رو بزار */}
            {["Ali", "Sara", "Reza"].map((employee, index) => (
              <li key={index} className="text-gray-700">
                {employee}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* مدال‌ها */}
      <CommentsModal
        isVisible={isCommentModalVisible}
        onClose={() => setIsCommentModalVisible(false)}
        onSubmit={(newComment) => console.log("New comment:", newComment)}
        cardTitles={getCardTitles()}
        username="نام کاربر"
      />

      <Modals
        isAddCardModalVisible={isAddCardModalVisible}
        setIsAddCardModalVisible={setIsAddCardModalVisible}
        newCardInfo={newCardInfo}
        setNewCardInfo={setNewCardInfo}
        isEditMode={isEditMode}
        saveCard={saveCard}
      />
    </div>
  );
};

export default Board;

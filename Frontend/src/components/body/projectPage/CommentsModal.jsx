import React, { useState } from "react";

const CommentsModal = ({ isVisible, onClose, onSubmit, cardTitles, username }) => {
  const [comment, setComment] = useState("");
  const [selectedCard, setSelectedCard] = useState(""); // کارت انتخاب‌شده
  const [comments, setComments] = useState([]);

  const handleAddComment = () => {
    if (comment.trim() && selectedCard && username) {
      const newComment = {
        card: selectedCard,
        text: comment,
        user: username,  // اضافه کردن اسم کاربر
      };
      setComments((prev) => [newComment, ...prev]);
      onSubmit(newComment);
      setComment("");
      setSelectedCard("");
    }
  };

  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h3 className="text-lg font-bold mb-4">ارسال نظر</h3>
        <select
          value={selectedCard}
          onChange={(e) => setSelectedCard(e.target.value)}
          className="w-full border border-gray-300 rounded-lg p-2 mb-4 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="" disabled>
            انتخاب کارت
          </option>
          {cardTitles.map((title, index) => (
            <option key={index} value={title}>
              {title}
            </option>
          ))}
        </select>
        <textarea
          placeholder="نظر خود را بنویسید..."
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="w-full border border-gray-300 rounded-lg p-4 mb-4 h-32 resize-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        />
        <div className="flex justify-between mb-4">
          <button
            className="bg-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-600 transition duration-300"
            onClick={onClose}
          >
            بستن
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-300"
            onClick={handleAddComment}
          >
            ارسال
          </button>
        </div>
        <div className="max-h-60 overflow-y-auto">
          {comments.map((c, index) => (
            <div key={index} className="border-b border-gray-300 pb-2 mb-2">
              <p className="font-bold text-gray-800">تسک: {c.card}</p>
              <p className="text-sm text-gray-600">کاربر: {c.user}</p> {/* نمایش اسم کاربر */}
              <p className="text-sm text-gray-700">{c.text}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CommentsModal;

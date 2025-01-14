import React, { useState, useEffect } from "react";

const Modal = ({ card, onClose }) => {
  const [comments, setComments] = useState([]);
  const [commentInput, setCommentInput] = useState("");

  const addComment = () => {
    if (commentInput.trim()) {
      setComments((prev) => [...prev, commentInput]);
      setCommentInput("");
    }
  };

  useEffect(() => {
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = "auto";
    };
  }, []);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h3 className="text-lg font-bold mb-4">{card.name}</h3>
        <div className="max-h-40 overflow-y-auto border border-gray-300 rounded-lg p-3 bg-gray-100 mb-4">
          {comments.map((comment, index) => (
            <div
              key={index}
              className="bg-gray-200 p-2 rounded mb-2 text-sm text-gray-800"
            >
              {comment}
            </div>
          ))}
        </div>
        <textarea
          value={commentInput}
          onChange={(e) => setCommentInput(e.target.value)}
          className="w-full border border-gray-300 rounded-lg p-2 mb-4"
          rows="2"
          placeholder="نظر خود را وارد کنید..."
        />
        <div className="flex justify-end space-x-4">
          <button
            className="bg-red-500 text-white text-sm py-2 px-4 rounded hover:bg-red-600 transition"
            onClick={onClose}
          >
            لغو
          </button>
          <button
            className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600 transition"
            onClick={addComment}
          >
            ارسال
          </button>
        </div>
      </div>
    </div>
  );
};

export default Modal;

import React from 'react';

function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-purple-700 via-purple-500 to-blue-300 p-6 rtl">
      <div className="flex space-x-4 space-x-reverse w-full max-w-7xl">
        <div className="bg-white rounded-lg shadow-lg w-1/3 flex flex-col mx-2">
          <div className="box-header">کارها</div>
          <div id="todo-column" className="card-container flex-1 overflow-y-auto p-4"></div>
          <button className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600 m-4" onClick={() => addCard('todo-column')}>افزودن کارت</button>
        </div>
        <div className="bg-white rounded-lg shadow-lg w-1/3 flex flex-col mx-2">
          <div className="box-header">در حال انجام</div>
          <div id="doing-column" className="card-container flex-1 overflow-y-auto p-4"></div>
          <button className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600 m-4" onClick={() => addCard('doing-column')}>افزودن کارت</button>
        </div>
        <div className="bg-white rounded-lg shadow-lg w-1/3 flex flex-col mx-2">
          <div className="box-header">انجام شده</div>
          <div id="done-column" className="card-container flex-1 overflow-y-auto p-4"></div>
          <button className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600 m-4" onClick={() => addCard('done-column')}>افزودن کارت</button>
        </div>
      </div>
      <div id="comment-modal" className="modal hidden">
        <div className="modal-content">
          <h3 className="text-lg font-semibold mb-4">نظرات</h3>
          <div id="comment-list" className="comment-list"></div>
          <textarea id="comment-input" className="w-full border border-gray-300 rounded-lg p-2" rows="2" placeholder="نظر خود را وارد کنید..."></textarea>
          <div className="flex justify-end space-x-14 space-x-reverse mt-4">
            <button className="bg-red-600 text-white text-sm py-2 px-4 mr-3 rounded hover:bg-gray-500" onClick={closeCommentModal}>لغو</button>
            <button className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600" onClick={addComment}>ارسال</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
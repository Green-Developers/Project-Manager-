import React, { useState, useEffect } from "react"; 
import { useParams } from "react-router-dom"; 
import Column from "./Column"; 
import Modal from "./Modal"; 
import Card from "./Card"; 
import DatePicker from "react-multi-date-picker"; 
import persian from "react-date-object/calendars/persian"; 
import persian_fa from "react-date-object/locales/persian_fa"; 
import {convertJalaliToGregorianISO , convertPersianToEnglish} from "../../../Utils/utils" 
 
 
 
 
// تابع Project به صورت جداگانه 
const Board = ({ projectId ,card}) => { 
  const [formData, setFormData] = useState({ 
    name: card?.name || "", 
    description:card?.description , 
    start_date: card?.start_date || null, 
    end_date: card?.end_date || null, 
    employee_id: card?.employee_id || null , 
    status: card?.status || "در حال انجام", 
    project_id: card?.project_id 
  }); 
 
  const [newCardInfo, setNewCardInfo] = useState({ 
    name: "", 
    description: "", 
    employee_id: "", 
    status: "todo", 
    start_date: null, 
    end_date: null, 
  }); 
 
  const createNewTask = async (formData) => { 
     
   
    // Convert and assign project_id to formData 
    const updatedFormData = { 
      ...newCardInfo, 
      start_date: convertJalaliToGregorianISO( 
        convertPersianToEnglish(newCardInfo.start_date) 
      ), 
      end_date: convertJalaliToGregorianISO( 
        convertPersianToEnglish(newCardInfo.end_date) 
      ), 
      project_id: projectId, 
    }; 
   
    try { 
      const res = await fetch(`http://127.0.0.1:8000/tasks/${projectId}/tasks`, { 
        method: "POST", 
        headers: { 
          "Content-Type": "application/json", 
          Authorization: "Bearer " + localStorage.getItem("token"), 
        }, 
        body: JSON.stringify(updatedFormData), // Use the updated formData 
      }); 
   
      if (res.status === 200) { 
        const resJson = await res.json(); 
        console.log("Registration successful", resJson); 
        alert("Task created successfully"); 
      } else { 
        const resJson = await res.json(); 
        console.log(resJson); 
      } 
    } catch (e) { 
      console.log("Error:", e); 
      alert("An error occurred. Please try again."); 
    } 
  }; 
const [downloadLink, setDownloadLink] = useState(null); 
 
const fetchAndDownloadFile = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/projects/export", {
      method: "GET",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"), // اگر توکن نیاز دارید
      },
    });

    if (response.ok) {
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);

      // ایجاد یک لینک برای دانلود فایل
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "projects.xlsx"); // نام فایل دانلودی
      document.body.appendChild(link);
      link.click();
      link.remove();

      // آزادسازی URL
      window.URL.revokeObjectURL(url);
    } else {
      console.error("Failed to download the file");
    }
  } catch (error) {
    console.error("Error:", error);
  }
};

  const [isAccordionView, setIsAccordionView] = useState(false); 
  const [expanded, setExpanded] = useState(null); 
  const [columns, setColumns] = useState({ 
    todo: [], 
    doing: [], 
    done: [], 
  }); 
  const [currentCard, setCurrentCard] = useState(null); 
  const [isModalVisible, setIsModalVisible] = useState(false); 
  const [isAddCardModalVisible, setIsAddCardModalVisible] = useState(false); 
 
  const [isEditMode, setIsEditMode] = useState(false); 
  const [isCommentModalVisible, setIsCommentModalVisible] = useState(false); 
  const [comment, setComment] = useState(""); 
  const [comments, setComments] = useState([]); 
 
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
 
  const addCard = () => { 
    setNewCardInfo({ 
      name: "", 
      description: "", 
      employee_id: "", 
      status: "todo", 
      start_date: null, 
      end_date: null, 
    }); 
    setIsEditMode(false); 
    setIsAddCardModalVisible(true);


}; 
  const saveCard = () => { 
    if (!newCardInfo.name.trim() || !newCardInfo.description.trim()) return; 
 
    const targetColumnId = newCardInfo.status; // ستون مناسب بر اساس وضعیت 
 
    if (isEditMode) { 
      setColumns((prev) => { 
        const updatedColumns = { 
          ...prev, 
          [currentCard.status]: prev[currentCard.status].filter((card) => card.id !== currentCard.id), 
        }; 
        updatedColumns[targetColumnId] = [ 
          ...updatedColumns[targetColumnId], 
          { ...currentCard, ...newCardInfo }, 
        ]; 
        return updatedColumns; 
      }); 
    } else { 
      const newCard = { 
        id: Date.now(), // نیاز به تغییر به شناسه یکتا داریم 
        ...newCardInfo, 
      }; 
      setColumns((prev) => ({ 
        ...prev, 
        [targetColumnId]: [...prev[targetColumnId], newCard], 
      })); 
    } 
    setIsAddCardModalVisible(false); 
    createNewTask(); 
  }; 
 
  const editCard = (columnId, card) => { 
    setCurrentCard(card); 
    setNewCardInfo({ ...card }); 
    setIsEditMode(true); 
    setIsAddCardModalVisible(true); 
  }; 
 
  // حذف کارت 
  const deleteCard = (columnId, cardId) => { 
    setColumns((prev) => ({ 
      ...prev, 
      [columnId]: prev[columnId].filter((c) => c.id !== cardId), 
    })); 
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
        // حالت سه ستونی برای صفحات بزرگ 
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
 
      {isAddCardModalVisible && (

<div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"> 
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md"> 
            <h3 className="text-lg font-bold mb-4"> 
              {isEditMode ? "ویرایش کارت" : "افزودن کارت جدید"} 
            </h3> 
            <input 
              type="text" 
              placeholder="عنوان کارت" 
              value={newCardInfo.name} 
              onChange={(e) => 
                setNewCardInfo((prev) => ({ ...prev, name: e.target.value })) 
              } 
              className="w-full border border-gray-300 rounded-lg p-2 mb-4" 
            /> 
            <textarea 
              placeholder="توضیحات کارت" 
              value={newCardInfo.description} 
              onChange={(e) => 
                setNewCardInfo((prev) => ({ 
                  ...prev, 
                  description: e.target.value, 
                })) 
              } 
              className="w-full border border-gray-300 rounded-lg p-2 mb-4" 
              rows="3" 
            /> 
            <input 
              type="text" 
              placeholder="نام کارمند" 
              value={newCardInfo.employee_id} 
              onChange={(e) => 
                setNewCardInfo((prev) => ({ 
                  ...prev, 
                  employee_id: e.target.value, 
                })) 
              } 
              className="w-full border border-gray-300 rounded-lg p-2 mb-4" 
            /> 
            <div className="grid grid-cols-2 gap-4 mb-4"> 
              <div> 
                <label className="block text-sm font-medium text-gray-700"> 
                  تاریخ شروع 
                </label> 
                <DatePicker 
                  value={newCardInfo.start_date} 
                  onChange={(date) => 
                    setNewCardInfo((prev) => ({ 
                      ...prev, 
                      start_date: date?.format("YYYY/MM/DD"), 
                    })) 
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
                  value={newCardInfo.end_date} 
                  onChange={(date) => 
                    setNewCardInfo((prev) => ({ 
                      ...prev, 
                      end_date: date?.format("YYYY/MM/DD"), 
                    })) 
                  } 
                  calendar={persian} 
                  locale={persian_fa} 
                  inputClass="mt-1 block w-full rounded-lg border-gray-300 shadow-md focus:ring-indigo-500 focus:border-indigo-500" 
                  format="YYYY/MM/DD" 
                  placeholder="تاریخ پایان را انتخاب کنید" 
                /> 
              </div> 
            </div> 
            <select 
              value={newCardInfo.status} 
              onChange={(e) => 
                setNewCardInfo((prev) => ({ 
                  ...prev, 
                  status: e.target.value, 
                })) 
              } 
              className="w-full border border-gray-300 rounded-lg p-2 mb-4" 
            > 
              <option value="todo">معلق</option> 
              <option value="doing">در حال انجام</option> 
              <option value="done">انجام شده</option> 
            </select> 
            <div className="flex justify-end space-x-4"> 
              <button 
                className="bg-red-500 text-white text-sm py-2 px-4 rounded hover:bg-red-600 transition" 
                onClick={() => setIsAddCardModalVisible(false)} 
              > 
                لغو 
              </button> 
              <button

className="bg-blue-500 text-white text-sm py-2 px-4 rounded hover:bg-blue-600 transition" 
                onClick={saveCard} 
              > 
               ذخیره  
              </button> 
            </div> 
          </div> 
        </div> 
      )} 
      <button
  onClick={fetchAndDownloadFile}
  className="bg-green-600 text-white p-3 rounded-full shadow-lg hover:bg-green-700 transition"
>
  دانلود فایل
</button>

 
      {/* دکمه نظردهی */} 
      <button 
        className="fixed bottom-4 left-4 bg-blue-600 text-white p-3 rounded-full shadow-lg hover:bg-blue-700 transition" 
        onClick={() => setIsCommentModalVisible(true)} 
      > 
        نظر دهید 
      </button> 
      {isCommentModalVisible && ( 
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"> 
          <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg"> 
            <h3 className="text-lg font-bold mb-4">ارسال نظر</h3> 
            <textarea 
              placeholder="نظر خود را بنویسید..." 
              value={comment} 
              onChange={(e) => setComment(e.target.value)} 
              className="w-full border border-gray-300 rounded-lg p-2 mb-4" 
              rows="4" 
            /> 
            <div className="flex justify-between"> 
              <button 
                className="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600 transition" 
                onClick={() => setIsCommentModalVisible(false)} 
              > 
                بستن 
              </button> 
              <button 
                className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition" 
                onClick={() => { 
                  if (comment.trim()) { 
                    setComments((prev) => [comment, ...prev]); 
                    setComment(""); 
                  } 
                }} 
              > 
                ارسال 
              </button> 
            </div> 
            <div className="mt-4"> 
              {comments.map((c, index) => ( 
                <p key={index} className="border-b border-gray-300 pb-2 mb-2"> 
                  {c} 
                </p> 
              ))} 
            </div> 
          </div> 
        </div> 
      )} 
    </div> 
  ); 
}; 
 
export default Board;
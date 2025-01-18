import React, { useState } from "react";
import DatePicker from "react-multi-date-picker";
import persian from "react-date-object/calendars/persian";
import persian_fa from "react-date-object/locales/persian_fa";

const Modals = ({
  isAddCardModalVisible,
  setIsAddCardModalVisible,
  newCardInfo,
  setNewCardInfo,
  isEditMode,
  saveCard,
  employeeList = ["Ali", "Sara", "Reza", "Mina"], // لیست فرضی
}) => {
  const [filteredEmployees, setFilteredEmployees] = useState([]);

  const handleEmployeeInputChange = (e) => {
    const value = e.target.value;
    setNewCardInfo((prev) => ({ ...prev, employee: value }));

    // فیلتر کردن لیست کارمندان بر اساس ورودی
    const filtered = employeeList.filter((employee) =>
      employee.toLowerCase().includes(value.toLowerCase())
    );
    setFilteredEmployees(filtered);
  };

  const handleEmployeeFocus = () => {
    // نمایش کل لیست هنگام کلیک روی تکست‌باکس
    setFilteredEmployees(employeeList);
  };

  return isAddCardModalVisible ? (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
        <h3 className="text-lg font-bold mb-4">
          {isEditMode ? "ویرایش کارت" : "اضافه کردن کارت جدید"}
        </h3>
        <div className="space-y-4">
          <input
            type="text"
            placeholder="نام کارت"
            value={newCardInfo.name}
            onChange={(e) =>
              setNewCardInfo((prev) => ({ ...prev, name: e.target.value }))
            }
            className="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
          <textarea
            placeholder="توضیحات"
            value={newCardInfo.description}
            onChange={(e) =>
              setNewCardInfo((prev) => ({
                ...prev,
                description: e.target.value,
              }))
            }
            className="w-full border border-gray-300 rounded-lg p-2 h-20 resize-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
          <div className="relative">
            <input
              type="text"
              placeholder="نام کارمند"
              value={newCardInfo.employee}
              onChange={handleEmployeeInputChange}
              onFocus={handleEmployeeFocus} // افزودن این رویداد
              className="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />
            {filteredEmployees.length > 0 && (
              <ul className="absolute bg-white border border-gray-300 w-full rounded-lg shadow-lg max-h-40 overflow-y-auto z-10">
                {filteredEmployees.map((employee, index) => (
                  <li
                    key={index}
                    onClick={() => {
                      setNewCardInfo((prev) => ({
                        ...prev,
                        employee: employee,
                      }));
                      setFilteredEmployees([]); // پاک کردن لیست پیشنهادات
                    }}
                    className="p-2 hover:bg-blue-100 cursor-pointer"
                  >
                    {employee}
                  </li>
                ))}
              </ul>
            )}
          </div>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                تاریخ شروع
              </label>
              <DatePicker
                value={newCardInfo.startDate}
                onChange={(date) =>
                  setNewCardInfo((prev) => ({
                    ...prev,
                    startDate: date?.format("YYYY/MM/DD"),
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
                value={newCardInfo.endDate}
                onChange={(date) =>
                  setNewCardInfo((prev) => ({
                    ...prev,
                    endDate: date?.format("YYYY/MM/DD"),
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
              setNewCardInfo((prev) => ({ ...prev, status: e.target.value }))
            }
            className="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="todo">معلق</option>
            <option value="doing">در حال انجام</option>
            <option value="done">انجام شده</option>
          </select>
        </div>
        <div className="flex justify-between mt-4">
          <button
            className="bg-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-600 transition duration-300"
            onClick={() => setIsAddCardModalVisible(false)}
          >
            بستن
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-300"
            onClick={saveCard}
          >
            {isEditMode ? "ذخیره تغییرات" : "افزودن"}
          </button>
        </div>
      </div>
    </div>
  ) : null;
};

export default Modals;


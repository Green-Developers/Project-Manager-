import React, { useEffect, useState } from "react";
import Board from "./Board";
import { useParams } from "react-router-dom";
import Card from "./Card";

const Project = () => {
  const { projectId } = useParams(); // گرفتن projectId از URL
  const [tasks, setTasks] = useState([]); // ذخیره تسک‌ها
  const [loading, setLoading] = useState(false); // مدیریت وضعیت بارگذاری
  const [error, setError] = useState(null); // مدیریت خطاها

  // واکشی تسک‌ها بر اساس projectId
  useEffect(() => {
    async function fetchTasks() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(
          `http://127.0.0.1:8000/tasks/${projectId}/tasks`,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: "Bearer " + localStorage.getItem("token"),
            },
            method: "GET",
          }
        );
        if (!res.ok) {
          throw new Error(`خطا در واکشی تسک‌ها: ${res.statusText}`);
        }
        const resJson = await res.json();
        setTasks(resJson); // ذخیره داده‌های تسک‌ها در حالت
      } catch (error) {
        setError(error.message); // ذخیره پیام خطا
      } finally {
        setLoading(false); // پایان بارگذاری
      }
    }
    fetchTasks();
  }, [projectId]);

 

  return (
    <div className="bg-gradient-to-r from-blue-500 via-purple-500 to-purple-700 min-h-screen flex justify-center items-start p-4 sm:p-6">
      {/* ارسال داده‌های تسک‌ها به Board */}
      <Board projectId={projectId} />
      <Card cards={tasks}/>
    </div>
  );
};

export default Project;
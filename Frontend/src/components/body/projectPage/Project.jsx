import React, { useEffect } from "react";
import Board from "./Board";
import { useParams } from "react-router-dom";

const Project = () => {
  const { projectId } = useParams();
  console.log(projectId);

  useEffect(() => {
    async function getProject() {
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
        const resJson = await res.json();
        console.log(resJson);
      } catch (error) {}
    }
    getProject();
  }, []);
  return (
    <div className="bg-gradient-to-r from-blue-500 via-purple-500 to-purple-700 min-h-screen flex justify-center items-start p-4 sm:p-6">
      <Board projectId={projectId}/>
    </div>
  );
};

export default Project;

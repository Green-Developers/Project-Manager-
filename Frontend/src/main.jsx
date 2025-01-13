import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import SignUp from "./SignUp";
import SignIn from "./signIn";
import Project from "./Project";
import Home from "./Home";
import App from "./App";
import { BrowserRouter, Routes, Route } from "react-router";

const container = document.getElementById("root");
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        {/* <Route path="/signup" element={<SignUp />} /> */}
        <Route path="/signin" element={<SignIn />} />
        <Route path="/home" element={<Home />} />
        <Route path="/project" element={<Project />} />
        <Route path="/" index element={<SignUp />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

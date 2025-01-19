import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

function SignIn() {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  let navigate = useNavigate();

  async function signIn(e) {
    e.preventDefault();
    try {
      const formData = new URLSearchParams();
      formData.append("username", userName);
      formData.append("password", password);

      const res = await fetch("http://127.0.0.1:8000/auth/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData,
      });

      const resJson = await res.json();
      if (res.status === 200) {
        localStorage.setItem("token", resJson.access_token);
        console.log("Login successful");
        setUserName("");
        setPassword("");
        navigate("/home", { replace: true });
      } else {
        console.log("Login failed:", resJson.detail);
        alert("Password or username is incorrect.");
      }
    } catch (e) {
      console.log("Error:", e);
      alert("An error occurred. Please try again.");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-purple-500 to-blue-500 p-4">
      <div className="bg-white shadow-2xl rounded-lg p-8 w-full max-w-md">
        <div className="flex flex-col items-center mb-6">
          <div className="bg-gray-100 p-3 rounded-full shadow-md mb-4">
            <img src="./login.png" className="logo w-16 h-16" alt="Vite logo" />
          </div>
          <h2 className="text-center text-3xl font-extrabold text-gray-800 mb-4">
            Welcome Back
          </h2>
          <p className="text-center text-gray-600 mb-8">
            Please enter your details to sign in.
          </p>

          <form className="w-full space-y-6" onSubmit={signIn}>
            <div className="mb-6">
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="username"
              >
                Username
              </label>
              <input
                id="username"
                type="text"
                value={userName}
                onChange={(e) => setUserName(e.target.value)}
                placeholder="Enter your username"
                className="w-full px-4 py-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-300 transition"
              />
            </div>

            <div className="mb-6">
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="password"
              >
                Password
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter your password"
                className="w-full px-4 py-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-300 transition"
              />
            </div>

            <button
              type="submit"
              className="w-full bg-purple-600 text-white py-2 rounded-md font-semibold shadow-md hover:bg-purple-700 transition"
            >
              Sign in
            </button>
          </form>

          <p className="text-center text-gray-600 mt-6 text-sm">
            Don't have an account?{" "}
            <Link
              className="text-purple-600 font-medium hover:underline"
              to="/signup"
            >
              Sign Up
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}

export default SignIn;

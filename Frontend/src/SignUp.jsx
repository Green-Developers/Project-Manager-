import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router";

function SignUp() {
  const [userName, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  let navigate = useNavigate();

  async function register(e) {
    e.preventDefault();
    try {
      const res = await fetch("http://127.0.0.1:8000/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: userName,
          email: email,
          password: password,
        }),
      });

      if (res.status === 200) {
        const resJson = await res.json();
        console.log("Registration successful", resJson);
        setUserName("");
        setEmail("");
        setPassword("");
        navigate("/signin", { replace: true });
      } else {
        const resJson = await res.json();
        console.log("Registration failed:", resJson.detail);
        alert(resJson.detail);
      }
    } catch (e) {
      console.log("Error:", e);
      alert("An error occurred. Please try again.");
    }
  }


  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-300 to-violet-700">
      <div className="bg-white shadow-2xl rounded-lg p-8 w-full max-w-md">
        <div className="flex justify-center mb-6">
          <div className="bg-gray-100 p-3 rounded-full shadow-md">
          <img src="./login.png" className="logo w-16 h-16" alt="Vite logo" />
          </div>
        </div>
        <h2 className="text-center text-3xl font-extrabold text-gray-800 mb-4">
          Create an Account
        </h2>
        <p className="text-center text-gray-600 mb-8">
          Please fill in your details to sign up.
        </p>
        <form onSubmit={register}>
          <div className="mb-6">
            <label
              className="block text-gray-700 font-medium mb-2"
              htmlFor="full_name"
            >
              Username
            </label>
            <input
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
              id="username"
              type="text"
              placeholder="Enter your Username"
              className="w-full px-4 py-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-300 transition"
            />
          </div>
          <div className="mb-6">
            <label
              className="block text-gray-700 font-medium mb-2"
              htmlFor="email"
            >
              E-Mail Address
            </label>
            <input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              id="email"
              type="email"
              placeholder="Enter your email"
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
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              id="password"
              type="password"
              placeholder="Enter your password"
              className="w-full px-4 py-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-300 transition"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-purple-600 text-white py-2 rounded-md font-semibold shadow-md hover:bg-purple-700 transition"
          >
            Sign Up
          </button>
        </form>
        <p className="text-center text-gray-600 mt-6 text-sm">
          Already have an account?{" "}
          <a
            href="/signin"
            className="text-purple-600 font-medium hover:underline"
          >
            Sign In
          </a>
        </p>
      </div>
    </div>
  );
}

export default SignUp;

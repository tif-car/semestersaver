import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5002/api/hello")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error("Failed to fetch:", err));
  }, []);

  return (
    <div>
      <h1>{message || "To do list"}</h1>
      <h2>Add tasks</h2>
    </div>
  );
}

export default App;



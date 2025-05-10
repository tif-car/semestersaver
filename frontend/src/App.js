import React, { useEffect, useState } from "react";

function App() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    fetch("http://127.0.0.1:5001/api/hello") // 👈 Flask endpoint
      .then((res) => res.json())
      .then((data) => setMsg(data.message))
      .catch((err) => setMsg("Failed to connect to backend"));
  }, []);

  return (
    <div>
      <h1>{msg}</h1>
    </div>
  );
}

export default App;



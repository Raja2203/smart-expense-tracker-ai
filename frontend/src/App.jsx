import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Expenses from "./pages/Expenses";
import Navbar from "./components/Navbar";
import "./App.css";

function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div>
      <Navbar />

      <div className="container">
        <div className="page-buttons">
          <button onClick={() => setPage("dashboard")}>Dashboard</button>
          <button onClick={() => setPage("expenses")}>Expenses</button>
        </div>

        {page === "dashboard" && <Dashboard />}
        {page === "expenses" && <Expenses />}
      </div>
    </div>
  );
}

export default App;
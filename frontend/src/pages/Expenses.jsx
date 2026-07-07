import { useEffect, useState } from "react";
import ExpenseForm from "../components/ExpenseForm";
import ExpenseTable from "../components/ExpenseTable";
import { getExpenses, createExpense } from "../services/api";

function Expenses() {
  const [expenses, setExpenses] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadExpenses = async () => {
    try {
      setLoading(true);
      const data = await getExpenses();
      setExpenses(data);
    } catch (error) {
      console.error("Error fetching expenses:", error);
      alert("Failed to load expenses. Please check backend server.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadExpenses();
  }, []);

const handleAddExpense = async (newExpense) => {
  try {
    console.log("Sending expense payload:", newExpense);

    const savedExpense = await createExpense(newExpense);
    setExpenses([savedExpense, ...expenses]);
  } catch (error) {
  console.error("Error adding expense:", error);
  console.log("Full backend error:", error.response?.data);

  if (error.response?.data?.detail) {
    error.response.data.detail.forEach((err, index) => {
      console.log(`Error ${index + 1}:`);
      console.log("Missing field:", err.loc);
      console.log("Message:", err.msg);
    });
  }

  alert(JSON.stringify(error.response?.data, null, 2));
}
};

  return (
    <div>
      <h1>Expenses</h1>
      <p>Add, view, and manage your daily expenses here.</p>

      <ExpenseForm onAddExpense={handleAddExpense} />

      {loading ? (
        <p>Loading expenses...</p>
      ) : (
        <ExpenseTable expenses={expenses} />
      )}
    </div>
  );
}

export default Expenses;
import { useState } from "react";

function ExpenseForm({ onAddExpense }) {
  const [formData, setFormData] = useState({
    description: "",
    amount: "",
    category: "",
    expense_date: "",
    source: "manual",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.description || !formData.amount || !formData.expense_date) {
      alert("Please fill description, amount, and date");
      return;
    }

    const expensePayload = {
      description: formData.description,
      amount: Number(formData.amount),
      category: formData.category || "Uncategorized",
      expense_date: formData.expense_date,
      source: formData.source,
    };

    onAddExpense(expensePayload);

    setFormData({
      description: "",
      amount: "",
      category: "",
      expense_date: "",
      source: "manual",
    });
  };

  return (
    <form className="expense-form" onSubmit={handleSubmit}>
      <h2>Add Expense</h2>

      <input
        type="text"
        name="description"
        placeholder="Description e.g. Swiggy dinner"
        value={formData.description}
        onChange={handleChange}
      />

      <input
        type="number"
        name="amount"
        placeholder="Amount"
        value={formData.amount}
        onChange={handleChange}
      />

      <input
        type="text"
        name="category"
        placeholder="Category e.g. Food"
        value={formData.category}
        onChange={handleChange}
      />

      <input
        type="date"
        name="expense_date"
        value={formData.expense_date}
        onChange={handleChange}
      />

      <button type="submit">Add Expense</button>
    </form>
  );
}

export default ExpenseForm;
import { useState } from "react";

function ExpenseForm({ onAddExpense }) {
  const [formData, setFormData] = useState({
    title: "",
    amount: "",
    category: "",
    payment_mode: "",
    description: "",
    expense_date: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (
      !formData.title ||
      !formData.amount ||
      !formData.category ||
      !formData.payment_mode ||
      !formData.expense_date
    ) {
      alert("Please fill title, amount, category, payment mode, and date");
      return;
    }

    const expensePayload = {
      title: formData.title,
      amount: Number(formData.amount),
      category: formData.category,
      payment_mode: formData.payment_mode,
      description: formData.description,
      expense_date: formData.expense_date,
    };

    console.log("Sending expense payload:", expensePayload);

    onAddExpense(expensePayload);

    setFormData({
      title: "",
      amount: "",
      category: "",
      payment_mode: "",
      description: "",
      expense_date: "",
    });
  };

  return (
    <form className="expense-form" onSubmit={handleSubmit}>
      <h2>Add Expense</h2>

      <input
        type="text"
        name="title"
        placeholder="Title e.g. Swiggy dinner"
        value={formData.title}
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

      <select
        name="payment_mode"
        value={formData.payment_mode}
        onChange={handleChange}
      >
        <option value="">Select Payment Mode</option>
        <option value="UPI">UPI</option>
        <option value="Cash">Cash</option>
        <option value="Credit Card">Credit Card</option>
        <option value="Debit Card">Debit Card</option>
        <option value="Net Banking">Net Banking</option>
      </select>

      <input
        type="text"
        name="description"
        placeholder="Description optional"
        value={formData.description}
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
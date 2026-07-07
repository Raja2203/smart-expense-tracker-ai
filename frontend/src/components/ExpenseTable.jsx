function ExpenseTable({ expenses }) {
  return (
    <div className="expense-table">
      <h2>Expense List</h2>

      {expenses.length === 0 ? (
        <p>No expenses added yet.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Description</th>
              <th>Amount</th>
              <th>Category</th>
              <th>Date</th>
              <th>Source</th>
            </tr>
          </thead>

          <tbody>
            {expenses.map((expense, index) => (
              <tr key={index}>
                <td>{expense.description}</td>
                <td>₹{expense.amount}</td>
                <td>{expense.category || "Uncategorized"}</td>
                <td>{expense.date}</td>
                <td>{expense.source}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ExpenseTable;
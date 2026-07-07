function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <p>View your expense summary, monthly insights, and spending patterns.</p>

      <div className="dashboard-cards">
        <div className="card">
          <h3>Total Expenses</h3>
          <p>₹0</p>
        </div>

        <div className="card">
          <h3>This Month</h3>
          <p>₹0</p>
        </div>

        <div className="card">
          <h3>Top Category</h3>
          <p>Food</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
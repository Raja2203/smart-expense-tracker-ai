import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const getExpenses = async () => {
  const response = await api.get("/expenses");
  return response.data;
};

export const createExpense = async (expenseData) => {
  const response = await api.post("/expenses", expenseData);
  return response.data;
};

export const deleteExpense = async (id) => {
  const response = await api.delete(`/expenses/${id}`);
  return response.data;
};

export const getInsights = async () => {
  const response = await api.get("/insights");
  return response.data;
};

export default api;
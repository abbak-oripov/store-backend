import express from "express";
import cors from "cors";

const app = express();
// Изменили порт на 5001, чтобы избежать конфликтов
const PORT = 5001;

// Middleware
app.use(cors());
app.use(express.json());

// Тестовые товары
const products = [
  { id: 1, name: "iPhone 15 Pro", price: 1200 },
  { id: 2, name: "MacBook Air M3", price: 1800 },
  { id: 3, name: "AirPods Pro", price: 250 },
];

// Главная проверка
app.get("/", (req, res) => {
  res.send("✅ Backend работает!");
});

// Получить все товары
app.get("/api/products", (req, res) => {
  res.json(products);
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
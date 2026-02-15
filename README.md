# 📈 Stock Market Mini Analyzer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-orange)
![Gradio](https://img.shields.io/badge/Gradio-Interactive%20UI-yellow)
[![HuggingFace Spaces](https://img.shields.io/badge/🤗%20Live%20Demo-HuggingFace%20Spaces-blue?logo=huggingface)](https://huggingface.co/spaces/IqRogueRex/Stock-Market-Mini-Analyzer)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Deployed-success)

An interactive financial analytics web application built using **Python, NumPy, and Gradio**.  
This project simulates stock price data and performs quantitative analysis including daily return computation, volatility measurement, and identification of the best-performing stock per trading day.

---

## 📌 Project Overview

The Stock Market Mini Analyzer is a lightweight financial modeling application designed to demonstrate:

- Vectorized numerical computation using NumPy  
- Core financial mathematics (returns & volatility)  
- Clean, modular Python design  
- Interactive data applications using Gradio  

The project highlights strong foundations in **data analysis, financial analytics, and Python-based application development**.

---

## 🚀 Core Features

### 1️⃣ Synthetic Stock Data Generation
- Generates simulated price data for three assets:
  - Stock A  
  - Stock B  
  - Stock C  
- User-defined number of trading days  
- Randomized price range between 100–500  

### 2️⃣ Daily Percentage Returns

\[
Return = \frac{P_t - P_{t-1}}{P_{t-1}} \times 100
\]

- Fully vectorized implementation  
- Efficient NumPy-based computation  

### 3️⃣ Volatility Calculation
- Computes standard deviation of daily returns  
- Provides a simple measure of risk exposure  

### 4️⃣ Best Performing Stock Per Day
- Identifies the stock with the highest return each day  
- Outputs both stock name and return percentage  

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| NumPy | Numerical and vectorized computations |
| Gradio | Interactive web interface |

---

## 🧠 Concepts Demonstrated

- Vectorized array operations  
- Financial return modeling  
- Risk quantification via standard deviation  
- State management in Gradio  
- Tab-based UI structuring  

---

## 📂 Project Structure

```
.
├── app.py          # Main Gradio application
├── README.md       # Project documentation
```

---

## ▶️ Running the Project Locally

### Clone the Repository

```bash
git clone https://github.com/yourusername/stock-market-mini-analyzer.git
cd stock-market-mini-analyzer
```

### Install Dependencies

```bash
pip install numpy gradio
```

### Run the Application

```bash
python app.py
```

The app will launch in your local browser.

---

## 🔮 Future Improvements

- Integration with real-time market data (Yahoo Finance API)  
- Price visualizations (Matplotlib / Plotly)  
- Moving averages and technical indicators  
- Sharpe Ratio and risk-adjusted metrics  
- CSV upload & export functionality  

---

## 🎯 Professional Value

This project demonstrates:

- Strong understanding of financial metrics  
- Efficient numerical computation using NumPy  
- Clean, structured Python code  
- Ability to deploy interactive applications via Hugging Face Spaces  

Relevant for roles in:
- Data Science  
- Financial Analytics  
- Quantitative Research  
- Python Development  

---

## 👨‍💻 Author

**Chinmay V Chatradamath**

---

## 📄 License

This project is licensed under the MIT License.

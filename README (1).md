# 💰 portfolio — Indian Stock Portfolio Tracker

> Track your Indian stocks from the terminal. No browser needed.

A simple, beautiful CLI tool for tracking NSE/BSE stocks — built with Python.

---

## ✨ Features

- 📈 **Live Prices** — Get real-time stock prices from NSE
- 📁 **Track Portfolio** — Save your stocks with buy price & quantity
- 💹 **Gain / Loss** — See exactly how much you've made or lost

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install yfinance rich
```

### 2. Check a live stock price
```bash
python portfolio.py price RELIANCE
python portfolio.py price TCS
python portfolio.py price INFY
```

### 3. Add stocks to your portfolio
```bash
python portfolio.py add RELIANCE 10 2500
#                       ^symbol  ^qty ^buy price
```

### 4. View your full portfolio + P&L
```bash
python portfolio.py show
```

### 5. Remove a stock
```bash
python portfolio.py remove RELIANCE
```

---

## 📸 Example Output

```
╭─────────────────────────────────╮
│           RELIANCE.NS           │
│ Reliance Industries Limited     │
│ ₹2,834.50  ▲ 24.30 (0.87%)    │
│                                 │
│ Day High: ₹2,840  Low: ₹2,798  │
╰─────────────────────────────────╯
```

---

## 📦 Supported Symbols

Works with all NSE-listed stocks. Just use the ticker symbol:
- `RELIANCE` → Reliance Industries
- `TCS` → Tata Consultancy Services
- `INFY` → Infosys
- `HDFCBANK` → HDFC Bank
- `WIPRO` → Wipro

---

## 🛠️ Built With

- [yfinance](https://github.com/ranaroussi/yfinance) — Stock data
- [rich](https://github.com/Textualize/rich) — Beautiful terminal output

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or want a feature, open an issue.

---

## 📄 License

MIT License — free to use and modify.

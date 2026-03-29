# 💰 portfolio — Indian Stock Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/NSE-Live%20Prices-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Google%20Colab-Ready-orange?style=for-the-badge&logo=googlecolab&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</p>

<p align="center">
  Track Indian stocks from your <b>terminal</b> or <b>Google Colab</b>. No browser. No app. Just Python.
</p>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📈 **Live Prices** | Real-time NSE stock prices in your terminal |
| 📁 **Portfolio Tracker** | Save stocks with quantity & buy price |
| 💹 **Gain / Loss** | See exactly how much you've made or lost |
| 🗑️ **Remove Stocks** | Clean up your portfolio anytime |
| 🌐 **Colab Ready** | Works in Google Colab — no install needed |

---

## 🚀 Quick Start

### Option 1 — Google Colab (Easiest, no install)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vignesh-N17/portfolio/blob/main/portfolio_colab.ipynb)

Just click the button above and run the cells!

---

### Option 2 — Run locally

**Install dependencies:**
```bash
pip install yfinance rich
```

**Check a live stock price:**
```bash
python portfolio.py price RELIANCE
python portfolio.py price TCS
python portfolio.py price HDFCBANK
```

**Add stocks to your portfolio:**
```bash
python portfolio.py add RELIANCE 10 2500
#                        ^symbol  ^qty  ^buy price (₹)
```

**View full portfolio with P&L:**
```bash
python portfolio.py show
```

**Remove a stock:**
```bash
python portfolio.py remove RELIANCE
```

---

## 📸 Demo

```
╭──────────────────── RELIANCE.NS ─────────────────────╮
│ Reliance Industries Limited                           │
│ ₹2,834.50  ▲ 24.30 (0.87%)                          │
│                                                       │
│ Day High: ₹2,840   Day Low: ₹2,798                   │
╰───────────────────────────────────────────────────────╯

           💰 My Portfolio
╭───────────┬─────┬───────────┬───────────┬────────────╮
│ Stock     │ Qty │ Buy Price │ Current   │ Return %   │
├───────────┼─────┼───────────┼───────────┼────────────┤
│ RELIANCE  │ 10  │ ₹2,500   │ ₹2,834   │ +13.36%   │
│ TCS       │ 5   │ ₹3,800   │ ₹4,102   │ +7.95%    │
│ INFY      │ 8   │ ₹1,500   │ ₹1,623   │ +8.20%    │
╰───────────┴─────┴───────────┴───────────┴────────────╯

 Total Invested: ₹56,000   Current: ₹62,431   ▲ +11.48%
```

---

## 📦 Supported Stocks

Works with all **NSE-listed** stocks. Just use the ticker:

`RELIANCE` `TCS` `INFY` `HDFCBANK` `WIPRO` `SBIN` `TATAMOTORS` `BAJFINANCE` and 2000+ more!

---

## 🛠️ Built With

- [yfinance](https://github.com/ranaroussi/yfinance) — Live stock data
- [rich](https://github.com/Textualize/rich) — Beautiful terminal output

---

## 🤝 Contributing

Contributions are welcome! If you have an idea or found a bug:

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and share.

---

<p align="center">Made with ❤️ for Indian investors</p>

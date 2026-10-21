# 🇮🇳 Indian Mutual Funds & ETFs Screener

An interactive, high-performance web dashboard to explore, screen, filter, and compare 165+ Indian Mutual Funds, Index Funds, and ETFs across all major AMCs.

### 🌐 Live Web App (Always Online 24/7):
👉 **[https://gnjnshh.github.io/MFs_ETF_screener/](https://gnjnshh.github.io/MFs_ETF_screener/)**

---

## 🚀 Key Features

1. **Multi-Parameter Filtering:**
   - Instant search across 165+ schemes and 29 AMCs (SBI, Parag Parikh, HDFC, ICICI, Nippon, Mirae, Quant, etc.).
   - Category filtering: Large Cap, Mid Cap, Small Cap, Flexi Cap, Index Funds, EV & New Age, Gold & Silver ETFs, Sectoral, ELSS.
   - Fund Type filtering: Active Equity, Index Fund, ETF, Hybrid, Debt/Liquid.
   - Dynamic sorting by AUM (₹ Cr), 1M, 3M, 6M, 1Y, 3Y, and 5Y returns.

2. **Head-to-Head Comparison:**
   - Select 2 to 4 funds and compare them side-by-side with metric deltas.

3. **Mobile-First & Ultra-Responsive:**
   - Touch-friendly horizontal category pills, expandable scheme details (Expense Ratio, Benchmark, Risk Rating).
   - Zero installation required — works directly in any mobile or desktop browser.

4. **Python Streamlit Version:**
   - Includes full Python source (`app.py`) with Plotly visualizations and live AMFI API NAV tracking.

---

## 🏃‍♂️ Running Locally (Optional)

### Run the Web Dashboard:
Simply open `index.html` in any browser, or view live on GitHub Pages.

### Run the Python Streamlit App:
```bash
pip install -r requirements.txt
streamlit run app.py
```
Or double-click `run_dashboard.bat`.

---

## 📊 Dataset
All data is compiled in [`mutual_funds_data.csv`](mutual_funds_data.csv) covering 165+ schemes with AUM and multi-period annualized returns.

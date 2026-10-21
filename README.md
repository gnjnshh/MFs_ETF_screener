# 🇮🇳 Indian Mutual Funds & Index Funds Screener Dashboard

An interactive, high-performance Python dashboard built with **Streamlit** and **Plotly** to explore, filter, screen, and compare Indian Mutual Funds, Index Funds, ETFs, and Hybrid schemes.

## 🚀 Key Features

1. **Multi-Parameter Filtering:**
   - Search by scheme name, benchmark, or AMC keyword.
   - Filter by **Category** (Large Cap, Mid Cap, Small Cap, Flexi Cap, Multi Cap, Large & Mid Cap, Value/Contra, ELSS, Focused, Sectoral/Thematic, Index Funds, ETFs, Hybrid, Arbitrage, Liquid).
   - Filter by **Fund Type** (Active Equity, Index Fund, ETF, Hybrid, Debt).
   - Filter by **Fund House (AMC)** (SBI, HDFC, ICICI Prudential, Nippon India, Kotak, Parag Parikh, Mirae Asset, Axis, UTI, Bandhan, Tata, Motilal Oswal, DSP, Canara Robeco, Quant, etc.).
   - Dynamic **AUM Range Slider** (₹ Cr).
   - Minimum return thresholds for **1M, 3M, 6M, 1Y, 3Y, and 5Y** returns.
   - Filter by **SEBI Risk Rating**.

2. **Interactive Visual Analytics (Plotly):**
   - **Top 10 Performers:** Dynamic bar charts switchable across 1M, 3M, 6M, 1Y, 3Y, and 5Y return horizons.
   - **Category Comparison:** Average returns across categories.
   - **Risk-Return Scatter Plot:** 1-Year vs. 3-Year CAGR with bubble size representing AUM.
   - **AUM Distribution Sunburst/Treemap:** Interactive hierarchy by Category and Fund House.

3. **Side-by-Side Scheme Comparison:**
   - Compare 2 to 4 schemes across all metrics (AUM, 1M, 3M, 6M, 1Y, 3Y, 5Y returns, Benchmark, Expense Ratio, Risk) in a clean comparison table and bar chart.

4. **Live AMFI NAV Inspector & Tracker:**
   - Query live NAV records directly from official AMFI data (`api.mfapi.in`).
   - Interactive historical NAV charts with timeframe selectors (1M, 6M, 1Y, 3Y, 5Y, Max).

5. **One-Click CSV Export:**
   - Download the filtered dataset with one click.

---

## 🏃‍♂️ How to Run the Dashboard

In PowerShell or Command Prompt, run:

```bash
cd "C:\Users\gnjns\.gemini\antigravity\scratch\mutual_fund_dashboard"
streamlit run app.py
```

Or simply double-click **`run_dashboard.bat`** (Local access) or **`share_dashboard.bat`** (Public shareable link).

---

## 🌐 Public Sharing & Mobile Access

You can share the dashboard or access it from your phone without being on the same network using Cloudflare Tunnel:

- Run `share_dashboard.bat` to launch the app and obtain a public HTTPS `*.trycloudflare.com` URL.


"""
Interactive Indian Mutual Funds & Index Funds Analytics Dashboard
Built with Streamlit and Plotly.
Filters, visualizes, and compares Indian Mutual Funds, Index Funds, ETFs, and Hybrid schemes.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import requests
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="India Mutual Funds & Index Funds Screener",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.2rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 8px;
        padding: 12px 16px;
        border: 1px solid #E2E8F0;
    }
    .stDataFrame {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Load Dataset
@st.cache_data
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), "mutual_funds_data.csv")
    if not os.path.exists(csv_path):
        import build_dataset
    df = pd.read_csv(csv_path)
    return df

df = load_data()

# Sidebar: Filters
st.sidebar.image("https://img.icons8.com/color/96/bullish.png", width=64)
st.sidebar.title("Filter Schemes")

# 1. Text Search
search_term = st.sidebar.text_input("🔍 Search Scheme or AMC", "").strip().lower()

# 2. Fund Type Multi-select
fund_types = sorted(df["Fund Type"].unique().tolist())
selected_fund_types = st.sidebar.multiselect("Fund Type", fund_types, default=fund_types)

# 3. Category Multi-select
available_categories = sorted(df[df["Fund Type"].isin(selected_fund_types)]["Category"].unique().tolist())
selected_categories = st.sidebar.multiselect("Category", available_categories, default=available_categories)

# 4. AMC Multi-select
available_amcs = sorted(df[df["Category"].isin(selected_categories)]["AMC"].unique().tolist())
selected_amcs = st.sidebar.multiselect("Fund House (AMC)", available_amcs, default=[])

# 5. AUM Slider
min_aum = int(df["AUM (Cr)"].min())
max_aum = int(df["AUM (Cr)"].max())
selected_aum = st.sidebar.slider("AUM (₹ Crores)", min_value=0, max_value=max_aum, value=(0, max_aum), step=500)

# 6. Return Filters
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Minimum Return Filters")
col_s1, col_s2 = st.sidebar.columns(2)
with col_s1:
    min_1y = st.number_input("Min 1Y Return (%)", value=-20.0, step=1.0)
    min_3y = st.number_input("Min 3Y CAGR (%)", value=0.0, step=1.0)
with col_s2:
    min_6m = st.number_input("Min 6M Return (%)", value=-20.0, step=1.0)
    min_5y = st.number_input("Min 5Y CAGR (%)", value=0.0, step=1.0)

# Filter Data
filtered_df = df.copy()

if search_term:
    filtered_df = filtered_df[
        filtered_df["Scheme Name"].str.lower().str.contains(search_term) |
        filtered_df["AMC"].str.lower().str.contains(search_term) |
        filtered_df["Benchmark"].str.lower().str.contains(search_term)
    ]

if selected_fund_types:
    filtered_df = filtered_df[filtered_df["Fund Type"].isin(selected_fund_types)]

if selected_categories:
    filtered_df = filtered_df[filtered_df["Category"].isin(selected_categories)]

if selected_amcs:
    filtered_df = filtered_df[filtered_df["AMC"].isin(selected_amcs)]

filtered_df = filtered_df[
    (filtered_df["AUM (Cr)"] >= selected_aum[0]) & 
    (filtered_df["AUM (Cr)"] <= selected_aum[1]) &
    (filtered_df["1Y (%)"] >= min_1y) &
    (filtered_df["3Y (%)"] >= min_3y) &
    (filtered_df["6M (%)"] >= min_6m) &
    (filtered_df["5Y (%)"] >= min_5y)
]

# Header Section
st.markdown('<div class="main-title">🇮🇳 Indian Mutual Funds & Index Funds Screener</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Explore, screen, and compare Indian Mutual Funds, Index Funds, ETFs, and Hybrids by AUM and multi-horizon returns (1M, 3M, 6M, 1Y, 3Y, 5Y).</div>', unsafe_allow_html=True)

# Top KPI Summary Cards
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
with kpi1:
    st.metric("Total Schemes", f"{len(filtered_df):,}", f"out of {len(df)}")
with kpi2:
    total_aum_lakh_cr = filtered_df["AUM (Cr)"].sum() / 100000
    st.metric("Total AUM", f"₹{total_aum_lakh_cr:.2f} L Cr")
with kpi3:
    med_1y = filtered_df["1Y (%)"].median() if not filtered_df.empty else 0.0
    st.metric("Median 1Y Return", f"{med_1y:+.2f}%")
with kpi4:
    med_3y = filtered_df["3Y (%)"].median() if not filtered_df.empty else 0.0
    st.metric("Median 3Y CAGR", f"{med_3y:.2f}%")
with kpi5:
    top_fund = filtered_df.sort_values(by="3Y (%)", ascending=False).iloc[0]["Scheme Name"] if not filtered_df.empty else "N/A"
    top_3y = filtered_df["3Y (%)"].max() if not filtered_df.empty else 0.0
    st.metric("Top 3Y Performer", f"{top_3y:.2f}%", top_fund[:20] + "...")

st.markdown("---")

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Schemes Table", 
    "📊 Charts & Visual Insights", 
    "⚖️ Side-by-Side Compare", 
    "🌐 Live AMFI NAV Inspector"
])

# ==========================================================
# TAB 1: INTERACTIVE TABLE
# ==========================================================
with tab1:
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.subheader(f"Matching Schemes ({len(filtered_df)})")
    with col_t2:
        sort_by = st.selectbox(
            "Sort by", 
            ["AUM (Cr)", "3Y (%)", "5Y (%)", "1Y (%)", "6M (%)", "1M (%)", "Scheme Name"], 
            index=0
        )
        sort_asc = False if sort_by != "Scheme Name" else True

    display_df = filtered_df.sort_values(by=sort_by, ascending=sort_asc).reset_index(drop=True)

    # Style table
    def color_returns(val):
        if isinstance(val, (int, float)):
            if val > 0:
                return 'color: #059669; font-weight: 500;'
            elif val < 0:
                return 'color: #DC2626; font-weight: 500;'
        return ''

    # Format numeric columns for clean view
    format_dict = {
        "AUM (Cr)": "₹{:,.0f}",
        "1M (%)": "{:+.2f}%",
        "3M (%)": "{:+.2f}%",
        "6M (%)": "{:+.2f}%",
        "1Y (%)": "{:+.2f}%",
        "3Y (%)": "{:.2f}%",
        "5Y (%)": "{:.2f}%",
        "Expense Ratio (%)": "{:.2f}%"
    }

    styled_df = display_df.style.applymap(color_returns, subset=["1M (%)", "3M (%)", "6M (%)", "1Y (%)", "3Y (%)", "5Y (%)"]).format(format_dict)
    st.dataframe(styled_df, use_container_width=True, height=520)

    # Download Button
    csv_bytes = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Schemes (CSV)",
        data=csv_bytes,
        file_name=f"mutual_funds_filtered_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ==========================================================
# TAB 2: VISUAL ANALYTICS
# ==========================================================
with tab2:
    if filtered_df.empty:
        st.warning("No schemes match your filter criteria to plot charts.")
    else:
        st.subheader("Performance & AUM Visual Analytics")
        
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            return_horizon = st.selectbox("Select Horizon for Top 10 Performers", ["3Y (%)", "5Y (%)", "1Y (%)", "6M (%)", "1M (%)"])
            top_10 = filtered_df.sort_values(by=return_horizon, ascending=False).head(10)
            fig_top = px.bar(
                top_10, 
                x=return_horizon, 
                y="Scheme Name", 
                orientation="h",
                color=return_horizon,
                color_continuous_scale="Viridis",
                title=f"Top 10 Schemes by {return_horizon}",
                labels={return_horizon: f"Return ({return_horizon})", "Scheme Name": ""},
                text_auto=".2f"
            )
            fig_top.update_layout(yaxis={'categoryorder': 'total ascending'}, height=420)
            st.plotly_chart(fig_top, use_container_width=True)

        with row1_col2:
            cat_perf = filtered_df.groupby("Category")[["1Y (%)", "3Y (%)", "5Y (%)"]].mean().reset_index()
            cat_perf = cat_perf.sort_values(by="3Y (%)", ascending=False)
            fig_cat = px.bar(
                cat_perf, 
                x="Category", 
                y=["1Y (%)", "3Y (%)", "5Y (%)"], 
                barmode="group",
                title="Average Performance by Category (1Y vs 3Y vs 5Y)",
                labels={"value": "Return (%)", "variable": "Horizon"}
            )
            fig_cat.update_layout(height=420, xaxis_tickangle=-45)
            st.plotly_chart(fig_cat, use_container_width=True)

        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            fig_scatter = px.scatter(
                filtered_df,
                x="3Y (%)",
                y="1Y (%)",
                size="AUM (Cr)",
                color="Category",
                hover_name="Scheme Name",
                hover_data=["AUM (Cr)", "5Y (%)", "AMC"],
                title="Risk-Return Mapping: 1Y vs 3Y Return (Bubble Size = AUM)",
                labels={"3Y (%)": "3-Year CAGR (%)", "1Y (%)": "1-Year Return (%)"}
            )
            fig_scatter.update_layout(height=450)
            st.plotly_chart(fig_scatter, use_container_width=True)

        with row2_col2:
            fig_tree = px.treemap(
                filtered_df,
                path=["Category", "AMC", "Scheme Name"],
                values="AUM (Cr)",
                title="AUM Distribution by Category & Fund House",
                color="AUM (Cr)",
                color_continuous_scale="Blues"
            )
            fig_tree.update_layout(height=450)
            st.plotly_chart(fig_tree, use_container_width=True)

# ==========================================================
# TAB 3: SIDE-BY-SIDE SCHEME COMPARISON
# ==========================================================
with tab3:
    st.subheader("Compare 2 to 4 Schemes Side-by-Side")
    compare_schemes = st.multiselect(
        "Select Schemes to Compare",
        options=df["Scheme Name"].unique().tolist(),
        default=df["Scheme Name"].head(3).tolist(),
        max_selections=4
    )

    if compare_schemes:
        comp_df = df[df["Scheme Name"].isin(compare_schemes)].set_index("Scheme Name")
        
        # Display Transposed Matrix
        matrix_df = comp_df[["Category", "AMC", "Fund Type", "AUM (Cr)", "1M (%)", "3M (%)", "6M (%)", "1Y (%)", "3Y (%)", "5Y (%)", "Benchmark", "Expense Ratio (%)", "Risk Rating"]].T
        st.table(matrix_df)

        # Comparative Bar Chart
        ret_cols = ["1M (%)", "3M (%)", "6M (%)", "1Y (%)", "3Y (%)", "5Y (%)"]
        plot_comp_df = comp_df[ret_cols].reset_index().melt(id_vars="Scheme Name", var_name="Period", value_name="Return (%)")
        fig_comp = px.bar(
            plot_comp_df,
            x="Period",
            y="Return (%)",
            color="Scheme Name",
            barmode="group",
            title="Return Comparison Across Time Horizons",
            text_auto=".2f"
        )
        st.plotly_chart(fig_comp, use_container_width=True)
    else:
        st.info("Select at least 2 schemes to view the comparison matrix.")

# ==========================================================
# TAB 4: LIVE AMFI / MFAPI NAV INSPECTOR
# ==========================================================
with tab4:
    st.subheader("Live Official AMFI NAV History & Tracker")
    st.markdown("Fetch official real-time daily NAV records and calculate custom historical returns for any mutual fund scheme via `api.mfapi.in` (powered by AMFI).")

    col_l1, col_l2 = st.columns([2, 1])
    with col_l1:
        scheme_search_name = st.text_input("Enter Scheme Keyword to Search AMFI Code (e.g. Parag Parikh, HDFC Flexi, Small Cap):", "Parag Parikh Flexi Cap")
    
    # Live Search in mfapi
    @st.cache_data(ttl=3600)
    def search_mf_codes(query):
        try:
            res = requests.get("https://api.mfapi.in/mf", timeout=5)
            if res.status_code == 200:
                all_schemes = res.json()
                matches = [s for s in all_schemes if query.lower() in s["schemeName"].lower()]
                return matches[:20]
        except Exception as e:
            return []
        return []

    if scheme_search_name:
        results = search_mf_codes(scheme_search_name)
        if results:
            options_dict = {f"{r['schemeCode']} - {r['schemeName']}": r['schemeCode'] for r in results}
            chosen_label = st.selectbox("Select Matching Scheme from AMFI Registry:", list(options_dict.keys()))
            chosen_code = options_dict[chosen_label]

            # Fetch Scheme Historical NAV
            @st.cache_data(ttl=1800)
            def fetch_nav_data(code):
                try:
                    res = requests.get(f"https://api.mfapi.in/mf/{code}", timeout=10)
                    if res.status_code == 200:
                        return res.json()
                except Exception:
                    return None
                return None

            nav_data = fetch_nav_data(chosen_code)
            if nav_data and "data" in nav_data and len(nav_data["data"]) > 0:
                meta = nav_data.get("meta", {})
                st.success(f"**Found:** {meta.get('scheme_name')} | **Fund House:** {meta.get('fund_house')} | **Category:** {meta.get('scheme_category')}")

                # Parse NAVs
                nav_records = nav_data["data"]
                history_df = pd.DataFrame(nav_records)
                history_df["date"] = pd.to_datetime(history_df["date"], format="%d-%m-%Y")
                history_df["nav"] = pd.to_numeric(history_df["nav"])
                history_df = history_df.sort_values(by="date").reset_index(drop=True)

                latest_nav = history_df.iloc[-1]["nav"]
                latest_date = history_df.iloc[-1]["date"].strftime("%d-%b-%Y")

                # Metric Cards
                m1, m2 = st.columns(2)
                m1.metric("Latest NAV", f"₹{latest_nav:.4f}", f"As of {latest_date}")
                
                # Interactive Plotly NAV Chart
                fig_nav = px.line(
                    history_df, 
                    x="date", 
                    y="nav", 
                    title=f"Historical NAV Chart: {meta.get('scheme_name')}",
                    labels={"date": "Date", "nav": "Net Asset Value (₹)"}
                )
                fig_nav.update_xaxes(
                    rangeslider_visible=True,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(count=3, label="3y", step="year", stepmode="backward"),
                            dict(count=5, label="5y", step="year", stepmode="backward"),
                            dict(step="all", label="All")
                        ])
                    )
                )
                st.plotly_chart(fig_nav, use_container_width=True)
            else:
                st.error("Failed to fetch historical NAV for this scheme code.")
        else:
            st.info("No matching schemes found. Try a different keyword.")

# Footer
st.markdown("---")
st.caption("Data reflects Indian Mutual Fund industry metrics as of October 2026. Sourced from AMFI disclosures, fund factsheets, and public exchange filings. Past performance is not indicative of future returns.")

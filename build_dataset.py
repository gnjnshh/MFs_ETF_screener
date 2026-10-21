"""
Script to generate the comprehensive Mutual Funds and Index Funds dataset for the dashboard.
Contains 150+ schemes across Active Equity, Index Funds, ETFs, Hybrid, and Debt with
AUM (Cr), 1M, 3M, 6M, 1Y, 3Y, 5Y returns, Benchmark, Expense Ratio, and Risk Rating.
"""
import pandas as pd
import os

data = [
    # ==========================================
    # 1. LARGE CAP ACTIVE EQUITY
    # ==========================================
    {
        "Scheme Name": "ICICI Prudential Large Cap Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 80200, "1M (%)": 0.85, "3M (%)": -1.20, "6M (%)": 3.10, "1Y (%)": -2.10, "3Y (%)": 13.10, "5Y (%)": 12.45,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 0.95, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Large Cap Fund",
        "AMC": "SBI Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 55250, "1M (%)": 0.60, "3M (%)": -1.80, "6M (%)": 2.40, "1Y (%)": -3.60, "3Y (%)": 9.45, "5Y (%)": 9.15,
        "Benchmark": "BSE 100 TRI", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Large Cap Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 51296, "1M (%)": 1.10, "3M (%)": -0.90, "6M (%)": 4.20, "1Y (%)": -1.95, "3Y (%)": 14.85, "5Y (%)": 14.30,
        "Benchmark": "BSE 100 TRI", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Large Cap Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 38600, "1M (%)": 0.70, "3M (%)": -1.50, "6M (%)": 2.80, "1Y (%)": -3.40, "3Y (%)": 12.60, "5Y (%)": 12.10,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 1.05, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset Large Cap Fund",
        "AMC": "Mirae Asset Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 38100, "1M (%)": 0.40, "3M (%)": -2.10, "6M (%)": 1.90, "1Y (%)": -4.30, "3Y (%)": 8.90, "5Y (%)": 8.40,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Axis Large Cap Fund",
        "AMC": "Axis Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 30350, "1M (%)": 0.30, "3M (%)": -2.40, "6M (%)": 1.50, "1Y (%)": -4.10, "3Y (%)": 7.80, "5Y (%)": 5.60,
        "Benchmark": "BSE 100 TRI", "Expense Ratio (%)": 0.72, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Aditya Birla Sun Life Frontline Equity Fund",
        "AMC": "Aditya Birla Sun Life Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 26500, "1M (%)": 0.70, "3M (%)": -1.35, "6M (%)": 2.70, "1Y (%)": -2.60, "3Y (%)": 11.10, "5Y (%)": 10.60,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 0.98, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Canara Robeco Large Cap Fund",
        "AMC": "Canara Robeco Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 14200, "1M (%)": 0.80, "3M (%)": -1.10, "6M (%)": 3.30, "1Y (%)": -2.30, "3Y (%)": 11.90, "5Y (%)": 11.50,
        "Benchmark": "BSE 100 TRI", "Expense Ratio (%)": 0.55, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "UTI Large Cap Fund (Mastershare)",
        "AMC": "UTI Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 12800, "1M (%)": 0.65, "3M (%)": -1.60, "6M (%)": 2.50, "1Y (%)": -3.10, "3Y (%)": 10.40, "5Y (%)": 9.90,
        "Benchmark": "BSE 100 TRI", "Expense Ratio (%)": 0.90, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Kotak Large Cap Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 10500, "1M (%)": 0.75, "3M (%)": -1.40, "6M (%)": 2.90, "1Y (%)": -2.80, "3Y (%)": 11.20, "5Y (%)": 10.80,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Edelweiss Large Cap Fund",
        "AMC": "Edelweiss Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 3150, "1M (%)": 0.82, "3M (%)": -1.15, "6M (%)": 3.40, "1Y (%)": -2.20, "3Y (%)": 12.10, "5Y (%)": 11.80,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 0.52, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Baroda BNP Paribas Large Cap Fund",
        "AMC": "Baroda BNP Paribas Mutual Fund", "Category": "Large Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 2180, "1M (%)": 0.78, "3M (%)": -1.25, "6M (%)": 3.10, "1Y (%)": -2.50, "3Y (%)": 11.80, "5Y (%)": 11.40,
        "Benchmark": "Nifty 100 TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },

    # ==========================================
    # 2. PASSIVE INDEX FUNDS
    # ==========================================
    {
        "Scheme Name": "UTI Nifty 50 Index Fund",
        "AMC": "UTI Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 19500, "1M (%)": 0.72, "3M (%)": -1.45, "6M (%)": 2.75, "1Y (%)": -3.90, "3Y (%)": 9.20, "5Y (%)": 9.35,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.18, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Nifty 50 Index Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 16800, "1M (%)": 0.71, "3M (%)": -1.46, "6M (%)": 2.73, "1Y (%)": -3.92, "3Y (%)": 9.18, "5Y (%)": 9.33,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.20, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Nifty 50 Index Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 12500, "1M (%)": 0.72, "3M (%)": -1.44, "6M (%)": 2.76, "1Y (%)": -3.89, "3Y (%)": 9.22, "5Y (%)": 9.36,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.17, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Nifty 50 Index Fund",
        "AMC": "SBI Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 11200, "1M (%)": 0.70, "3M (%)": -1.48, "6M (%)": 2.71, "1Y (%)": -3.94, "3Y (%)": 9.15, "5Y (%)": 9.30,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.20, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Nifty 50 Index Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 3400, "1M (%)": 0.71, "3M (%)": -1.45, "6M (%)": 2.74, "1Y (%)": -3.91, "3Y (%)": 9.19, "5Y (%)": 9.34,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.20, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bandhan Nifty 50 Index Fund",
        "AMC": "Bandhan Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 1850, "1M (%)": 0.72, "3M (%)": -1.44, "6M (%)": 2.75, "1Y (%)": -3.90, "3Y (%)": 9.20, "5Y (%)": 9.35,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.10, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Navi Nifty 50 Index Fund",
        "AMC": "Navi Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 2400, "1M (%)": 0.73, "3M (%)": -1.43, "6M (%)": 2.77, "1Y (%)": -3.88, "3Y (%)": 9.24, "5Y (%)": 9.38,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.06, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC S&P BSE Sensex Index Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 9400, "1M (%)": 0.68, "3M (%)": -1.52, "6M (%)": 2.65, "1Y (%)": -3.75, "3Y (%)": 8.95, "5Y (%)": 9.10,
        "Benchmark": "BSE Sensex TRI", "Expense Ratio (%)": 0.20, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential S&P BSE Sensex Index Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 3600, "1M (%)": 0.69, "3M (%)": -1.50, "6M (%)": 2.67, "1Y (%)": -3.73, "3Y (%)": 8.98, "5Y (%)": 9.12,
        "Benchmark": "BSE Sensex TRI", "Expense Ratio (%)": 0.18, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "UTI Nifty Next 50 Index Fund",
        "AMC": "UTI Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 5200, "1M (%)": 0.95, "3M (%)": -0.80, "6M (%)": 4.80, "1Y (%)": 4.20, "3Y (%)": 13.50, "5Y (%)": 11.80,
        "Benchmark": "Nifty Next 50 TRI", "Expense Ratio (%)": 0.32, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Nifty Next 50 Index Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 4100, "1M (%)": 0.96, "3M (%)": -0.78, "6M (%)": 4.82, "1Y (%)": 4.25, "3Y (%)": 13.55, "5Y (%)": 11.85,
        "Benchmark": "Nifty Next 50 TRI", "Expense Ratio (%)": 0.30, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Nifty Midcap 150 Index Fund",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 3950, "1M (%)": -0.40, "3M (%)": -2.60, "6M (%)": 5.10, "1Y (%)": 8.40, "3Y (%)": 14.80, "5Y (%)": 14.60,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.30, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Nifty Midcap 150 Index Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 2100, "1M (%)": -0.38, "3M (%)": -2.58, "6M (%)": 5.12, "1Y (%)": 8.45, "3Y (%)": 14.85, "5Y (%)": 14.65,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.28, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Nifty Smallcap 250 Index Fund",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 2800, "1M (%)": -1.10, "3M (%)": -4.20, "6M (%)": 3.80, "1Y (%)": 6.20, "3Y (%)": 13.70, "5Y (%)": 13.50,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.35, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Nifty Smallcap 250 Index Fund",
        "AMC": "SBI Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 1250, "1M (%)": -1.08, "3M (%)": -4.18, "6M (%)": 3.82, "1Y (%)": 6.25, "3Y (%)": 13.75, "5Y (%)": 13.55,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.32, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Zerodha Nifty LargeMidcap 250 Index Fund",
        "AMC": "Zerodha Fund House", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 1450, "1M (%)": 0.45, "3M (%)": -1.90, "6M (%)": 4.10, "1Y (%)": 3.80, "3Y (%)": 12.35, "5Y (%)": 12.10,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.25, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "DSP Nifty 50 Equal Weight Index Fund",
        "AMC": "DSP Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 1820, "1M (%)": 0.30, "3M (%)": -2.20, "6M (%)": 3.60, "1Y (%)": 1.20, "3Y (%)": 11.50, "5Y (%)": 11.10,
        "Benchmark": "Nifty 50 Equal Weight TRI", "Expense Ratio (%)": 0.40, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Nifty 500 Index Fund",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Index Fund", "Fund Type": "Index Fund",
        "AUM (Cr)": 1650, "1M (%)": 0.50, "3M (%)": -1.80, "6M (%)": 3.90, "1Y (%)": 2.10, "3Y (%)": 11.90, "5Y (%)": 11.60,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.38, "Risk Rating": "Very High"
    },

    # ==========================================
    # 3. EXCHANGE TRADED FUNDS (ETFs)
    # ==========================================
    {
        "Scheme Name": "Nippon India ETF Nifty 50 BeES (NIFTYBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Broad Market ETF", "Fund Type": "ETF",
        "AUM (Cr)": 34500, "1M (%)": 0.74, "3M (%)": -1.42, "6M (%)": 2.78, "1Y (%)": -3.88, "3Y (%)": 9.25, "5Y (%)": 9.40,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.04, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Nifty 50 ETF (SETFNIF50)",
        "AMC": "SBI Mutual Fund", "Category": "Broad Market ETF", "Fund Type": "ETF",
        "AUM (Cr)": 205000, "1M (%)": 0.73, "3M (%)": -1.44, "6M (%)": 2.75, "1Y (%)": -3.90, "3Y (%)": 9.20, "5Y (%)": 9.35,
        "Benchmark": "Nifty 50 TRI", "Expense Ratio (%)": 0.03, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI S&P BSE Sensex ETF (SENSEXETF)",
        "AMC": "SBI Mutual Fund", "Category": "Broad Market ETF", "Fund Type": "ETF",
        "AUM (Cr)": 128000, "1M (%)": 0.69, "3M (%)": -1.50, "6M (%)": 2.68, "1Y (%)": -3.75, "3Y (%)": 8.95, "5Y (%)": 9.10,
        "Benchmark": "BSE Sensex TRI", "Expense Ratio (%)": 0.03, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India ETF Junior BeES (JUNIORBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Broad Market ETF", "Fund Type": "ETF",
        "AUM (Cr)": 6800, "1M (%)": 0.98, "3M (%)": -0.75, "6M (%)": 4.88, "1Y (%)": 4.35, "3Y (%)": 13.65, "5Y (%)": 11.95,
        "Benchmark": "Nifty Next 50 TRI", "Expense Ratio (%)": 0.12, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India ETF Bank BeES (BANKBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral ETF", "Fund Type": "ETF",
        "AUM (Cr)": 14200, "1M (%)": 1.40, "3M (%)": -0.50, "6M (%)": 6.20, "1Y (%)": 2.80, "3Y (%)": 10.40, "5Y (%)": 10.10,
        "Benchmark": "Nifty Bank TRI", "Expense Ratio (%)": 0.16, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India ETF PSU Bank BeES (PSUBNKBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral ETF", "Fund Type": "ETF",
        "AUM (Cr)": 4100, "1M (%)": -1.80, "3M (%)": -4.80, "6M (%)": 5.40, "1Y (%)": 6.80, "3Y (%)": 24.50, "5Y (%)": 23.20,
        "Benchmark": "Nifty PSU Bank TRI", "Expense Ratio (%)": 0.49, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India ETF Nifty IT (ITBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral ETF", "Fund Type": "ETF",
        "AUM (Cr)": 3800, "1M (%)": -1.20, "3M (%)": 4.50, "6M (%)": 9.40, "1Y (%)": 7.40, "3Y (%)": 11.20, "5Y (%)": 8.90,
        "Benchmark": "Nifty IT TRI", "Expense Ratio (%)": 0.22, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Nifty Auto ETF (AUTOBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral ETF", "Fund Type": "ETF",
        "AUM (Cr)": 445, "1M (%)": 1.15, "3M (%)": -1.75, "6M (%)": 6.40, "1Y (%)": 4.30, "3Y (%)": 16.40, "5Y (%)": 15.60,
        "Benchmark": "Nifty Auto TRI", "Expense Ratio (%)": 0.22, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Nifty Pharma ETF (PHARMABEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral ETF", "Fund Type": "ETF",
        "AUM (Cr)": 620, "1M (%)": 1.25, "3M (%)": 2.20, "6M (%)": 11.80, "1Y (%)": 4.50, "3Y (%)": 17.80, "5Y (%)": 15.40,
        "Benchmark": "Nifty Pharma TRI", "Expense Ratio (%)": 0.22, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India ETF Infra BeES (INFRABEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 1450, "1M (%)": 0.75, "3M (%)": -1.20, "6M (%)": 5.90, "1Y (%)": -2.10, "3Y (%)": 19.40, "5Y (%)": 20.20,
        "Benchmark": "Nifty Infrastructure TRI", "Expense Ratio (%)": 0.49, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "CPSE ETF",
        "AMC": "Nippon India Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 41200, "1M (%)": -1.40, "3M (%)": -3.80, "6M (%)": 7.20, "1Y (%)": 8.40, "3Y (%)": 26.80, "5Y (%)": 27.40,
        "Benchmark": "Nifty CPSE Index", "Expense Ratio (%)": 0.05, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bharat 22 ETF (ICICIB22)",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 19800, "1M (%)": 0.20, "3M (%)": -2.40, "6M (%)": 6.80, "1Y (%)": 5.90, "3Y (%)": 21.20, "5Y (%)": 22.80,
        "Benchmark": "S&P BSE Bharat 22 Index", "Expense Ratio (%)": 0.05, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset Nifty EV and New Age Automotive ETF (EVINDIA)",
        "AMC": "Mirae Asset Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 180, "1M (%)": 1.10, "3M (%)": -2.40, "6M (%)": 5.40, "1Y (%)": 4.80, "3Y (%)": 16.50, "5Y (%)": 15.20,
        "Benchmark": "Nifty EV & New Age Automotive TRI", "Expense Ratio (%)": 0.29, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Groww Nifty EV and New Age Automotive ETF (GROWWEV)",
        "AMC": "Groww Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 200, "1M (%)": 1.08, "3M (%)": -2.42, "6M (%)": 5.38, "1Y (%)": 4.75, "3Y (%)": 16.45, "5Y (%)": 15.15,
        "Benchmark": "Nifty EV & New Age Automotive TRI", "Expense Ratio (%)": 0.32, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Nifty EV & New Age Auto ETF (EVIETF)",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 75, "1M (%)": 1.12, "3M (%)": -2.38, "6M (%)": 5.42, "1Y (%)": 4.82, "3Y (%)": 16.52, "5Y (%)": 15.22,
        "Benchmark": "Nifty EV & New Age Automotive TRI", "Expense Ratio (%)": 0.30, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset Nifty India New Age Consumption ETF (CONSUMER)",
        "AMC": "Mirae Asset Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 60, "1M (%)": 1.45, "3M (%)": 0.80, "6M (%)": 7.80, "1Y (%)": 12.40, "3Y (%)": 18.20, "5Y (%)": 16.10,
        "Benchmark": "Nifty India New Age Consumption TRI", "Expense Ratio (%)": 0.32, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Tata Nifty India Digital ETF (TNIDETF)",
        "AMC": "Tata Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 176, "1M (%)": 1.10, "3M (%)": 2.10, "6M (%)": 8.40, "1Y (%)": 11.20, "3Y (%)": 15.40, "5Y (%)": 13.80,
        "Benchmark": "Nifty India Digital TRI", "Expense Ratio (%)": 0.40, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Nifty India Defence ETF (MODEFENCE)",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Thematic ETF", "Fund Type": "ETF",
        "AUM (Cr)": 3100, "1M (%)": 1.75, "3M (%)": 2.30, "6M (%)": 14.60, "1Y (%)": 6.20, "3Y (%)": 35.20, "5Y (%)": 28.10,
        "Benchmark": "Nifty India Defence TRI", "Expense Ratio (%)": 0.35, "Risk Rating": "Very High"
    },

    # --- COMMODITY ETFS ---
    {
        "Scheme Name": "Nippon India ETF Gold BeES (GOLDBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 56800, "1M (%)": 2.80, "3M (%)": 6.40, "6M (%)": 14.20, "1Y (%)": 24.50, "3Y (%)": 15.80, "5Y (%)": 14.10,
        "Benchmark": "Domestic Price of Gold", "Expense Ratio (%)": 0.80, "Risk Rating": "High"
    },
    {
        "Scheme Name": "ICICI Prudential Gold ETF (GOLDIETF)",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 27580, "1M (%)": 2.82, "3M (%)": 6.45, "6M (%)": 14.30, "1Y (%)": 24.70, "3Y (%)": 16.05, "5Y (%)": 14.35,
        "Benchmark": "Domestic Price of Gold", "Expense Ratio (%)": 0.50, "Risk Rating": "High"
    },
    {
        "Scheme Name": "SBI Gold ETF (SETFGOLD)",
        "AMC": "SBI Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 26450, "1M (%)": 2.81, "3M (%)": 6.42, "6M (%)": 14.25, "1Y (%)": 24.60, "3Y (%)": 15.90, "5Y (%)": 14.20,
        "Benchmark": "Domestic Price of Gold", "Expense Ratio (%)": 0.65, "Risk Rating": "High"
    },
    {
        "Scheme Name": "HDFC Gold ETF (HDFCGOLD)",
        "AMC": "HDFC Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 23400, "1M (%)": 2.81, "3M (%)": 6.43, "6M (%)": 14.28, "1Y (%)": 24.65, "3Y (%)": 15.95, "5Y (%)": 14.25,
        "Benchmark": "Domestic Price of Gold", "Expense Ratio (%)": 0.59, "Risk Rating": "High"
    },
    {
        "Scheme Name": "Kotak Gold ETF (GOLD1)",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 14400, "1M (%)": 2.80, "3M (%)": 6.41, "6M (%)": 14.22, "1Y (%)": 24.55, "3Y (%)": 15.85, "5Y (%)": 14.15,
        "Benchmark": "Domestic Price of Gold", "Expense Ratio (%)": 0.55, "Risk Rating": "High"
    },
    {
        "Scheme Name": "Zerodha Gold ETF (GOLDCASE)",
        "AMC": "Zerodha Fund House", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 2850, "1M (%)": 2.84, "3M (%)": 6.48, "6M (%)": 14.35, "1Y (%)": 24.85, "3Y (%)": 16.20, "5Y (%)": 14.50,
        "Benchmark": "Domestic Price of Gold", "Expense Ratio (%)": 0.32, "Risk Rating": "High"
    },
    {
        "Scheme Name": "Nippon India Silver ETF (SILVERBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 31195, "1M (%)": 4.20, "3M (%)": 9.10, "6M (%)": 22.40, "1Y (%)": 31.80, "3Y (%)": 18.90, "5Y (%)": 15.40,
        "Benchmark": "Domestic Price of Silver", "Expense Ratio (%)": 0.56, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Silver ETF (SILVERIETF)",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 14340, "1M (%)": 4.25, "3M (%)": 9.20, "6M (%)": 22.60, "1Y (%)": 32.10, "3Y (%)": 19.10, "5Y (%)": 15.60,
        "Benchmark": "Domestic Price of Silver", "Expense Ratio (%)": 0.40, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Silver ETF (HDFCSILVER)",
        "AMC": "HDFC Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 7724, "1M (%)": 4.22, "3M (%)": 9.15, "6M (%)": 22.50, "1Y (%)": 31.95, "3Y (%)": 19.00, "5Y (%)": 15.50,
        "Benchmark": "Domestic Price of Silver", "Expense Ratio (%)": 0.50, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Silver ETF (SBISILVER)",
        "AMC": "SBI Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 5817, "1M (%)": 4.24, "3M (%)": 9.18, "6M (%)": 22.55, "1Y (%)": 32.05, "3Y (%)": 19.05, "5Y (%)": 15.55,
        "Benchmark": "Domestic Price of Silver", "Expense Ratio (%)": 0.41, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Tata Silver ETF (TATSILV)",
        "AMC": "Tata Mutual Fund", "Category": "Commodity ETF", "Fund Type": "ETF",
        "AUM (Cr)": 5165, "1M (%)": 4.26, "3M (%)": 9.22, "6M (%)": 22.65, "1Y (%)": 32.15, "3Y (%)": 19.12, "5Y (%)": 15.62,
        "Benchmark": "Domestic Price of Silver", "Expense Ratio (%)": 0.46, "Risk Rating": "Very High"
    },

    # --- INTERNATIONAL ETFS ---
    {
        "Scheme Name": "Motilal Oswal Nasdaq 100 ETF (MON100)",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "International ETF", "Fund Type": "ETF",
        "AUM (Cr)": 8400, "1M (%)": 2.10, "3M (%)": 5.80, "6M (%)": 12.90, "1Y (%)": 19.40, "3Y (%)": 17.80, "5Y (%)": 16.50,
        "Benchmark": "NASDAQ-100 TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset NYSE FANG+ ETF (MAFANG)",
        "AMC": "Mirae Asset Mutual Fund", "Category": "International ETF", "Fund Type": "ETF",
        "AUM (Cr)": 2850, "1M (%)": 2.60, "3M (%)": 7.10, "6M (%)": 16.40, "1Y (%)": 24.80, "3Y (%)": 22.60, "5Y (%)": 20.40,
        "Benchmark": "NYSE FANG+ TRI", "Expense Ratio (%)": 0.33, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset S&P 500 Top 50 ETF (MASPTOP50)",
        "AMC": "Mirae Asset Mutual Fund", "Category": "International ETF", "Fund Type": "ETF",
        "AUM (Cr)": 1150, "1M (%)": 1.80, "3M (%)": 4.90, "6M (%)": 11.20, "1Y (%)": 17.20, "3Y (%)": 15.40, "5Y (%)": 14.80,
        "Benchmark": "S&P 500 Top 50 TRI", "Expense Ratio (%)": 0.35, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India ETF Hang Seng BeES (HNGSNGBEES)",
        "AMC": "Nippon India Mutual Fund", "Category": "International ETF", "Fund Type": "ETF",
        "AUM (Cr)": 480, "1M (%)": 3.80, "3M (%)": 8.40, "6M (%)": 18.20, "1Y (%)": 14.50, "3Y (%)": 4.20, "5Y (%)": -2.40,
        "Benchmark": "Hang Seng Index", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },

    # ==========================================
    # 4. FLEXI CAP ACTIVE FUNDS
    # ==========================================
    {
        "Scheme Name": "Parag Parikh Flexi Cap Fund",
        "AMC": "PPFAS Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 145070, "1M (%)": 0.90, "3M (%)": -1.10, "6M (%)": 3.80, "1Y (%)": -4.55, "3Y (%)": 12.42, "5Y (%)": 10.79,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.63, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Flexi Cap Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 108547, "1M (%)": 0.85, "3M (%)": -1.30, "6M (%)": 4.10, "1Y (%)": -3.52, "3Y (%)": 14.70, "5Y (%)": 15.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Kotak Flexi Cap Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 56392, "1M (%)": 0.45, "3M (%)": -2.20, "6M (%)": 1.90, "1Y (%)": -5.83, "3Y (%)": 9.15, "5Y (%)": 8.28,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.65, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Aditya Birla Sun Life Flexi Cap Fund",
        "AMC": "Aditya Birla Sun Life Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 27982, "1M (%)": 1.20, "3M (%)": 0.20, "6M (%)": 5.40, "1Y (%)": 2.10, "3Y (%)": 11.35, "5Y (%)": 13.80,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.90, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Flexicap Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 25500, "1M (%)": 1.15, "3M (%)": 0.40, "6M (%)": 5.80, "1Y (%)": 3.26, "3Y (%)": 14.40, "5Y (%)": 14.15,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "UTI Flexi Cap Fund",
        "AMC": "UTI Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 22495, "1M (%)": 0.35, "3M (%)": -2.50, "6M (%)": 1.10, "1Y (%)": -5.06, "3Y (%)": 7.85, "5Y (%)": 4.50,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.92, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Flexicap Fund",
        "AMC": "SBI Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 22109, "1M (%)": 0.60, "3M (%)": -1.70, "6M (%)": 2.60, "1Y (%)": -2.10, "3Y (%)": 8.12, "5Y (%)": 7.80,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Franklin India Flexi Cap Fund",
        "AMC": "Franklin Templeton Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 18780, "1M (%)": 0.80, "3M (%)": -1.40, "6M (%)": 3.40, "1Y (%)": -2.85, "3Y (%)": 9.90, "5Y (%)": 10.80,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.95, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Flexi Cap Fund",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 13800, "1M (%)": 1.05, "3M (%)": 0.10, "6M (%)": 6.10, "1Y (%)": 1.80, "3Y (%)": 15.60, "5Y (%)": 14.80,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Canara Robeco Flexi Cap Fund",
        "AMC": "Canara Robeco Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 13400, "1M (%)": 0.75, "3M (%)": -1.25, "6M (%)": 3.60, "1Y (%)": -2.40, "3Y (%)": 12.20, "5Y (%)": 11.90,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Axis Flexi Cap Fund",
        "AMC": "Axis Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 13600, "1M (%)": 0.40, "3M (%)": -2.15, "6M (%)": 1.80, "1Y (%)": -4.20, "3Y (%)": 8.40, "5Y (%)": 7.10,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.70, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "DSP Flexi Cap Fund",
        "AMC": "DSP Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 12200, "1M (%)": 0.70, "3M (%)": -1.45, "6M (%)": 3.20, "1Y (%)": -2.90, "3Y (%)": 11.40, "5Y (%)": 11.10,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Flexi Cap Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 9600, "1M (%)": 0.65, "3M (%)": -1.60, "6M (%)": 3.10, "1Y (%)": -3.10, "3Y (%)": 12.60, "5Y (%)": 12.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Quant Flexi Cap Fund",
        "AMC": "Quant Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 7350, "1M (%)": -0.80, "3M (%)": -3.90, "6M (%)": 2.40, "1Y (%)": -5.90, "3Y (%)": 14.80, "5Y (%)": 18.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.78, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "JM Flexicap Fund",
        "AMC": "JM Financial Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 5180, "1M (%)": 1.30, "3M (%)": 0.50, "6M (%)": 6.80, "1Y (%)": -1.10, "3Y (%)": 20.20, "5Y (%)": 18.60,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.52, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bank of India Flexi Cap Fund",
        "AMC": "Bank of India Mutual Fund", "Category": "Flexi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 2180, "1M (%)": 1.15, "3M (%)": 0.30, "6M (%)": 5.90, "1Y (%)": -1.60, "3Y (%)": 18.00, "5Y (%)": 17.50,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.55, "Risk Rating": "Very High"
    },

    # ==========================================
    # 5. MID CAP ACTIVE FUNDS
    # ==========================================
    {
        "Scheme Name": "HDFC Mid-Cap Opportunities Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 104500, "1M (%)": 0.40, "3M (%)": -1.80, "6M (%)": 4.60, "1Y (%)": -2.90, "3Y (%)": 18.20, "5Y (%)": 17.85,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.78, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Kotak Midcap Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 68900, "1M (%)": 0.35, "3M (%)": -1.95, "6M (%)": 4.10, "1Y (%)": -3.10, "3Y (%)": 15.90, "5Y (%)": 15.70,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.60, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Growth Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 50176, "1M (%)": 0.50, "3M (%)": -1.70, "6M (%)": 4.80, "1Y (%)": -2.75, "3Y (%)": 18.10, "5Y (%)": 17.20,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Midcap Fund",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 38000, "1M (%)": 1.20, "3M (%)": 0.60, "6M (%)": 7.40, "1Y (%)": 1.40, "3Y (%)": 22.40, "5Y (%)": 21.80,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Axis Midcap Fund",
        "AMC": "Axis Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 34450, "1M (%)": 0.20, "3M (%)": -2.10, "6M (%)": 3.20, "1Y (%)": -1.90, "3Y (%)": 12.80, "5Y (%)": 11.40,
        "Benchmark": "BSE 150 MidCap TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Midcap Fund (Magnum)",
        "AMC": "SBI Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 23282, "1M (%)": 0.15, "3M (%)": -2.30, "6M (%)": 3.10, "1Y (%)": -3.80, "3Y (%)": 12.90, "5Y (%)": 13.70,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset Midcap Fund",
        "AMC": "Mirae Asset Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 17500, "1M (%)": 0.40, "3M (%)": -1.90, "6M (%)": 3.90, "1Y (%)": -2.80, "3Y (%)": 13.60, "5Y (%)": 13.10,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.62, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "DSP Midcap Fund",
        "AMC": "DSP Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 18200, "1M (%)": 0.30, "3M (%)": -2.05, "6M (%)": 3.50, "1Y (%)": -3.40, "3Y (%)": 13.20, "5Y (%)": 12.80,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HSBC Midcap Fund",
        "AMC": "HSBC Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 11900, "1M (%)": 0.75, "3M (%)": -0.40, "6M (%)": 5.40, "1Y (%)": -0.40, "3Y (%)": 18.50, "5Y (%)": 16.80,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.72, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Edelweiss Mid Cap Fund",
        "AMC": "Edelweiss Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 8920, "1M (%)": 0.90, "3M (%)": 0.20, "6M (%)": 6.20, "1Y (%)": 0.90, "3Y (%)": 21.15, "5Y (%)": 19.80,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.55, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Invesco India Midcap Fund",
        "AMC": "Invesco India Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 6450, "1M (%)": 1.10, "3M (%)": 0.40, "6M (%)": 6.90, "1Y (%)": 1.85, "3Y (%)": 21.60, "5Y (%)": 19.40,
        "Benchmark": "BSE 150 MidCap TRI", "Expense Ratio (%)": 0.65, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Tata Mid Cap Growth Fund",
        "AMC": "Tata Mutual Fund", "Category": "Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 5400, "1M (%)": 0.55, "3M (%)": -1.60, "6M (%)": 4.40, "1Y (%)": -2.20, "3Y (%)": 16.40, "5Y (%)": 15.80,
        "Benchmark": "Nifty Midcap 150 TRI", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },

    # ==========================================
    # 6. SMALL CAP ACTIVE FUNDS
    # ==========================================
    {
        "Scheme Name": "Nippon India Small Cap Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 81200, "1M (%)": -0.80, "3M (%)": -3.80, "6M (%)": 4.10, "1Y (%)": -5.40, "3Y (%)": 17.65, "5Y (%)": 19.40,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.70, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Small Cap Fund",
        "AMC": "SBI Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 41850, "1M (%)": -0.90, "3M (%)": -3.90, "6M (%)": 3.40, "1Y (%)": -4.90, "3Y (%)": 13.40, "5Y (%)": 14.60,
        "Benchmark": "BSE 250 SmallCap TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Small Cap Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 40801, "1M (%)": -0.95, "3M (%)": -4.10, "6M (%)": 3.20, "1Y (%)": -5.80, "3Y (%)": 14.90, "5Y (%)": 16.30,
        "Benchmark": "BSE 250 SmallCap TRI", "Expense Ratio (%)": 0.72, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Quant Small Cap Fund",
        "AMC": "Quant Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 35557, "1M (%)": -1.40, "3M (%)": -5.80, "6M (%)": 2.10, "1Y (%)": -7.90, "3Y (%)": 16.80, "5Y (%)": 20.10,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.76, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Kotak Small Cap Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 18200, "1M (%)": -0.70, "3M (%)": -3.50, "6M (%)": 3.80, "1Y (%)": -4.20, "3Y (%)": 14.10, "5Y (%)": 15.20,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.55, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Franklin India Smaller Companies Fund",
        "AMC": "Franklin Templeton Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 14200, "1M (%)": -0.65, "3M (%)": -3.40, "6M (%)": 4.20, "1Y (%)": -4.60, "3Y (%)": 17.10, "5Y (%)": 18.20,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bandhan Small Cap Fund",
        "AMC": "Bandhan Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 11850, "1M (%)": 1.40, "3M (%)": 0.80, "6M (%)": 8.90, "1Y (%)": 3.80, "3Y (%)": 32.00, "5Y (%)": 23.40,
        "Benchmark": "BSE 250 SmallCap TRI", "Expense Ratio (%)": 0.45, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Axis Small Cap Fund",
        "AMC": "Axis Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 23400, "1M (%)": -0.50, "3M (%)": -3.20, "6M (%)": 4.10, "1Y (%)": -3.90, "3Y (%)": 13.90, "5Y (%)": 15.80,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.52, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Invesco India Smallcap Fund",
        "AMC": "Invesco India Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 6920, "1M (%)": 1.10, "3M (%)": 0.40, "6M (%)": 7.80, "1Y (%)": 1.90, "3Y (%)": 26.70, "5Y (%)": 22.10,
        "Benchmark": "BSE 250 SmallCap TRI", "Expense Ratio (%)": 0.50, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Canara Robeco Small Cap Fund",
        "AMC": "Canara Robeco Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 11500, "1M (%)": -0.60, "3M (%)": -3.10, "6M (%)": 4.40, "1Y (%)": -3.40, "3Y (%)": 16.50, "5Y (%)": 17.90,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.48, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Tata Small Cap Fund",
        "AMC": "Tata Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 9100, "1M (%)": -0.55, "3M (%)": -2.90, "6M (%)": 4.60, "1Y (%)": -3.10, "3Y (%)": 16.80, "5Y (%)": 18.40,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.42, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mahindra Manulife Small Cap Fund",
        "AMC": "Mahindra Manulife Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 5120, "1M (%)": 0.20, "3M (%)": -1.80, "6M (%)": 5.90, "1Y (%)": -2.40, "3Y (%)": 19.20, "5Y (%)": 17.50,
        "Benchmark": "BSE 250 SmallCap TRI", "Expense Ratio (%)": 0.45, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ITI Small Cap Fund",
        "AMC": "ITI Mutual Fund", "Category": "Small Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 2850, "1M (%)": 0.95, "3M (%)": 0.10, "6M (%)": 7.40, "1Y (%)": 0.60, "3Y (%)": 23.50, "5Y (%)": 18.90,
        "Benchmark": "Nifty Smallcap 250 TRI", "Expense Ratio (%)": 0.48, "Risk Rating": "Very High"
    },

    # ==========================================
    # 7. LARGE & MID CAP ACTIVE FUNDS
    # ==========================================
    {
        "Scheme Name": "Mirae Asset Large & Midcap Fund",
        "AMC": "Mirae Asset Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 44100, "1M (%)": 0.50, "3M (%)": -1.90, "6M (%)": 3.40, "1Y (%)": -4.10, "3Y (%)": 11.80, "5Y (%)": 11.20,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.62, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Large & Midcap Fund",
        "AMC": "SBI Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 41400, "1M (%)": 0.60, "3M (%)": -1.60, "6M (%)": 3.80, "1Y (%)": -2.50, "3Y (%)": 13.85, "5Y (%)": 13.90,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.78, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Kotak Equity Opportunities Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 32325, "1M (%)": 0.65, "3M (%)": -1.55, "6M (%)": 3.90, "1Y (%)": -2.65, "3Y (%)": 14.10, "5Y (%)": 13.50,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.60, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Large & Mid Cap Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 31628, "1M (%)": 0.95, "3M (%)": -0.80, "6M (%)": 5.10, "1Y (%)": 0.45, "3Y (%)": 16.20, "5Y (%)": 16.05,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Large and Mid Cap Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 29400, "1M (%)": 0.70, "3M (%)": -1.45, "6M (%)": 4.20, "1Y (%)": -3.15, "3Y (%)": 15.10, "5Y (%)": 15.05,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.80, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bandhan Core Equity Fund",
        "AMC": "Bandhan Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 19900, "1M (%)": 1.10, "3M (%)": -0.20, "6M (%)": 5.80, "1Y (%)": 0.90, "3Y (%)": 17.80, "5Y (%)": 16.20,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.65, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Canara Robeco Emerging Equities Fund",
        "AMC": "Canara Robeco Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 23500, "1M (%)": 0.68, "3M (%)": -1.50, "6M (%)": 4.10, "1Y (%)": -2.80, "3Y (%)": 13.90, "5Y (%)": 13.40,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Motilal Oswal Large and Midcap Fund",
        "AMC": "Motilal Oswal Mutual Fund", "Category": "Large & Mid Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 9840, "1M (%)": 1.35, "3M (%)": 0.70, "6M (%)": 8.10, "1Y (%)": 3.10, "3Y (%)": 24.80, "5Y (%)": 21.50,
        "Benchmark": "Nifty LargeMidcap 250 TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },

    # ==========================================
    # 8. MULTI CAP ACTIVE FUNDS
    # ==========================================
    {
        "Scheme Name": "Nippon India Multi Cap Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Multi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 53767, "1M (%)": 0.60, "3M (%)": -1.70, "6M (%)": 4.50, "1Y (%)": -3.20, "3Y (%)": 16.40, "5Y (%)": 17.10,
        "Benchmark": "Nifty 500 Multicap 50:25:25 TRI", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Kotak Multicap Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Multi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 30335, "1M (%)": 0.55, "3M (%)": -1.80, "6M (%)": 4.20, "1Y (%)": -3.40, "3Y (%)": 16.90, "5Y (%)": 16.50,
        "Benchmark": "Nifty 500 Multicap 50:25:25 TRI", "Expense Ratio (%)": 0.48, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Multi Cap Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Multi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 19490, "1M (%)": 0.50, "3M (%)": -1.90, "6M (%)": 3.90, "1Y (%)": -3.60, "3Y (%)": 15.80, "5Y (%)": 15.40,
        "Benchmark": "Nifty 500 Multicap 50:25:25 TRI", "Expense Ratio (%)": 0.60, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Multicap Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Multi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 14200, "1M (%)": 0.70, "3M (%)": -1.40, "6M (%)": 4.80, "1Y (%)": -2.40, "3Y (%)": 16.10, "5Y (%)": 15.80,
        "Benchmark": "Nifty 500 Multicap 50:25:25 TRI", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Baroda BNP Paribas Multi Cap Fund",
        "AMC": "Baroda BNP Paribas Mutual Fund", "Category": "Multi Cap", "Fund Type": "Active Equity",
        "AUM (Cr)": 3800, "1M (%)": 0.65, "3M (%)": -1.50, "6M (%)": 4.40, "1Y (%)": -2.90, "3Y (%)": 15.40, "5Y (%)": 14.90,
        "Benchmark": "Nifty 500 Multicap 50:25:25 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },

    # ==========================================
    # 9. VALUE & CONTRA FUNDS
    # ==========================================
    {
        "Scheme Name": "ICICI Prudential Value Discovery Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Value / Contra", "Fund Type": "Active Equity",
        "AUM (Cr)": 58600, "1M (%)": 0.90, "3M (%)": -0.70, "6M (%)": 4.80, "1Y (%)": -1.20, "3Y (%)": 15.60, "5Y (%)": 16.10,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.95, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Contra Fund",
        "AMC": "SBI Mutual Fund", "Category": "Value / Contra", "Fund Type": "Active Equity",
        "AUM (Cr)": 46200, "1M (%)": 0.75, "3M (%)": -1.30, "6M (%)": 4.20, "1Y (%)": -2.80, "3Y (%)": 16.10, "5Y (%)": 18.25,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bandhan Sterling Value Fund",
        "AMC": "Bandhan Mutual Fund", "Category": "Value / Contra", "Fund Type": "Active Equity",
        "AUM (Cr)": 12500, "1M (%)": 0.85, "3M (%)": -0.90, "6M (%)": 4.90, "1Y (%)": -1.50, "3Y (%)": 15.20, "5Y (%)": 16.80,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.62, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Tata Equity P/E Fund",
        "AMC": "Tata Mutual Fund", "Category": "Value / Contra", "Fund Type": "Active Equity",
        "AUM (Cr)": 8400, "1M (%)": 0.80, "3M (%)": -1.10, "6M (%)": 4.40, "1Y (%)": -2.10, "3Y (%)": 14.80, "5Y (%)": 15.40,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.78, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "UTI Value Fund",
        "AMC": "UTI Mutual Fund", "Category": "Value / Contra", "Fund Type": "Active Equity",
        "AUM (Cr)": 9100, "1M (%)": 0.70, "3M (%)": -1.35, "6M (%)": 3.90, "1Y (%)": -2.60, "3Y (%)": 13.90, "5Y (%)": 14.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.95, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Invesco India Contra Fund",
        "AMC": "Invesco India Mutual Fund", "Category": "Value / Contra", "Fund Type": "Active Equity",
        "AUM (Cr)": 15800, "1M (%)": 0.78, "3M (%)": -1.20, "6M (%)": 4.10, "1Y (%)": -2.40, "3Y (%)": 14.50, "5Y (%)": 15.10,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.65, "Risk Rating": "Very High"
    },

    # ==========================================
    # 10. ELSS (TAX SAVER) FUNDS
    # ==========================================
    {
        "Scheme Name": "SBI ELSS Tax Saver Fund",
        "AMC": "SBI Mutual Fund", "Category": "ELSS (Tax Saver)", "Fund Type": "Active Equity",
        "AUM (Cr)": 31735, "1M (%)": 0.80, "3M (%)": -1.20, "6M (%)": 4.50, "1Y (%)": -2.20, "3Y (%)": 16.50, "5Y (%)": 15.80,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.95, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Axis ELSS Tax Saver Fund",
        "AMC": "Axis Mutual Fund", "Category": "ELSS (Tax Saver)", "Fund Type": "Active Equity",
        "AUM (Cr)": 31450, "1M (%)": 0.25, "3M (%)": -2.60, "6M (%)": 1.20, "1Y (%)": -4.80, "3Y (%)": 7.90, "5Y (%)": 5.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset ELSS Tax Saver Fund",
        "AMC": "Mirae Asset Mutual Fund", "Category": "ELSS (Tax Saver)", "Fund Type": "Active Equity",
        "AUM (Cr)": 26428, "1M (%)": 0.55, "3M (%)": -1.85, "6M (%)": 3.10, "1Y (%)": -3.70, "3Y (%)": 11.50, "5Y (%)": 11.10,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Parag Parikh ELSS Tax Saver Fund",
        "AMC": "PPFAS Mutual Fund", "Category": "ELSS (Tax Saver)", "Fund Type": "Active Equity",
        "AUM (Cr)": 6800, "1M (%)": 0.88, "3M (%)": -1.15, "6M (%)": 3.90, "1Y (%)": -3.80, "3Y (%)": 13.10, "5Y (%)": 12.80,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.65, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "DSP ELSS Tax Saver Fund",
        "AMC": "DSP Mutual Fund", "Category": "ELSS (Tax Saver)", "Fund Type": "Active Equity",
        "AUM (Cr)": 15600, "1M (%)": 0.72, "3M (%)": -1.35, "6M (%)": 3.80, "1Y (%)": -2.70, "3Y (%)": 13.40, "5Y (%)": 13.10,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bandhan ELSS Tax Saver Fund",
        "AMC": "Bandhan Mutual Fund", "Category": "ELSS (Tax Saver)", "Fund Type": "Active Equity",
        "AUM (Cr)": 6400, "1M (%)": 0.90, "3M (%)": -0.80, "6M (%)": 5.10, "1Y (%)": -1.10, "3Y (%)": 15.80, "5Y (%)": 15.20,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },

    # ==========================================
    # 11. FOCUSED FUNDS
    # ==========================================
    {
        "Scheme Name": "SBI Focused Equity Fund",
        "AMC": "SBI Mutual Fund", "Category": "Focused", "Fund Type": "Active Equity",
        "AUM (Cr)": 50650, "1M (%)": 0.65, "3M (%)": -1.65, "6M (%)": 2.80, "1Y (%)": -2.40, "3Y (%)": 9.60, "5Y (%)": 7.90,
        "Benchmark": "BSE 500 TRI", "Expense Ratio (%)": 0.70, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Focused 30 Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Focused", "Fund Type": "Active Equity",
        "AUM (Cr)": 27350, "1M (%)": 0.95, "3M (%)": -0.85, "6M (%)": 5.20, "1Y (%)": -0.95, "3Y (%)": 16.40, "5Y (%)": 17.40,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Focused Equity Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Focused", "Fund Type": "Active Equity",
        "AUM (Cr)": 9400, "1M (%)": 0.85, "3M (%)": -1.10, "6M (%)": 4.60, "1Y (%)": -1.80, "3Y (%)": 14.80, "5Y (%)": 14.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Mirae Asset Focused Fund",
        "AMC": "Mirae Asset Mutual Fund", "Category": "Focused", "Fund Type": "Active Equity",
        "AUM (Cr)": 8800, "1M (%)": 0.50, "3M (%)": -1.95, "6M (%)": 3.10, "1Y (%)": -3.80, "3Y (%)": 10.90, "5Y (%)": 10.20,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.58, "Risk Rating": "Very High"
    },

    # ==========================================
    # 12. SECTORAL, THEMATIC & INNOVATION FUNDS
    # ==========================================
    {
        "Scheme Name": "HDFC Defence Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 5450, "1M (%)": 1.80, "3M (%)": 2.40, "6M (%)": 14.80, "1Y (%)": 6.40, "3Y (%)": 35.60, "5Y (%)": 28.50,
        "Benchmark": "Nifty India Defence TRI", "Expense Ratio (%)": 0.68, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Automotive Opportunities Fund",
        "AMC": "SBI Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 6200, "1M (%)": 1.05, "3M (%)": -1.80, "6M (%)": 6.20, "1Y (%)": 4.10, "3Y (%)": 16.20, "5Y (%)": 15.40,
        "Benchmark": "Nifty Auto TRI", "Expense Ratio (%)": 0.78, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Innovation Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 7800, "1M (%)": 1.25, "3M (%)": 0.40, "6M (%)": 7.10, "1Y (%)": 3.80, "3Y (%)": 17.10, "5Y (%)": 16.40,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.72, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI Innovative Opportunities Fund",
        "AMC": "SBI Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 5493, "1M (%)": 1.10, "3M (%)": -0.20, "6M (%)": 6.40, "1Y (%)": 2.90, "3Y (%)": 15.80, "5Y (%)": 14.90,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.75, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Innovation Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 3050, "1M (%)": 1.18, "3M (%)": 0.10, "6M (%)": 6.70, "1Y (%)": 3.20, "3Y (%)": 16.40, "5Y (%)": 15.60,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.79, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential India Opportunities Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 36469, "1M (%)": 0.95, "3M (%)": -0.60, "6M (%)": 5.40, "1Y (%)": -0.80, "3Y (%)": 17.40, "5Y (%)": 17.90,
        "Benchmark": "Nifty 500 TRI", "Expense Ratio (%)": 0.72, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "LIC MF Infrastructure Fund",
        "AMC": "LIC Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 1120, "1M (%)": 0.85, "3M (%)": -0.90, "6M (%)": 6.80, "1Y (%)": -1.40, "3Y (%)": 20.50, "5Y (%)": 21.20,
        "Benchmark": "Nifty Infrastructure TRI", "Expense Ratio (%)": 1.15, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Power & Infra Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 7640, "1M (%)": 0.80, "3M (%)": -1.10, "6M (%)": 6.20, "1Y (%)": -2.30, "3Y (%)": 19.90, "5Y (%)": 20.80,
        "Benchmark": "Nifty Infrastructure TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Bank of India Manufacturing & Infra Fund",
        "AMC": "Bank of India Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 680, "1M (%)": 0.90, "3M (%)": -0.75, "6M (%)": 6.50, "1Y (%)": -0.80, "3Y (%)": 19.60, "5Y (%)": 20.10,
        "Benchmark": "BSE India Manufacturing & Infra", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "DSP India T.I.G.E.R. Fund",
        "AMC": "DSP Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 5420, "1M (%)": 0.70, "3M (%)": -1.25, "6M (%)": 5.80, "1Y (%)": -1.90, "3Y (%)": 17.80, "5Y (%)": 19.60,
        "Benchmark": "BSE India Infrastructure TRI", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "SBI PSU Fund",
        "AMC": "SBI Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 4950, "1M (%)": -1.75, "3M (%)": -4.60, "6M (%)": 5.80, "1Y (%)": 5.40, "3Y (%)": 18.70, "5Y (%)": 20.90,
        "Benchmark": "BSE PSU TRI", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Aditya Birla Sun Life PSU Equity Fund",
        "AMC": "Aditya Birla Sun Life Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 5680, "1M (%)": -1.70, "3M (%)": -4.50, "6M (%)": 6.10, "1Y (%)": 5.80, "3Y (%)": 18.90, "5Y (%)": 21.40,
        "Benchmark": "BSE PSU TRI", "Expense Ratio (%)": 0.78, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Technology Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 14500, "1M (%)": -1.10, "3M (%)": 4.80, "6M (%)": 9.40, "1Y (%)": 7.90, "3Y (%)": 12.10, "5Y (%)": 9.40,
        "Benchmark": "S&P BSE Teck TRI", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Tata Digital India Fund",
        "AMC": "Tata Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 11200, "1M (%)": -1.05, "3M (%)": 4.60, "6M (%)": 9.20, "1Y (%)": 7.60, "3Y (%)": 11.80, "5Y (%)": 9.10,
        "Benchmark": "Nifty IT TRI", "Expense Ratio (%)": 0.42, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "ICICI Prudential Pharma Healthcare and Diagnostics Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 4850, "1M (%)": 1.20, "3M (%)": 2.10, "6M (%)": 11.40, "1Y (%)": 4.20, "3Y (%)": 17.50, "5Y (%)": 15.10,
        "Benchmark": "BSE Healthcare TRI", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "Nippon India Pharma Fund",
        "AMC": "Nippon India Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 8400, "1M (%)": 1.25, "3M (%)": 2.25, "6M (%)": 11.90, "1Y (%)": 4.60, "3Y (%)": 18.10, "5Y (%)": 15.80,
        "Benchmark": "Nifty Pharma TRI", "Expense Ratio (%)": 0.88, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "UTI Transportation and Logistics Fund",
        "AMC": "UTI Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 4200, "1M (%)": 1.00, "3M (%)": -1.85, "6M (%)": 6.10, "1Y (%)": 3.90, "3Y (%)": 15.90, "5Y (%)": 15.10,
        "Benchmark": "Nifty Transportation and Logistics", "Expense Ratio (%)": 0.85, "Risk Rating": "Very High"
    },
    {
        "Scheme Name": "HDFC Transportation and Logistics Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Sectoral / Thematic", "Fund Type": "Active Equity",
        "AUM (Cr)": 2080, "1M (%)": 0.95, "3M (%)": -1.90, "6M (%)": 5.90, "1Y (%)": 3.70, "3Y (%)": 15.60, "5Y (%)": 14.80,
        "Benchmark": "Nifty Transportation and Logistics", "Expense Ratio (%)": 0.82, "Risk Rating": "Very High"
    },

    # ==========================================
    # 13. HYBRID & ARBITRAGE FUNDS
    # ==========================================
    {
        "Scheme Name": "HDFC Balanced Advantage Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Balanced Advantage", "Fund Type": "Hybrid",
        "AUM (Cr)": 105200, "1M (%)": 0.65, "3M (%)": -0.90, "6M (%)": 3.80, "1Y (%)": -1.80, "3Y (%)": 14.90, "5Y (%)": 15.65,
        "Benchmark": "Nifty 50 Hybrid Composite Debt 50:50", "Expense Ratio (%)": 0.72, "Risk Rating": "High"
    },
    {
        "Scheme Name": "SBI Equity Hybrid Fund",
        "AMC": "SBI Mutual Fund", "Category": "Aggressive Hybrid", "Fund Type": "Hybrid",
        "AUM (Cr)": 87400, "1M (%)": 0.55, "3M (%)": -1.10, "6M (%)": 3.10, "1Y (%)": -1.45, "3Y (%)": 9.80, "5Y (%)": 8.95,
        "Benchmark": "CRISIL Hybrid 35+65 Aggressive", "Expense Ratio (%)": 0.75, "Risk Rating": "High"
    },
    {
        "Scheme Name": "ICICI Prudential Multi-Asset Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Multi Asset Allocation", "Fund Type": "Hybrid",
        "AUM (Cr)": 86000, "1M (%)": 1.10, "3M (%)": 0.80, "6M (%)": 5.60, "1Y (%)": 2.40, "3Y (%)": 15.80, "5Y (%)": 16.40,
        "Benchmark": "Nifty 200 (65%) + Debt + Gold", "Expense Ratio (%)": 0.68, "Risk Rating": "High"
    },
    {
        "Scheme Name": "Kotak Equity Arbitrage Fund",
        "AMC": "Kotak Mahindra Mutual Fund", "Category": "Arbitrage", "Fund Type": "Hybrid",
        "AUM (Cr)": 75500, "1M (%)": 0.62, "3M (%)": 1.85, "6M (%)": 3.75, "1Y (%)": 7.45, "3Y (%)": 7.60, "5Y (%)": 6.65,
        "Benchmark": "Nifty 50 Arbitrage Index", "Expense Ratio (%)": 0.38, "Risk Rating": "Low"
    },
    {
        "Scheme Name": "ICICI Prudential Balanced Advantage Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Balanced Advantage", "Fund Type": "Hybrid",
        "AUM (Cr)": 73600, "1M (%)": 0.50, "3M (%)": -0.60, "6M (%)": 3.20, "1Y (%)": 1.85, "3Y (%)": 11.40, "5Y (%)": 10.90,
        "Benchmark": "CRISIL Hybrid 50+50 Moderate", "Expense Ratio (%)": 0.85, "Risk Rating": "High"
    },
    {
        "Scheme Name": "ICICI Prudential Equity & Debt Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Aggressive Hybrid", "Fund Type": "Hybrid",
        "AUM (Cr)": 51600, "1M (%)": 0.80, "3M (%)": -0.70, "6M (%)": 4.40, "1Y (%)": 1.10, "3Y (%)": 15.25, "5Y (%)": 15.90,
        "Benchmark": "CRISIL Hybrid 35+65 Aggressive", "Expense Ratio (%)": 0.78, "Risk Rating": "High"
    },
    {
        "Scheme Name": "SBI Arbitrage Opportunities Fund",
        "AMC": "SBI Mutual Fund", "Category": "Arbitrage", "Fund Type": "Hybrid",
        "AUM (Cr)": 46800, "1M (%)": 0.61, "3M (%)": 1.82, "6M (%)": 3.70, "1Y (%)": 7.35, "3Y (%)": 7.50, "5Y (%)": 6.55,
        "Benchmark": "Nifty 50 Arbitrage Index", "Expense Ratio (%)": 0.40, "Risk Rating": "Low"
    },
    {
        "Scheme Name": "SBI Balanced Advantage Fund",
        "AMC": "SBI Mutual Fund", "Category": "Balanced Advantage", "Fund Type": "Hybrid",
        "AUM (Cr)": 40545, "1M (%)": 0.45, "3M (%)": -0.80, "6M (%)": 2.90, "1Y (%)": 1.20, "3Y (%)": 11.15, "5Y (%)": 10.40,
        "Benchmark": "Nifty 50 Hybrid Composite Debt 50:50", "Expense Ratio (%)": 0.75, "Risk Rating": "High"
    },
    {
        "Scheme Name": "ICICI Prudential Equity Arbitrage Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Arbitrage", "Fund Type": "Hybrid",
        "AUM (Cr)": 34100, "1M (%)": 0.60, "3M (%)": 1.80, "6M (%)": 3.68, "1Y (%)": 7.30, "3Y (%)": 7.45, "5Y (%)": 6.50,
        "Benchmark": "Nifty 50 Arbitrage Index", "Expense Ratio (%)": 0.42, "Risk Rating": "Low"
    },

    # ==========================================
    # 14. LIQUID & DEBT GIANTS
    # ==========================================
    {
        "Scheme Name": "SBI Liquid Fund",
        "AMC": "SBI Mutual Fund", "Category": "Liquid", "Fund Type": "Debt",
        "AUM (Cr)": 82500, "1M (%)": 0.58, "3M (%)": 1.76, "6M (%)": 3.55, "1Y (%)": 7.15, "3Y (%)": 7.10, "5Y (%)": 6.05,
        "Benchmark": "NIFTY Liquid Index A-I", "Expense Ratio (%)": 0.18, "Risk Rating": "Low to Moderate"
    },
    {
        "Scheme Name": "HDFC Liquid Fund",
        "AMC": "HDFC Mutual Fund", "Category": "Liquid", "Fund Type": "Debt",
        "AUM (Cr)": 74200, "1M (%)": 0.57, "3M (%)": 1.75, "6M (%)": 3.52, "1Y (%)": 7.12, "3Y (%)": 7.08, "5Y (%)": 6.02,
        "Benchmark": "CRISIL Liquid Debt A-I Index", "Expense Ratio (%)": 0.20, "Risk Rating": "Low to Moderate"
    },
    {
        "Scheme Name": "ICICI Prudential Liquid Fund",
        "AMC": "ICICI Prudential Mutual Fund", "Category": "Liquid", "Fund Type": "Debt",
        "AUM (Cr)": 62400, "1M (%)": 0.58, "3M (%)": 1.76, "6M (%)": 3.54, "1Y (%)": 7.14, "3Y (%)": 7.09, "5Y (%)": 6.04,
        "Benchmark": "NIFTY Liquid Index A-I", "Expense Ratio (%)": 0.19, "Risk Rating": "Low to Moderate"
    },
    {
        "Scheme Name": "Zerodha Nifty 1D Rate Liquid ETF (LIQUIDCASE)",
        "AMC": "Zerodha Fund House", "Category": "Liquid ETF", "Fund Type": "ETF",
        "AUM (Cr)": 3800, "1M (%)": 0.56, "3M (%)": 1.72, "6M (%)": 3.48, "1Y (%)": 7.05, "3Y (%)": 6.95, "5Y (%)": 5.95,
        "Benchmark": "Nifty 1D Rate Index", "Expense Ratio (%)": 0.22, "Risk Rating": "Low"
    },
    {
        "Scheme Name": "Bharat Bond ETF - April 2030 (EBBETF0430)",
        "AMC": "Edelweiss Mutual Fund", "Category": "Debt ETF", "Fund Type": "ETF",
        "AUM (Cr)": 18500, "1M (%)": 0.65, "3M (%)": 1.95, "6M (%)": 4.10, "1Y (%)": 7.80, "3Y (%)": 7.65, "5Y (%)": 7.40,
        "Benchmark": "Nifty BHARAT Bond Index - April 2030", "Expense Ratio (%)": 0.0005, "Risk Rating": "Moderate"
    }
]

df = pd.DataFrame(data)
output_path = os.path.join(os.path.dirname(__file__), "mutual_funds_data.csv")
df.to_csv(output_path, index=False)
print(f"Dataset successfully compiled at: {output_path}")
print(f"Total schemes: {len(df)}")
print(f"Categories: {df['Category'].nunique()} distinct categories")
print(f"AMCs: {df['AMC'].nunique()} fund houses")

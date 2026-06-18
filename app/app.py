from pathlib import Path
import time
import subprocess
import json
import os
import sys
from datetime import datetime

# #region agent log
def debug_log(message, data=None, hypothesis_id=None):
    log_path = "/home/user/Documents/ai-valuation-eda/.cursor/debug-d0f0a8.log"
    log_entry = {
        "sessionId": "d0f0a8",
        "timestamp": int(datetime.now().timestamp() * 1000),
        "location": "app/app.py:top",
        "message": message,
        "data": data or {},
        "hypothesisId": hypothesis_id
    }
    try:
        with open(log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except:
        pass

import streamlit as st
debug_log("Streamlit runtime check", {
    "version": getattr(st, "__version__", "unknown"),
    "file": getattr(st, "__file__", "unknown"),
    "has_components": hasattr(st, "components"),
    "dir_st": [attr for attr in dir(st) if not attr.startswith("_")]
}, hypothesis_id="1,2,3")
# #endregion

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent.parent / "analysis_data" / "analysis_base.csv"
CORE_METRICS = ["Total Revenue", "Net Income"]


def load_analysis_data() -> dict[str, pd.DataFrame]:
    analysis_base = pd.read_csv(DATA_PATH)
    analysis_base["fiscal_year_end"] = pd.to_datetime(analysis_base["fiscal_year_end"])

    core_financials = (
        analysis_base.loc[analysis_base["metric"].isin(CORE_METRICS), :]
        .sort_values(by=["symbol", "metric", "fiscal_year_end"])
        .copy()
    )
    
    core_financials["yoy_change"] = core_financials.groupby(["symbol", "metric"])["amount"].pct_change().mul(100)

    latest_core = core_financials.groupby(["symbol", "metric"], as_index=False).tail(1)

    valuation_snapshot = (
        analysis_base.drop_duplicates(subset=["symbol"])
        [
            [
                "symbol",
                "price_to_sales",
                "trailingPE",
                "forwardPE",
                "profitMargins",
                "info_total_revenue",
            ]
        ]
        .set_index("symbol")
        .round(2)
    )

    latest_wide = latest_core.pivot(
        index="symbol",
        columns="metric",
        values="amount",
    ).round(2)

    comparison = valuation_snapshot.join(latest_wide)

    comparison["valuation_label"] = np.where(
        comparison["price_to_sales"] == comparison["price_to_sales"].min(),
        "lower valuation",
        "higher valuation",
    )
    comparison["margin_label"] = np.where(
        comparison["profitMargins"] == comparison["profitMargins"].max(),
        "higher margin",
        "lower margin",
    )

    return {
        "latest_core": latest_core,
        "valuation_snapshot": valuation_snapshot,
        "comparison": comparison,
        "core_financials": core_financials, # --- ADD THIS LINE ---
    }


@st.cache_data
def get_data() -> dict[str, pd.DataFrame]:
    return load_analysis_data()


def billions(value: float) -> float:
    return value / 1_000_000_000


st.set_page_config(page_title="MSFT vs GOOGL Valuation", layout="wide")

# --- Sidebar Pipeline Trigger ---
with st.sidebar:
    st.header("Pipeline Control")
    
    if st.button("🔄 Run Data Pipeline", use_container_width=True):
        # 1. Create a progress bar
        progress_bar = st.progress(0)
        
        # Real-time terminal logs section
        st.markdown("### 📄 Real-Time Terminal Logs")
        log_placeholder = st.empty()
        log_lines = []
        
        def log(text):
            log_lines.append(text)
            log_placeholder.code("\n".join(log_lines), language="bash")
        
        try:
            with st.status("Initializing pipeline...", expanded=True) as status:
                # Step 1: Fetching Data
                status.update(label="📥 Step 1: Fetching raw data from Yahoo Finance...")
                progress_bar.progress(25)
                log("=== STEP 1: FETCH LOGS ===")
                
                # Run the fetch script and stream output in real-time
                process = subprocess.Popen(
                    [sys.executable, "data_fetch/fetch.py"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                if process.stdout:
                    for line in process.stdout:
                        log(line.strip())
                process.wait()
                if process.returncode != 0:
                    raise subprocess.CalledProcessError(process.returncode, process.args)
                time.sleep(1) # Small pause for visual effect
                
                # Step 2: SQL Transformations
                status.update(label="🔄 Step 2: Running DuckDB SQL transformations...")
                progress_bar.progress(60)
                log("\n=== STEP 2: SQL LOGS ===")
                
                # Run the SQL transformation files
                import duckdb
                con = duckdb.connect()
                sql_files = [
                    "sql/phase-b.sql",
                    "sql/phase-c.sql",
                    "sql/phase-d.sql",
                    "sql/phase-e.sql"
                ]
                for sql_file in sql_files:
                    log(f"Executing {sql_file}...")
                    with open(sql_file, "r") as f:
                        con.execute(f.read())
                    time.sleep(0.5)
                time.sleep(1)
                
                # Step 3: Reloading Data
                status.update(label="📊 Step 3: Reloading dashboard data...")
                progress_bar.progress(90)
                log("\n=== STEP 3: RELOAD ===")
                log("Cache cleared and dashboard reloaded.")
                st.cache_data.clear() # Clear Streamlit cache to load fresh data
                time.sleep(1)
                
                # Complete
                progress_bar.progress(100)
                status.update(label="✅ Pipeline completed successfully!", state="complete", expanded=False)
                
                # Save logs to session state (for subsequent runs, if needed)
                st.session_state["pipeline_logs"] = "\n".join(log_lines)
                
                # --- Capture Metadata on Success ---
                st.session_state["last_run_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state["run_status"] = "✅ Success"
                
            st.success("Dashboard updated with live data!")
            time.sleep(1)
            st.rerun() # Rerun the app to show the fresh data
        except Exception as e:
            # --- Capture Metadata on Failure ---
            st.session_state["last_run_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state["run_status"] = "❌ Failed"
            st.error(f"Pipeline Error: {e}")

    # --- Display Pipeline Metadata (Only in Sidebar) ---
    if "last_run_time" in st.session_state:
        st.divider()
        st.markdown("### 🛰️ Last Run Metadata")
        col_meta1, col_meta2 = st.columns(2)
        col_meta1.caption("**Timestamp:**")
        col_meta1.write(st.session_state["last_run_time"])
        col_meta2.caption("**Status:**")
        col_meta2.write(st.session_state["run_status"])

data = get_data()
latest_core = data["latest_core"]
valuation_snapshot = data["valuation_snapshot"]
comparison = data["comparison"]
core_financials = data["core_financials"] # <--- ADD THIS LINE HERE
msft = comparison.loc["MSFT"]
googl = comparison.loc["GOOGL"]

# --- 1. Latest Scale Section ---
with st.expander("📊 1. View Latest Revenue & Net Income Scale", expanded=False):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("MSFT Revenue ($B)", f"{billions(msft['Total Revenue']):.1f}")
    c2.metric("GOOGL Revenue ($B)", f"{billions(googl['Total Revenue']):.1f}")
    c3.metric("MSFT Net Income ($B)", f"{billions(msft['Net Income']):.1f}")
    c4.metric("GOOGL Net Income ($B)", f"{billions(googl['Net Income']):.1f}")

    scale_long = latest_core.assign(amount_b=latest_core["amount"] / 1_000_000_000)
    fig_scale = px.bar(
        scale_long, x="amount_b", y="symbol", color="symbol",
        facet_col="metric", orientation="h", text="amount_b",
        title="Latest Reported Scale ($ Billions)"
    )
    fig_scale.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    st.plotly_chart(fig_scale, use_container_width=True)

# --- 2. Valuation Section ---
with st.expander("📈 2. View Valuation Multiples Comparison"):
    val_long = valuation_snapshot.reset_index().melt(
        id_vars="symbol", value_vars=["price_to_sales", "trailingPE", "forwardPE"],
        var_name="metric", value_name="value"
    )
    metric_labels = {"price_to_sales": "P/S", "trailingPE": "Trailing P/E", "forwardPE": "Forward P/E"}
    val_long["metric"] = val_long["metric"].map(metric_labels)

    fig_val = px.bar(
        val_long, x="value", y="symbol", color="symbol",
        facet_col="metric", orientation="h", text="value",
        title="Valuation Multiples (Lower is usually 'cheaper')"
    )
    fig_val.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    st.plotly_chart(fig_val, use_container_width=True)

# --- 3. NEW: Growth Trajectory Section (The missing 10%) ---
with st.expander("🚀 3. View Growth Trajectory (YoY % Change)"):
    st.write("How fast are these companies growing? (Percentage change from previous year)")
    fig_growth = px.line(
        core_financials.dropna(), 
        x="fiscal_year_end", y="yoy_change", color="symbol", 
        facet_col="metric", markers=True,
        labels={"yoy_change": "Growth %", "fiscal_year_end": "Year"},
        title="Year-over-Year Growth Trends"
    )
    st.plotly_chart(fig_growth, use_container_width=True)

# --- 4. Comparison Table ---
with st.expander("📋 4. View Side-by-Side Raw Data"):
    st.dataframe(comparison, use_container_width=True)

# --- 5. Recommendations & Final Takeaway ---
with st.expander("🎯 5. View Recommendations & Final Takeaway"):
    
    # 1. Interactive Recommendation Engine
    st.markdown("### 🤖 Strategy Calculator")
    choice = st.radio(
        "Select your primary investment criteria:",
        ["Value (Lower P/S)", "Profitability (Higher Margins)", "Scale (Higher Revenue)"],
        horizontal=True,
        key="main_priority"
    )

    # Logic
    if choice == "Value (Lower P/S)":
        winner, reason = comparison['price_to_sales'].idxmin(), f"Lower P/S ratio of **{comparison['price_to_sales'].min():.2f}**"
    elif choice == "Profitability (Higher Margins)":
        winner, reason = comparison['profitMargins'].idxmax(), f"Higher profit margin of **{comparison['profitMargins'].max()*100:.1f}%**"
    else:
        winner, reason = comparison['Total Revenue'].idxmax(), f"Leading revenue of **${billions(comparison['Total Revenue'].max()):.1f}B**"

    # Subtle Interactive Result (No big green box)
    st.markdown(f"**Recommendation based on your criteria:** :blue[{winner}] ({reason})")
    
    st.divider()

    # 2. Final Research Conclusion (Compact & Informative)
    if st.button("🔍 Show Final Research Summary", use_container_width=True):
        st.markdown("### 💡 Research Conclusion: **Microsoft (MSFT)**")
        
        # Informative Grid
        col_logic, col_meta = st.columns([2, 1])
        
        with col_logic:
            st.markdown("**The Investment Hypothesis:**")
            st.write("MSFT offers a superior **price-versus-profit trade-off**. While GOOGL is larger in sheer scale, MSFT is currently 'cheaper' per dollar of sales and more efficient at retaining profit.")
            st.markdown("""
            - ✅ **Valuation:** Lower P/S multiple than GOOGL.
            - ✅ **Efficiency:** Higher net income margins.
            - ⚠️ **Scale:** Smaller total revenue footprint.
            """)

        with col_meta:
            st.markdown("**Data Context:**")
            st.caption("📅 **Period:** FY 2022–2025")
            st.caption("🔌 **Source:** Yahoo Finance API")
            st.caption("📊 **Focus:** P/S & Net Margin")
            st.warning("Not investment advice.", icon="⚠️")


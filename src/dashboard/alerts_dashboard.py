import sqlite3
import pandas as pd
import streamlit as st


def show_alerts():

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        project_name,
        priority,
        alert_message
    FROM alerts
    ORDER BY alert_id DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    # Rename columns
    df.columns = [
        "Project",
        "Priority",
        "Alert"
    ]

    # Shorten long project names
    df["Project"] = (
        df["Project"]
        .str.slice(0, 70) + "..."
    )

    # Shorten long alert messages
    df["Alert"] = (
        df["Alert"]
        .str.slice(0, 120) + "..."
    )

    st.subheader("🚨 Opportunity Alerts")

    high_count = len(
        df[df["Priority"] == "High Potential"]
    )

    st.info(
        f"🚨 Active Opportunity Alerts: {len(df)} | "
        f"High Potential: {high_count}"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
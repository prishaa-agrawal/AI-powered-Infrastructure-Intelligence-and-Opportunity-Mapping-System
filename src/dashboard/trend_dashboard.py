import sqlite3
import pandas as pd
import streamlit as st


def show_trend_intelligence():

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        project_type,
        project_count,
        avg_score,
        trend_level
    FROM trend_intelligence
    ORDER BY avg_score DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    df.columns = [
        "Sector",
        "Projects",
        "Avg Score",
        "Trend"
    ]

    st.subheader("📈 Trend Intelligence")

    hot_count = len(
        df[df["Trend"] == "Hot"]
    )

    growing_count = len(
        df[df["Trend"] == "Growing"]
    )

    st.info(
        f"📈 Sectors Tracked: {len(df)} | "
        f"Hot: {hot_count} | "
        f"Growing: {growing_count}"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
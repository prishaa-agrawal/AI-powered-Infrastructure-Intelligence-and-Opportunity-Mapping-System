import sqlite3
import pandas as pd
import streamlit as st


def show_agency_intelligence():

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        agency_name,
        project_count,
        avg_score,
        influence_level
    FROM agency_intelligence
    ORDER BY avg_score DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    df.columns = [
        "Agency",
        "Projects",
        "Avg Score",
        "Influence"
    ]

    # Show only Top 10 agencies
    df = df.head(10)

    st.subheader("🏛️ Agency Intelligence")

    high_count = len(
        df[df["Influence"] == "High"]
    )

    medium_count = len(
        df[df["Influence"] == "Medium"]
    )

    st.info(
        f"🏛️ Agencies Shown: {len(df)} | "
        f"High Influence: {high_count} | "
        f"Medium Influence: {medium_count}"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
import sqlite3
import pandas as pd
import streamlit as st


def show_opportunities():

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        project_name,
        agency,
        score,
        priority,
        reason
    FROM high_opportunities
    ORDER BY score DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    df["project_name"] = (
        df["project_name"]
        .str.slice(0, 80) + "..."
    )

    df.columns = [
        "Project",
        "Agency",
        "Score",
        "Priority",
        "Reason"
    ]

    st.subheader("🎯 Recommended Opportunities")
    st.dataframe(df, use_container_width=True)
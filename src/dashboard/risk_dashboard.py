import sqlite3
import pandas as pd
import streamlit as st


def show_risk_intelligence():

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        project_name,
        opportunity_score,
        risk_score,
        risk_level
    FROM risk_intelligence
    ORDER BY risk_score DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    df.columns = [
        "Project",
        "Opportunity Score",
        "Risk Score",
        "Risk Level"
    ]

    # Calculate counts from FULL dataset
    high_risk = len(
        df[df["Risk Level"] == "High"]
    )

    medium_risk = len(
        df[df["Risk Level"] == "Medium"]
    )

    low_risk = len(
        df[df["Risk Level"] == "Low"]
    )

    # Show only Top 10 in table
    df_display = df.head(10)

    st.subheader("⚠️ Risk Intelligence")

    st.info(
        f"⚠️ Total Projects: {len(df)} | "
        f"High Risk: {high_risk} | "
        f"Medium Risk: {medium_risk} | "
        f"Low Risk: {low_risk}"
    )

    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True
    )
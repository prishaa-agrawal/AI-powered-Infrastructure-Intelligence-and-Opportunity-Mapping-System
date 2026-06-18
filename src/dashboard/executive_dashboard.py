import sqlite3
import pandas as pd
import streamlit as st


def show_executive_intelligence():

    conn = sqlite3.connect("database/news.db")

    # Top Opportunity
    top_project = pd.read_sql_query("""
    SELECT
        project_name,
        opportunity_score
    FROM projects
    ORDER BY opportunity_score DESC
    LIMIT 1
    """, conn)

    # Top Agency
    top_agency = pd.read_sql_query("""
    SELECT
        agency_name,
        avg_score
    FROM agency_intelligence
    ORDER BY avg_score DESC
    LIMIT 1
    """, conn)

    # Top Trend
    top_trend = pd.read_sql_query("""
    SELECT
        project_type,
        avg_score
    FROM trend_intelligence
    ORDER BY avg_score DESC
    LIMIT 1
    """, conn)

    # Forecast Insight
    forecast = pd.read_sql_query("""
    SELECT
        total_projects
    FROM daily_metrics
    ORDER BY metric_id DESC
    LIMIT 1
    """, conn)

    # High Risk Projects
    risk_summary = pd.read_sql_query("""
    SELECT COUNT(*) as total
    FROM risk_intelligence
    WHERE risk_level = 'High'
    """, conn)

    conn.close()

    st.subheader("🧠 Executive Intelligence")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(
            f"🏆 Top Opportunity\n\n"
            f"{top_project.iloc[0]['project_name'][:50]}\n\n"
            f"Score: {top_project.iloc[0]['opportunity_score']}"
    
        )

    with col2:
        st.info(
            f"🏛️ Leading Agency\n\n"
            f"{top_agency.iloc[0]['agency_name']}\n\n"
            f"Avg Score: {round(top_agency.iloc[0]['avg_score'],1)}"
        )

    with col3:
        st.warning(
            f"📈 Strongest Sector\n\n"
            f"{top_trend.iloc[0]['project_type']}\n\n"
            f"Avg Score: {round(top_trend.iloc[0]['avg_score'],1)}"
        )

    st.metric(
        "🔮 Current Project Volume",
        int(forecast.iloc[0]["total_projects"])
    )

    st.metric(
        "⚠️ High Risk Projects",
        int(risk_summary.iloc[0]["total"])
    )

    st.markdown(f"""
    ### 📋 Executive Summary

    - **Leading Agency:** {top_agency.iloc[0]['agency_name']}
    - **Strongest Sector:** {top_trend.iloc[0]['project_type']}
    - **Current Opportunities:** {forecast.iloc[0]['total_projects']}
    - **High Risk Projects:** {risk_summary.iloc[0]['total']}

    **Recommendation:**

    Focus on high-scoring projects in the **{top_trend.iloc[0]['project_type']}** sector while monitoring identified high-risk opportunities.
    """)
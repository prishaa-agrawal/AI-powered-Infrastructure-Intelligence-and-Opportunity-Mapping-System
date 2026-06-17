import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


def show_historical_trends():

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        snapshot_date,
        total_projects,
        high_opportunities,
        avg_score,
        total_agencies
    FROM daily_metrics
    ORDER BY snapshot_date
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    st.subheader("📊 Historical Trends")

    if len(df) > 0:

        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Projects",
                int(df["total_projects"].iloc[-1])
            )

        with col2:
            st.metric(
                "High Opportunities",
                int(df["high_opportunities"].iloc[-1])
            )

        with col3:
            st.metric(
                "Avg Score",
                round(df["avg_score"].iloc[-1], 2)
            )

        with col4:
            st.metric(
                "Agencies",
                int(df["total_agencies"].iloc[-1])
            )

        # Projects Trend
        fig1 = px.line(
            df,
            x="snapshot_date",
            y="total_projects",
            title="Total Projects Over Time"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        # Opportunities Trend
        fig2 = px.line(
            df,
            x="snapshot_date",
            y="high_opportunities",
            title="High Opportunities Over Time"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # Average Score Trend
        fig3 = px.line(
            df,
            x="snapshot_date",
            y="avg_score",
            title="Average Opportunity Score Over Time"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
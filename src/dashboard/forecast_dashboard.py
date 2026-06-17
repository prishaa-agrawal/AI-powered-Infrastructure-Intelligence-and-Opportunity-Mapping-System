import sqlite3
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression


def show_forecast():

    conn = sqlite3.connect("database/news.db")

    df = pd.read_sql_query("""
    SELECT
        metric_id,
        total_projects
    FROM daily_metrics
    ORDER BY metric_id
    """, conn)

    conn.close()

    st.subheader("🔮 Opportunity Forecast")

    if len(df) < 2:

        st.warning(
            "Not enough historical data for forecasting."
        )

    else:

        X = df[["metric_id"]]
        y = df["total_projects"]

        model = LinearRegression()
        model.fit(X, y)

        next_day = pd.DataFrame(
            {
                "metric_id": [
                    df["metric_id"].max() + 1
                ]
            }
        )

        prediction = model.predict(next_day)[0]

        st.metric(
            "Forecasted Projects (Next Snapshot)",
            int(round(prediction))
        )
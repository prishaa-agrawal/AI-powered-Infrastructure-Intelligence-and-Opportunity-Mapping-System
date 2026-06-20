import streamlit as st
import pandas as pd


def show_agency_ranking(df):

    st.subheader("🏢 Agency Opportunity Ranking")

    agency_scores = (
        df.groupby("agency")["opportunity_score"]
        .mean()
        .reset_index()
        .sort_values(
            by="opportunity_score",
            ascending=False
        )
    )

    agency_scores["opportunity_score"] = (
        agency_scores["opportunity_score"]
        .round(1)
    )

    

    st.dataframe(
        agency_scores,
        use_container_width=True,
        hide_index=True
    )

    if not agency_scores.empty:

        top_agency = agency_scores.iloc[0]

        st.success(
            f"🏆 Top Performing Agency: "
            f"{top_agency['agency']} "
            f"({top_agency['opportunity_score']})"
        )
import streamlit as st


def show_portfolio_intelligence(df):

    st.subheader("💼 Opportunity Portfolio Intelligence")

    high = len(
        df[df["opportunity_score"] >= 70]
    )

    medium = len(
        df[
            (df["opportunity_score"] >= 40)
            &
            (df["opportunity_score"] < 70)
        ]
    )

    low = len(
        df[df["opportunity_score"] < 40]
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🟢 High Value Opportunities",
            high
        )

    with col2:
        st.metric(
            "🟠 Medium Value Opportunities",
            medium
        )

    with col3:
        st.metric(
            "🔴 Low Value Opportunities",
            low
        )

    st.markdown("---")

    st.subheader(
        "🎯 Top Recommended Opportunity Portfolio"
    )

    top_projects = (
        df.sort_values(
            by="opportunity_score",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_projects[
            [
                "project_name",
                "agency",
                "project_type",
                "opportunity_score"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("📊 Portfolio Health Score")

    portfolio_score = round(
        df["opportunity_score"].mean(),
        1
 )

    if portfolio_score >= 70:
        status = "Excellent"
    elif portfolio_score >= 50:
        status = "Good"
    else:
        status = "Needs Improvement"

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Portfolio Health Score",
            portfolio_score
    )

    with col2:
        st.metric(
            "Portfolio Status",
            status
        )

    st.markdown("---")

    st.subheader("🧠 AI Portfolio Recommendation")

    if portfolio_score >= 70:
        recommendation = (
            "The opportunity portfolio is strong. "
            "Focus on accelerating stakeholder engagement "
            "and project acquisition activities."
        )

    elif portfolio_score >= 50:
        recommendation = (
            "The portfolio is stable but contains several "
            "medium-value opportunities that require deeper analysis."
        )

    else:
        recommendation = (
            "The portfolio is heavily weighted toward low-value "
            "opportunities. Focus on sourcing higher-value projects "
            "and improving opportunity quality."
        )

    st.info(recommendation)
    st.markdown("---")

    st.subheader("📈 Sector Allocation Analysis")

    sector_counts = (
        df["project_type"]
        .value_counts()
        .reset_index()
    )

    sector_counts.columns = [
        "Sector",
        "Projects"
    ]

    st.dataframe(
        sector_counts,
        use_container_width=True,
        hide_index=True
    )
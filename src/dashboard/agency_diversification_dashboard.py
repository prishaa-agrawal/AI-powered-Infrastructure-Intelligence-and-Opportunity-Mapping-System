import streamlit as st


def show_agency_diversification(df):

    st.subheader("🏢 Agency Diversification Analysis")

    agency_counts = (
        df["agency"]
        .value_counts()
        .reset_index()
    )

    agency_counts.columns = [
        "Agency",
        "Projects"
    ]

    st.dataframe(
        agency_counts,
        use_container_width=True,
        hide_index=True
    )

    total_agencies = (
        df["agency"]
        .replace("", None)
        .dropna()
        .nunique()
    )

    st.metric(
        "Unique Agencies",
        total_agencies
    )

    if total_agencies >= 15:
        st.success(
            "Well-diversified agency portfolio."
        )

    elif total_agencies >= 8:
        st.warning(
            "Moderately diversified agency portfolio."
        )

    else:
        st.error(
            "High dependency on a small number of agencies."
        )
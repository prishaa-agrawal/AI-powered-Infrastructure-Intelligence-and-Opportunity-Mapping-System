import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from reports.generate_report import generate_pdf

st.set_page_config(
    page_title="Infrastructure Intelligence Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏗️ AI-Powered Infrastructure Intelligence & Opportunity Mapping System")

conn = sqlite3.connect("database/news.db")

query = """
SELECT
    project_name,
    project_type,
    budget,
    location,
    agency,
    opportunity_score
FROM projects
"""

df = pd.read_sql_query(query, conn)

conn.close()

df["project_name"] = (
    df["project_name"]
    .str.split(" - ")
    .str[0]
)

df["opportunity_score"] = (
    df["opportunity_score"]
    .fillna(0)
    .astype(int)
)

df["rank"] = df["opportunity_score"].apply(
    lambda x: "🟢 High"
    if x >= 70
    else "🟠 Medium"
    if x >= 40
    else "🔴 Low"
)

st.sidebar.title("Filters")

project_types = ["All"] + sorted(
    df["project_type"].dropna().unique().tolist()
)

selected_type = st.sidebar.selectbox(
    "Project Type",
    project_types
)

agencies = ["All"] + sorted(
    df["agency"].dropna().unique().tolist()
)

selected_agency = st.sidebar.selectbox(
    "Agency",
    agencies
)

search_project = st.sidebar.text_input(
    "Search Project"
)

filtered_df = df.copy()

if selected_type != "All":
    filtered_df = filtered_df[
        filtered_df["project_type"] == selected_type
    ]

if selected_agency != "All":
    filtered_df = filtered_df[
        filtered_df["agency"] == selected_agency
    ]

if search_project:
    filtered_df = filtered_df[
        filtered_df["project_name"]
        .str.contains(
            search_project,
            case=False,
            na=False
        )
    ]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Projects",
        len(df)
    )

with col2:
    st.metric(
        "High Opportunity",
        len(df[df["opportunity_score"] >= 70])
    )

with col3:
    st.metric(
        "Agencies",
        df["agency"].replace("", pd.NA).dropna().nunique()
    )

with col4:
    st.metric(
        "Avg Score",
        round(df["opportunity_score"].mean(), 1)
    )

st.download_button(
    label="⬇ Download Project Data",
    data=df.to_csv(index=False),
    file_name="projects.csv",
    mime="text/csv"
)

st.subheader("🏆 Top Opportunity Projects")

top5 = df.sort_values(
    by="opportunity_score",
    ascending=False
).head(5)

card_cols = st.columns(5)

for col, (_, row) in zip(card_cols, top5.iterrows()):

    with col:
        st.markdown(
            f"""
            ### ⭐ {int(row['opportunity_score'])}

            **{row['project_name'][:50]}**

            🏢 {row['agency']}
            """
        )

st.subheader("📌 Opportunity Categories")

rank_counts = df["rank"].value_counts()

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        f"High: {rank_counts.get('🟢 High', 0)}"
    )

with c2:
    st.warning(
        f"Medium: {rank_counts.get('🟠 Medium', 0)}"
    )

with c3:
    st.error(
        f"Low: {rank_counts.get('🔴 Low', 0)}"
    )

st.subheader("📝 Executive Summary")

if st.button("Generate Executive Summary"):

    top_agency = (
        df["agency"]
        .replace("", pd.NA)
        .dropna()
        .value_counts()
        .idxmax()
    )

    top_project = (
        df.sort_values(
            "opportunity_score",
            ascending=False
        )
        .iloc[0]
    )

    common_type = (
        df["project_type"]
        .value_counts()
        .idxmax()
    )

    summary = f"""
    ## Infrastructure Intelligence Report

    A total of **{len(df)}** infrastructure projects were analyzed across multiple sectors including railways, transportation, and public infrastructure.

    **{top_agency}** emerged as the most active agency in the current dataset.

    The most common project category is **{common_type}**.

    ## Highest-Ranked Opportunity

    **{top_project['project_name']}**

    **Agency:** {top_project['agency']}

    **Opportunity Score:** {top_project['opportunity_score']}

    ## Key Observation

    Transportation and large-scale infrastructure projects continue to dominate the current project pipeline, with public sector agencies contributing the majority of high-opportunity initiatives.
    """

    st.markdown(summary)

KNOWN_AGENCIES = [
    "Indian Railways",
    "ADB",
    "World Bank",
    "L&T",
    "Larsen & Toubro",
    "RailTel",
    "Google",
    "Uber",
    "NHIDCL",
    "MMRDA",
    "NLC India"
]

st.subheader("📄 PDF Report")

if st.button("Generate PDF Report"):

    generate_pdf()

    with open(
        "src/reports/infrastructure_report.pdf",
        "rb"
    ) as file:

        st.download_button(
            label="⬇ Download Report",
            data=file,
            file_name="infrastructure_report.pdf",
            mime="application/pdf"
        )

st.subheader("🏢 Agency Influence Map")

agency_df = df.copy()

agency_df["agency"] = (
    agency_df["agency"]
    .fillna("")
    .str.strip()
)

agency_df = agency_df[
    agency_df["agency"].isin(KNOWN_AGENCIES)
]

agency_counts = (
    agency_df["agency"]
    .value_counts()
    .reset_index()
)

agency_counts.columns = [
    "agency",
    "projects"
]
fig_agency = px.bar(
    agency_counts,
    x="projects",
    y="agency",
    orientation="h",
    color="projects",
    template="plotly_dark",
    title="Top Infrastructure Agencies by Project Count",
    color_continuous_scale="viridis"
)

fig_agency.update_layout(
    xaxis_title="Number of Projects",
    yaxis_title="Agency",
    height=300,
    coloraxis_showscale=False
)


st.plotly_chart(
    fig_agency,
    use_container_width=True
)

# ==========================================
# PROJECT SEARCH & RECOMMENDATION ENGINE
# ==========================================

st.subheader("🔍 Project Search & Recommendation Engine")

search_query = st.text_input(
    "Enter Keyword (e.g. Railway, Infrastructure, Metro)"
)

if search_query:

    recommendations = df[
        (
            df["project_name"]
            .str.contains(
                search_query,
                case=False,
                na=False
            )
        )
        |
        (
            df["project_type"]
            .str.contains(
                search_query,
                case=False,
                na=False
            )
        )
        |
        (
            df["agency"]
            .str.contains(
                search_query,
                case=False,
                na=False
            )
        )
    ]

    recommendations = recommendations.sort_values(
        by="opportunity_score",
        ascending=False
    )

    if len(recommendations) > 0:

        st.success(
            f"Found {len(recommendations)} matching projects"
        )

        st.subheader(
            "🎯 Top Recommended Opportunities"
        )

        top_recommendations = (
            recommendations.head(5)
        )
        st.dataframe(
         top_recommendations[
            [
                 "project_name",
                 "agency",
                "project_type",
                "opportunity_score",
                 "rank"
             ]
        ],
        use_container_width=True,
        hide_index=True
          )

        st.subheader(
            "📋 All Matching Projects"
        )

        st.dataframe(
            recommendations[
                [
                    "project_name",
                    "agency",
                    "project_type",
                    "opportunity_score",
                    "rank"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "No matching projects found."
        )

# ==========================================
# LOCATION ANALYTICS
# ==========================================

st.subheader("📍 Location Analytics")

location_df = df.copy()

location_df["location"] = (
    location_df["location"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)

location_counts = (
    location_df["location"]
    .value_counts()
    .head(10)
    .reset_index()
)

location_counts.columns = [
    "location",
    "projects"
]

fig_location = px.bar(
    location_counts,
    x="projects",
    y="location",
    orientation="h",
    color="projects",
    template="plotly_dark",
    title="Top Infrastructure Opportunity Locations",
    color_continuous_scale="viridis"
)

fig_location.update_layout(
    xaxis_title="Number of Projects",
    yaxis_title="Location",
    coloraxis_showscale=False,
    height=450
)

st.plotly_chart(
    fig_location,
    use_container_width=True
)

# ==========================================
# LOCATION INSIGHTS
# ==========================================

top_location = (
    location_df["location"]
    .value_counts()
    .idxmax()
)

total_locations = (
    location_df["location"]
    .nunique()
)

col1, col2 = st.columns(2)

with col1:
    st.info(
        f"📍 Most Active Location: {top_location}"
    )

with col2:
    st.info(
        f"🌍 Unique Locations: {total_locations}"
    )

st.dataframe(
    location_counts,
    use_container_width=True,
    hide_index=True
)
st.subheader("📋 Infrastructure Projects")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.subheader("📊 Project Type Distribution")

project_counts = (
    df["project_type"]
    .value_counts()
    .reset_index()
)

project_counts.columns = [
    "project_type",
    "count"
]

fig_bar = px.bar(
    project_counts,
    x="count",
    y="project_type",
    orientation="h",
    color="count",
    template="plotly_dark",
    title="Project Type Distribution"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

st.subheader("📈 Opportunity Score Distribution")

fig_hist = px.histogram(
    df,
    x="opportunity_score",
    color="rank",
    nbins=10,
    template="plotly_dark",
    title="Opportunity Score Distribution",
    color_discrete_map={
        "🟢 High": "#2ecc71",
        "🟠 Medium": "#f39c12",
        "🔴 Low": "#e74c3c"
    }
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

st.subheader("🔍 Project Details")

for _, row in filtered_df.head(20).iterrows():

    with st.expander(row["project_name"]):

        st.write("**Agency:**", row["agency"])
        st.write("**Project Type:**", row["project_type"])
        st.write("**Budget:**", row["budget"])
        st.write("**Location:**", row["location"])
        st.write("**Opportunity Score:**", row["opportunity_score"])
        st.write("**Rank:**", row["rank"])

st.divider()

st.caption(
    "AI-Powered Infrastructure Intelligence & Opportunity Mapping System"
)
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Infrastructure Intelligence Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏗️ AI-Powered Infrastructure Intelligence System")

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

st.sidebar.header("Filters")

project_types = ["All"] + sorted(
    list(df["project_type"].dropna().unique())
)

selected_type = st.sidebar.selectbox(
    "Project Type",
    project_types
)

agencies = ["All"] + sorted(
    list(df["agency"].dropna().unique())
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
        .str.contains(search_project, case=False, na=False)
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
        df["agency"].nunique()
    )

with col4:
    st.metric(
        "Average Score",
        round(df["opportunity_score"].mean(), 1)
    )

st.download_button(
    label="⬇ Download Project Data",
    data=df.to_csv(index=False),
    file_name="projects.csv",
    mime="text/csv"
)

st.subheader("🏆 Top 5 Opportunity Projects")

top5 = df.sort_values(
    by="opportunity_score",
    ascending=False
).head(5)

for _, row in top5.iterrows():

    st.info(
        f"""
        Project: {row['project_name']}

        Opportunity Score: {row['opportunity_score']}

        Agency: {row['agency']}
        """
    )

st.subheader("📋 Infrastructure Projects")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.subheader("📊 Project Type Distribution")

fig_pie = px.pie(
    df,
    names="project_type",
    title="Project Type Distribution"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

st.subheader("📈 Opportunity Score Distribution")

fig_hist = px.histogram(
    df,
    x="opportunity_score",
    nbins=10,
    title="Opportunity Score Distribution"
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

st.subheader("🔍 Project Details")

for _, row in filtered_df.head(20).iterrows():

    with st.expander(row["project_name"]):

        st.write(f"**Agency:** {row['agency']}")
        st.write(f"**Project Type:** {row['project_type']}")
        st.write(f"**Budget:** {row['budget']}")
        st.write(f"**Location:** {row['location']}")
        st.write(f"**Opportunity Score:** {row['opportunity_score']}")

st.success("Dashboard Loaded Successfully!")
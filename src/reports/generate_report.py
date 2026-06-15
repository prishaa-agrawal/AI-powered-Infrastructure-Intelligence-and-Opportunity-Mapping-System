from fpdf import FPDF
from datetime import datetime
import sqlite3
import pandas as pd


def clean_text(text):

    text = str(text)

    replacements = {
        "₹": "Rs.",
        "€": "EUR ",
        "$": "USD ",
        "£": "GBP ",
        "–": "-",
        "—": "-",
        "‘": "'",
        "’": "'"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.encode(
        "ascii",
        errors="ignore"
    ).decode()


def generate_pdf():
    

    conn = sqlite3.connect("database/news.db")

    query = """
    SELECT
        project_name,
        agency,
        project_type,
        opportunity_score
    FROM projects
    """

    df = pd.read_sql_query(query, conn)

    conn.close()
    if df.empty:
     print("No project data available.")
     return

    df["agency"] = df["agency"].fillna("Unknown")
    df["project_type"] = df["project_type"].fillna("Unknown")
    df["opportunity_score"] = (
        df["opportunity_score"]
        .fillna(0)
        .astype(int)
    )

    agency_counts_all = (
        df["agency"]
        .replace("", pd.NA)
        .dropna()
        .value_counts()
    )

    top_agency = (
        agency_counts_all.idxmax()
        if not agency_counts_all.empty
        else "Unknown"
    )

    common_type = (
        df["project_type"]
        .value_counts()
        .idxmax()
    )

    high_projects = len(
        df[df["opportunity_score"] >= 70]
    )

    medium_projects = len(
        df[
            (df["opportunity_score"] >= 40)
            &
            (df["opportunity_score"] < 70)
        ]
    )

    low_projects = len(
        df[df["opportunity_score"] < 40]
    )

    avg_score = round(
        df["opportunity_score"].mean(),
        1
    )

    top_projects = (
        df.sort_values(
            by="opportunity_score",
            ascending=False
        )
        .head(10)
    )

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

    agency_df = df[
        df["agency"].isin(KNOWN_AGENCIES)
    ]

    agency_counts = (
        agency_df["agency"]
        .value_counts()
        .head(5)
    )

    pdf = FPDF()

    pdf.add_page()

    # Title

    pdf.set_font(
        "Helvetica",
        "B",
        16
    )

    pdf.cell(
        0,
        10,
        "Infrastructure Intelligence Report",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font(
        "Helvetica",
        "",
        11
    )

    pdf.cell(
        0,
        8,
        f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(4)

    # Executive Summary

    pdf.set_font(
        "Helvetica",
        "B",
        14
    )

    pdf.cell(
        0,
        10,
        "Executive Summary",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font(
        "Helvetica",
        "",
        12
    )

    summary = f"""
Total Projects Analyzed: {len(df)}

High Opportunity Projects: {high_projects}
Medium Opportunity Projects: {medium_projects}
Low Opportunity Projects: {low_projects}

Average Opportunity Score: {avg_score}

Most Active Agency: {clean_text(top_agency)}

Most Common Project Type: {clean_text(common_type)}

Key Insight:
Transportation and public infrastructure projects continue to dominate the opportunity landscape, with Indian Railways leading project activity.
"""

    pdf.multi_cell(
        0,
        7,
        clean_text(summary)
    )

    pdf.ln(3)

    # Top Projects

    pdf.set_font(
        "Helvetica",
        "B",
        18
    )

    pdf.cell(
        0,
        10,
        "Top 10 Opportunity Projects",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font(
        "Helvetica",
        "",
        10
    )

    for i, (_, row) in enumerate(
        top_projects.iterrows(),
        start=1
    ):

        project_name = clean_text(
            row["project_name"]
        )

        if len(project_name) > 100:
            project_name = (
                project_name[:100] + "..."
            )

        agency = clean_text(
            row["agency"]
        )

        project_type = clean_text(
            row["project_type"]
        )

        pdf.multi_cell(
            0,
            5,
            f"{i}. {project_name}\n"
            f"Agency: {agency}\n"
            f"Type: {project_type}\n"
            f"Score: {row['opportunity_score']}"
        )

        pdf.ln(1)

    # Agency Analysis

    pdf.ln(4)

    pdf.set_font(
        "Helvetica",
        "B",
        14
    )

    pdf.cell(
        0,
        10,
        "Agency Influence Analysis",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font(
        "Helvetica",
        "",
        11
    )

    for agency, count in agency_counts.items():

        pdf.cell(
            0,
            7,
            f"{agency}: {count} projects",
            new_x="LMARGIN",
            new_y="NEXT"
        )

    # Footer

    pdf.ln(5)

    pdf.set_font(
        "Helvetica",
        "I",
        9
    )

    pdf.multi_cell(
        0,
        6,
        "Generated by AI-Powered Infrastructure Intelligence & Opportunity Mapping System"
    )

    output_file = (
        "src/reports/infrastructure_report.pdf"
    )

    pdf.output(output_file)

    print("\nPDF Report Generated Successfully!")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    generate_pdf()
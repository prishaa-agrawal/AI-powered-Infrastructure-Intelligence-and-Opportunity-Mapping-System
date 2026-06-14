# AI-Powered Infrastructure Intelligence & Opportunity Mapping System

## Project Overview

The AI-Powered Infrastructure Intelligence & Opportunity Mapping System is designed to automatically collect, analyze, and visualize infrastructure project opportunities from news sources.

The system uses Natural Language Processing (NLP) techniques to extract project details such as project name, agency, location, project type, and budget. It then calculates an opportunity score and presents insights through an interactive dashboard.

---

## Problem Statement

Infrastructure project information is scattered across multiple news sources and government announcements, making it difficult for consulting firms, contractors, and business development teams to identify potential opportunities.

This system automates project discovery and opportunity analysis.

---

## Key Features

- Automated Infrastructure News Collection
- Project Information Extraction
- Agency Identification
- Project Type Classification
- Opportunity Scoring Engine
- Opportunity Recommendation Engine
- Location Analytics
- Sector Opportunity Analysis
- PDF Report Generation
- Interactive Streamlit Dashboard

---

## Technology Stack

### Programming Language
- Python

### Database
- SQLite

### Libraries
- Pandas
- Streamlit
- Plotly
- BeautifulSoup
- Newspaper3k
- ReportLab

### NLP Techniques
- Keyword Extraction
- Entity Recognition
- Rule-Based Classification

---

## System Architecture

News Sources
↓
News Collection
↓
Project Extraction
↓
Agency Extraction
↓
Project Type Classification
↓
Opportunity Scoring
↓
SQLite Database
↓
Streamlit Dashboard
↓
PDF Report Generation

---

## Dashboard Modules

### Executive Dashboard
Displays:
- Total Projects
- High Opportunity Projects
- Agencies
- Average Opportunity Score

### Opportunity Recommendation Engine
Allows users to search projects using keywords and view recommended opportunities.

### Agency Influence Map
Visualizes agencies with the highest project activity.

### Location Analytics
Shows project distribution across different locations.

### Sector Opportunity Analysis
Compares average opportunity scores across project sectors.

### Detailed Project Explorer
Provides expandable project-level information.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run src/dashboard/app.py
```

---

## Project Structure

```text
project/
│
├── database/
│   └── news.db
│
├── src/
│   ├── dashboard/
│   │   └── app.py
│   │
│   ├── reports/
│   │   ├── generate_report.py
│   │   └── infrastructure_report.pdf
│   │
│   ├── extraction/
│   │   ├── agency_extractor.py
│   │   ├── project_type_extractor.py
│   │   └── opportunity_score.py
│
├── README.md
└── requirements.txt
```

---

## Testing Summary

| Module | Status |
|----------|----------|
| Dashboard Loading | Passed |
| Project Search | Passed |
| Opportunity Scoring | Passed |
| PDF Generation | Passed |
| Location Analytics | Passed |
| Sector Analysis | Passed |

---

## Results

- Successfully analyzed 100+ infrastructure projects.
- Generated automated opportunity scores.
- Identified high-value infrastructure opportunities.
- Produced executive reports and visual analytics.

---

## Future Enhancements

- GIS Map Integration
- Real-Time News Monitoring
- Machine Learning-Based Opportunity Prediction
- Tender Data Integration
- Automated Email Alerts
- Advanced Semantic Search

---

## Author

Prisha Agrawal

AI-Powered Infrastructure Intelligence & Opportunity Mapping System
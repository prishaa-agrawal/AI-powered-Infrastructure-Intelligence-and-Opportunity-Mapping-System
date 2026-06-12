import sqlite3
import networkx as nx
from pyvis.network import Network

conn = sqlite3.connect("database/news.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    project_name,
    agency,
    location,
    project_type
FROM projects
""")

projects = cursor.fetchall()

conn.close()

G = nx.Graph()

for project_name, agency, location, project_type in projects:

    project_name = str(project_name).strip()

    G.add_node(
        project_name,
        label=project_name,
        color="#3498db",
        size=20
    )

    if agency and agency.strip():

        agency = agency.strip()

        G.add_node(
            agency,
            label=agency,
            color="#e74c3c",
            size=15
        )

        G.add_edge(
            project_name,
            agency
        )

    if location and location.strip():

        location = location.strip()

        G.add_node(
            location,
            label=location,
            color="#2ecc71",
            size=15
        )

        G.add_edge(
            project_name,
            location
        )

    if project_type and project_type.strip():

        project_type = project_type.strip()

        G.add_node(
            project_type,
            label=project_type,
            color="#f39c12",
            size=15
        )

        G.add_edge(
            project_name,
            project_type
        )

net = Network(
    height="900px",
    width="100%",
    bgcolor="#111111",
    font_color="white"
)

net.from_nx(G)

net.barnes_hut()

net.write_html(
    "knowledge_graph.html",
    open_browser=True
)

print("Knowledge Graph Created Successfully!")
print("Open knowledge_graph.html in your browser.")
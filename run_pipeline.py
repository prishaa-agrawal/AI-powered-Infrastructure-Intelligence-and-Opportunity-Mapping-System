import os
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline Started")

print("=" * 50)
print("INFRASTRUCTURE INTELLIGENCE PIPELINE")
print("=" * 50)

print("\n[1/4] Collecting news...")
result = os.system("python src/scraper/store_news.py")

if result != 0:
    logging.error("News collection failed")
    print("Pipeline failed at news collection.")
    exit()

print("\n[2/4] Extracting projects...")
result = os.system("python src/nlp/store_extracted_projects.py")

if result != 0:
    logging.error("Project extraction failed")
    print("Pipeline failed at project extraction.")
    exit()

print("\n[3/4] Calculating scores...")
result = os.system("python src/scoring/score_projects.py")

if result != 0:
    logging.error("Score calculation failed")
    print("Pipeline failed at score calculation.")
    exit()

print("\n[4/4] Generating report...")
result = os.system("python src/reports/generate_report.py")

if result != 0:
    logging.error("Report generation failed")
    print("Pipeline failed at report generation.")
    exit()

print("\nPipeline completed successfully!")

logging.info("Pipeline Completed Successfully")
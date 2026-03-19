import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine

password = quote_plus("YOUR_PASSWORD")

engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost:3306/wi_data_center_conflict_db"
)

queries = {
    "company_report_counts": """
        SELECT company_name, COUNT(*) AS total_reports
        FROM reports
        GROUP BY company_name
        ORDER BY total_reports DESC
    """,
    "project_stage_summary": """
        SELECT project_stage, COUNT(*) AS total_reports
        FROM reports
        GROUP BY project_stage
        ORDER BY total_reports DESC
    """,
    "primary_conflict_frames": """
        SELECT primary_conflict_frame, COUNT(*) AS total_reports
        FROM reports
        GROUP BY primary_conflict_frame
        ORDER BY total_reports DESC
    """
}

for name, query in queries.items():
    df = pd.read_sql(query, engine)
    print(f"\n{name}")
    print(df.head(10))
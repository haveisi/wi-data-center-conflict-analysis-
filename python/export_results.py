import os
import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine

password = quote_plus("YOUR_PASSWORD")

engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost:3306/wi_data_center_conflict_db"
)

output_dir = r"C:\Users\hveis\OneDrive - UWSP\2026\MySql\outputs"
os.makedirs(output_dir, exist_ok=True)

exports = {
    "company_report_counts.csv": """
        SELECT company_name, COUNT(*) AS total_reports
        FROM reports
        GROUP BY company_name
        ORDER BY total_reports DESC
    """,
    "project_stage_summary.csv": """
        SELECT project_stage, COUNT(*) AS total_reports
        FROM reports
        GROUP BY project_stage
        ORDER BY total_reports DESC
    """,
    "primary_conflict_frames.csv": """
        SELECT primary_conflict_frame, COUNT(*) AS total_reports
        FROM reports
        GROUP BY primary_conflict_frame
        ORDER BY total_reports DESC
    """
}

for filename, query in exports.items():
    df = pd.read_sql(query, engine)
    save_path = os.path.join(output_dir, filename)
    df.to_csv(save_path, index=False)
    print(f"Saved: {save_path}")
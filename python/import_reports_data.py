import os
import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

file_path = r"C:\Users\hveis\OneDrive - UWSP\2026\MySql\coded_cases_clean.csv"

print("File exists:", os.path.exists(file_path))

df = pd.read_csv(file_path, encoding="utf-8-sig", low_memory=False)

df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace("\ufeff", "", regex=False)

df = df.rename(columns={
    "ID": "report_id",
    "date": "publication_date",
    "company": "company_name",
    "primary": "primary_conflict_frame",
    "secondary": "secondary_conflict_frame",
    "governance": "governance_issue",
    "transparency": "transparency_issue",
    "land_use": "land_use_issue",
    "evidence": "evidence_type"
})

password = quote_plus("YOUR_PASSWORD")

engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost:3306/wi_data_center_conflict_db"
)

with engine.connect() as conn:
    print("Connected to MySQL successfully")
    print(conn.execute(text("SELECT DATABASE();")).fetchone())

df.to_sql(name="reports", con=engine, if_exists="append", index=False)

print("Import complete.")
print(f"Rows imported: {len(df)}")
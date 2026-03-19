CREATE DATABASE IF NOT EXISTS wi_data_center_conflict_db;
SHOW DATABASES;

USE wi_data_center_conflict_db;
SELECT DATABASE();

CREATE TABLE reports (
    report_id INT,
    title TEXT,
    publication_date DATE,
    outlet VARCHAR(200),
    location VARCHAR(200),
    company_name VARCHAR(200),
    article_type VARCHAR(100),
    project_stage VARCHAR(100),
    primary_conflict_frame VARCHAR(150),
    secondary_conflict_frame VARCHAR(150),
    actors_present TEXT,
    actors_quoted TEXT,
    benefits_emphasized TEXT,
    risks_emphasized TEXT,
    governance_issue INT,
    transparency_issue INT,
    energy_issue INT,
    water_issue INT,
    land_use_issue INT,
    tone VARCHAR(50),
    evidence_type VARCHAR(100),
    notable_quote TEXT,
    memo TEXT,
    source_file VARCHAR(255)
);

SHOW TABLES;
DESCRIBE reports;

USE wi_data_center_conflict_db;

SELECT COUNT(*) AS total_reports FROM reports;
SELECT * FROM reports LIMIT 5;
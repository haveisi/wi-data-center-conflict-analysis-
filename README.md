# WI-data-center-conflict-analysis-
SQL + Python analysis of community conflicts around data center development in Wisconsin, focusing on energy, water, governance, and policy dynamics.
Here is a more **professional, polished, and portfolio-ready version** of your project description:

Data Center Conflict Analysis — Wisconsin
Overview
This project examines community responses and policy conflicts associated with data center development in Wisconsin using a combination of SQL and Python-based data analysis. The study systematically analyzes media coverage to identify key patterns in infrastructure-related conflict, with particular attention to environmental, governance, and socio-economic dimensions.

........................................................................................................................................................................................................................

The analysis focuses on:
1. Energy demand and infrastructure capacity
2. Water use and environmental impacts
3. Governance, regulation, and transparency
4. Project development stages
5. Media framing and tone
   
........................................................................................................................................................................................................................

Tools and Technologies
1. MySQL — database design, management, and analytical queries
2. Python (pandas, SQLAlchemy)** — data processing and integration
3. Excel / CSV — data outputs and intermediate analysis
4. GitHub— version control and project documentation
........................................................................................................................................................................................................................

Dataset
The dataset consists of 64 coded media reports related to data center development. Sources include:
1. Regional and national media outlets
2. Policy and regulatory reports
3. Investigative journalism
4. Each report is coded for conflict themes, actors, project stages, and media tone.
   
........................................................................................................................................................................................................................

Research Questions
This analysis addresses the following key questions:
1. Which companies are most frequently associated with conflict?
2. At which stages of project development do conflicts emerge?
3. What are the dominant conflict themes across cases?
4. How does media tone vary across different types of conflicts?
   
........................................................................................................................................................................................................................

Key Findings
1. Conflicts are most concentrated during "early project stages", particularly policy debates and planning processes.
2. Energy demand and water use** are the most prominent sources of concern.
3. Microsoftis the most frequently referenced company in conflict-related reporting.
4. Media coverage is predominantly **mixed and conflict-oriented**, reflecting ongoing policy debates rather than uniformly negative narratives.
........................................................................................................................................................................................................................

Example Queries
1. Company–Stage–Conflict Matrix
```sql
SELECT 
    company_name,
    project_stage,
    primary_conflict_frame,
    COUNT(*) AS reports
FROM reports
GROUP BY company_name, project_stage, primary_conflict_frame;

............................................................................................

2. Company × Stage × Conflict × Tone

SELECT 
    company_name,
    project_stage,
    primary_conflict_frame,
    tone,
    COUNT(*) AS reports,
    
    SUM(water_issue) AS water_mentions,
    SUM(energy_issue) AS energy_mentions,
    SUM(governance_issue) AS governance_mentions

FROM reports

GROUP BY 
    company_name,
    project_stage,
    primary_conflict_frame,
    tone

ORDER BY reports DESC;

.........................................................................................................................................................................................................................

Outputs
The project generates structured outputs to support analysis and visualization, including:
1. Company frequency tables
2. Conflict theme distributions
3. Project stage analysis
4. Media tone summaries

........................................................................................................................................................................................................................

Future Work
Planned extensions of this project include:
1. GIS-based mapping of conflict hotspots
2. Network analysis of actors and conflict themes
3. Integration with ESG frameworks for risk assessment and policy evaluation


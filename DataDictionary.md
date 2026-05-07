Vulnerability Data (NVD)

ID  
A unique identifier assigned to each vulnerability (e.g., CVE‑2021‑34527). Used to identify and deduplicate vulnerability records.

PubDate  
The date the vulnerability was first published in the National Vulnerability Database. Used to extract the year for aggregation.

ModDate 
The date the vulnerability entry was last updated by NVD. Ensures the most recent version of each CVE is used.

Status  
Indicates whether the CVE is analyzed, modified, rejected, or still under review. Used to filter out rejected or incomplete entries.

Severity  
The harmonized severity label for each vulnerability. Values include Low, Medium, High, and Critical. Derived by checking CVSS v3.1 first, then v3.0, then v2 if needed.

Combined R&D Tables

Fiscal year  
The fiscal year for which R&D expenditures were reported. Used to align with CVE data by converting to a standard year variable.

All R&D expenditures  
Total research and development spending across all Federally Funded Research and Development Centers (FFRDCs) for the given fiscal year.

Federal government  
Portion of total R&D expenditures funded directly by the U.S. federal government.

State and local government  
Portion of R&D expenditures funded by state and local government entities.

Business  
Portion of R&D expenditures funded by private‑sector businesses.

Nonprofit organizations  
Portion of R&D expenditures funded by nonprofit institutions.

All other sourcesa  
R&D expenditures funded by sources not included in the above categories (e.g., foreign entities, miscellaneous funding). The “a” indicates a footnote in the original NSF table.

Year  
A standardized year variable used for merging with NVD data. Derived from “Fiscal year.” The year 2001 was removed to match the NVD range (2002–2024).

Total All R&D Expenditures  
Total R&D expenditures across all research types (basic, applied, and experimental development). Used as a primary independent variable in analysis.

Total Basic Research Amount  
Dollar amount spent on basic research activities.

Total Basic Research Percent  
Percentage of total R&D expenditures allocated to basic research.

Total Applied Research Amount  
Dollar amount spent on applied research activities. Used as a secondary independent variable.

Total Applied Research Percent  
Percentage of total R&D expenditures allocated to applied research.

Total Experimental Development Amount  
Dollar amount spent on experimental development activities. Used as a secondary independent variable.

Total Experimental Development Percent  
Percentage of total R&D expenditures allocated to experimental development.

Federally Financed R&D Expenditures  
Total R&D expenditures funded specifically by the federal government.

Federally Financed Basic Research Amount  
Dollar amount of federally funded basic research.

Federally Financed Basic Research Percent  
Percentage of federally funded R&D allocated to basic research.

Federally Financed Applied Research Amount  
Dollar amount of federally funded applied research.

Federally Financed Applied Research Percent  
Percentage of federally funded R&D allocated to applied research.

Federally Financed Experimental Development Amount  
Dollar amount of federally funded experimental development.

Federally Financed Experimental Development Percent  
Percentage of federally funded R&D allocated to experimental development.

CVE Count  
The number of vulnerabilities (from NVD) for the corresponding year. In your merged dataset, this typically refers to the count of Critical CVEs or the total CVE count depending on the specific analysis.

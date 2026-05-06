rule analysis.py:
    input:
        "none_combined.csv",
        "low_combined.csv",
        "medium_combined.csv",
        "high_combined.csv",
        "critical_combined.csv"
    output:
        "none_model_summary.txt",
        "low_model_summary.txt",
        "medium_model_summary.txt",
        "high_model_summary.txt",
        "critical_model_summary.txt",
        "analysis_results.png"
    shell:
        "python analysis.py"

rule combined_data.py:
    input:
        "CVE_data.csv",
        "rd_parsed_001.csv",
        "rd_parsed_002.csv"
    output:
        "none_combined.csv",
        "low_combined.csv",
        "medium_combined.csv",
        "high_combined.csv",
        "critical_combined.csv"
    shell:
        "python combined_data.py"

rule fetch_tables:
    output:
        "tab001.xlsx",
        "tab002.xlsx"
    shell:
        "python fetch_data_rd.py"


rule fetch_data:
    output:
        "nvdcve-2.0-2002.json.zip",
        "nvdcve-2.0-2003.json.zip",
        "nvdcve-2.0-2004.json.zip",
        "nvdcve-2.0-2005.json.zip",
        "nvdcve-2.0-2006.json.zip",
        "nvdcve-2.0-2007.json.zip",
        "nvdcve-2.0-2008.json.zip",
        "nvdcve-2.0-2009.json.zip",
        "nvdcve-2.0-2010.json.zip",
        "nvdcve-2.0-2011.json.zip",
        "nvdcve-2.0-2012.json.zip",
        "nvdcve-2.0-2013.json.zip",
        "nvdcve-2.0-2014.json.zip",
        "nvdcve-2.0-2015.json.zip",
        "nvdcve-2.0-2016.json.zip",
        "nvdcve-2.0-2017.json.zip",
        "nvdcve-2.0-2018.json.zip",
        "nvdcve-2.0-2019.json.zip",
        "nvdcve-2.0-2020.json.zip",
        "nvdcve-2.0-2021.json.zip",
        "nvdcve-2.0-2022.json.zip",
        "nvdcve-2.0-2023.json.zip",
        "nvdcve-2.0-2024.json.zip",
        "nvdcve-2.0-2002.json",
        "nvdcve-2.0-2003.json",
        "nvdcve-2.0-2004.json",
        "nvdcve-2.0-2005.json",
        "nvdcve-2.0-2006.json",
        "nvdcve-2.0-2007.json",
        "nvdcve-2.0-2008.json",
        "nvdcve-2.0-2009.json",
        "nvdcve-2.0-2010.json",
        "nvdcve-2.0-2011.json",
        "nvdcve-2.0-2012.json",
        "nvdcve-2.0-2013.json",
        "nvdcve-2.0-2014.json",
        "nvdcve-2.0-2015.json",
        "nvdcve-2.0-2016.json",
        "nvdcve-2.0-2017.json",
        "nvdcve-2.0-2018.json",
        "nvdcve-2.0-2019.json",
        "nvdcve-2.0-2020.json",
        "nvdcve-2.0-2021.json",
        "nvdcve-2.0-2022.json",
        "nvdcve-2.0-2023.json",
        "nvdcve-2.0-2024.json",
        "CVE_data.csv"
    shell:
        "python fetch_data.py"
    
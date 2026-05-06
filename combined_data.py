import pandas as pd

df = pd.read_csv("CVE_data.csv")
df1 = pd.read_csv("rd_parsed_001.csv")
df2 = pd.read_csv("rd_parsed_002.csv")

#yearly analysis of CVEs
df["PubDate"] = pd.to_datetime(df["PubDate"])
df.groupby(pd.Grouper(key="PubDate", freq="YE")).count()
df = df[df["PubDate"] > pd.to_datetime("2002-01-01")]
df = df[df["PubDate"] < pd.to_datetime("2025-01-01")]

#severity
df_low = df[df["Severity"] == 'LOW']
df_low = df_low.groupby(pd.Grouper(key="PubDate", freq="YE")).count()
#print(df_low)

df_medium = df[df["Severity"] == 'MEDIUM']
df_medium = df_medium.groupby(pd.Grouper(key="PubDate", freq="YE")).count()
#print(df_medium)

df_high = df[df["Severity"] == 'HIGH']
df_high = df_high.groupby(pd.Grouper(key="PubDate", freq="YE")).count()
#print(df_high)

df_critical = df[df["Severity"] == 'CRITICAL']
df_critical = df_critical.groupby(pd.Grouper(key="PubDate", freq="YE")).count()
#print(df_critical)

df_none = df[df["Severity"] == 'NONE']
df_none = df_none.groupby(pd.Grouper(key="PubDate", freq="YE")).count()
#print(df_none)

#merge the dataframes on the year column

def merge_data_on_year(df_yr):
    df_yr = df_yr.reset_index()
    df_sev = pd.DataFrame({"index": range(len(df_yr))})
    for i in range(len(df_yr)):
        for column in df1.columns:
            df_sev.loc[i,column] = df1.loc[i,column]
        for column in df2.columns:
            df_sev.loc[i,column] = df2.loc[i,column]
        #for column in df_yr.columns:
            #df_sev.loc[i,column] = df_yr.loc[i,column]
        df_sev.loc[i,"CVE Count"] = df_yr.loc[i,"ID"]
    df_sev.drop(columns=["index","Unnamed: 0"], inplace=True)
    return df_sev

df_none = merge_data_on_year(df_none)
df_none.to_csv("none_combined.csv")

df_low = merge_data_on_year(df_low)
df_low.to_csv("low_combined.csv")

df_medium = merge_data_on_year(df_medium)
df_medium.to_csv("medium_combined.csv")

df_high = merge_data_on_year(df_high)
df_high.to_csv("high_combined.csv")

df_critical = merge_data_on_year(df_critical)
df_critical.to_csv("critical_combined.csv")
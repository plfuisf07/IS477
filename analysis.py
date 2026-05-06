#analysis

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df_none = pd.read_csv("none_combined.csv")
df_low = pd.read_csv("low_combined.csv")
df_medium = pd.read_csv("medium_combined.csv")
df_high = pd.read_csv("high_combined.csv")
df_critical = pd.read_csv("critical_combined.csv")

#high severity model
high_model = sm.OLS(df_high["Total All R&D Expenditures"], sm.add_constant(df_high["CVE Count"])).fit()
open("high_model_summary.txt", "w").write(high_model.summary().as_text())



#none severity model
none_model = sm.OLS(df_none["Total All R&D Expenditures"], sm.add_constant(df_none["CVE Count"])).fit()
open("none_model_summary.txt", "w").write(none_model.summary().as_text())

#low severity model
low_model = sm.OLS(df_low["Total All R&D Expenditures"], sm.add_constant(df_low["CVE Count"])).fit()
open("low_model_summary.txt", "w").write(low_model.summary().as_text())

#medium severity model
medium_model = sm.OLS(df_medium["Total All R&D Expenditures"], sm.add_constant(df_medium["CVE Count"])).fit()
open("medium_model_summary.txt", "w").write(medium_model.summary().as_text())

#critical severity model
critical_model = sm.OLS(df_critical["Total All R&D Expenditures"], sm.add_constant(df_critical["CVE Count"])).fit()
open("critical_model_summary.txt", "w").write(critical_model.summary().as_text())

#visualizations
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(df_none["CVE Count"], df_none["Total All R&D Expenditures"], label="None", marker="x")
ax.plot(df_high["CVE Count"], df_high["Total All R&D Expenditures"], label="High", marker="o")
ax.plot(df_low["CVE Count"], df_low["Total All R&D Expenditures"], label="Low", marker="s")
ax.plot(df_medium["CVE Count"], df_medium["Total All R&D Expenditures"], label="Medium", marker="^")
ax.plot(df_critical["CVE Count"], df_critical["Total All R&D Expenditures"], label="Critical", marker="d")
ax.set_xlabel("CVE Count")
ax.set_ylabel("Total All R&D Expenditures")
ax.set_title("R&D Expenditures vs. CVE Count by Severity")
ax.legend()
plt.savefig("analysis_results.png")

fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(df_none["CVE Count"],df_none["CVE Count"]*none_model._results.params[1]+none_model._results.params[0], label="None", marker="x")
ax.scatter(df_none["CVE Count"], df_none["Total All R&D Expenditures"], label="None", marker="x")
ax.set_xlabel("CVE Count")
ax.set_ylabel("Total All R&D Expenditures")
ax.set_title("R&D Expenditures vs. CVE Count for None Severity")
ax.legend()
plt.savefig("none_severity_analysis.png")
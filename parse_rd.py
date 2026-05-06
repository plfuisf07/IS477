import pandas as pd

df = pd.read_excel(io="tab001.xlsx",header=1,engine="calamine",skiprows=2)
df.to_csv("rd_parsed_001.csv")

df = pd.read_excel(io="tab002.xlsx",header=2,engine="calamine",skiprows=3)
df.rename(inplace=True,columns={"Unnamed: 0":"Year","Unnamed: 1":"Total All R&D Expenditures", "Amount":"Total Basic Research Amount", "Percent":"Total Basic Research Percent", "Amount.1":"Total Applied Research Amount", "Percent.1":"Total Applied Research Percent", "Amount.2":"Total Experimental Development Amount", "Percent.2":"Total Experimental Development Percent", "Unnamed: 8":"Federally Financed R&D Expenditures", "Amount.3":"Federally Financed Basic Research Amount", "Percent.3":"Federally Financed Basic Research Percent", "Amount.4":"Federally Financed Applied Research Amount", "Percent.4":"Federally Financed Applied Research Percent", "Amount.5":"Federally Financed Experimental Development Amount", "Percent.5":"Federally Financed Experimental Development Percent"})
df.to_csv("rd_parsed_002.csv")


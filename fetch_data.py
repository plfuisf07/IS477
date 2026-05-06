import pandas as pd
import requests
import zipfile
entries = []

j = -1

for file in range(2002,2025):
    response = requests.get("https://nvd.nist.gov/feeds/json/cve/2.0/nvdcve-2.0-%s.json.zip"%(str(file)))
    with open("nvdcve-2.0-%s.json.zip"%(str(file)), "wb") as f:
        f.write(response.content)
    with open("nvdcve-2.0-%s.json.zip"%(str(file)), "rb") as f:
      zip_file = zipfile.ZipFile(f)
      zip_file.extractall(".")
    df = pd.read_json("nvdcve-2.0-%s.json"%(str(file)))
    for i in range(len(df)):
      j = j+1
      #print(file,i,j)
      entries.append({
          "ID":df.iloc[1]["vulnerabilities"]["cve"]["id"],
          "PubDate":df.iloc[i]["vulnerabilities"]["cve"]["published"],
          "Status":df.iloc[i]["vulnerabilities"]["cve"]["vulnStatus"],
          "ModDate":df.iloc[i]["vulnerabilities"]["cve"]["lastModified"]
          })
      if entries[j]["Status"] in ["Rejected", "Awaiting Analysis" "Deferred"] or len(df.iloc[i]["vulnerabilities"]["cve"]["metrics"]) <= 0:
          entries[j]["Severity"] = "NONE"
      elif "baseSeverity" in next(iter (df.iloc[i]["vulnerabilities"]["cve"]["metrics"].values()))[0]:
          entries[j]["Severity"] = next(iter(df.iloc[i]["vulnerabilities"]["cve"]["metrics"].values()))[0]["baseSeverity"]
      else:
         entries[j]["Severity"] = next(iter(df.iloc[i] ["vulnerabilities"]["cve"]["metrics"].values()))[0]["cvssData"]["baseSeverity"]
df2= pd.DataFrame(entries)
df2
df2.to_csv("CVE_data.csv")
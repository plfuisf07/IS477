import requests 

response = requests.get("https://ncses.nsf.gov/pubs/nsf25348/assets/data-tables/tables/nsf25348-tab002.xlsx")
with open("tab002.xlsx", "wb") as f:
    f.write(response.content)

response = requests.get("https://ncses.nsf.gov/pubs/nsf25348/assets/data-tables/tables/nsf25348-tab001.xlsx")
with open("tab001.xlsx", "wb") as f:
    f.write(response.content)


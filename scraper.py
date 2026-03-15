import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

data = []

for title in titles:
    name = title.text
    link = title.find("a")["href"]
    
    data.append({
        "title": name,
        "link": link
    })

df = pd.DataFrame(data)

df.to_csv("companies.csv", index=False)
df.to_json("companies.json", orient="records")

print("Scraping Complete")
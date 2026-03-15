from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

url = "https://www.ycombinator.com/companies"
driver.get(url)

time.sleep(5)

for i in range(6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

companies = driver.find_elements(By.CSS_SELECTOR,"a[href^='/companies/']")

data = []

for c in companies:
    text = c.text.split("\n")

    if len(text) >= 3:
        name = text[0]
        location = text[1]
        description = text[2]

        data.append({
            "company": name,
            "location": location,
            "description": description
        })

df = pd.DataFrame(data).drop_duplicates()

df.to_csv("startups.csv", index=False)

print("Saved", len(df), "companies")

driver.quit()
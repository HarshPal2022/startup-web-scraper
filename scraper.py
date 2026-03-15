from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

url = "https://www.ycombinator.com/companies"

driver.get(url)

time.sleep(5)

companies = driver.find_elements(By.CLASS_NAME, "_company_i9oky_355")

data = []

for company in companies:
    name = company.text
    data.append({"company": name})

df = pd.DataFrame(data)

df.to_csv("startups.csv", index=False)

print("Startup data saved!")

driver.quit()
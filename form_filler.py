from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
time.sleep(2)

# Fill form
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Amandeep")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Singh")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("harry@gmail.com")
driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("123456789")

time.sleep(1)

# Get values back from the form
form_data = {
    "First Name": driver.find_element(By.XPATH, "//input[@placeholder='First Name']").get_attribute("value"),
    "Last Name": driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").get_attribute("value"),
    "Email": driver.find_element(By.XPATH, "//input[@type='email']").get_attribute("value"),
    "Phone": driver.find_element(By.XPATH, "//input[@type='tel']").get_attribute("value"),
}

# ✅ Export to JSON
with open("form_data.json", "w") as json_file:
    json.dump(form_data, json_file, indent=4)



# ✅ Export to Excel
df = pd.DataFrame([form_data])
df.to_excel("form_data.xlsx", index=False)

df.to_excel("output.xlsx", index=False)

import os
os.startfile("output.xlsx")  # Only works on Windows

df = pd.read_excel("output.xls", engine='xlrd')
print(df)



driver.quit()

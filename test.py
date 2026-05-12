from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service('/usr/bin/chromedriver')

driver = webdriver.Chrome(service=service, options=options)

driver.get("file:///var/snap/jenkins/5022/workspace/devops-pipeline4/index.html")

text = driver.find_element(By.TAG_NAME, "h1").text

assert "Success" in text

print("Test Passed Successfully")

driver.quit()

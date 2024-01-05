from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.justdial.com/"
driver = webdriver.Chrome()
driver.set_page_load_timeout(5)
driver.get(link)

# Get Xpath of the Element
x_path = """/html/body/div/div/section/section[2]/div/div/div[5]/div/div[2]/div[1]/div[2]/div"""

first_popular_searches = driver.find_element(By.XPATH, x_path)
# Print Element Text
print(first_popular_searches.text)

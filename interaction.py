from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Locate the element that contains the number of articles
# number_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
number_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(number_articles.text)

# Click the link
# number_articles.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Reference desk")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")

# any keys you have on the keyboard can be replicated using the Keys class
search.send_keys("Python", Keys.ENTER)

# # Close the browser
# driver.quit()

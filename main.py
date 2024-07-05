from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.toysrus.com.my/intex-unicorn-ride-on-1021502.html")
# price_dollar = driver.find_element(By.CLASS_NAME, value="value")
# print(f"Price of ToyRus Unicorn is {price_dollar.text}")

driver.get("https://www.python.org/")
# In the text input bar there are different elements like id, name, type (in the browser Inspect)
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# https://www.w3schools.com/xml/xpath_intro.asp
# Using the Xpath to locate the specific element
"""
In your browser inspect, right click -> copy -> XPATH
"""
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

upcoming_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in upcoming_time:
    print(time.text)

upcoming_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in upcoming_name:
    print(name.text)
events = {}

for n in range(len(upcoming_time)):
    events[n] = {
        "time": time.text,
        "name": name.text
    }
print(events)

# driver.close()
driver.quit()
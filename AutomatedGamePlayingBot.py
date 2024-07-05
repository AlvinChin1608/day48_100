from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

# Record the start time
start_time = time.time()

# Function to click the cookie for a given duration
def click_for_duration(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        cookie.click()

# Click for the first 5 minutes (300 seconds)
click_for_duration(300)

# Pause for 1 minute (60 seconds)
time.sleep(60)

# Click for the next 5 minutes (300 seconds)
click_for_duration(300)

# Pause for 1 minute (60 seconds)
time.sleep(60)

# Click for the next 5 minutes (300 seconds)
click_for_duration(300)

"""
Using time.time() - start_time is a way to measure the elapsed time since start_time. 
Here's a step-by-step explanation of why and how this works:
"""
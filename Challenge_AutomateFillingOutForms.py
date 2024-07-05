from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Alvin", Keys.TAB)
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Chin", Keys.TAB)


# # this work but let's do the proper way
# email_box = driver.find_element(By.NAME, value="email")
# email_box.send_keys("alvinwen3@gmail.com", Keys.ENTER)

email_box = driver.find_element(By.NAME, value="email")
email_box.send_keys("alvinwen3@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
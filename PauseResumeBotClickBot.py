from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

# Global variable to control the pause/resume state
clicking_paused = False

def click_cookie():
    global clicking_paused
    while True:
        if not clicking_paused:
            cookie.click()
        time.sleep(0.01)  # Add a small delay to prevent high CPU usage

def toggle_clicking():
    global clicking_paused
    while True:
        command = input("Enter 'p' to pause, 'r' to resume: ").strip().lower()
        if command == 'p':
            clicking_paused = True
            print("Clicking paused.")
        elif command == 'r':
            clicking_paused = False
            print("Clicking resumed.")
        elif command == 'q':
            print("Exiting...")
            break

# Start the clicking thread
clicking_thread = threading.Thread(target=click_cookie)
clicking_thread.start()

# Start the toggle control thread
toggle_thread = threading.Thread(target=toggle_clicking)
toggle_thread.start()

# Wait for the toggle thread to finish before closing the browser
toggle_thread.join()

# Optionally, close the browser
driver.quit()

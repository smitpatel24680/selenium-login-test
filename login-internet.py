"""
Selenium Challenge #2: The Internet - Form Login
URL: https://the-internet.herokuapp.com/login
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   # 1
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/login")



    def login(username, password):
        # Common locators
        username_box = driver.find_element(By.ID, "username")
        password_box = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")   # 2


        username_box.clear()
        password_box.clear()
        username_box.send_keys(username)
        password_box.send_keys(password)
        login_button.click()
        time.sleep(2)
        message = driver.find_element(By.ID, "flash").text    # 3  Also what is type in <input>, where username has type="text" and password has type="password"
        return message

    # 1️⃣ VALID LOGIN
    print("\nTest Case 1: Valid Login")
    msg = login("tomsmith", "SuperSecretPassword!")
    if "You logged into a secure area!" in msg:
        print("✓ Valid login successful")
    else:
        print("✗ Valid login failed")

    # Logout after success
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()   # 4
    time.sleep(2)

    # 2️⃣ INVALID LOGIN
    print("\nTest Case 2: Invalid Login")
    msg = login("invalidUser", "WrongPass")
    if "Your username is invalid!" in msg:
        print("✓ Correct error message shown for invalid credentials")
    else:
        print("✗ Incorrect behavior for invalid login")

    # 3️⃣ EMPTY FIELDS
    print("\nTest Case 3: Empty Fields")
    msg = login("", "")
    if "Your username is invalid!" in msg:
        print("✓ Proper error message shown for empty input")
    else:
        print("✗ Empty input not handled correctly")

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser closed. Ride complete 🤠")

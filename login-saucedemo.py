"""
Selenium: SauceDemo Login Automation
Practice site: https://www.saucedemo.com/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
    # Test Case 1: Valid Login
    print("Test Case 1: Valid Login 🤠")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()
    
    time.sleep(2)
    
    # Check if login successful
    if "inventory" in driver.current_url:
        print("✓ Logged in successfully, partner!")
    else:
        print("✗ Login failed, partner.")
    
    # Logout
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    # Wait until logout link becomes clickable
    wait = WebDriverWait(driver, 10)
    logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_link.click()

   
    #driver.find_element(By.ID, "logout_sidebar_link").click()
    #time.sleep(2)
    
    # Test Case 2: Invalid Login
    print("\nTest Case 2: Invalid Login 🤠")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    
    username.send_keys("wrong_user")
    password.send_keys("wrong_pass")
    login_btn.click()
    
    time.sleep(2)
    
    # Verify error message
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if "Username and password do not match" in error.text:
        print("✓ Error message displayed correctly")
    else:
        print("✗ Error message missing")

finally:
    driver.quit()
    print("\nBrowser closed. Ride complete 🤠")

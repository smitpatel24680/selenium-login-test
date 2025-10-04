"""
Selenium Basics: Login Test Automation
Practice Site: https://practicetestautomation.com/practice-test-login/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    
    # Test Case 1: Valid Login
    print("Test Case 1: Valid Login")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "submit")
    
    username_field.send_keys("student")
    password_field.send_keys("Password123")
    submit_button.click()
    
    time.sleep(2)
    
    # Verify successful login
    success_message = driver.find_element(By.CSS_SELECTOR, ".post-title")
    if "Logged In Successfully" in success_message.text:
        print("✓ Login successful")
    else:
        print("✗ Login failed")
    
    # Logout
    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
    logout_button.click()
    time.sleep(2)
    
    # Test Case 2: Invalid Username
    print("\nTest Case 2: Invalid Username")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "submit")
    
    username_field.send_keys("invalidUser")
    password_field.send_keys("Password123")
    submit_button.click()
    
    time.sleep(2)
    
    # Verify error message
    error_message = driver.find_element(By.ID, "error")
    if "Your username is invalid!" in error_message.text:
        print("✓ Error message displayed correctly")
    else:
        print("✗ Error message not found")


    # Test Case 3: Empty Username and Password
    print("\nTest Case 3: Empty Fields")

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "submit")

    # Don’t type anything, just click Login
    username_field.send_keys("")
    password_field.send_keys("")
    submit_button.click()

    time.sleep(2)

    # Verify error message
    error_message = driver.find_element(By.ID, "error")
    if "Your username is invalid!" in error_message.text:
        print("✓ Error message displayed correctly for empty fields")
    else:
        print("✗ Error message not found for empty fields")

finally:
    # Cleanup
    driver.quit()
    print("\nBrowser closed")
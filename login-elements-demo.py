"""
Selenium Elements Demo (RDR2-style but practical)

Demonstrates locating the same elements on:
https://practicetestautomation.com/practice-test-login/

Locators shown:
 - By.ID
 - By.NAME
 - By.CLASS_NAME
 - By.CSS_SELECTOR
 - By.XPATH
 - find_elements (plural)
Then runs 3 tests: valid login, invalid username, empty fields.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def describe(el):
    """Small helper to print useful info about a found element."""
    try:
        return {
            "tag": el.tag_name,
            "id": el.get_attribute("id"),
            "name": el.get_attribute("name"),
            "class": el.get_attribute("class"),
            "value": el.get_attribute("value"),
            "text": el.text[:80]  # preview
        }
    except Exception as e:
        return {"error": str(e)}

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()

    # Wait until the username input is present (useful guard)
    wait.until(EC.presence_of_element_located((By.ID, "username")))

    print("\n=== Locating the same fields using different methods ===\n")

    # 1) By ID (Sheriff's badge - unique)
    el_username_by_id = driver.find_element(By.ID, "username")
    print("By.ID -> username:", describe(el_username_by_id))

    el_password_by_id = driver.find_element(By.ID, "password")
    print("By.ID -> password:", describe(el_password_by_id))

    el_submit_by_id = driver.find_element(By.ID, "submit")
    print("By.ID -> submit:", describe(el_submit_by_id))

    print("\n--- Also try other locators that might target same elements ---\n")

    # 2) By NAME (alias)
    try:
        el_username_by_name = driver.find_element(By.NAME, "username")
        print("By.NAME -> username:", describe(el_username_by_name))
    except Exception:
        print("By.NAME: username not found")

    try:
        el_password_by_name = driver.find_element(By.NAME, "password")
        print("By.NAME -> password:", describe(el_password_by_name))
    except Exception:
        print("By.NAME: password not found")

    # 3) By CLASS_NAME (gang outfit) - MAY return first matching element for find_element
    # Here we'll use class names that exist on the form inputs (if present)
    try:
        el_by_class = driver.find_element(By.CLASS_NAME, "wp-block-button__link")
        print("By.CLASS_NAME -> submit-ish element (first match):", describe(el_by_class))
    except Exception:
        print("By.CLASS_NAME: example class not found or different on site")

    # 4) By CSS Selector (flexible tracker)
    el_username_css = driver.find_element(By.CSS_SELECTOR, "input#username")
    print("By.CSS_SELECTOR -> input#username:", describe(el_username_css))

    el_password_css = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    print("By.CSS_SELECTOR -> input[type='password'] (first match):", describe(el_password_css))

    el_submit_css = driver.find_element(By.CSS_SELECTOR, "button#submit")
    print("By.CSS_SELECTOR -> button#submit:", describe(el_submit_css))

    # 5) By XPath (treasure map)
    el_username_xpath = driver.find_element(By.XPATH, "//input[@id='username']")
    print("By.XPATH -> //input[@id='username']:", describe(el_username_xpath))

    el_password_xpath = driver.find_element(By.XPATH, "//input[@id='password']")
    print("By.XPATH -> //input[@id='password']:", describe(el_password_xpath))

    el_submit_xpath = driver.find_element(By.XPATH, "//button[@id='submit']")
    print("By.XPATH -> //button[@id='submit']:", describe(el_submit_xpath))

    # 6) find_elements (grab the whole posse)
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"\nfind_elements(By.TAG_NAME, 'input') -> found {len(inputs)} inputs. Preview first two:")
    for i, inp in enumerate(inputs[:3], start=1):
        print(f"  input #{i} ->", describe(inp))

    # Small pause before test cases
    time.sleep(1)

    print("\n=== Running Login Tests (will interact with the page) ===\n")

    # Helper that uses ID locators to fill and submit
    def run_login_test(username, password, description):
        print(f"\n-- Test: {description}")
        # Because previous tests may have left us on a different page,
        # ensure we're on the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        wait.until(EC.presence_of_element_located((By.ID, "username")))

        u = driver.find_element(By.ID, "username")
        p = driver.find_element(By.ID, "password")
        s = driver.find_element(By.ID, "submit")

        # clear before typing (defensive)
        u.clear(); p.clear()
        u.send_keys(username)
        p.send_keys(password)
        s.click()

        # give the site a moment
        time.sleep(1.5)

        # After clicking, either logged in (post-title present) or error element shows up
        # We attempt to detect both
        try:
            success = driver.find_element(By.CSS_SELECTOR, ".post-title")
            if "Logged In Successfully" in success.text:
                print("  ✓ Result: Logged in successfully (post-title found).")
                # logout to reset
                try:
                    logout = driver.find_element(By.LINK_TEXT, "Log out")
                    logout.click()
                    time.sleep(1)
                except Exception:
                    pass
                return
        except Exception:
            pass

        # look for error block
        try:
            err = driver.find_element(By.ID, "error")
            print("  ↳ Error block text:", err.text.strip())
        except Exception:
            print("  ✗ Neither success nor error detected (site may have changed).")

    # Test cases:
    run_login_test("student", "Password123", "Valid credentials")
    run_login_test("invalidUser", "Password123", "Invalid username")
    run_login_test("", "", "Empty username and password")

    print("\nAll done. Check the prints above to see how each locator behaved.")
finally:
    print("\nCleaning up: closing browser in 2 seconds...")
    time.sleep(2)
    driver.quit()
    print("Browser closed.")

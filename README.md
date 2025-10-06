# 🎯 Selenium Login Automation Challenge

This project demonstrates **automated login tests** on three different websites using **Python and Selenium WebDriver**.  
It’s a beginner-to-intermediate project designed to teach **element locators, interactions, waits, and error handling** — all in a practical, real-world context.

---

## 🌐 Websites Covered

1. **Practice Test Automation** – [https://practicetestautomation.com/practice-test-login/](https://practicetestautomation.com/practice-test-login/)  
   - Simple login form for beginners  
   - Good for learning **ID, name, and CSS selectors**

2. **The Internet – Form Authentication** – [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)  
   - Classic login challenge  
   - Shows error handling and page reload effects (stale elements)

3. **SauceDemo E-Commerce Login** – [https://www.saucedemo.com/](https://www.saucedemo.com/)  
   - Realistic e-commerce login simulation  
   - Teaches interaction with dynamic pages and handling sidebar logout

---

## 🚀 Project Overview

For each website, the scripts cover:

- ✅ **Valid login**
- ❌ **Invalid login**
- ⚠️ **Empty input validation** (where applicable)
- Element locating techniques:
  - `By.ID`
  - `By.NAME`
  - `By.CLASS_NAME`
  - `By.CSS_SELECTOR`
  - `By.XPATH`
- Interactions:
  - `send_keys()` to input text
  - `click()` to submit forms or links
- Basic **message verification** (`.text`)  
- Optional **logout flow**  

Each website has its **own Python script**:

| Script File | Website | Description |
|-------------|---------|-------------|
| `login-practice.py` | Practice Test Automation | Basic login tests with success/error messages |
| `login-internet.py` | The Internet | Tests valid, invalid, and empty logins; handles stale elements |
| `login-saucedemo.py` | SauceDemo | Valid/invalid login tests, interacts with dynamic inventory page, and logout menu |

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/smitpatel24680/selenium-login-challenge.git
cd selenium-login-challenge

2. **Install Dependencies**
```bash
pip install selenium webdriver-manager

3. **Run a Script**
```bash
python login-practice.py
python login-internet.py
python login-saucedemo.py


## Watch the magic happen — Selenium opens Chrome, performs login tests, and prints results to the console.

### 🧠 What You’ll Learn

How to automate login flows across multiple websites

Difference between element locators (ID, NAME, CLASS, CSS, XPATH)

How to handle dynamic content and stale elements

Using functions to reuse login code

Reading and validating success/error messages

Timing and waits for stable automation
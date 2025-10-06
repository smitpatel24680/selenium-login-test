# 🧭 Selenium Login Elements Demo

This project is a beginner-friendly **Selenium automation script** that demonstrates how to locate and interact with web elements on a login page.

## 🚀 Overview

The file `login-elements-demo.py` showcases **five common element locator strategies** used in Selenium:

- **By ID**
- **By Name**
- **By Class Name**
- **By CSS Selector**
- **By XPath**

Each locator targets the username, password, and login button fields on the [Practice Test Automation Login Page](https://practicetestautomation.com/practice-test-login/).

It also demonstrates how to:
- Read element attributes (`id`, `name`, `value`, `text`)
- Type into input boxes using `send_keys()`
- Click buttons using `click()`
- Understand when to use `.text` vs `.get_attribute("value")`

---

## 🧠 What You’ll Learn

- The purpose of each locator strategy  
- How Selenium identifies elements on a webpage  
- How to perform basic interactions with web elements  
- The difference between *element attributes* and *visible text*

---

## ⚙️ Setup Instructions

1. Install the dependencies:
   ```bash
   pip install selenium webdriver-manager

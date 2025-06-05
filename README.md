# 🔐 GitHub Login Bot using Selenium

This project is a lightweight automation script that uses **Selenium WebDriver** to log in to any website. It demonstrates basic browser automation with added error handling for a robust experience.

---

## 📌 Features

- ✅ Automatically installs and manages ChromeDriver using `webdriver-manager`
- ✅ Automates login using Selenium
- ✅ Error handling for:
  - WebDriver setup
  - Missing HTML elements
  - Unexpected runtime exceptions
- ✅ Ensures browser cleanup via `finally` block

---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.x
- Google Chrome
- Packages:
  - `selenium`
  - `webdriver-manager`
 ---

### 🛠 Installation
```bash
pip install selenium webdriver-manager
```
---

### ⚙️ Usage
Update the username, password, and url variables in the script:
``` bash
username = "Example@gmail.com"
password = "Pass"
url = "https://example.com/login"

```

Then, run the script:
```bash
python AutoLogin.py
```

The browser will open, log you in to website, and wait for you to press Enter before closing.

---

## ⚠️ Disclaimer
This script is for educational purposes only. Do not use it to automate login on other people's accounts or violate any website's terms of service.

---

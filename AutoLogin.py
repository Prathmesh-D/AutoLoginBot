from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    WebDriverException,
    TimeoutException
)
from webdriver_manager.chrome import ChromeDriverManager

def startBot(username, password, url):
    try:
        # Automatically manage the correct ChromeDriver version
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        driver.get(url)
        
        try:
            # Enter the username and password
            driver.find_element(By.ID, "login_field").send_keys(username)    # Manage the field id's accordingly.
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "commit").click()
        
        except NoSuchElementException as e:
            print("Error: One or more elements were not found on the page.")
            print(f"Details: {e}")
        
        # Wait for user input before closing the browser
        input("Press Enter to close the browser...")
    
    except WebDriverException as e:
        print("Error initializing the WebDriver.")
        print(f"Details: {e}")
    
    except Exception as e:
        print("An unexpected error occurred.")
        print(f"Details: {e}")
    
    finally:
        
        try:
            driver.quit()
        except:
            pass


# Driver Code
username = "Example@gmail.com"          # Example username
password = "Pass"                       # Example password
url      = "https://example.com/login"  # Example login URL

startBot(username, password, url)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Prompt user for contact number, date, time, and message first
contact_number = input("Enter the contact number (with country code, e.g., +1234567890): ")
date = input("Enter the date (e.g., 2025-01-28): ")
time_str = input("Enter the time (e.g., 15:30): ")

# Combine date and time to create a full timestamp
date_time = f"{date} {time_str}"

# Get the message
message = input("Enter the message you want to send: ")

# Prepare the message with date and time
message = f"{message} | Sent at: {date_time}"

# Path to the ChromeDriver you downloaded
driver_path = r"C:\webdrivers\chromedriver-win64\chromedriver.exe"  # Use raw string for path

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(driver_path))

try:
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    print("Please scan the QR code to log in...")

    # Wait for the QR code to be scanned and WhatsApp Web to fully load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="chat"]')))
    print("WhatsApp Web is now loaded.")

    # Wait for a moment before searching
    time.sleep(3)

    # Search for the contact by phone number
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    search_box.send_keys(contact_number)  # Use the phone number provided by the user
    search_box.send_keys(Keys.ENTER)  # Hit Enter to select the contact
    time.sleep(3)  # Wait for the chat to open

    # Find the message input box and send the message
    message_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )
    message_box.send_keys(message)  # Type the message
    message_box.send_keys(Keys.ENTER)  # Hit Enter to send the message

    print(f"Message sent to {contact_number} successfully!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Wait for a moment before closing the browser
    time.sleep(5)
    driver.quit()

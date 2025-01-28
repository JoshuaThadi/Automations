from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Path to the ChromeDriver you downloaded
driver_path = "C:\webdrivers\chromedriver-win64\chromedriver.exe"  # Replace this with the full path to your ChromeDriver

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(driver_path))

try:
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    print("Please scan the QR code to log in...")

    # Wait for the user to scan the QR code and WhatsApp Web to load
    time.sleep(20)  # Increase this if WhatsApp Web takes longer to load

    # Specify the name of the contact or group you want to send a message to
    contact_name = "Myself(You)"  # Replace with the name of your contact in WhatsApp
    message = "Hello, this is an automated message!"  # Replace with your custom message

    # Search for the contact by name
    search_box = driver.find_element(By.XPATH, '//*[@title="Search input textbox"]')
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)  # Hit Enter to select the contact
    time.sleep(3)  # Wait for the chat to open

    # Find the message input box
    message_box = driver.find_element(By.XPATH, '//*[@class="_13NKt"]')
    message_box.send_keys(message)  # Type the message
    message_box.send_keys(Keys.ENTER)  # Hit Enter to send the message

    print(f"Message sent to {contact_name} successfully!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Wait for a moment before closing the browser
    time.sleep(5)
    driver.quit()

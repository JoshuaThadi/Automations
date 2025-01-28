import pyautogui
import time
import datetime
import os

def send_whatsapp_message(phone_number, message, send_time):
    # Wait until the specified time
    while datetime.datetime.now() < send_time:
        time.sleep(1)  # Check every second

    # Open WhatsApp Desktop app (Ensure it is open and logged in)
    pyautogui.hotkey("win", "s")  # Open Windows search
    time.sleep(1)
    pyautogui.write("WhatsApp")  # Search for WhatsApp app
    time.sleep(1)
    pyautogui.press("enter")  # Open WhatsApp app
    time.sleep(5)  # Allow WhatsApp to load

    # Press 'Esc' to close any existing open chat
    pyautogui.press('esc')  # Close any open chat or search results
    time.sleep(1)  # Give it time to close the active chat

    # Clear the search bar completely
    pyautogui.hotkey("ctrl", "l")  # Focus the address bar
    time.sleep(1)
    pyautogui.press("backspace")  # Clear the search bar
    time.sleep(1)
    pyautogui.press("backspace")  # Ensure it's fully cleared
    time.sleep(1)

    # Now enter the full phone number properly
    pyautogui.write(f"{phone_number}")  # Format phone number in 'wa.me' link
    pyautogui.press("enter")  # Open the chat with the number
    time.sleep(5)  # Wait for the chat to load

    # Focus on the message input box and type the message
    message_box_coordinates = (960, 980)  # Coordinates for message input box (bottom-center)

    # Click on the message box to ensure focus
    pyautogui.click(message_box_coordinates)
    time.sleep(1)  # Ensure the message box is focused

    # Type the message and send it
    pyautogui.write(message)  # Type the message
    pyautogui.press("enter")  # Send the message
    print(f"Message sent to {phone_number}: {message}")

    # Close WhatsApp after sending the message
    pyautogui.hotkey("alt", "f4")  # Close the WhatsApp application
    time.sleep(2)  # Allow some time for the app to close

# Input from the user
phone_number = input("Enter the recipient's phone number (including country code, e.g., +1234567890): ")
message = input("Enter the message to send: ")

# Input for date and time when you want to send the message
year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day of the month (1-31): "))
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))
second = int(input("Enter the second (0-59): "))

# Set the specific time for sending the message
send_time = datetime.datetime(year, month, day, hour, minute, second)

# Call the function to send the message at the specified time
send_whatsapp_message(phone_number, message, send_time)

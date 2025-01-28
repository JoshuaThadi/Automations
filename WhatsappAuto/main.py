# Required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# twilio credentials
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

# design message sending function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_= "whatsapp:+14155238886",
            body = message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f'Messages sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

# user input
name = input('Enter the recipient name -> ')
recipient_number = input('Enter the recipient whatsapp number with country code (e.g: +91) -> ')
message_body = input(f'Enter the message you want to send to {name}: ')

# parse date/time and calculate delay
date_str = input('Enter the date to send the message (yyyy-mm-dd) -> ')
time_str = input('Enter the time to send the message (HH:MM in 24hour format) -> ')

# datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time -> ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

# wait until the schedule time
time.sleep(delay_seconds)

# send the message
send_whatsapp_message(recipient_number, message_body)
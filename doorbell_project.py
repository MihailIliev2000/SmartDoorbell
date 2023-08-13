import RPi.GPIO as GPIO
import webbrowser
from twilio.rest import Client
import time

# Set up the GPIO pin for the motion sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

# Set up the GPIO pin for the button
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define the Jitsi Meet URL and room name
url = 'https://meet.google.com/bju-yvad-iqq'

# Define the Twilio account SID, auth token, and phone number
account_sid = 'AC45f4b8b3e18a3d3e901124b43591ddf3'
auth_token = '29b83849674c664fc5194e922fd1e2c4'
twilio_phone_number = 'whatsapp:+14155238886'
my_phone_number = 'whatsapp:+447404768346'

# Create a Twilio client object
client = Client(account_sid, auth_token)

# Define a function to launch the Jitsi Meet video call
def start_video_call(channel):
    webbrowser.open(url)
    message = client.messages.create(
        body='Join:https://meet.google.com/bju-yvad-iqq',
        from_=twilio_phone_number,
        to=my_phone_number
    )
    print(message.sid)

# Define a function to send a WhatsApp message
def send_whatsapp_message(channel):
    message = client.messages.create(
        body="Motion detected!",
        from_=twilio_phone_number,
        to=my_phone_number
    )
    print(message.sid)

# Add event detection for both motion and button events
GPIO.add_event_detect(17, GPIO.RISING, callback=send_whatsapp_message, bouncetime=1000)
GPIO.add_event_detect(5, GPIO.RISING, callback=start_video_call, bouncetime=1000)

# Wait for events
while True:
    time.sleep(1)

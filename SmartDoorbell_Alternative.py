# Import required libraries
import RPi.GPIO as GPIO
import time
import webbrowser
import subprocess
from twilio.rest import Client

# Set GPIO pin mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pin numbers
speaker_pin1 = 2
speaker_pin2 = 6
motion_pin1 = 14
motion_pin2 = 11
motion_pin3 = 4
push_button_pin1 = 17
push_button_pin2 = 20

# Set GPIO pin modes
GPIO.setup(speaker_pin1, GPIO.OUT)
GPIO.setup(speaker_pin2, GPIO.OUT)
GPIO.setup(motion_pin1, GPIO.IN)
GPIO.setup(motion_pin2, GPIO.IN)
GPIO.setup(motion_pin3, GPIO.IN)
GPIO.setup(push_button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(push_button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to make a WhatsApp call
def make_call():
    subprocess.run(["yowsup-cli", "dial", "+447404768346"])

# Function to send a WhatsApp message
def send_message():
    subprocess.run(["yowsup-cli", "demos", "-s", "+447404768346", "-m", "Motion detected at the door."])

# Function to turn on the Pi camera, USB microphone, and speaker
def turn_on_components():
    # Code to turn on the Pi camera and USB microphone
    subprocess.run(["command to turn on the Pi camera"])
    subprocess.run(["command to turn on the USB microphone"])

    # Code to turn on the speaker
    GPIO.output(speaker_pin1, GPIO.HIGH)
    GPIO.output(speaker_pin2, GPIO.HIGH)

# Function to turn off the Pi camera, USB microphone, and speaker
def turn_off_components():
    # Code to turn off the Pi camera and USB microphone
    subprocess.run(["command to turn off the Pi camera"])
    subprocess.run(["command to turn off the USB microphone"])

    # Code to turn off the speaker
    GPIO.output(speaker_pin1, GPIO.LOW)
    GPIO.output(speaker_pin2, GPIO.LOW)

# Function to handle the push momentary button event
def button_callback(channel):
    print("Button Pressed")
    turn_on_components()
    make_call()

# Function to handle the motion sensor event
def motion_callback(channel):
    print("Motion Detected")
    send_message()

# Set up event detection for push momentary button
GPIO.add_event_detect(push_button_pin1, GPIO.FALLING, callback=button_callback, bouncetime=200)

# Set up event detection for motion sensor
GPIO.add_event_detect(motion_pin1, GPIO.RISING, callback=motion_callback, bouncetime=200)
GPIO.add_event_detect(motion_pin2, GPIO.RISING, callback=motion_callback, bouncetime=200)
GPIO.add_event_detect(motion_pin3, GPIO.RISING, callback=motion_callback, bouncetime=200)

try:
    # Run the code indefinitely
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO pins on keyboard interrupt
    GPIO.cleanup()

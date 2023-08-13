# Smart Doorbell
I have developed a smart doorbell based on Raspberry Pi 3, which provides a reliable and efficient way to monitor your home while safeguarding your privacy and security. The Raspberry Pi uses a Linux distribution as its operating system, ensuring the security and privacy of your data.
#
My doorbell incorporates several essential components, including a speaker, USB microphone, push button, motion sensor, Pi camera, and a small 3-inch LCD screen. When a visitor presses the doorbell button, a bell sound will play for 5 seconds, and the homeowner will receive an immediate notification via WhatsApp with a link to a video call, enabling real-time communication. The USB microphone, speaker, and Pi camera are all enabled during this time, allowing for clear two-way communication.
#
The video call takes place via Google Meet, a well known video service, while the WhatsApp messages are sent through Twilio, a service used for engagement platforms. Additionally, the doorbell is equipped with motion detection capabilities at the front door, which is particularly useful for security purposes. While the doorbell is not in use, the camera is continuously active and records any activity occurring at the front door.
# Components List: 
* Raspberry Pi 3.
* Pi Camera.
* PIR Motion Sensor.
* Speaker.
* Push Momentary Button.
* USB Microphone.
* LCD Screen.
* Jumper Wires.
* Wiring Tape.
* PowerBank
# Project Aims and objectives:
* Pi camera, microphone, speaker, motion sensor, push button and LCD should all be working without error and be detected by the raspberry pi having them connected to the correct GPIO pins.
* Link twilio account with whatsapp.
* Create a google room link.
* The motion sensor should detect nearby movement and send a whatsapp notification to notify the homeowner that motion has been detected.
* When the button is pressed a doorbell sound should play for 5-10 seconds and then the Raspberry Pi should perform two actions simultaneously. Firstly, it should open a URL leading to a Google Meet room, allowing visitors to enter it automatically. Secondly, it should send a WhatsApp message containing a link to the same Google Meet room, allowing visitors to enter it via their mobile devices. This way communication can happen between the homeowner and the visitor.
* Once the video call is finished the program should go back to detecting movement at the front door with the motion sensor.
* Take screenshots using the Pi camera every 10 seconds acting as a CCTV.
* Build a 3D printed enclosing case for the components using BlocksCAD Software.
# Pins Used: 
* Push button : Pin 17 (3.3v) and Pin 29 (GPIO 5).
* Motion Sensor : Pin 4 (5v Power), pin 11 (GPIO 17) and pin 14 (GND Ground).
* Speaker : Pin 2 (5v Power) and pin 6 (GND Ground). The wires should also be connected to the same pins found on the speaker.

  ![](images/riskregister3.png?raw=true)









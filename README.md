# Snippet-Bot
            Instructions
Snip-Bot Detection and Execution Bot/AI
            by R.O.Riesner

# What is Snip-Bot:

Snip-Bot is a simple and easy to configurate script, that detects pre-configured
picture snippet's (like buttons) captured/created by the user, from the desktop, softwares, games
or even videos and react on detecting the snippet's on screen.
The way the script reacts is determand in the "config.ini" file

# How to use:

- First you need to open the "config.ini" file in any text editor

- Now you need to add a participant that should look like this:

[Image1]

- next up, you need to add a path to the snippet you want the script to look for:

Path: example_folder/example_file.png

- And at last you need to determand a action the script should execute if it dectects the snippet:

Action: click_location	| example for clicking the center of the detected snippet

-or-

Action: button_press	| example for a simulated keyboard key getting pressed
Key: space				| determens the key that the script simulates getting pressed

# Template for "config.ini" :

[Image1]
Path: example_folder/example_file_1.png
Action: click_location

[Image2]
Path: example_folder/example_file_2.png
Action: button_press
Key: space

-end of template-

# Planed features:
- External "config.ini" File [PARTICIPANT_%NO; IMAGEPATH; HANDLE_ON_DETECTION; (KEYPRESS_KEY); SLEEP_TIMER_AFTER_ACTION]
- Graphical User Interface for easy control and configuration
- Support for MacOS and Linux
- Graphical feedback on screen (box around detected object)
- Configuralebyle area of detection
- Multi- Screen support
- Additional configuralebyles on detection (like run-command; quit-after-detection; log-actions; send-signal-to_local_maschine; send-signal-to_webserver)
- AI with access to Google Picture for improved detection and deep-learning
- WebCam support for detection of People; Animals and maybe even Objects
- Easy remote execution or configuration from local network
- Send state or command to a external WebServer using encripted SSH-Communication

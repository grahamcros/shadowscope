#!/user/bin/env python3
# Shadow Scope

# The following five libraries come pre-installed on the Raspberry Pi, but need to be imported to use.
# gpiozero makes it easy to use the pins
import gpiozero
# picamera has tons of camera control features
import picamera
# tkinter allows to you control windows
from tkinter import *
# time allows you to use time
import time
# random allows for the generation of random numbers
import random
# PIL is the photo manager
from PIL import ImageTk, Image
# import sys
import os

# if os.environ.get('DISPLAY','') == '':
#    print('no display found. Using :0.0')
#    os.environ.__setitem__('DISPLAY', ':0.0')

# The next batch of lines define variables associated with physical devices (camera, button, LEDs)
# For guide to pin numbers, see: http://gpiozero.readthedocs.io/en/stable/recipies.html
# Picamera v2 connected to Raspberry Pi camera port via ribbon cable
camera = picamera.PiCamera()
# One side of button connects to GPIO2 (pin 3) and the other side goes to Ground (pin 6)
button = gpiozero.Button(19)
# The arcade button has two LEDs connected in parallel with a built-in 200 Ohm resistor. It can take either 3.3 v or 5 v.
# Positve side (marked) of LED connects to GPIO4 (pin 7)
# and the negative side (marked) connects to Ground (pin 9)
# buttonLED = gpiozero.LED(4)
buttonLED = gpiozero.PWMLED(26)
# The pinhole LED takes 3 volts at 20 mA and has a brightness of 15,000 mcd.
# Positive side (long leg) of LED goes through 100 Ohm resistor before connecting to GPIO18 (pin 12)
# and the negative side (short leg) connects to Ground (pin 14)
pinholeLED = gpiozero.LED(16)

imageNumber = 0


# Define the touch screen button actions
def leftButtonAction():
    global imageNumber
    imageNumber = (imageNumber - 1) % 5
    print(imageNumber)


def rightButtonAction():
    global imageNumber
    imageNumber = (imageNumber + 1) % 5
    print(imageNumber)


inactive = 0

splashWindow = Tk()
splashWindow.wm_attributes('-type', 'splash')
splashWindow.geometry("470x870+0+0")
splashWindow.configure(bg='black')
splash = Canvas(splashWindow, height=870, width=470, bg='black')
img = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/CSU-Ram-Long-Dark.png"))
splash.create_image(0, -5, anchor=NW, image=img)
# words = splash.create_text(235, 540, text='SHADOW SCOPE')
# words = splash.create_text(235, 700, text='Press the GREEN button to turn on')
splash.pack()
splashWindow.update_idletasks()
splashWindow.update()

dialogWindow = Toplevel()

dialogWindow.geometry("470x300+0+480")
dialogWindow.configure(bg='white')

c = Canvas(dialogWindow, height=470, width=300, bg='white')
c.pack(expand=YES, fill=BOTH)


# Finds the name of the directory where removable drives are stored and returns the file path.
# Would be better to do this with a function like os.listmounts() but that doesn't work in Unix. Will work as long as file structure is maintained between systems
def findDrivePath():
    directory = "/media/pi/"
    subs = os.listdir(directory)
    directory += subs[0] + "/"
    return directory


while True:
    buttonLED.pulse()

    button.wait_for_press()

    buttonLED.value = 0

    # Define and place the buttons
    leftButton = Button(dialogWindow, text='<<Tips', width=8, height=10, bg='light goldenrod', fg='black',
                        activebackground='light goldenrod', activeforeground='black', command=leftButtonAction).place(
        x=0, y=110)
    rightButton = Button(dialogWindow, text='>>Tips', width=10, height=10, bg='light goldenrod', fg='black',
                         activebackground='light goldenrod', activeforeground='black', command=rightButtonAction).place(
        x=365, y=110)

    camera.preview_fullscreen = False
    camera.preview_window = (0, 5, 470, 470)
    camera.resolution = (1280, 1280)
    camera.start_preview()
    pinholeLED.on()
    dialogWindow.update_idletasks()
    dialogWindow.update()

    time.sleep(1)

    dialogWindow.deiconify()
    previousImageNumber = -1
    while True:
        inactive = inactive + 1
        print(inactive)
        if inactive >= 200000:
            inactive = 0
            break

        if imageNumber != previousImageNumber:
            if imageNumber == 0:
                c.delete('all')
                words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/Tip1.png"))
                c.create_image(105, 95, anchor=NW, image=img2)
                words = c.create_text(230, 270, text='Keep on truckin!')
                previousImageNumber = 0
            if imageNumber == 1:
                c.delete('all')
                words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/Tip2.png"))
                c.create_image(105, 100, anchor=NW, image=img2)
                words = c.create_text(230, 270, text='Peace!')
                previousImageNumber = 1
            if imageNumber == 2:
                c.delete('all')
                words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/Tip3.png"))
                c.create_image(105, 100, anchor=NW, image=img2)
                words = c.create_text(230, 270, text='Thumbs up!')
                previousImageNumber = 2
            if imageNumber == 3:
                c.delete('all')
                # words = c.create_text(225, 50, text='When you see something neat,')
                # words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/Tip4.png"))
                c.create_image(105, 100, anchor=NW, image=img2)
                words = c.create_text(230, 270, text='Onegaishimasu!')
                previousImageNumber = 3

            if imageNumber == 4:
                c.delete('all')
                # words = c.create_text(225, 50, text='When you see something neat,')
                # words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 50, text='When you see something neat,')
                words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/Tip5.png"))
                c.create_image(105, 100, anchor=NW, image=img2)
                words = c.create_text(230, 270, text='Thank you!!')
                previousImageNumber = 4

        if button.is_pressed:
            print("capturing")
            buttonLED.on()
            random.seed()
            id = random.randint(10000, 99999)
            c.delete('all')
            img2 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/VideoRecorded.png"))
            c.create_image(105, 95, anchor=NW, image=img2)
            words = c.create_text(225, 40, text="Video ID: " + str(id) + " (Snap a pic for your records).")
            words = c.create_text(225, 60, text="View/download from our website! (in a day or so)")
            words = c.create_text(225, 80, text="https://stasevichlab.colostate.edu/shadow-scope/videos.html")
            timestr = time.strftime("%Y%m%d-%H%M%S")
            directory = findDrivePath()
            camera.start_recording(directory + str(id) + '_shadow_scope1.h264')
            # camera.annotate_text = "Date stamp"
            camera.wait_recording(10)
            camera.stop_recording()
            buttonLED.off()
            inactive = 0

        dialogWindow.update_idletasks()
        dialogWindow.update()

    pinholeLED.off()
    camera.stop_preview()
    dialogWindow.withdraw()

#         sleep(2)
#     if buttonPressed == 1 and button.is_pressed:
#         buttonPressed = 0
#         print("camera off")
#         red.off()
#         sleep(2)
#     if pir.motion_detected and buttonPressed == 1:
#         camera.capture('/home/pi/Pictures/%s.jpg' % photonumber)
#         print("photo taken")
#         photonumber = photonumber + 1
#         sleep(30)

# camera.capture('/home/pi/Pictures/%s.jpg' % photonumber);
# print("photo taken");
# photonumber = photonumber + 1


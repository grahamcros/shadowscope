#Shadow Scope

#The following five libraries come pre-installed on the Raspberry Pi, but need to be imported to use.
#gpiozero makes it easy to use the pins
import gpiozero
#picamera has tons of camera control features
import picamera
#tkinter allows to you control windows
from tkinter import *
#time allows you to use time
import time
#random allows for the generation of random numbers
import random
#PIL is the photo manager
from PIL import ImageTk, Image


 #The next batch of lines define variables associated with physical devices (camera, button, LEDs)
#For guide to pin numbers, see: http://gpiozero.readthedocs.io/en/stable/recipies.html
#Picamera v2 connected to Raspberry Pi camera port via ribbon cable
camera = picamera.PiCamera()
#One side of button connects to GPIO2 (pin 3) and the other side goes to Ground (pin 6)
button = gpiozero.Button(19)
#The arcade button has two LEDs connected in parallel with a built-in 200 Ohm resistor. It can take either 3.3 v or 5 v.
#Positve side (marked) of LED connects to GPIO4 (pin 7)
#and the negative side (marked) connects to Ground (pin 9)
#buttonLED = gpiozero.LED(4)
buttonLED = gpiozero.PWMLED(26)
#The pinhole LED takes 3 volts at 20 mA and has a brightness of 15,000 mcd.
#Positive side (long leg) of LED goes through 100 Ohm resistor before connecting to GPIO18 (pin 12)
#and the negative side (short leg) connects to Ground (pin 14)
pinholeLED = gpiozero.LED(16)

imageNumber = 1


#Define the touch screen button actions
def leftButtonAction():
        global imageNumber
        imageNumber = imageNumber - 1
        print(imageNumber)
def rightButtonAction():
        global imageNumber
        imageNumber = imageNumber + 1
        print(imageNumber)

inactive = 0

splashWindow = Tk()
splashWindow.wm_attributes('-type', 'splash')
splashWindow.geometry("470x470+0+0")
splashWindow.configure(bg='white')
splash = Canvas(splashWindow, height=470, width=470, bg='white')
#words = splash.create_text(235, 140, text='SHADOW SCOPE')
#words = splash.create_text(235, 200, text='Press the GREEN button to turn on')
img = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/ShadowScopeImages/CSU-Ram.png"))
splash.create_image(0,-5, anchor=NW, image=img)

splash.pack()
splashWindow.update_idletasks()
splashWindow.update()

dialogWindow = Toplevel()

dialogWindow.geometry("470x300+0+480")
dialogWindow.configure(bg='white')

c = Canvas(dialogWindow, height=470, width=300, bg='white')
c.pack(expand=YES, fill=BOTH)

while True:
    buttonLED.pulse()

    button.wait_for_press()

    buttonLED.value = 0

    #Define and place the buttons
    leftButton = Button(dialogWindow, text='Back', width=8, height=10, bg='light goldenrod', fg='black', activebackground='light goldenrod', activeforeground='black', command=leftButtonAction).place(x=0,y=110)
    rightButton = Button(dialogWindow, text='Next', width=10, height=10, bg='light goldenrod', fg='black', activebackground='light goldenrod', activeforeground='black', command=rightButtonAction).place(x=365,y=110)


    camera.preview_fullscreen=False
    camera.preview_window=(0,5,470,470)
    camera.resolution=(1280,1280)
    camera.start_preview()
    pinholeLED.on()
    dialogWindow.update_idletasks()
    dialogWindow.update()

    time.sleep(1)

    dialogWindow.deiconify()
    previousImageNumber = 0
    while True:
        inactive = inactive + 1
        print(inactive)
        if inactive >= 1000000:
            inactive = 0
            break
        
        if imageNumber != previousImageNumber:
            if imageNumber == 1:
                c.delete('all')
                words = c.create_text(225, 50, text='Scan the QR code to visit our website!')
                #words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("ShadowScopeImages/CSU-Ram.png"))
                c.create_image(105,95, anchor=NW, image=img2)
                #words = c.create_text(230, 270, text='This is a Hydra')
                previousImageNumber = 1
            if imageNumber == 2:
                c.delete('all')
                words = c.create_text(225, 50, text='Scan the QR code to visit our website!')
                #words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("ShadowScopeImages/CSU-Ram.png"))
                c.create_image(105,100, anchor=NW, image=img2)
                #words = c.create_text(230, 270, text='This is a Mosquito larvae')
                previousImageNumber = 2
            if imageNumber == 3:
                c.delete('all')
                words = c.create_text(225, 50, text='Scan the QR code to visit our website!')
                #words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("ShadowScopeImages/CSU-Ram.png"))
                c.create_image(105,100, anchor=NW, image=img2)
                #words = c.create_text(230, 270, text='This is a Cocklebur')
                previousImageNumber = 3
            if imageNumber == 4:
                c.delete('all')
                words = c.create_text(225, 50, text='Scan the QR code to visit our website!')
                #words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("ShadowScopeImages/CSU-Ram.png"))
                c.create_image(105,100, anchor=NW, image=img2)
                #words = c.create_text(230, 270, text='This is a Hyalleia')
                previousImageNumber = 4
            if imageNumber == 5:
                c.delete('all')
                #words = c.create_text(225, 50, text='When you see something neat,')
                #words = c.create_text(225, 70, text='press the GREEN button to record it for our website!')
                img2 = ImageTk.PhotoImage(Image.open("ShadowScopeImages/CSU-Ram.png"))
                c.create_image(105,30, anchor=NW, image=img2)
                #words = c.create_text(230, 270, text='Scan this code to visit our website!')
                previousImageNumber = 5

        if button.is_pressed:
            print("capturing")
            buttonLED.on()
            random.seed()
            id = random.randint(100000000,999999999)
            c.delete('all')
            words = c.create_text(225, 50, text= "Your unique ID is " + str(id) + ".")
            words = c.create_text(225, 70, text = "Take a picture of it and use it on our website!")
            #timestr = time.strftime("%Y%m%d-%H%M%S")
            camera.start_recording("ShadowScopeVideos/" + str(id) + 'shadow_scope1.h264')
            #camera.annotate_text = "Date stamp"
            camera.wait_recording(5)
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

import gpiozero
import picamera
from tkinter import *
from time import sleep

camera = picamera.PiCamera()
button = gpiozero.Button(27)
red = gpiozero.LED(17)
buttonPressed = 0

root = Tk()
root.geometry("320x240+90+400")
#root.configure(background='grey')
#path = "test.jpg"
#img = ImageTk.PhotoImage(Image.open(path))
#panel = tk.Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
c = Canvas(root, height=320, width=240)
c.pack()
words = c.create_text(120, 20, text='When you see something neat,')
words = c.create_text(120, 40, text='press the yellow button')

camera.preview_fullscreen=False
camera.preview_window=(90,100,320,240)
camera.resolution=(640,640)
camera.start_preview()

while True:
    if buttonPressed == 0 and button.is_pressed:
        buttonPressed = 1
        print("capturing")
        red.on()
        camera.start_recording('myvideo.h264')
        #camera.annotate_text = "Date stamp"
        camera.wait_recording(10)
        camera.stop_recording()
        red.off()
        buttonPressed = 0
    root.update_idletasks()
    root.update()

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


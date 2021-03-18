import pyautogui as py  # It is required for taking a screenshot of desktop
from PIL import Image, ImageTk  # Important for showing BSOD
import winsound
import time
import subprocess  # To run AHK script to max the volume
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

time.sleep(5)

py.hotkey("win", "d")
time.sleep(0.7)
im = py.screenshot('ss.png')
ISRUN = False
TOTALLOOP = 0


def toggle_geom():
    pass  # To prevent <ESC> and <ALT+F4> to work


subprocess.Popen("ahk.exe sound.ahk")  # Maximize the sound
root = tk.Tk()
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),
              root.winfo_screenheight()))
bg = tk.PhotoImage(file="ss.png")
bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(),
                   height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)


def update(ind):  # Play GIF file
    global TOTALLOOP
    if ind == 80:
        ind = 0
        TOTALLOOP += 1
    if ind < 10:
        indText = "0" + str(ind)
    else:
        indText = str(ind)
    directoryName = "./BSOD/bsodgif/frame_" + indText + "_delay-0.05s.png"
    img = Image.open(directoryName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    bg2 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg2)
    bgimage.image = bg2
    root.update()
    ind += 1
    if TOTALLOOP < 4:
        root.after(5, update, ind)
    else:
        img = Image.open("./BSOD/bsod7.png").resize((root.winfo_screenwidth(),
                                                     root.winfo_screenheight()), Image.ANTIALIAS)
        bg1 = ImageTk.PhotoImage(img)
        bgimage.configure(image=bg1)
        bgimage.image = bg1
        root.update()
        winsound.PlaySound(None, winsound.SND_ASYNC)
        time.sleep(6)
        root.destroy()
        exit()


def updateImg(numb, sleepNum):  # Image changer
    imgName = "./BSOD/bsod" + str(numb) + ".png"
    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor='none')
    bgimage.image = bg1
    root.update()
    time.sleep(sleepNum)


def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1, 4)
        updateImg(2, 6)
        updateImg(3, 7)
        updateImg(4, 0.01)
        winsound.PlaySound('noise1.wav', winsound.SND_ASYNC)
        updateImg(3, 3)
        winsound.PlaySound('noise2.wav', winsound.SND_ASYNC)
        updateImg(6, 0.01)
        updateImg(3, 1.5)
        winsound.PlaySound('noise3.wav', winsound.SND_ASYNC)
        updateImg(4, 0.01)
        updateImg(3, 0.75)
        winsound.PlaySound('final.wav', winsound.SND_ASYNC)
        updateImg(5, 3)
        winsound.PlaySound('loop.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        root.after(0, update, 0)


bgimage.bind('<Button-1>', initiate)
root.attributes("-fullscreen", True)
root.bind('<Escape>', toggle_geom)
root.attributes('-topmost', True)
root.update()
# root.protocol("WM_DELETE_WINDOW",toggle_geom)
root.mainloop()

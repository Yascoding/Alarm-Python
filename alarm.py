from time import strftime 
from tkinter import * 
import time
import datetime
import winsound
import sys
from pygame import mixer
from sqlalchemy import column
 
root = Tk() 
root.title('Alarm-Clock') 
 
def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 20, 'bold'),
            text="Wake up! ",bg="DodgerBlue2",fg="white").grid(row=7,columnspan=4)
            print("wake up!")
            mixer.init()
            mixer.music.load("FallWithMe.mp3")
            mixer.music.play()
            return

def countdownclock(time_left): 
    total_seconds = (hrss.get() * 3600) + (minss.get() * 60) + (secss.get() * 1)
    time_now=datetime.datetime.now().strftime("%H:%M:%S")
    while True:
        print(total_seconds,"\r", end='') # overwrite previous line and set it to empty 
        time.sleep(1)
        total_seconds -= 1
        if total_seconds <= 0:
            print("Time is up!")
            mixer.init()
            mixer.music.load("FallWithMe.mp3")
            mixer.music.play()
            return


def snooze(snooze):
    mixer.music.stop()
    time_now=300
    while True:
        print(time_now,"\r", end='')
        time.sleep(1)
        time_now -= 1
        if time_now== 0:
            Wakeup=Label(root, font = ('arial', 20, 'bold'),
            text="Wake up! ",bg="DodgerBlue2",fg="white").grid(row=7,columnspan=4)
            print("wake up!")
            mixer.init()
            mixer.music.load("FallWithMe.mp3")
            mixer.music.play()
            return

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    return alarmtime

# declaring variables
hrs=StringVar()
mins=StringVar()
secs=StringVar()

hrss=IntVar()
minss=IntVar()
secss=IntVar()

#labels
greet=Label(root, font = ('arial', 12),
text="Set timer").grid(row=1,columnspan=2, column=2)
greet=Label(root, font = ('arial', 12),
text="Countdown").grid(row=1,columnspan=2, column=20)

hour_label = Label(root, font = ('arial',12),
text="Hours").grid(row=2,column=5)
min_label = Label(root, font = ('arial',12),
text="Minutes").grid(row=3,column=5)
sec_label = Label(root, font = ('arial',12),
text="Seconds").grid(row=4,column=5)

#buttons
setbtn=Button(root,text="set alarm \n",command= lambda: alarmclock(setalarm()),bg="DeepSkyBlue4",
fg="white",font = ('arial', 20, 'bold')).grid(row=8,columnspan=4,ipadx=0, column=1)

setbtg=Button(root,text="set count \n",command=lambda: countdownclock(setalarm()),bg="DeepSkyBlue4",
fg="white",font = ('arial', 20, 'bold')).grid(row=8,column=20, columnspan=3, ipadx=0)

resetg=Button(root,text="Snooze 5 min \n",command= lambda: snooze(setalarm()),bg="red",
fg="white",font = ('arial', 20, 'bold')).grid(row=9,column=1, columnspan=20, ipadx=130)

# Alarm
hrbt=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold'))
hrbt.grid(row=2,column=3),

minbt=Entry(root,textvariable=mins,
width=5,font = ('arial', 20, 'bold')).grid(row=3,column=3)

secbt=Entry(root,textvariable=secs,
width=5,font = ('arial', 20, 'bold')).grid(row=4,column=3)

# countdown 2de colom
hrbtn=Entry(root,textvariable=hrss,width=5,font =('arial', 20, 'bold'))
hrbtn.grid(row=2,column=20),

minbtn=Entry(root,textvariable=minss,
width=5,font = ('arial', 20, 'bold')).grid(row=3,column=20)

secbtn=Entry(root,textvariable=secss,
width=5,font = ('arial', 20, 'bold')).grid(row=4,column=20)
 
root.mainloop() 


from tkinter import *
from playsound import playsound
from datetime import datetime
from tkinter import messagebox
import time


def Alarm(given_time):
    while True:
        time.sleep(1)
        actual_time = datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        print(cur_time)
        if cur_time == given_time:
            playsound('sound.wav')
            messagebox.showinfo(title="Alarm", message="Alarm is ringing.")
            break

def Time():
    hour = int(hour_entry.get())
    min = int(min_entry.get())
    sec = int(sec_entry.get())
    if hour < 10:
        hour = f"0{hour}"
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"
    time = f"{hour}:{min}:{sec}"
    Alarm(time)

window = Tk()
window.title("Alarm Clock")
window.geometry('400x220')
window.config(bg="#176B87")
frame = Frame(window, height=50, width=400, bg="#053B50")
frame.grid(row=0, columnspan=4, column=0)
label = Label(frame, compound= TOP, text="Alarm Clock", font='Verdana 25 bold', fg="white", bg="#053B50")
label.place(x=90, y=5)
hour_label = Label(text="Hours", font='Verdana 12 bold', bg="#176B87")
min_label = Label(text="Minutes", font='Verdana 12 bold', bg="#176B87")
sec_label = Label(text="Seconds", font='Verdana 12 bold', bg="#176B87")
hour_label.grid(row=1, column=1, pady=10)
min_label.grid(row=1, column=2, pady=10)
sec_label.grid(row=1, column=3, pady=10)
text_label = Label(text="Set time: ", font='Verdana 17 bold', bg="#176B87")
text_label.grid(row=2, column=0)
hour_entry = Entry(width=8)
min_entry = Entry(width=8)
sec_entry = Entry(width=8)
hour_entry.grid(row=2, column=1)
min_entry.grid(row=2, column=2)
sec_entry.grid(row=2, column=3)
submit = Button(text="Set Alarm", font='Verdana 12 bold', bg="#053B50", fg="white", command=Time)
submit.grid(row=3, column=1, columnspan=2, pady=10)
msg_label = Label(text="Please enter time in 24 hour format!", font='Verdana 12 bold', bg="#176B87")
msg_label.grid(row=4, column=0, columnspan=4)
window.mainloop()
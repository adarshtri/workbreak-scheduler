#the main scheduler file
import schedule
import time
import sys
import threading
from tkinter import *
import os

def job():
        tot_sec=int(e2.get())
        os.system("sudo rtcwake -m mem -s "+str(tot_sec*60))

def run_scheduler():
        schedule.every(int(e1.get())).minutes.do(job)
        global cond
        while cond:
                schedule.run_pending()
                time.sleep(1)

def show_entry_fields():
        total_min=int(e1.get())+int(e2.get())
        global scheduler_thread
        global cond
        cond = True
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.start()

def exit_program():
    global cond
    global master
    cond = False
    master.destroy()

cond = True
scheduler_thread = None
master = Tk()
Label(master, text="Work Time in Minutes").grid(row=0)
Label(master, text="Break Time in Minutes").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=lambda : exit_program()).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop()

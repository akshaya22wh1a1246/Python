
from tkinter import *

win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window


can=Canvas(win, width=1000, height=500) #creating the canvas
oval=can.create_oval(100, 100, 200, 180,fill='red') #drawing an oval 
can.pack()

win.mainloop() #running the loop that works as a trigger

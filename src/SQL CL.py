#SQL Query Client End

import socket
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter as tk


#Network connection-- Not finish
def network(destip):
    socket1=socket.socket()
    destpt=7900     #Use port 7900 to communicate
    socket1.connect((destip,destpt))
    

#GUI Part- Not finish
class UI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.Widgets()
    def Widgets(self):
        messagebox.showinfo('Message','Welcome to SQL Client end.')
        self.Viewbutton=Button(self,text='Enter the destnation address of databse to query the databse',command=self.EstablishNetwork)
        self.Viewbutton.pack()
        self.IPEntry=Entry(self)
        self.IPEntry.pack()
    def EstablishNetwork(self):
        IPaddress=self.IPEntry.get()
        self.EstablishNetwork=tk.Toplevel(self.master)
        self.NETI=NETUI(self.EstablishNetwork)
        
class NETUI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.CreateWidgets()
    def CreateWidgets(self):
        messagebox.showinfo('Message','Select the thing that you want to query')
        self.TimeButton=Button(self,text='Query the log at a specific time')
        self.CommentButton=Button(self,text='Query the Key word of the comment')
        self.TimeEntry=Entry()
        self.CommentEntry=Entry()
        self.TimeEntry.pack()
        self.TimeButton.pack()
        self.CommentEntry.pack()
        self.CommentButton.pack()


UI=UI()
UI.mainloop()


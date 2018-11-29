import os
from tkinter import *

#GUI interface
class UI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.Widgets()
    def Widgets(self):          #In this fuction, I made some buttons that are used to open different modules
        self.SQLCLbutton=Button(self,text='Open the network interface bandwidth configuration tool',command=self.openbandwidth)   #Create a button used to open the bandwidth setting tools
        self.SQLCLbutton.pack()
        self.NDopenbutton=Button(self,text='Open network diagnosticer',command=self.openND)  #Create a button use to open the Network Diagnostic tools
        self.NDopenbutton.pack()
        self.OpenSettingToolsButton=Button(self,text='Open the setting tools to set you capture interface',command=self.OpenSettingTools)   #Create a button used to open the interface setting tools
        self.OpenSettingToolsButton.pack()




    def openbandwidth(self):
        os.system('ChangeBandwidth.py')
    def openND(self):
        os.system('Network_Diagnosticer.py')
    def OpenSettingTools(self):
        os.system('"Interface Setting.py"')








UI=UI()
UI.master.title('Main user interface')
UI.mainloop()

from tkinter import *
import tkinter.messagebox as messagebox
import time
import os




#In this module, the user interface only includes two buttons and one input box
#The button above is used to capture the program with 10 seconds
#If the user want to capture the packets for other times, they can input a number in the text box and press the lowest button
class CAP_UI(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand=True)
        self.ButtWidgets()
    def ButtWidgets(self):
        self.SixtysButton=Button(self,text='Capture 10 Seconds',command=self.CheckInterfaceAndCap)  #Capture the packet for 10 seconds by using the CheckInterfaceAndCap() method
        self.SixtysButton.pack()
        self.Timeinput=Entry(self)
        self.Timeinput.pack()
        self.TimeinputButton=Button(self,text='If you want capture for other seconds, input your number and press me',command=self.CheckInterfaceAndCap_Any)
        self.TimeinputButton.pack()
    def CheckInterfaceAndCap(self):
        checkfile=open("User.txt")
        line=checkfile.readline()               #Get the name of the network interface input by the user in the interface configuration program
        if line=="Capture Interface=Wi-Fi":         
            self.OpenTshark_WiFi()              #Using OpenTshark_WiFi() method to capture packets via Wi-Fi
            checkfile.close()                   #Close the file
            return 0                            #The purpose of return 0 is return a value and end this method so that the program will not continue (Or otherwise the program will capture twice because of the else statement)
        if line=="Capture Interface=Ethernet":
            self.OpenTshark_Ethernet()          #Using OpenTshark_Ethernet() method to capture packets via Ethernet
            checkfile.close()
            return 0
        else:
            self.OpenTshark_Any(line)           #If the name of interface is neither Wi-Fi nor Ethernet, the program will get take the name of the network interface and pass this as a parameter to OpenTshark_Any(line) method
            checkfile.close()
            return 0
    
    #In the following code, tshark -i [name of the interface] will let tshark using this interface to capture
    #-a duration: [time] will let tshark stop capturing automatically after that time period
    #>> D:\CapSyslog\A.txt will stored the syslog of CMD to D:\CapSyslog\A.txt
    def OpenTshark_WiFi(self):
        file=open("D:\CapSyslog\A.txt",'w')     #'w' mode will erase all the text in the file when it's opened by the program
        file.write("Capture time:10 \n")        #Write the Capture time to the txt file so that the reading will know how long does the capture last
        file.close()
        ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -i Wi-Fi -a duration:10 >> D:\CapSyslog\A.txt')     #Cause tshark is in C:\Program Files\Wireshark, so before it's executed in CMD, we need to change the location first.
        messagebox.showinfo('Message','Capture is Finished, please close the program and open the reader to analyse')  #Return a message to user and inform them that the capture is finished. 
    def OpenTshark_Ethernet(self):
        file=open("D:\CapSyslog\A.txt",'w')
        file.write("Capture time:10 \n")
        file.close()
        ExecuteCMD('"pushd C:\Program Files\Wireshark" & tshark -i Ethernet -a duration:10 >>D:\CapSyslog\A.txt')
        messagebox.showinfo('Message','Capture is Finished, please close the program and open the reader to analyse')
    def OpenTshark_Any(self,interface):
        interface_index=interface.find('Capture Interface=',0)
        interface_index+=18
        Name_Of_Interface=""
        Length=len(interface)-1
        while interface_index<=Length:
            Name_Of_Interface+=interface[interface_index]           #Get the name of the interface
            interface_index+=1
        command='"pushd C:\Program Files\Wireshark" & tshark -i '+str(Name_Of_Interface) +' -a duration: 10 >>D:\CapSyslog\A.txt'       #Form the command
        file=open("D:\CapSyslog\A.txt",'w')
        file.write("Capture time:10 \n")
        file.close()
        ExecuteCMD(command)
        messagebox.showinfo('Message','Capture is Finished, please close the program and open the reader to analyse')

    #Similar to the method CheckInterfaceAndCap(), but here, it take the time input by user as a parameter of the capturing methods
    def CheckInterfaceAndCap_Any(self):
        checkfile=open("User.txt")
        line=checkfile.readline()
        time=self.Timeinput.get()
        if line=="Capture Interface=Wi-Fi":
            self.OpenTshark_WiFi_Any(time)
            checkfile.close()
            return 0
        if line=="Capture Interface=Ethernet":
            self.OpenTshark_Ethernet_Any(time)
            checkfile.close()
            return 0
        else:
            self.OpenTshark_Any_Any(line,time)
            checkfile.close()
            return 0
    #Similar to the Capturing methods above but here it takes time_Cap as the parameter
    def OpenTshark_WiFi_Any(self,time_Cap):
        file=open("D:\CapSyslog\A.txt",'w')
        Text="Capture time:"+str(time_Cap)
        file.write(Text+' \n')
        file.close()
        command='"pushd C:\Program Files\Wireshark" & tshark -i Wi-Fi -a duration:'+str(time_Cap)+' >>D:\CapSyslog\A.txt'
        ExecuteCMD(command)
        messagebox.showinfo('Message','Capture is Finished, please close the program and open the reader to analyse')
    def OpenTshark_Ethernet_Any(self,time_Cap):
        file=open("D:\CapSyslog\A.txt",'w')
        Text="Capture time:"+str(time_Cap)
        file.write(Text+' \n')
        file.close()
        command='"pushd C:\Program Files\Wireshark" & tshark -i Ethernet -a duration:'+str(time_Cap)+' >>D:\CapSyslog\A.txt'
        ExecuteCMD(command)
        messagebox.showinfo('Message','Capture is Finished, please close the program and open the reader to analyse')
    def OpenTshark_Any_Any(self,interface,time_Cap):
        file=open("D:\CapSyslog\A.txt",'w')
        Text="Capture time:"+str(time_Cap)
        file.write(Text+' \n')
        file.close()
        interface_index=interface.find('Capture Interface=',0)
        interface_index+=18
        Name_Of_Interface=""
        Length=len(interface)-1
        while interface_index<=Length:
            Name_Of_Interface+=interface[interface_index]
            interface_index+=1
        command='"pushd C:\Program Files\Wireshark" & tshark -i '+str(Name_Of_Interface) +' -a duration:'+str(time_Cap)+' >>D:\CapSyslog\A.txt'
        ExecuteCMD(command)
        message.showinfo('Message','Capture is Finished, please close the program and open the reader to analyse')

        
#This function is used to execute the command by using CMD
def ExecuteCMD(command):
    os.system(command)

UI=CAP_UI()
UI.master.title('Capture program')
UI.mainloop()

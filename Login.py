import os
from tkinter import *
import tkinter.messagebox as messagebox
import hashlib
filetxt='unpp.txt'      #Name of the file that stored the username and password
class UI(Frame):        #This class is used to define the GUI interface
    def __init__(self,master=None):
        Frame.__init__(self,master)                #Inherit from the master class: "Frame" of tkinter
        self.pack(expand=True)                # Build the interface, "expand=True" will let the main interface be in the middle if user maximize it
        self.createWidgets()
    def createWidgets(self):
        self.UNinput=Entry(self)    #Build a input box that allows user to input the username
        self.UNinput.pack()         #Pack the input box
        self.PPinput=Entry(self,show='*')   #Build a input box that alloows user to input the password. show='*' will let the password input by user shown as '*' for security
        self.PPinput.pack()         #Pack the input box
        self.loginbutton=Button(self,text='Login',command=self.hello)              #Build a Login Button and execute the self "hello" method if the user press it
        self.loginbutton.pack()     #Pack the login button
        self.changeUNPPbutton=Button(self,text='Change Username and Password', command=self.openmodule)    #Build a button and execute self "openmodule" if the user press it
        self.changeUNPPbutton.pack()  #Pack the button
        
    def hello(self):
        password=self.PPinput.get()         #Get the username input by user
        username=self.UNinput.get()         #Get the password input by user
        if check_UNPP(username,password)==True:              #By using the function, check if the password is correct
            os.system('main_user_interface.py')       #Open the main user interface if the username and password are correct.
        else:
            messagebox.showinfo('Message','Wrong password! \nOr password can not be blank')     #Return an error message if the user input a wrong username or password
    def openmodule(self):
        os.system('ChangeUNPPmodule.py')    #Open the module that used to change the username and password
  

            

        
            
def storage():
    global un       #un stands for username
    global pp       #pp stands for password
    filename=open(filetxt,'r')
    un=filename.readline()  #Read the username in the file
    pp=filename.readline()  #Read the password in the file

def check_UNPP(us,pw):
    us=us.encode('utf-8')       #Before we hash, we need to encode the information as utf-8
    pw=pw.encode('utf-8')
    Hash_US=hashlib.sha512()    #Using SHA-512 hashing method to hash 
    Hash_PP=hashlib.sha512()    #Using SHA-512 hashing method to hash 
    Hash_US.update(us)          #Hash the username
    Hash_PP.update(pw)          #Hash the password
    After_Hash_US=Hash_US.hexdigest()+'\n'      #Get the information after hashing and format to hexadecimal
    After_Hash_PP=Hash_PP.hexdigest()           #Get the information after hashing and format to hexadecimal
    if After_Hash_US==un and After_Hash_PP==pp:     
        return True         #Return a "True" Boolean value if the matching is correct

storage()   #Call the file
LGUI=UI()
LGUI.master.title('Login')      #Title of the program
LGUI.mainloop()

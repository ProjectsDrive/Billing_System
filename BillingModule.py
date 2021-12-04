from tkinter import *
from tkinter import messagebox
import os
root=Tk()
root.geometry('1366x768')
root.resizable(0,0)
root.title('Billing System')
root.iconbitmap('./Images/icon.ico')

class Tools:
    def setBackground(self,address):
        self.bg=PhotoImage(file=address)
        label1=Label(root,image=self.bg)
        label1.place(x=0,y=0)
    def eventLoop(self):
        root.mainloop()   

class MainPage:
    def __init__(self):
        pass
    
    def displayLabel(self,X,Y):
        label2=Label(root,text="Login As ?",font=("Times New Roman bold",40),background="#63b8e4")
        label2.place(x=X,y=Y)
    
    def admin(self):
        root.withdraw()
        os.system('AdmLogin.py')
        root.deiconify()

    def addAdminBtn(self,X,Y):
        button=Button(root,text="Admin",font=("Arial",18),cursor="hand2",command=self.admin)
        button.place(x=X,y=Y,width=146,height=60)

    def employee(self):
        root.withdraw()
        os.system('EmpLogin.py')
        root.deiconify()
    
    def addEmployeeBtn(self,X,Y):
        button=Button(root,text="Employee",font=("Arial",18),cursor="hand2",command=self.employee)
        button.place(x=X,y=Y,width=146,height=60)

class AdmLogin:
    def __init__(self):
        self.admId=StringVar()
        self.admPwd=StringVar()

    def createFrame(self):
        frame1=Canvas(root,height=450,width=600,background="skyblue")
        frame1.place(x=380,y=150)
        frame2=Canvas(root,height=100,width=600,background="orange")
        frame2.place(x=380,y=150)
        frame3=Canvas(root,height=80,width=600,background="orange")
        frame3.place(x=380,y=520)

    def createForm(self):
        label1=Label(root,text="Login as Admin",font=("Times New Roman bold",30),background="orange",foreground="white")
        label1.place(x=550,y=175)
        label2=Label(root,text="Admin Id : ",font=("Times New Roman",18),background="skyblue")
        label2.place(x=493,y=320)
        entry1=Entry(root,width=22,font=("Times New Roman",18),textvariable=self.admId)
        entry1.place(x=610,y=320)
        label3=Label(root,text="Password : ",font=("Times New Roman",18),background="skyblue")
        label3.place(x=493,y=400)
        entry2=Entry(root,width=22,show='*',font=("Times New Roman",18),textvariable=self.admPwd)
        entry2.place(x=610,y=400)

    def Exit(self):
        root.destroy()
    
    def Reset(self):
        self.admId.set('')
        self.admPwd.set('')

    def Login(self):
        id=self.admId.get()
        pwd=self.admPwd.get()
        if(id=='admin' and pwd=='1234'):
            root.withdraw()
            os.system('AdminPanel.py')
            root.deiconify()
        elif(id=='' or pwd==''):
            messagebox.showerror("Error","All fields should be filled !")
        else:
            messagebox.showerror("Error","Invalid id or password !")
            self.admId.set('')
            self.admPwd.set('')
    
    def buttonArea(self):
        button1=Button(root,text="Back",width=5,height=1,font=("Times New Roman",16),background="red",foreground="white",cursor="hand2",command=self.Exit)
        button1.place(x=487,y=540)
        button2=Button(root,text="Reset",width=5,height=1,font=("Times New Roman",16),background="blue",foreground="white",cursor="hand2",command=self.Reset)
        button2.place(x=637,y=540)
        button3=Button(root,text="Login",width=5,height=1,font=("Times New Roman",16),background="green",foreground="white",cursor="hand2",command=self.Login)
        button3.place(x=787,y=540)

class EmpLogin:
    def __init__(self):
        self.empId=StringVar()
        self.empPwd=StringVar()

    def createFrame(self):
        frame1=Canvas(root,height=450,width=600,background="skyblue")
        frame1.place(x=380,y=150)
        frame2=Canvas(root,height=100,width=600,background="orange")
        frame2.place(x=380,y=150)
        frame3=Canvas(root,height=80,width=600,background="orange")
        frame3.place(x=380,y=520)

    def createForm(self):
        label1=Label(root,text="Login as Employee",font=("Times New Roman bold",30),background="orange",foreground="white")
        label1.place(x=520,y=175)
        label2=Label(root,text="Employee Id : ",font=("Times New Roman",18),background="skyblue")
        label2.place(x=465,y=320)
        entry1=Entry(root,width=22,font=("Times New Roman",18),textvariable=self.empId)
        entry1.place(x=610,y=320)
        label3=Label(root,text="Password : ",font=("Times New Roman",18),background="skyblue")
        label3.place(x=493,y=400)
        entry2=Entry(root,width=22,show='*',font=("Times New Roman",18),textvariable=self.empPwd)
        entry2.place(x=610,y=400)

    def Exit(self):
        root.destroy()

    def Reset(self):
        self.empId.set('')
        self.empPwd.set('')

    def Login(self):
        id=self.empId.get()
        pwd=self.empPwd.get()
        if(id=='employee' and pwd=='1234'):
            root.withdraw()
            os.system('Billdesk.py')
            root.deiconify()
        elif(id=='' or pwd==''):
            messagebox.showerror("Error","All fields should be filled !")
        else:
            messagebox.showerror("Error","Invalid id or password !")
            self.empId.set('')
            self.empPwd.set('')
    
    def buttonArea(self):
        button1=Button(root,text="Back",width=5,height=1,font=("Times New Roman",16),background="red",foreground="white",cursor="hand2",command=self.Exit)
        button1.place(x=487,y=540)
        button2=Button(root,text="Reset",width=5,height=1,font=("Times New Roman",16),background="blue",foreground="white",cursor="hand2",command=self.Reset)
        button2.place(x=637,y=540)
        button3=Button(root,text="Login",width=5,height=1,font=("Times New Roman",16),background="green",foreground="white",cursor="hand2",command=self.Login)
        button3.place(x=787,y=540)

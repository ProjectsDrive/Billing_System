from ast import Str
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

#For Tkinter
root=Tk()
root.geometry('1366x768')
root.resizable(0,0)
root.title('Billing System')
root.iconbitmap('./Images/icon.ico')

#Common tools
class Tools:
    def setBackground(self,address):
        self.bg=PhotoImage(file=address)
        label1=Label(root,image=self.bg)
        label1.place(x=0,y=0)
    def eventLoop(self):
        root.mainloop()   

#Main Page
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
    
#Admin Login Page
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
            self.admId.set('')
            self.admPwd.set('')
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
#Employee Login Page
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
            self.empId.set('')
            self.empPwd.set('')
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

#Billdesk
class Billdesk:
    def __init__(self):
        self.btnfont=15     #font size of button
        self.lffont=16      #font size of labelframe  
       
    def Heading(self):
        label1=Label(root,text="Billing System",font=("Georgia",30))
        label1.place(x=550,y=20)

    def logout(self):
        self.sure=messagebox.askyesno("Logout","Are you sure you want to logout ?")
        if self.sure:
            root.destroy()
    
    def AddLogoutBtn(self):
        button1=Button(root,text="Logout",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.logout)
        button1.place(x=25,y=25)
    
    def customerDetails(self):
        frame1=Frame(root,width=1320,height=100)
        frame1.place(x=20,y=100)
        lframe1=LabelFrame(frame1,width=1320,height=100,text="  Customer Details  ",font=("Times New Roman",self.lffont),padx=2,pady=3)
        lframe1.pack()
        #Customer name
        label1=Label(lframe1,text="Customer Name ",font=("Times new roman",15))
        label1.place(x=30,y=13)
        entry1=Entry(lframe1,font=("Times new roman",15),width=25)
        entry1.place(x=170,y=13)

        #Customer number
        label2=Label(lframe1,text="Customer Number ",font=("Times new roman",15))
        label2.place(x=460,y=13)
        entry2=Entry(lframe1,font=("Times new roman",15),width=18)
        entry2.place(x=620,y=13)

        #Customer email
        label3=Label(lframe1,text="Customer Email ",font=("Times new roman",15))
        label3.place(x=860,y=13)
        entry3=Entry(lframe1,font=("Times new roman",15),width=25)
        entry3.place(x=1002,y=13)
    
    def products(self):
        frame1=Frame(root,height=420,width=600)
        frame1.place(x=20,y=210)
        lframe1=LabelFrame(frame1,height=420,width=600,text="  Products  ",font=("Times new roman",self.lffont))
        lframe1.pack()

        #Category
        label1=Label(lframe1,text="Select Category ",font=("Times new roman",15))
        label1.place(x=30,y=20)
        entry1=ttk.Combobox(lframe1,font=("Times new roman",15),width=25)
        entry1.place(x=170,y=20)
        entry1['values']=('C1','C2','C3')

        #Product
        label2=Label(lframe1,text="Select Product ",font=("Times new roman",15))
        label2.place(x=30,y=80)
        entry2=ttk.Combobox(lframe1,font=("Times new roman",15),width=25)
        entry2.place(x=170,y=80)
        entry2['values']=('P1','P2','P3')

        #Quantity
        label3=Label(lframe1,text="Quantity ",font=("Times new roman",15))
        label3.place(x=30,y=140)
        entry3=Entry(lframe1,font=("Times new roman",15),width=5)
        entry3.place(x=170,y=140)

        #Price
        label4=Label(lframe1,text="Price ",font=("Times new roman",15))
        label4.place(x=30,y=200)
        entry4=Entry(lframe1,font=("Times new roman",15),width=8)
        entry4.place(x=170,y=200)

        #Individual Total
        label5=Label(lframe1,text="Total ",font=("Times new roman",15))
        label5.place(x=30,y=260)
        entry5=Entry(lframe1,font=("Times new roman",15),width=8)
        entry5.place(x=170,y=260)

        #Add to Cart Btn
        button1=Button(lframe1,text="Add to Cart",width=10,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button1.place(x=100,y=320)

        #Remove Item Btn
        button2=Button(lframe1,text="Remove",width=7,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button2.place(x=270,y=320)

        #Clear individual item Btn
        button3=Button(lframe1,text="Clear",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button3.place(x=410,y=320)
    
    def billOption(self):
        frame1=Frame(root,height=104,width=600)
        frame1.place(x=20,y=640)
        lframe1=LabelFrame(frame1,height=104,width=600,text="  Bill Options  ",font=("Times new roman",self.lffont))
        lframe1.pack()

        #Grand Total Btn
        button1=Button(lframe1,text="Total",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button1.place(x=100,y=10)

        #Generate Bill Btn
        button2=Button(lframe1,text="Generate",width=7,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button2.place(x=200,y=10)

        #Clear Bill Btn
        button3=Button(lframe1,text="Clear",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button3.place(x=320,y=10)
        button4=Button(lframe1,text="Exit",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        button4.place(x=420,y=10)

    def billWindow(self):
        frame1=Frame(root,height=535,width=700,background="Yellow")
        frame1.place(x=630,y=210)
        lframe1=LabelFrame(frame1,height=535,width=700,text="  Bill Window  ",font=("Times new roman",self.lffont))
        lframe1.pack()

        #For Searching a bill
        label1=Label(lframe1,text="Bill Number ",font=("Times new roman",15))
        label1.place(x=30,y=13)
        entry1=Entry(lframe1,font=("Times new roman",15))
        entry1.place(x=140,y=13)
        button1=Button(lframe1,text="Search",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.logout)
        button1.place(x=330,y=5)

        #Bill Preview
        frame2=Frame(lframe1,height=456,width=696)
        frame2.place(x=0,y=52)
        lframe2=LabelFrame(frame2,height=456,width=696)
        lframe2.pack()
        
    
        
        
from ast import Str
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import tempfile
from unicodedata import category

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
            self.admPwd.set('')
            self.admId.set('')           
    
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

#Print Bill
class Print_Bill:
    def __init__(self):
        root=Tk()
        root.geometry('500x1000')
        root.resizable(0,0)
        root.title('Bill')
        root.iconbitmap('./Images/icon.ico')
        self.frame1=Canvas(root,height=1000,width=500,background="white")
        self.frame1.place(x=1,y=1)
        comName=Label(self.frame1,text='Company name',font=('Times new roman bold',20),background='white')
        comName.place(x=150,y=10)   
        btn=Button(self.frame1,text='Print',command=self.printBill)
        btn.place(x=450,y=25)
        comAddr=Label(self.frame1,text='Sarat Chandra Pally, Haiderpara, Siliguri-734006',font=('Times new roman',12),background='white')
        comAddr.place(x=90,y=50)  
        comPh=Label(self.frame1,text='Ph no. : ',font=('Times new roman',12),background='white')
        comPh.place(x=160,y=75)  
        comPhNo=Label(self.frame1,text='+917384599719',font=('Times new roman',12),background='white')
        comPhNo.place(x=210,y=75)  
        title=Label(self.frame1,text='**Tax Invoice**',font=('Times new roman bold',15),background='white')
        title.place(x=170,y=100)
        billId=Label(self.frame1,text='Bill Id : ',font=('Times new roman',12),background='white')
        billId.place(x=30,y=130)
        billIdNo=Label(self.frame1,text='B001 ',font=('Times new roman',12),background='white')
        billIdNo.place(x=80,y=130)
        date=Label(self.frame1,text='31-12-2021 ',font=('Times new roman',12),background='white')
        date.place(x=280,y=130)
        time=Label(self.frame1,text='10:35:49 PM ',font=('Times new roman',12),background='white')
        time.place(x=380,y=130)
        billTo=Label(self.frame1,text='Bill to - ',font=('Times new roman bold',14),background='white')
        billTo.place(x=30,y=160)
        cName=Label(self.frame1,text='Mr. Arup Paul ',font=('Times new roman',12),background='white')
        cName.place(x=50,y=190)
        cAddr=Label(self.frame1,text='Haiderpara, Siliguri, 734006 ',font=('Times new roman',12),background='white')
        cAddr.place(x=50,y=210)
        cPh=Label(self.frame1,text='Ph : ',font=('Times new roman',12),background='white')
        cPh.place(x=50,y=231)
        cPh=Label(self.frame1,text='9832371225',font=('Times new roman',12),background='white')
        cPh.place(x=80,y=231)
        label1=Label(self.frame1,text="Sl.",font=("Times new roman bold",12),background='white')
        label1.place(x=45,y=265)
        label2=Label(self.frame1,text="Category",font=("Times new roman bold",12),background='white')
        label2.place(x=95,y=265)
        label2=Label(self.frame1,text="Item",font=("Times new roman bold",12),background='white')
        label2.place(x=185,y=265)
        label4=Label(self.frame1,text="Qty",font=("Times new roman bold",12),background='white')
        label4.place(x=275,y=265)
        label5=Label(self.frame1,text="Rate",font=("Times new roman bold",12),background='white')
        label5.place(x=335,y=265)
        label6=Label(self.frame1,text="Amt",font=("Times new roman bold",12),background='white')
        label6.place(x=415,y=265) 
        label7=Label(self.frame1,text="---------------------------------------------------------------------------------",background='white')
        label7.place(x=40,y=287)
        #Items
        for i in range(1,16):
            label=Label(self.frame1,text=i,font=("Times new roman",10),background='white')
            label.place(x=45,y=295+23*i)
        label8=Label(self.frame1,text="---------------------------------------------------------------------------------",background='white')
        label8.place(x=50,y=675)
        label9=Label(self.frame1,text="Total : ",font=("Times new roman bold",12),background='white')
        label9.place(x=70,y=695)
        label10=Label(self.frame1,text="00000.00 ",font=("Times new roman bold",12),background='white')
        label10.place(x=120,y=695)
        label11=Label(self.frame1,text="Particular : ",font=("Times new roman bold",12),background='white')
        label11.place(x=290,y=695)
        label12=Label(self.frame1,text="Cash",font=("Times new roman bold",12),background='white')
        label12.place(x=370,y=695)
        endlabel=Label(self.frame1,text='***Thank you, Visit again***',font=('Times new roman bold',12),background='white')
        endlabel.place(x=140,y=730)
        root.mainloop()
    def printBill(self):
        pass

#Billdesk
class Billdesk:
    def __init__(self):
        self.btnfont=15     #font size of button
        self.lffont=16      #font size of labelframe 
        self.i=0
        self.j=1
        self.category=StringVar()
        self.product=StringVar()
        self.quantity=StringVar()
        self.price=StringVar()
        self.particular=StringVar()
        self.productList=[]
        #to remove item
        self.sl=StringVar()
        self.total()
       
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
        frame1=Frame(root,width=600,height=220)
        frame1.place(x=20,y=100)
        lframe1=LabelFrame(frame1,width=600,height=220,text="  Customer Details  ",font=("Times New Roman",self.lffont),padx=2,pady=3)
        lframe1.pack()
        #Customer name
        label1=Label(lframe1,text="Customer Name ",font=("Times new roman",15))
        label1.place(x=30,y=13)
        entry1=Entry(lframe1,font=("Times new roman",15),width=25)
        entry1.place(x=200,y=13)

        #Customer number
        label2=Label(lframe1,text="Customer Number ",font=("Times new roman",15))
        label2.place(x=30,y=55)
        entry2=Entry(lframe1,font=("Times new roman",15),width=18)
        entry2.place(x=200,y=55)

        #Customer email
        label3=Label(lframe1,text="Customer Email ",font=("Times new roman",15))
        label3.place(x=30,y=95)
        entry3=Entry(lframe1,font=("Times new roman",15),width=25)
        entry3.place(x=200,y=95)

        #Customer address
        label4=Label(lframe1,text="Customer Address ",font=("Times new roman",15))
        label4.place(x=30,y=135)
        entry4=Entry(lframe1,font=("Times new roman",15),width=30)
        entry4.place(x=200,y=135)
    
    def addToCart(self):
        l=self.productList
        category=self.category.get()
        product=self.product.get()
        qty=self.quantity.get()
        price=self.price.get()
        if(category!='' and product!='' and qty!='' and price!=''):
            self.i+=1
            i=self.i
            if len(self.productList)<15:
                category=self.category.get()
                product=self.product.get()
                qty=int(self.quantity.get())
                price=int(self.price.get())
                total=qty*price
                productDict={'Sl':len(l)+1,'cat':category,'pro':product,'qty':qty,'price':price,'tot':total}
                self.productList.append(productDict)
                #print(self.productList)
                self.show()
            else:
                messagebox.showwarning("Overflow","Can\'t add new item")
            self.total()
            self.clr()
        else:
            messagebox.showwarning("Invalid","No item to add")
      
    def show(self):
        l=self.productList
        frame=Frame(root,height=402,width=696,background="white")
        frame.place(x=631,y=177)   
        for x in l:
            label1=Label(root,text=x['Sl'],font=('Times new roman',14),anchor='w',background="white")
            label1.place(x=670,y=152+25*x['Sl'])
            label2=Label(root,text=x['cat'],font=('Times new roman',14),width=25,anchor='w',background="white")
            label2.place(x=780,y=152+25*x['Sl'])
            label3=Label(root,text=x['pro'],font=('Times new roman',14),width=25,anchor='w',background="white")
            label3.place(x=930,y=152+25*x['Sl'])
            label4=Label(root,text=x['qty'],font=('Times new roman',14),width=3,anchor='w',background="white")
            label4.place(x=1055,y=152+25*x['Sl'])
            label5=Label(root,text=x['price'],font=('Times new roman',14),width=5,anchor='w',background="white")
            label5.place(x=1130,y=152+25*x['Sl'])
            label6=Label(root,text=x['tot'],font=('Times new roman',14),width=6,anchor='w',background="white")
            label6.place(x=1230,y=152+25*x['Sl'])

    def clr(self):
        self.price.set('')
        self.quantity.set('')
        self.product.set('')
        self.category.set('')
        self.particular.set('')
    
  

    def products(self):
        frame1=Frame(root,height=340,width=600)
        frame1.place(x=20,y=323)
        lframe1=LabelFrame(frame1,height=340,width=600,text="  Products  ",font=("Times new roman",self.lffont))
        lframe1.pack()

        #Category
        my_list=[]
        def change(*args):
            if(self.category.get()=="Chocolate"):
                my_list.clear()
                l=['Dairy Milk','Kit kat','5 Star','Snickers']
                my_list.extend(l)
                entry2['values']=my_list
            elif(self.category.get()=="Biscuit"):
                my_list.clear()
                l=['Good Day','Bourbon','Oreo','Marie']
                my_list.extend(l)
                entry2['values']=my_list
            elif(self.category.get()=="Soap"):
                my_list.clear()
                l=['Dettol','Lifebuoy','Sinthol','Lux','Savnol']
                my_list.extend(l)
                entry2['values']=my_list
            elif(self.category.get()=="Snacks"):
                my_list.clear()
                l=['Lays','Kurkure','Uncle Chips']
                my_list.extend(l)
                entry2['values']=my_list
            elif(self.category.get()==""):
                my_list.clear()
                entry2['values']=my_list
        label1=Label(lframe1,text="Select Category ",font=("Times new roman",15))
        label1.place(x=30,y=20)
        entry1=ttk.Combobox(lframe1,font=("Times new roman",15),width=25,textvariable=self.category)
        entry1.place(x=170,y=20)
        entry1['values']=('','Chocolate','Biscuit','Soap','Snacks')
        self.category.trace("w",change)

        #Product
        pricelist={'':'0','Dairy Milk':'30','Kit kat':'20','5 Star':'25','Snickers':'25','Good Day':'30','Bourbon':'40','Oreo':'50','Marie':'30','Dettol':'10','Lifebuoy':'10','Sinthol':'12','Lux':'20','Savnol':'15','Lays':'20','Kurkure':'20','Uncle Chips':'20'}
        def setPrice(*args):
            self.price.set(pricelist[self.product.get()])
        label2=Label(lframe1,text="Select Product ",font=("Times new roman",15))
        label2.place(x=30,y=80)
        entry2=ttk.Combobox(lframe1,values=my_list,font=("Times new roman",15),width=25,textvariable=self.product)
        entry2.place(x=170,y=80)
        self.product.trace('w',setPrice)

        #Quantity
        label3=Label(lframe1,text="Quantity ",font=("Times new roman",15))
        label3.place(x=30,y=140)
        entry3=Entry(lframe1,font=("Times new roman",15),width=5,textvariable=self.quantity)
        entry3.place(x=170,y=140)

        #Price
        label4=Label(lframe1,text="Rate ",font=("Times new roman",15))
        label4.place(x=30,y=200)
        entry4=Entry(lframe1,font=("Times new roman",15),width=8,textvariable=self.price)
        entry4.place(x=170,y=200)

        #Add to Cart Btn
        button1=Button(lframe1,text="Add to Cart",width=10,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.addToCart)
        button1.place(x=170,y=250)

        #Edit Btn
        #button1=Button(lframe1,text="Edit",width=10,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.addToCart)
        #button1.place(x=70,y=320)

        #Remove Item Btn
        #button2=Button(lframe1,text="Remove",width=7,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2")
        #button2.place(x=270,y=320)

        #Clear individual item Btn
        button3=Button(lframe1,text="Clear",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.clr)
        button3.place(x=320,y=250)
    
    def payment(self):
        frame1=Frame(root,height=65,width=600)
        frame1.place(x=20,y=670)
        lframe1=LabelFrame(frame1,height=65,width=600,text="  Payment Method  ",font=("Times new roman",self.lffont))
        lframe1.pack()
        label1=Label(lframe1,text="Particular",font=("Times New Roman",self.btnfont))
        label1.place(x=15,y=5)
        entry1=ttk.Combobox(lframe1,font=("Times new roman",15),width=25,textvariable=self.particular)
        entry1.place(x=170,y=5)
        entry1['values']=('Cash','Cheque','Net Banking','UPI','Debit Card','Credit Card')


    def total(self):
        tot=0
        for x in self.productList:
            tot=tot+x['tot']
        frame1=Frame(root,height=73,width=600)
        frame1.place(x=630,y=590)
        lframe1=LabelFrame(frame1,height=73,width=700,text="",font=("Times new roman",self.lffont))
        lframe1.pack()
        label1=Label(lframe1,text="Grand Total : ",font=('Times new roman bold',18))
        label1.place(x=10,y=15)
        label2=Label(lframe1,text=tot,font=('Times new roman bold',20),foreground="red",width=6,anchor="w")
        label2.place(x=180,y=12)

    def remove(self):
        sl=StringVar()
        def removeItem():
            l=self.productList
            s=int(entry1.get())
            if(s<=len(l)):
                del l[s-1]
                for x in range(s-1,len(l)):
                    i=l[x]['Sl']
                    #print(x)
                    l[x]['Sl']=i-1
                #print(self.productList)
                messagebox.showinfo("Successful","Item removed successfully")
                self.show()
                self.total()
            else:
                messagebox.showwarning("Invalid","Item not found")
            root.withdraw()
        if(len(self.productList)>0):
            root=Tk()
            root.geometry('350x150')
            root.title("Remove item")
            root.iconbitmap('./Images/icon.ico')
            
            label1=Label(root,text="Enter Sl. No. of the product ",font=('Times new Roman',15))
            label1.place(x=20,y=20)
            entry1=Entry(root,width=5,font=('Times new Roman',15),textvariable=sl)
            entry1.place(x=250,y=20)
            button1=Button(root,text="Remove",background="red",foreground="white",font=('Times new Roman',13),command=removeItem)
            button1.place(x=140,y=60)
            root.mainloop()
        else:
            messagebox.showwarning("Empty","No item to remove")
    
    def clear(self):
        sure=messagebox.askyesno("Clear","Are you sure you want to clear the billdesk ?")
        if(sure):
            self.productList.clear()
            self.clr()
            self.show()
            self.total()

    def edit(self):
        messagebox.showinfo("Under Construction","Coming Soon")

    


    def generate(self):
        def print_bill():
            q=self.textarea.get('1.0','end-1c')
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,'Print')
        self.root=Tk()
        self.root.geometry('500x550')
        self.root.resizable(0,0)
        self.root.title('Bill')
        self.root.iconbitmap('./Images/icon.ico')
        self.frame1=Frame(self.root,width=500,height=5000,background="white")
        self.frame1.place(x=0,y=0)
        self.frame2=Frame(self.root,width=500,height=50,background='white')
        self.frame2.place(x=0,y=450)
        self.textarea=Text(self.frame1)
        self.textarea.place(x=0,y=0)
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,'Company Name\n')
        self.textarea.insert(END,'Company Address\n')
        self.textarea.insert(END,'Ph No. : +91 **********\n')
        self.textarea.insert(END,'\nBill to --\n')
        self.textarea.insert(END,'Customer name \n')
        self.textarea.insert(END,'Customer address\n')
        self.textarea.insert(END,'Customer Ph. No. : +91 **********\n')
        self.textarea.insert(END,'\nSl.   Category\t\t  Product\t\tRate  \tQty\t  Amt\n')
        self.textarea.insert(END,'---------------------------------------------------------------------------\n')
        for x in self.productList:
            sl=x['Sl']
            category=x['cat']
            product=x['pro']
            rate=x['price']
            qty=x['qty']
            amt=x['tot']
            self.textarea.insert(END,' ')
            self.textarea.insert(END,sl)
            self.textarea.insert(END,'   ')
            self.textarea.insert(END,category)
            self.textarea.insert(END,'\t\t')
            self.textarea.insert(END,product)
            self.textarea.insert(END,'\t\t')
            self.textarea.insert(END,rate)
            self.textarea.insert(END,'  \t')
            self.textarea.insert(END,qty)
            self.textarea.insert(END,'\t  ')
            self.textarea.insert(END,amt)
            self.textarea.insert(END,'\n')
        self.btn=Button(self.frame2,text="Print",command=print_bill)
        self.btn.place(x=20,y=15)
    def billOption(self):
        frame1=Frame(root,height=65,width=700)
        frame1.place(x=630,y=670)
        lframe1=LabelFrame(frame1,height=65,width=700,text="",font=("Times new roman",self.lffont))
        lframe1.pack()

        #Generate Bill Btn
        button2=Button(lframe1,text="Generate",width=7,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.generate)
        button2.place(x=130,y=10)

        #Edit bills
        button3=Button(lframe1,text="Edit",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.edit)
        button3.place(x=250,y=10)

        #Remove Bill Btn
        button4=Button(lframe1,text="Remove",width=7,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.remove)
        button4.place(x=350,y=10)

        #clear button
        button5=Button(lframe1,text="Clear",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.clear)
        button5.place(x=470,y=10)

    def cart(self):
        frame1=Frame(root,height=482,width=700)
        frame1.place(x=630,y=100)
        lframe1=LabelFrame(frame1,height=482,width=700,text="  Items Added  ",font=("Times new roman",self.lffont))
        lframe1.pack()
        '''
        #For Searching a bill
        label1=Label(lframe1,text="Bill Number ",font=("Times new roman",15))
        label1.place(x=30,y=13)
        entry1=Entry(lframe1,font=("Times new roman",15))
        entry1.place(x=140,y=13)
        button1=Button(lframe1,text="Search",width=5,height=1,font=("Times New Roman",self.btnfont),background="red",foreground="white",cursor="hand2",command=self.logout)
        button1.place(x=330,y=5)
        '''
        
        #Items added
        frame2=Frame(lframe1,height=400,width=696)
        frame2.place(x=0,y=17)
        label=Label(frame2,text="\t\t\t\t\t\t\t\t         ",font=("Times new roman bold",15),background="black")
        label.place(x=1,y=5)
        label=Label(frame2,text="\t\t\t\t\t\t\t\t         ",font=("Times new roman bold",15))
        label.place(x=1,y=4)
        label1=Label(frame2,text="Sl. No.",font=("Times new roman bold",15))
        label1.place(x=30,y=2)
        label2=Label(frame2,text="Category",font=("Times new roman bold",15))
        label2.place(x=150,y=2)
        label3=Label(frame2,text="Product",font=("Times new roman bold",15))
        label3.place(x=300,y=2)
        label4=Label(frame2,text="Qty",font=("Times new roman bold",15))
        label4.place(x=420,y=2)
        label5=Label(frame2,text="Rate",font=("Times new roman bold",15))
        label5.place(x=500,y=2)
        label6=Label(frame2,text="Amount",font=("Times new roman bold",15))
        label6.place(x=600,y=2)  
        frame=Frame(root,height=402,width=696,background="white")
        frame.place(x=631,y=177)              
    
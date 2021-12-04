from tkinter import font
from BillingModule import *
from tkinter import *
billing=AdmLogin()
tools=Tools()
tools.setBackground("./Images/bg2.png")
billing.createFrame()
billing.createForm()
billing.buttonArea()
tools.eventLoop()
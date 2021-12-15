from BillingModule import *
billing=MainPage()
tools=Tools()
tools.setBackground("./Images/bg1.png")
billing.displayLabel(110,200)
billing.addAdminBtn(150,320)
billing.addEmployeeBtn(150,420)
tools.eventLoop()


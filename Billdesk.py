from BillingModule import *
tools=Tools()
bd=Billdesk()
bd.Heading()
bd.AddLogoutBtn()
bd.customerDetails()
bd.products()
bd.total()
bd.billOption()
bd.cart()

tools.eventLoop()
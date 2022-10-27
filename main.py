from email.mime import application
import numbers
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
import random 
import datetime
import time




class Train:
     def __init__(self, root , ):
        self.root = root
        self.root.title =("Advanced Train Ticketing System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')
        
        MainFrame = Frame (self.root ,bd=10, width =1350, height=700, bg="gainsboro" ,relief=RIDGE)
        MainFrame.grid()
        
        TopFramel = Frame (MainFrame ,bd=10, width =1340, height=100, bg="gainsboro" ,relief=RIDGE)
        TopFramel.grid()
        
        TopFrame2 = Frame (MainFrame ,bd=10, width =1300, height=500, bg="gainsboro" ,relief=RIDGE)
        TopFrame2.grid()
        
        fl = Frame(TopFrame2, width = 890,height = 500, bd=5, relief=RIDGE)
        fl.grid (row=1, column=0)
        
        f2 = Frame (TopFrame2, width =  400, height =  500, pady=2, bd=5, relief=RIDGE)
        f2.grid(row=1, column=1)

        frametopRight = Frame (f2, width = 404,height = 420, bd=5, relief=RIDGE) #Ticketing Receipt
        frametopRight.pack (side=TOP)

        frameBottomRight = Frame (f2, width =408,height  = 100, bd=5, pady=15, relief=RIDGE) # Buttons pady=10
        frameBottomRight.pack (side=BOTTOM)

        fla = Frame (fl, width = 900,height = 330, bd=5, relief=RIDGE)
        fla.pack (side=TOP)

        f2a = Frame (fl, width = 900,height = 320, bd=5, relief=RIDGE)
        f2a.pack (side=BOTTOM)

        topleftl = Frame (fla, width= 300,height = 200, bd=5,padx=20, pady=1, relief=RIDGE)
        topleftl.pack (side=LEFT)

        topLeft2 = Frame (fla, width = 300,height =  200, bd=5, relief=RIDGE)
        topLeft2.pack (side=RIGHT)

        topleft3 = Frame (fla, width  = 300,height = 200, bd=5, pady=5, relief=RIDGE)
        topleft3.pack (side=RIGHT)

        bottomLeft1 = Frame (f2a, width = 450,height =300, bd=5,pady=12, relief=RIDGE) #Frame For Tax, SubTotal and Total
        bottomLeft1.pack (side=LEFT)

        bottomLeft2 = Frame (f2a, width = 450,height  = 300, bd=5, relief=RIDGE) # Frame For Calculator
        bottomLeft2.pack (side=RIGHT)
#===================================================================================================================================================================
        lblTitle = Label(TopFramel, font=('arial',40, "bold"),text="Train Ticketing Booking",bd=5, width = 41,padx=4, justify='center')
        lblTitle. grid (row=0, column=0)
#===================================================================================================================================================================

        Date1 = StringVar ()
        time1 = StringVar ()
        Ticketclass = StringVar  ()
        TicketPrice = StringVar()
        Child_Ticket = StringVar()
        Adult_Ticket = StringVar ()
        From_Destination = StringVar ()
        To_Destination = StringVar ()        
        Fee_Price = StringVar ()
        Route= StringVar ()
        Receipt_Ref =StringVar ()
        text_Input = StringVar ()
        global operator
        operator= " "
        Ticketclass.set ("")
        TicketPrice.set ("")
        Child_Ticket.set ("")
        Adult_Ticket.set ("")
        From_Destination.set("")
        To_Destination.set("")
        Fee_Price.set("")
        Route.set("")
        Receipt_Ref.set("")


        var1 = IntVar () 
        var2 = IntVar ()
        var3 = IntVar ()
        var4 = IntVar ()
        var5 = IntVar ()
        var6 = StringVar ()
        var7 = StringVar ()
        var8 =StringVar ()
        var9 = StringVar ()
        var10 = IntVar ()
        var1l = IntVar ()
        var12 = IntVar ()


        Tax  = StringVar ()
        SubTotal = StringVar()
        Total = StringVar  ()

        var1.set ("0")
        var2.set ("0")
        var3.set ("0")
        var4.set ("0")
        var5.set ("0")
        var6.set ("0")
        var7.set ("0")
        var8.set ("0")
        var9.set ("0")
        var10.set ("0")
        var1l.set ("0")
        Tax .set("0")
        SubTotal.set("0")
        Total.set("0")     

#================================================================Functions==============================================================================================        
        def iExit ():
                iExit =mb.askyesno ("Train Ticketing System", "Confirm if you want to quit")
                if iExit > 0:
                        root.destroy ()
                        return
        def Reset():
                var1.set ("0")
                var2.set ("0")
                var3.set ("0")
                var4.set ("0")
                var5.set ("0")
                var6.set ("0")
                var7.set ("0")
                var8.set ("0")
                var9.set ("0")
                var10.set ("0")
                var1l.set ("0")
                Tax .set("0")
                SubTotal.set("0")
                Total.set("0")     
                Ticketclass.set ("")
                TicketPrice.set ("")
                Child_Ticket.set ("")
                Adult_Ticket.set ("")
                From_Destination.set("")
                To_Destination.set("")
                Fee_Price.set("")
                Route.set("")
                Receipt_Ref.set("")


        def btnClick(numbers):
                global operator
                operator = operator + str(numbers)
                text_Input.set(operator)


        def btncleardisp():
                global operator
                operator = ' '
                text_Input.set(operator)

        def benEqualsinput ():
                global operator
                sumup = str (eval (operator) )
                text_Input.set (sumup)
                operator = ""
        def Travel_Cost():
                if (var9.get()=="Thiruvallur" and var1.get() == 1 and var4.get() == 1):
                        Tcost = float (45.50)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("Standard")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)

                elif (var9.get()=="Chennai" and var1.get() == 1 and var5.get() == 1):
                        Tcost = float (50.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("Standard")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)                    


                elif (var9.get()=="Egmore" and var1.get() == 1 and var4.get() == 1):
                        Tcost = float (80.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("Standard")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      

                elif (var9.get()=="Thiruvallur" and var2.get() == 1 and var5.get() == 1):
                        Tcost = float (450.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("Economy")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      

                elif (var9.get()=="Chennai" and var2.get() == 1 and var4.get() == 1):
                        Tcost = float (500.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("Economy")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      


                elif (var9.get()=="Egmore" and var2.get() == 1 and var5.get() == 1):
                        Tcost = float (650.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("Economy")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      


                elif (var9.get()=="Thiruvallur" and var3.get() == 1 and var5.get() == 1):
                        Tcost = float (1450.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("First Class")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      

                elif (var9.get()=="Chennai" and var3.get() == 1 and var5.get() == 1):
                        Tcost = float (1500.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("First Class")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      


                elif (var9.get()=="Egmore" and var3.get() == 1 and var5.get() == 1):
                        Tcost = float (1650.75)
                        Single = float (var12.get())
                        Adult_Tax ="₹", str('%2.f'%((Tcost * Single) *90))
                        Adult_Fees ="₹", str('%2.f'%( (Tcost * Single)))
                        TotalCost = "₹", str ((Tcost * Single)+ ((Tcost * Single)*90.90))
                        Tax. set (Adult_Tax)
                        SubTotal. set (Adult_Fees)                        
                        Ticketclass.set ("First Class")
                        TicketPrice.set (Adult_Fees)
                        Child_Ticket.set ("No")
                        Adult_Ticket.set ("Yes")
                        From_Destination. set ("kannyakunari")
                        To_Destination. set ("Thiruvallur")
                        Fee_Price.set (TotalCost)
                        Total. set (TotalCost)
                        Route. set ("Direct")

                        

                        x = random.randint (109, 5876)
                        randomRef = str (x)
                        Receipt_Ref.set("TFL"+ randomRef)      

 

        def chkSbutton_value():

                if (var4.get() == 1):
                        var12.set("")
                        entSingle.focus()
                        entSingle.configure(state= NORMAL)
                        var5.set (0)
                        entSingle.configure(state= DISABLED)
                        var6.set (0)
                elif var4.get()== 0:
                         entSingle.configure(state= DISABLED)
                         var12.set(0)

        

 
        def chkRbutton_value():

                if (var5.get() == 1):
                        var6.set("")
                        entReturn.focus ()
                        entReturn.configure(state= NORMAL)
                        var4.set (0)
                elif var5.get()==0:
                        entReturn.configure(state= DISABLED)
                        var6.set (0)
 



#================================================================Lables==============================================================================================        
        lblReceipt=Label (frametopRight, font= ('arial',18,'bold'),text="Travelling Ticketing Systems",bd=5, pady=10, padx=4, width=28, justify='center')
        lblReceipt.grid (row=0, column=0)

        lblClassl=Label (frameBottomRight, font=('arial',14, 'bold'),text="Class", width = 8,relief = 'sunken',justify='center')
        lblClassl.grid (row=0, column=0)

        lblClass2=Label (frameBottomRight, font=("arial",14, 'bold'), width = 8,relief = 'sunken',textvariable=Ticketclass, justify='center')
        lblClass2.grid (row=1, column=0)

        lblTicketl=Label (frameBottomRight, font=('arial',14, "bold"),text="Ticket",width= 8,relief = 'sunken', justify='center')
        lblTicketl.grid (row=0, column=1)
        
        lblTicket2=Label (frameBottomRight, font=('arial',14, 'bold'), width = 8,relief = 'sunken',textvariable=TicketPrice, justify='center')
        lblTicket2.grid (row=1, column=1)

        lblAdultl=Label (frameBottomRight, font=('arial',14, 'bold'),text='Adult',width =8,relief = 'sunken',justify='center')
        lblAdultl.grid (row=0, column=2)
        
        lblAdult2=Label (frameBottomRight, font=('arial',14, 'bold'), width = 8,relief = 'sunken',textvariable=Adult_Ticket ,justify='center')
        lblAdult2.grid (row=1, column=2)

        lblChildl=Label (frameBottomRight, font=('arial',14, "bold"),text="Child",width = 8,relief = 'sunken',justify='center')
        lblChildl.grid (row=0, column=3)

        lblChild2=Label (frameBottomRight, font=('arial',14, 'bold'), width = 8,relief = 'sunken',textvariable=Child_Ticket ,justify='center')
        lblChild2.grid(row=1, column=3)

#=================================================================================================================================================================
        lb1sp=Label (frameBottomRight, font= ('arial',14, 'bold'),width = 36,height=2, relief ='sunken',justify = 'center',bg='lightgrey')
        lb1sp.grid (row=2, column=0, columnspan=4) # Space bar
#=================================================================================================================================================================
        lblFroml=Label (frameBottomRight, font= ('arial',14, 'bold'),text="From",width = 8,relief ='sunken', justify= 'center')
        lblFroml.grid (row=3, column=1)

        lblFrom2=Label (frameBottomRight, font=('arial',14, 'bold'), width = 8,relief = 'sunken',textvariable=From_Destination, justify='center')
        lblFrom2.grid (row=3, column=2)
#=================================================================================================================================================================
        lb1To1=Label (frameBottomRight, font=('arial',14,'bold'),text="To",width = 8,relief ='sunken', justify= 'center')
        lb1To1.grid (row=4, column=1)

        lblTo2=Label (frameBottomRight, font=('arial',14, 'bold'), width = 8,relief = 'sunken',textvariable=To_Destination, justify='center')
        lblTo2.grid (row=4, column=2)

        lblPricel=Label (frameBottomRight, font=('arial',14, 'bold'),text="Price",width = 8,relief = 'sunken' , justify='center')
        lblPricel.grid (row=5, column=1)

        lblPrice2=Label (frameBottomRight, font = ('arial',14, 'bold'), justify='center')
        lblPrice2.grid (row=5,column=2)

#=================================================================================================================================================================        

        lb1sp=Label (frameBottomRight, font= ('arial',14, 'bold'),width = 36,height=2, relief ='sunken',justify = 'center',bg='lightgrey')
        lb1sp.grid (row=6, column=0, columnspan=4) # Space bar


#=================================================================================================================================================================
        lblRefNo1=Label (frameBottomRight, font=('arial',14, 'bold'),text="Ref No", width  = 8,relief = 'sunken',justify='center')
        lblRefNo1.grid (row=7, column=0)

        lblRefNo2=Label (frameBottomRight, font= ('arial',14, 'bold'), width  = 8,relief = 'sunken', textvariable=Receipt_Ref,justify='center')
        lblRefNo2.grid (row=8, column=0)

        lblTime1=Label (frameBottomRight, font= ('arial',14, 'bold'),text="Time",width = 8,relief = 'sunken',justify='center')
        lblTime1.grid (row=7, column=1)

        lblTime2=Label (frameBottomRight, font=('arial',14, 'bold'), width = 8,relief = 'sunken',textvariable=time1,justify='center')
        lblTime2.grid (row=8, column=1)
                                                                        
        lblDate1=Label (frameBottomRight, font= ('arial',14, 'bold'),text="Date",width = 8,relief = 'sunken',justify='center')
        lblDate1.grid (row=7, column=2)

        lblDate2=Label (frameBottomRight, font=('arial',14, 'bold'), width  = 8 ,relief='sunken',textvariable= Date1 , justify='center')
        lblDate2.grid (row=8, column=2)

        lblRoute1=Label (frameBottomRight, font= ('arial',14, 'bold'),text="Route",width =  8,relief = 'sunken' ,justify='center')
        lblRoute1.grid (row=7, column=3)

        lblRoute2=Label (frameBottomRight, font= ('arial',14, 'bold'), width = 8,relief= 'sunken',textvariable=Route, justify='center')
        lblRoute2.grid (row=8, column=3)

#=================================================================================================================================================================        

        btnTotal = Button (frameBottomRight, font=('arial',14, 'bold'),text="Total", width = 8, height=1, padx=2, pady=16, bd =2,command=Travel_Cost)
        btnTotal.grid (row=10, column=0)

        btnClear = Button (frameBottomRight, font=('arial',14, 'bold'),text="Clear", width = 8, height=1, padx=2, pady=16, bd =2)
        btnClear.grid (row=10, column=1)

        btnReset = Button (frameBottomRight, font=('arial',14, "bold"),text="Reset", width = 8, height=1, padx=2, pady=16, bd =2,command=Reset)
        btnReset.grid (row=10, column=2)

        btnExit = Button (frameBottomRight, font=('arial',14, "bold"), text="Exit", width = 8, height=1, padx=2, pady=16, bd =2,command=iExit)
        btnExit.grid(row=10, column=3)


#=================================================================================================================================================================
        Date1.set (time.strftime("%d/%m/%Y")) # date
        time1.set (time.strftime("%H:%M:%S")) # time
#=================================================================================================================================================================

        lblClass = Label (topleftl, font=('arial',20, "bold") , text="Class", bd=8).grid(row =0, column = 0, sticky = W)

        chkStandard = Checkbutton (topleftl, font=('arial',20, "bold"),text="Standard", variable = var1, onvalue =1, offvalue =0).grid(row =1, column =0, sticky =W)

        chkEconomy = Checkbutton (topleftl, font=('arial',20, "bold"),text="Economy", variable = var2, onvalue =1, offvalue =0).grid(row =2, column =0, sticky =W)

        chkFirstClass= Checkbutton (topleftl, font=('arial',20, "bold"),text="First Class", variable = var3, onvalue =1, offvalue =0).grid (row =3, column =0, sticky =W)


#=================================================================================================================================================================
        lblSelect = Label (topleft3, font= ('arial',20, "bold"),text="Select Destination", bd=8) .grid(row =0, column =0, sticky =W,columnspan=2)

        lblDestination= Label (topleft3, font=('arial',20, "bold"),text="Destination", bd=8) .grid(row =1, column =0, sticky =W)

        cboDestination =ttk.Combobox (topleft3, textvariable = var9, font=('arial',20, "bold"), state ='readonly', width=8)

        cboDestination['value']= ( ' ','Thiruvallur','Chennai', 'Egmore')
        cboDestination.current (0)
        cboDestination.grid(row =1, column =1)

        chkAdult = Checkbutton (topleft3, font= ('arial',20, "bold"),text='Adult', variable = var4, onvalue =1, offvalue =0).grid(row =2, column =0, sticky =W)

        chkChild = Checkbutton (topleft3, font=('arial',20, "bold"),text='Child', variable = var5, onvalue =1, offvalue =0).grid(row =3, column =0, sticky =W)

#=================================================================================================================================================================
        lblTicketType = Label (topLeft2, font=('arial',20, 'bold'),text="Ticket Type", bd=8) .grid(row =0,column =0, sticky =W)

        chkSingle = Checkbutton (topLeft2, font=('arial',20, 'bold'),text="Single", variable = var4, onvalue = 1, offvalue = 0,command=chkSbutton_value) .grid(row =1, column =0, sticky =W)

        entSingle = Entry (topLeft2, font= ('arial',20, 'bold'), textvariable=var12, bd=8 , width = 8) .grid(row =1, column =1, sticky =W)

        chkReturn = Checkbutton (topLeft2, font=('arial',20, 'bold'),text="Return", variable = var5, onvalue =1, offvalue =0,command=chkRbutton_value) .grid(row =2, column =0, sticky =W)

        entReturn = Entry (topLeft2, font= ('arial',20, 'bold'), textvariable=var6, bd=8 , width=8) .grid(row =2, column =1, sticky =W)

        lblComment= Label (topLeft2, font=('arial',20, 'bold') ,text="Comment", bd=8).grid(row =3, column =0, sticky =W)

        entComment = Entry (topLeft2, font= ('arial',20, 'bold'),textvariable=var7, bd=8 , width=8).grid (row =3, column =1, sticky =W)
        
#=================================================================================================================================================================
        lb1Tax = Label (bottomLeft1, font=('arial',20, 'bold'), text="State Tax", bd=8).grid(row =0, column =0, sticky =W)

        entTax = Entry (bottomLeft1, font= ('arial',20, 'bold'),textvariable=Tax, bd=5 , width=28) .grid(row =0,column =1, sticky =W)
        
        lblSubTotal = Label(bottomLeft1, font=('arial',20, 'bold'),text="SubTotal", bd=8).grid (row =1, column =0, sticky =W)

        entSubTotal = Entry (bottomLeft1, font=('arial',20, 'bold'),textvariable=Tax, bd=5 , width=28) .grid(row =1, column =1, sticky =W)
        
        lblTotal = Label (bottomLeft1, font=('arial',20, 'bold'),text="Iotal", bd=8) .grid(row =2, column =0, sticky =W)

        entTotal = Entry (bottomLeft1, font=('arial',20, 'bold'),textvariable=Tax, bd=5, width=28) .grid (row =2, column =1, sticky =W)

#=================================================================================================================================================================

        self.txtDisplay = Entry (bottomLeft2, font=('arial', 19, 'bold'), textvariable=text_Input, bd=5, insertwidth=4, justify='right')
        self.txtDisplay.grid (columnspan=4)

        self.btn7=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="7",command=lambda: btnClick(7)).grid (row=1, column=0)

        self.btn8=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="8",command=lambda: btnClick(8)).grid (row=1, column=1)

        self.btn9=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="9",command=lambda: btnClick(9)).grid (row=1, column=2)

        Addition=Button(bottomLeft2, padx=6, pady=5,bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="+",command=lambda: btnClick ("+")).grid (row=1, column=3)

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        self.btn4=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="4",command=lambda: btnClick(4)).grid (row=3, column=0)

        self.btn5=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="5",command=lambda: btnClick(5)).grid (row=3, column=1)

        self.btn6=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="6",command=lambda: btnClick(6)).grid (row=3, column=2)

        Subraction=Button(bottomLeft2, padx=6, pady=5,bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="-",command=lambda: btnClick ("-")).grid (row=3, column=3)

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        self.btn1=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="1",command=lambda: btnClick(1)).grid (row=4, column=0)

        self.btn2=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="2",command=lambda: btnClick(2)).grid (row=4, column=1)

        self.btn3=Button(bottomLeft2,padx=6, pady=5, bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="3",command=lambda: btnClick(2)).grid (row=4, column=2)

        Multiplication=Button(bottomLeft2, padx=6, pady=5,bd=2, fg="black", font=('arial',16, 'bold'),width=4,text="*",command=lambda: btnClick ("*")).grid (row=4, column=3)

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        self.btn0=Button (bottomLeft2, padx=6, pady=5,bd=2, fg="black",font=('arial', 16, 'bold'),width=4,text="0", command=lambda :btnClick(0)) .grid (row=5, column=0)

        self.btnClear=Button (bottomLeft2, padx=6, pady=5, bd=2, fg="black", font= ('arial', 16, 'bold'),width=4,text="C",command=btncleardisp) .grid (row=5, column=1)

        self.btnEquals=Button (bottomLeft2, padx=6,pady=5,bd=2, fg="black",font = ('arial', 16, 'bold'),width=4, text="=",command=benEqualsinput) .grid (row=5, column=2)

        self.Division=Button (bottomLeft2, padx=6, pady=5, bd=2, fg="black", font=('arial', 16, 'bold'), width=4,text="/", command=lambda :btnClick("/")) .grid (row=5, column=3)

#=================================================================================================================================================================





if __name__ == '__main__':
    root = Tk()
    application = Train(root)
    root.mainloop()


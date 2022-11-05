# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:15:06 2022

@author: tivon_37vlsu0
"""

import tkinter as tk
from tkinter import ttk
from ChocAnon_BackEnd import * 

class ChocAnGUI:
    def __init__(self):
        #Root and Frames
        self.root = tk.Tk()
        
        #Begining size
        self.root.geometry('300x200')
        
        #Frames
        self.title_fr = tk.Frame(self.root)
        self.login_fr = tk.Frame(self.root)
        self.bottom_fr = tk.Frame(self.root)
        
        self.login_fr.place(relx=1/4, rely=4/16, relheight = 13/16, relwidth = 1)
        
        self.title_fr.place(relx=0, rely =0, relheight= 3/16, relwidth = 1)
        tk.Label(self.title_fr, text = 'ChocAn Terminal',
                  font = ('Arial 20 bold')).pack()
        
        usernameLabel = tk.Label(self.login_fr, text="User Name").grid(row=5, column=5)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(self.login_fr, textvariable=self.username).grid(row=5, column=6)
        passwordLabel = tk.Label(self.login_fr,text="Password").grid(row=6, column=5)  
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(self.login_fr, textvariable=self.password, show='*').grid(row=6, column=6) 
        self.radio_var = tk.IntVar()
        tk.Radiobutton(self.login_fr, text = 'Provider',variable = self.radio_var, value = 1).grid(row=7, column=5) 
        tk.Radiobutton(self.login_fr, text = 'Manager',variable = self.radio_var, value = 0).grid(row=7, column=6) 
        self.bottom_fr.pack(side = 'bottom')
        tk.Button(self.bottom_fr, text = 'Log in', fg = 'blue',command = self.logIn).pack()
        
        self.root.mainloop()
    def reset_func(self):
        self.root.destroy()
        self.__init__()
    
    def logIn(self):
        if self.radio_var.get() == 1:
            result = Provider.setInfo(Provider,self.username.get(),int(self.password.get()))
        elif self.radio_var.get() == 0:
            result = Manager.setInfo(Manager,self.username.get(),int(self.password.get()))
        if result == 1:
            self.root.destroy()
            self.providerUI()
        elif result == 2:
            self.root.destroy()
            self.managerUI()
        else:
            tk.Label(self.bottom_fr, text = 'Incorrect name/number',font = ('Arial 10 bold')).pack()
    
    def providerUI(self):
        result = 0
        self.root = tk.Tk()
        self.root.geometry('500x500')

        self.root.title("Provider Terminal-User")
        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        
        tabControl.add(tab1, text ='Find Member Account')
        tabControl.add(tab2, text ='Member Info')
        tabControl.add(tab3, text = "Make a Claim")
        tabControl.pack(expand = 1, fill ="both")
  
        tk.Label(tab1, text ="Type in Name and Number").grid(column = 0, row = 0,padx = 30,pady = 30)
        usernameLabel = tk.Label(tab1, text="User Name").grid(row=1, column=0)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(tab1, textvariable=self.username).grid(row=1, column=1)
        passwordLabel = tk.Label(tab1,text="Password").grid(row=2, column=0)  
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(tab1, textvariable=self.password, show='*').grid(row=2, column=1)
        tk.Button(tab1, text = "Search", fg = 'blue',command = self.searchAccount).grid(row=3, column=0)
        name,number,address,city,state,zipCode = "","","","","",""
        tk.Label(tab2,text ="Members Information:").grid(column = 0,row = 0, padx = 0,pady = 0)
        tk.Label(tab2,text ="Name:"+name).grid(column = 0,row = 1, padx = 0,pady = 0)
        tk.Label(tab2,text ="Number:"+number).grid(column = 0,row = 2, padx = 0,pady = 0)
        tk.Label(tab2,text ="Address:"+address).grid(column = 0,row = 3, padx = 0,pady = 0)
        tk.Label(tab2,text ="City:"+city).grid(column = 0,row = 4, padx = 0,pady = 0)
        tk.Label(tab2,text ="State:"+state).grid(column = 0,row = 5, padx = 0,pady = 0)
        tk.Label(tab2,text ="ZIP code:"+zipCode).grid(column = 0,row = 6, padx = 0,pady = 0)
        tk.Label(tab2,text ="TotalFee:").grid(column = 0,row = 7, padx = 0,pady = 0)
        tk.Label(tab3,text ="Member not selected").grid(column = 0,row = 0, padx = 0,pady = 0)
        self.root.mainloop()
        
    def managerUI(self):
        result = 0
        self.root = tk.Tk()
        self.root.geometry('800x500')

        self.root.title("Manager Terminal-User")
        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        tab5 = ttk.Frame(tabControl)
        tab6 = ttk.Frame(tabControl)
        tab7 = ttk.Frame(tabControl)
        tab8 = ttk.Frame(tabControl)
        
        tabControl.add(tab1, text ='Add Account')
        tabControl.add(tab2, text ='Remove Account')
        tabControl.add(tab3, text ='Update Account')
        tabControl.add(tab4, text = "Add Claim")
        tabControl.add(tab5, text = "Remove Claim")
        tabControl.add(tab6, text = "Update Claim")
        tabControl.add(tab7, text = "Submit Report")
        tabControl.add(tab8, text = "Sumbit Summary Report")
        tabControl.pack(expand = 1, fill ="both")
        
        #Tab 1
        nameLabel = tk.Label(tab1, text="Name:").grid(row=1, column=0)
        self.name = tk.StringVar()
        nameEntry = tk.Entry(tab1, textvariable=self.name).grid(row=1, column=1)
        
        numberLabel = tk.Label(tab1,text="Number:").grid(row=2, column=0)  
        self.number = tk.StringVar()
        numberEntry = tk.Entry(tab1, textvariable=self.number).grid(row=2, column=1)
        
        addrLabel = tk.Label(tab1, text="Address:").grid(row=3, column=0)
        self.addr = tk.StringVar()
        addrEntry = tk.Entry(tab1, textvariable=self.addr).grid(row=3, column=1)
        
        cityLabel = tk.Label(tab1,text="City:").grid(row=4, column=0)  
        self.city = tk.StringVar()
        cityEntry = tk.Entry(tab1, textvariable=self.city).grid(row=4, column=1)
        
        stateLabel = tk.Label(tab1, text="State:").grid(row=5, column=0)
        self.state = tk.StringVar()
        stateEntry = tk.Entry(tab1, textvariable=self.state).grid(row=5, column=1)
        
        zipCodeLabel = tk.Label(tab1,text="ZIP Code:").grid(row=6, column=0)  
        self.zipCode = tk.StringVar()
        zipCodeEntry = tk.Entry(tab1, textvariable=self.zipCode).grid(row=6, column=1)
        
        self.accCheck = tk.IntVar()
        accCheckLabel = tk.Label(tab1,text="Is this an Employee?:").grid(row=7, column=0)
        tk.Radiobutton(tab1, text = 'Yes',variable = self.accCheck, value = 1).grid(row=7, column=1) 
        tk.Radiobutton(tab1, text = 'No',variable = self.accCheck, value = 0).grid(row=7, column=2) 
        
        tk.Button(tab1, text = 'Add member', fg = 'blue',command = self.addAccount).grid(row=8, column=0)
        
        #Tab 2
        rNumberLabel = tk.Label(tab2, text="Members Number:").grid(row=1, column=0)
        self.rNumber = tk.StringVar()
        rNumberEntry = tk.Entry(tab2, textvariable=self.rNumber).grid(row=1, column=1)
        tk.Button(tab2, text = 'Remove member', fg = 'red',command = self.removeAccount).grid(row=7, column=0)
        
        #Tab 3
        nNameLabel = tk.Label(tab3, text="Name:").grid(row=1, column=0)
        self.nName = tk.StringVar()
        nNameEntry = tk.Entry(tab3, textvariable=self.nName).grid(row=1, column=1)
        
        nNumberLabel = tk.Label(tab3,text="Number:").grid(row=2, column=0)  
        self.nNumber = tk.StringVar()
        nNumberEntry = tk.Entry(tab3, textvariable=self.nNumber).grid(row=2, column=1)
        
        nAddrLabel = tk.Label(tab3, text="Address:").grid(row=3, column=0)
        self.nAddr = tk.StringVar()
        nAddrEntry = tk.Entry(tab3, textvariable=self.nAddr).grid(row=3, column=1)
        
        nCityLabel = tk.Label(tab3,text="City:").grid(row=4, column=0)  
        self.nCity = tk.StringVar()
        nCityEntry = tk.Entry(tab3, textvariable=self.nCity).grid(row=4, column=1)
        
        nStateLabel = tk.Label(tab3, text="State:").grid(row=5, column=0)
        self.nState = tk.StringVar()
        nStateEntry = tk.Entry(tab3, textvariable=self.nState).grid(row=5, column=1)
        
        nZipCodeLabel = tk.Label(tab3,text="ZIP Code:").grid(row=6, column=0)  
        self.nZipCode = tk.StringVar()
        nZipCodeEntry = tk.Entry(tab3, textvariable=self.nZipCode).grid(row=6, column=1)
        
        tk.Button(tab3, text = 'Update member', fg = 'blue',command = self.updateAccount).grid(row=7, column=0)
        
        #Tab 4
        mNameLabel = tk.Label(tab4, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        mNameEntry = tk.Entry(tab4, textvariable=self.mName).grid(row=1, column=1)
        
        mNumberLabel = tk.Label(tab4,text="Member Number:").grid(row=2, column=0)  
        self.mNumber = tk.StringVar()
        mNumberEntry = tk.Entry(tab4, textvariable=self.mNumber).grid(row=2, column=1)
        
        pNameLabel = tk.Label(tab4, text="Provider Name:").grid(row=1, column=0)
        self.pName = tk.StringVar()
        pNameEntry = tk.Entry(tab4, textvariable=self.pName).grid(row=1, column=1)
        
        pNumberLabel = tk.Label(tab4,text="Provider Number:").grid(row=2, column=0)  
        self.pNumber = tk.StringVar()
        pNumberEntry = tk.Entry(tab4, textvariable=self.pNumber).grid(row=2, column=1)
        
        sNameLabel = tk.Label(tab4, text="Service name (20 characters):").grid(row=3, column=0)
        self.sName = tk.StringVar()
        sNameEntry = tk.Entry(tab4, textvariable=self.sName).grid(row=3, column=1)
        
        sCodeLabel = tk.Label(tab4, text="Service code (6 digit):").grid(row=4, column=0)
        self.sCode = tk.StringVar()
        sCodeEntry = tk.Entry(tab4, textvariable=self.sCode).grid(row=4, column=1)
        
        feeLabel = tk.Label(tab4, text="fee (up to $999.99):").grid(row=5, column=0)
        self.fee = tk.StringVar()
        feeEntry = tk.Entry(tab4, textvariable=self.fee).grid(row=5, column=1)
        
        commentLabel = tk.Label(tab4, text="comments(100 characters)(optional):").grid(row=6, column=0)
        self.comment = tk.StringVar()
        commentEntry = tk.Entry(tab4, textvariable=self.comment).grid(row=7, column=0, ipadx=20,ipady=30)
        
        tk.Button(tab4, text = 'Add Claim', fg = 'blue',command = self.addServiceClaim).grid(row=8, column=0)
        
        #Tab 5
        mNameLabel = tk.Label(tab5, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        mNameEntry = tk.Entry(tab5, textvariable=self.mName).grid(row=1, column=1)
        
        mFileLabel = tk.Label(tab5, text="Member File Name:").grid(row=2, column=0)
        self.mFile = tk.StringVar()
        mFileEntry = tk.Entry(tab5, textvariable=self.mFile).grid(row=2, column=1)
        
        tk.Button(tab5, text = 'Remove Claim', fg = 'red',command = self.removeServiceClaim).grid(row=3, column=0)
        
        #Tab 6
        mNameLabel = tk.Label(tab6, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        mNameEntry = tk.Entry(tab6, textvariable=self.mName).grid(row=1, column=1)
        
        mNumberLabel = tk.Label(tab6,text="Member Number:").grid(row=2, column=0)
        self.mNumber = tk.StringVar()
        mNumberEntry = tk.Entry(tab6, textvariable=self.mNumber).grid(row=2, column=1)
        
        pNameLabel = tk.Label(tab6, text="Provider Name:").grid(row=1, column=0)
        self.pName = tk.StringVar()
        pNameEntry = tk.Entry(tab6, textvariable=self.pName).grid(row=1, column=1)
        
        pNumberLabel = tk.Label(tab6,text="Provider Number:").grid(row=2, column=0)  
        self.pNumber = tk.StringVar()
        pNumberEntry = tk.Entry(tab6, textvariable=self.pNumber).grid(row=2, column=1)
        
        mFileLabel = tk.Label(tab6, text="Member File Name:").grid(row=3, column=0)
        self.mFile = tk.StringVar()
        mFileEntry = tk.Entry(tab6, textvariable=self.mFile).grid(row=3, column=1)
        
        sNameLabel = tk.Label(tab6, text="Service name (20 characters):").grid(row=4, column=0)
        self.sName = tk.StringVar()
        sNameEntry = tk.Entry(tab6, textvariable=self.sName).grid(row=4, column=1)
        
        sCodeLabel = tk.Label(tab6, text="Service code (6 digit):").grid(row=5, column=0)
        self.sCode = tk.StringVar()
        sCodeEntry = tk.Entry(tab6, textvariable=self.sCode).grid(row=5, column=1)
        
        feeLabel = tk.Label(tab6, text="fee (up to $999.99):").grid(row=6, column=0)
        self.fee = tk.StringVar()
        feeEntry = tk.Entry(tab6, textvariable=self.fee).grid(row=6, column=1)
        
        commentLabel = tk.Label(tab6, text="comments(100 characters)(optional):").grid(row=7, column=0)
        self.comment = tk.StringVar()
        commentEntry = tk.Entry(tab6, textvariable=self.comment).grid(row=8, column=0, ipadx=20,ipady=30)
        
        tk.Button(tab6, text = 'Update Claim', fg = 'blue',command = self.updateServiceClaim).grid(row=9, column=0)
        
        #Tab 7
        mNameLabel = tk.Label(tab7, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        mNameEntry = tk.Entry(tab7, textvariable=self.mName).grid(row=1, column=1)
        
        mNumberLabel = tk.Label(tab7,text="Member Number:").grid(row=2, column=0)  
        self.mNumber = tk.StringVar()
        mNumberEntry = tk.Entry(tab7, textvariable=self.mNumber).grid(row=2, column=1)
        tk.Button(tab7, text = 'Submit Report', fg = 'blue',command = self.submitReport).grid(row=3, column=0)
        
        #Tab 8
        pNameLabel = tk.Label(tab8, text="Provider Name:").grid(row=1, column=0)
        self.pName = tk.StringVar()
        pNameEntry = tk.Entry(tab8, textvariable=self.pName).grid(row=1, column=1)
        
        pNumberLabel = tk.Label(tab8,text="Provider Number:").grid(row=2, column=0)  
        self.pNumber = tk.StringVar()
        pNumberEntry = tk.Entry(tab8, textvariable=self.pNumber).grid(row=2, column=1)
        tk.Button(tab8, text = 'Submit Summary', fg = 'blue',command = self.submitReport).grid(row=3, column=0)
        
        self.root.mainloop()
        
    def searchAccount(self):
        result = Provider.checkAccount(self.username.get(),int(self.password.get()))
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry('500x500')
        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab1, text ='Find Member Account')
        tabControl.add(tab2, text ='Member Info')
        tabControl.add(tab3, text = "Make a Claim")
        tabControl.pack(expand = 1, fill ="both")
        tk.Label(tab1, text ="Type in Name and Number").grid(column = 0, row = 0,padx = 30,pady = 30)
        usernameLabel = tk.Label(tab1, text="User Name").grid(row=1, column=0)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(tab1, textvariable=self.username).grid(row=1, column=1)
        passwordLabel = tk.Label(tab1,text="Password").grid(row=2, column=0)  
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(tab1, textvariable=self.password, show='*').grid(row=2, column=1)
        tk.Button(tab1, text = 'Search', fg = 'blue',command = self.searchAccount).grid(row=3, column=0)
        if result == 1:
            name,number,address,city,state,zipCode = Member.getInfo(Member)
            fee = Member.getFee(Member)
            sNameLabel = tk.Label(tab3, text="Service name (20 characters):").grid(row=1, column=0)
            self.sName = tk.StringVar()
            sNameEntry = tk.Entry(tab3, textvariable=self.sName).grid(row=1, column=1)
            sCodeLabel = tk.Label(tab3, text="Service code (6 digit):").grid(row=2, column=0)
            self.sCode = tk.StringVar()
            sCodeEntry = tk.Entry(tab3, textvariable=self.sCode).grid(row=2, column=1)
            feeLabel = tk.Label(tab3, text="fee (up to $999.99):").grid(row=3, column=0)
            self.fee = tk.StringVar()
            feeEntry = tk.Entry(tab3, textvariable=self.fee).grid(row=3, column=1)
            commentLabel = tk.Label(tab3, text="comments(100 characters)(optional):").grid(row=4, column=0)
            self.comment = tk.StringVar()
            commentEntry = tk.Entry(tab3, textvariable=self.comment).grid(row=5, column=0, ipadx=20,ipady=30)
            tk.Button(tab3, text = 'Make Claim', fg = 'blue',command = self.makeServiceClaim).grid(row=6, column=0)
        else:
            name,number,address,city,state,zipCode, fee = "","","","","","", ""
            tk.Label(tab3,text ="Member not selected").grid(column = 0,row = 0, padx = 0,pady = 0)
        tk.Label(tab2,text ="Members Information:").grid(column = 0,row = 0, padx = 0,pady = 0)
        tk.Label(tab2,text ="Name: "+name).grid(column = 0,row = 1, padx = 5,pady = 0)
        tk.Label(tab2,text ="Number: "+str(number)).grid(column = 0,row = 2, padx = 0,pady = 0)
        tk.Label(tab2,text ="Address: "+address).grid(column = 0,row = 3, padx = 0,pady = 0)
        tk.Label(tab2,text ="City: "+city).grid(column = 0,row = 4, padx = 0,pady = 0)
        tk.Label(tab2,text ="State: "+state).grid(column = 0,row = 5, padx = 0,pady = 0)
        tk.Label(tab2,text ="ZIP code: "+zipCode).grid(column = 0,row = 6, padx = 0,pady = 0)
        tk.Label(tab2,text ="TotalFee: "+str(fee)).grid(column = 0,row = 7, padx = 0,pady = 0)
        
    def addAccount(self):
        if len(self.number.get()) != 9:
            tk.messagebox.showerror(title="Insufficient Account Number", message="Account number needs to be 9 digit")
        else:
            Manager.addAccount(self.name.get(), int(self.number.get()), self.addr.get(), self.city.get(), self.state.get(), self.zipCode.get(), self.accCheck.get())
        
    def removeAccount(self):
        Manager.removeAccount(int(self.rNumber.get()))
        
    def updateAccount(self):
        Manager.addAccount(self.nName.get(), int(self.nNumber.get()), self.nAddr.get(), self.nCity.get(), self.nState.get(), self.nZipCode.get())
        
        
    def makeServiceClaim(self):
        Provider.makeClaim(Provider, self.sName.get(), self.sCode.get(), float(self.fee.get()), self.comment.get())
        
    def addServiceClaim(self):
        Manager.makeClaim(Manager, self.mName.get(), self.mNumber.get(), self.pName,get(), self.pNumber.get(), self.sName.get(), self.sCode.get(), float(self.fee.get()), self.comment.get())
       
    def removeServiceClaim(self):
        Manager.removeClaim(Manager, self.mName.get(), self.mFile.get())
        
    def updateServiceClaim(self):
        Manager.makeClaim(Manager, self.mName.get(), self.mNumber.get(), self.pName,get(), self.pNumber.get(), self.mFile.get(), self.sName.get(), self.sCode.get(), float(self.fee.get()), self.comment.get())
      
    def submitReport(self):
        Manager.report(Manager, self.mName.get(), self.mNumber.get())
        
    def submitSummaryReport(self):
        Manager.summaryReport(self.pName.get(), self.pNumber.get())
        
ChocAnGUI()

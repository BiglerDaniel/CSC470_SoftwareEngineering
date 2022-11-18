# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:15:06 2022

@author: tivon_37vlsu0
"""

import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import ast
from ChocAnon_BackEnd import * 
import random

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
        self.result = 0
        self.root = tk.Tk()
        self.root.geometry('400x600')

        self.root.title("Provider Terminal-User")
        style = ttk.Style(self.root)
        style.configure('lefttab.TNotebook', tabposition='wn')
        tabControl = ttk.Notebook(self.root,style='lefttab.TNotebook')
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        #tab4 = ttk.Frame(tabControl)
        
        
        tabControl.add(tab1, text ='Members')
        #tabControl.add(tab1, text ='Member Info')
        #tabControl.add(tab1, text = "Make a Claim")
        tabControl.add(tab2, text = "Report")
        tabControl.add(tab3, text = "Log Out")
        tabControl.pack(expand = 1, fill ="both")
        block1 = tk.LabelFrame(tab1, text="Search Account", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block1.grid(column=0, row=0)
        name,number,address,city,state,zipCode, fee, date, status = "","","","","","", "", "", ""
        tk.Label(block1, text ="Type in Name and Number").grid(column = 0, row = 0,padx = 0,pady = 0)
        usernameLabel = tk.Label(block1, text="Member Search").grid(row=1, column=0)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(block1, textvariable=self.username).grid(row=1, column=1)
        passwordLabel = tk.Label(block1,text="Password").grid(row=2, column=0)  
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(block1, textvariable=self.password, show='*').grid(row=2, column=1)
        tk.Button(block1, text = 'Search', fg = 'blue',command = self.searchAccount).grid(row=3, column=0)
        block2 = tk.LabelFrame(tab1, text="Member Info", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block2.grid(column=0, row=1)
        tk.Label(block2,text ="Members Information:").grid(column = 0,row = 0, padx = 0,pady = 0)
        tk.Label(block2,text ="Name: "+name).grid(column = 0,row = 1, padx = 0,pady = 0)
        tk.Label(block2,text ="Number: "+str(number)).grid(column = 0,row = 2, padx = 0,pady = 0)
        tk.Label(block2,text ="Address: "+address).grid(column = 0,row = 3, padx = 0,pady = 0)
        tk.Label(block2,text ="City: "+city).grid(column = 0,row = 4, padx = 0,pady = 0)
        tk.Label(block2,text ="State: "+state).grid(column = 0,row = 5, padx = 0,pady = 0)
        tk.Label(block2,text ="ZIP code: "+zipCode).grid(column = 0,row = 6, padx = 0,pady = 0)
        tk.Label(block2,text ="TotalFee: "+str(fee)).grid(column = 0,row = 7, padx = 0,pady = 0)
        tk.Label(block2,text ="Due: "+date).grid(column = 0,row = 9, padx = 0,pady = 0)
        tk.Label(block2,text ="Status: "+status).grid(column = 0,row = 9, padx = 0,pady = 0)
        block3 = tk.LabelFrame(tab1, text="Make a Claim", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block3.grid(column=0, row=2)
        tk.Label(block3,text ="Member not selected").grid(column = 0,row = 0, padx = 0,pady = 0)
        
        block4 = tk.LabelFrame(tab2, text="Submit Report", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block4.grid(column=0, row=0)
        mNameLabel = tk.Label(block4, text="Member Name:").grid(row=1, column=0)
        self.m1Name = tk.StringVar()
        mNameEntry = tk.Entry(block4, textvariable=self.mName).grid(row=1, column=1)
        
        mNumberLabel = tk.Label(block4,text="Member Number:").grid(row=2, column=0)  
        self.mNumber = tk.StringVar()
        mNumberEntry = tk.Entry(block4, textvariable=self.mNumber).grid(row=2, column=1)
        
        sMonthLabel = tk.Label(block4,text="Start Month:").grid(row=3, column=0)  
        self.sMonth = tk.StringVar()
        sMonthEntry = tk.Entry(block4, textvariable=self.sMonth).grid(row=3, column=1)
        
        sDayLabel = tk.Label(block4,text="Start Day:").grid(row=4, column=0)  
        self.sDay = tk.StringVar()
        sDayEntry = tk.Entry(block4, textvariable=self.sDay).grid(row=4, column=1)
        
        sYearLabel = tk.Label(block4,text="Start Year:").grid(row=5, column=0)  
        self.sYear = tk.StringVar()
        sYearEntry = tk.Entry(block4, textvariable=self.sYear).grid(row=5, column=1)
        
        eMonthLabel = tk.Label(block4,text="End Month:").grid(row=6, column=0)  
        self.eMonth = tk.StringVar()
        eMonthEntry = tk.Entry(block4, textvariable=self.eMonth).grid(row=6, column=1)
        
        eDayLabel = tk.Label(block4,text="End Day:").grid(row=7, column=0)  
        self.eDay = tk.StringVar()
        eDayEntry = tk.Entry(block4, textvariable=self.eDay).grid(row=7, column=1)
        
        eYearLabel = tk.Label(block4,text="End Year:").grid(row=8, column=0)  
        self.eYear = tk.StringVar()
        eYearEntry = tk.Entry(block4, textvariable=self.eYear).grid(row=8, column=1)
        tk.Button(block4, text = 'Submit Report', fg = 'blue',command = self.submitReport).grid(row=9, column=0)
        
        #Tab 8
        block5 = tk.LabelFrame(tab2, text="Submit Summary Report", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block5.grid(column=0, row=1)
        pNameLabel = tk.Label(block5, text="Provider Name:").grid(row=1, column=0)
        self.pName = tk.StringVar()
        pNameEntry = tk.Entry(block5, textvariable=self.pName).grid(row=1, column=1)
        
        pNumberLabel = tk.Label(block5,text="Provider Number:").grid(row=2, column=0)  
        self.pNumber = tk.StringVar()
        pNumberEntry = tk.Entry(block5, textvariable=self.pNumber).grid(row=2, column=1)
        
        spMonthLabel = tk.Label(block5,text="Start Month:").grid(row=3, column=0)  
        self.spMonth = tk.StringVar()
        spMonthEntry = tk.Entry(block5, textvariable=self.spMonth).grid(row=3, column=1)
        
        spDayLabel = tk.Label(block5,text="Start Day:").grid(row=4, column=0)  
        self.spDay = tk.StringVar()
        spDayEntry = tk.Entry(block5, textvariable=self.spDay).grid(row=4, column=1)
        
        spYearLabel = tk.Label(block5,text="Start Year:").grid(row=5, column=0)  
        self.spYear = tk.StringVar()
        spYearEntry = tk.Entry(block5, textvariable=self.spYear).grid(row=5, column=1)
        
        epMonthLabel = tk.Label(block5,text="End Month:").grid(row=6, column=0)  
        self.epMonth = tk.StringVar()
        epMonthEntry = tk.Entry(block5, textvariable=self.epMonth).grid(row=6, column=1)
        
        epDayLabel = tk.Label(block5,text="End Day:").grid(row=7, column=0)  
        self.epDay = tk.StringVar()
        epDayEntry = tk.Entry(block5, textvariable=self.epDay).grid(row=7, column=1)
        
        epYearLabel = tk.Label(block5,text="End Year:").grid(row=8, column=0)  
        self.epYear = tk.StringVar()
        epYearEntry = tk.Entry(block5, textvariable=self.epYear).grid(row=8, column=1)
        
        tk.Button(block5, text = 'Submit Summary', fg = 'blue',command = self.submitSummaryReport).grid(row=9, column=0)
        
        tk.Button(tab3, text = 'Log Out', fg = 'red',command = self.logOut).grid(row=0, column=0)
        self.root.mainloop()
        
    def managerUI(self):
        result = 0
        self.root = tk.Tk()
        self.root.geometry('750x400')

        self.root.title("Manager Terminal-User")
        style = ttk.Style(self.root)
        style.configure('lefttab.TNotebook', tabposition='wn')
        tabControl = ttk.Notebook(self.root,style='lefttab.TNotebook')
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        
        tabControl.add(tab1, text ='Account')
        tabControl.add(tab2, text = "Claim")
        tabControl.add(tab3, text = "Report")
        tabControl.add(tab4, text = "Log Out")
        tabControl.pack(expand = 1, fill ="both")
        
        #Tab 1
        block1 = tk.LabelFrame(tab1, text="Add Account", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block1.grid(column=0, row=0)
        nameLabel = tk.Label(block1, text="Name:").grid(row=1, column=0)
        self.name = tk.StringVar()
        nameEntry = tk.Entry(block1, textvariable=self.name).grid(row=1, column=1)
        
        # numberLabel = tk.Label(tab1,text="Number:").grid(row=2, column=0)  
        # self.number = tk.StringVar()
        # numberEntry = tk.Entry(tab1, textvariable=self.number).grid(row=2, column=1)
        
        addrLabel = tk.Label(block1, text="Address:").grid(row=2, column=0)
        self.addr = tk.StringVar()
        addrEntry = tk.Entry(block1, textvariable=self.addr).grid(row=2, column=1)
        
        cityLabel = tk.Label(block1,text="City:").grid(row=3, column=0)  
        self.city = tk.StringVar()
        cityEntry = tk.Entry(block1, textvariable=self.city).grid(row=3, column=1)
        
        stateLabel = tk.Label(block1, text="State:").grid(row=4, column=0)
        self.state = tk.StringVar()
        stateEntry = tk.Entry(block1, textvariable=self.state).grid(row=4, column=1)
        
        zipCodeLabel = tk.Label(block1,text="ZIP Code:").grid(row=5, column=0)  
        self.zipCode = tk.StringVar()
        zipCodeEntry = tk.Entry(block1, textvariable=self.zipCode).grid(row=5, column=1)
        
        self.accCheck = tk.IntVar()
        accCheckLabel = tk.Label(block1,text="Is this an Employee?:").grid(row=6, column=0)
        tk.Radiobutton(block1, text = 'Yes',variable = self.accCheck, value = 1).grid(row=6, column=1) 
        tk.Radiobutton(block1, text = 'No',variable = self.accCheck, value = -1).grid(row=6, column=2) 
        
        tk.Button(block1, text = 'Add member', fg = 'blue',command = self.addAccount).grid(row=8, column=0)
        
        #Tab 2
        block2 = tk.LabelFrame(tab1, text="Remove Account", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block2.grid(column=0, row=1)
        rNumberLabel = tk.Label(block2, text="Members Number:").grid(row=1, column=0)
        self.rNumber = tk.StringVar()
        rNumberEntry = tk.Entry(block2, textvariable=self.rNumber).grid(row=1, column=1)
        tk.Button(block2, text = 'Remove member', fg = 'red',command = self.removeAccount).grid(row=2, column=0)
        
        #Tab 3
        block3 = tk.LabelFrame(tab1, text="Update Account", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block3.grid(column=1, row=0)
        nNameLabel = tk.Label(block3, text="Name:").grid(row=1, column=0)
        self.nName = tk.StringVar()
        nNameEntry = tk.Entry(block3, textvariable=self.nName).grid(row=1, column=1)
        
        nNumberLabel = tk.Label(block3,text="Number:").grid(row=2, column=0)  
        self.nNumber = tk.StringVar()
        nNumberEntry = tk.Entry(block3, textvariable=self.nNumber).grid(row=2, column=1)
        
        nAddrLabel = tk.Label(block3, text="Address:").grid(row=3, column=0)
        self.nAddr = tk.StringVar()
        nAddrEntry = tk.Entry(block3, textvariable=self.nAddr).grid(row=3, column=1)
        
        nCityLabel = tk.Label(block3,text="City:").grid(row=4, column=0)  
        self.nCity = tk.StringVar()
        nCityEntry = tk.Entry(block3, textvariable=self.nCity).grid(row=4, column=1)
        
        nStateLabel = tk.Label(block3, text="State:").grid(row=5, column=0)
        self.nState = tk.StringVar()
        nStateEntry = tk.Entry(block3, textvariable=self.nState).grid(row=5, column=1)
        
        nZipCodeLabel = tk.Label(block3,text="ZIP Code:").grid(row=6, column=0)  
        self.nZipCode = tk.StringVar()
        nZipCodeEntry = tk.Entry(block3, textvariable=self.nZipCode).grid(row=6, column=1)
        
        self.nAccCheck = tk.IntVar()
        nAccCheckLabel = tk.Label(block3,text="Is this an Employee?:").grid(row=7, column=0)
        tk.Radiobutton(block3, text = 'Yes',variable = self.nAccCheck, value = 1).grid(row=7, column=1) 
        tk.Radiobutton(block3, text = 'No',variable = self.nAccCheck, value = -1).grid(row=7, column=2) 
        
        tk.Button(block3, text = 'Update member', fg = 'blue',command = self.updateAccount).grid(row=8, column=0)
        
        #Tab 4
        block1 = tk.LabelFrame(tab2, text="Add Claim", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block1.grid(column=0, row=0)
        m1NameLabel = tk.Label(block1, text="Member Name:").grid(row=1, column=0)
        self.m1Name = tk.StringVar()
        m1NameEntry = tk.Entry(block1, textvariable=self.m1Name).grid(row=1, column=1)
        
        m1NumberLabel = tk.Label(block1,text="Member Number:").grid(row=2, column=0)  
        self.m1Number = tk.StringVar()
        m1NumberEntry = tk.Entry(block1, textvariable=self.m1Number).grid(row=2, column=1)
        
        p1NameLabel = tk.Label(block1, text="Provider Name:").grid(row=3, column=0)
        self.p1Name = tk.StringVar()
        p1NameEntry = tk.Entry(block1, textvariable=self.p1Name).grid(row=3, column=1)
        
        p1NumberLabel = tk.Label(block1,text="Provider Number:").grid(row=4, column=0)  
        self.p1Number = tk.StringVar()
        p1NumberEntry = tk.Entry(block1, textvariable=self.p1Number).grid(row=4, column=1)
        
        sNameLabel = tk.Label(block1, text="Service name (20 characters):").grid(row=5, column=0)
        self.sName = tk.StringVar()
        sNameEntry = tk.Entry(block1, textvariable=self.sName).grid(row=5, column=1)
        
        sCodeLabel = tk.Label(block1, text="Service code (6 digit):").grid(row=6, column=0)
        self.sCode = tk.StringVar()
        sCodeEntry = tk.Entry(block1, textvariable=self.sCode).grid(row=6, column=1)
        
        # feeLabel = tk.Label(tab4, text="fee (up to $999.99):").grid(row=7, column=0)
        # self.fee = tk.StringVar()
        # feeEntry = tk.Entry(tab4, textvariable=self.fee).grid(row=7, column=1)
        
        commentLabel = tk.Label(block1, text="comments(100 characters)(optional):").grid(row=7, column=0)
        self.comment = tk.StringVar()
        commentEntry = tk.Entry(block1, textvariable=self.comment).grid(row=8, column=0, ipadx=20,ipady=30)
        
        tk.Button(block1, text = 'Add Claim', fg = 'blue',command = self.addServiceClaim).grid(row=10, column=0)
        
        #Tab 5
        block2 = tk.LabelFrame(tab2, text="Remove Claim", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block2.grid(column=0, row=1)
        rNameLabel = tk.Label(block2, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        rNameEntry = tk.Entry(block2, textvariable=self.mName).grid(row=1, column=1)
        
        rFileLabel = tk.Label(block2, text="Member File Name:").grid(row=2, column=0)
        self.rFile = tk.StringVar()
        rFileEntry = tk.Entry(block2, textvariable=self.rFile).grid(row=2, column=1)
        
        tk.Button(block2, text = 'Remove Claim', fg = 'red',command = self.removeServiceClaim).grid(row=3, column=0)
        
        #Tab 6
        block3 = tk.LabelFrame(tab2, text="Update Claim", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block3.grid(column=1, row=0)
        uNameLabel = tk.Label(block3, text="Member Name:").grid(row=1, column=0)
        self.uName = tk.StringVar()
        uNameEntry = tk.Entry(block3, textvariable=self.uName).grid(row=1, column=1)
        
        uNumberLabel = tk.Label(block3,text="Member Number:").grid(row=2, column=0)
        self.uNumber = tk.StringVar()
        uNumberEntry = tk.Entry(block3, textvariable=self.uNumber).grid(row=2, column=1)
        
        upNameLabel = tk.Label(block3, text="Provider Name:").grid(row=3, column=0)
        self.upName = tk.StringVar()
        upNameEntry = tk.Entry(block3, textvariable=self.upName).grid(row=3, column=1)
        
        upNumberLabel = tk.Label(block3,text="Provider Number:").grid(row=4, column=0)  
        self.upNumber = tk.StringVar()
        upNumberEntry = tk.Entry(block3, textvariable=self.upNumber).grid(row=4, column=1)
        
        uFileLabel = tk.Label(block3, text="Member File Name:").grid(row=5, column=0)
        self.uFile = tk.StringVar()
        uFileEntry = tk.Entry(block3, textvariable=self.uFile).grid(row=5, column=1)
        
        uSNameLabel = tk.Label(block3, text="Service name (20 characters):").grid(row=6, column=0)
        self.uSName = tk.StringVar()
        uSNameEntry = tk.Entry(block3, textvariable=self.uSName).grid(row=6, column=1)
        
        uCodeLabel = tk.Label(block3, text="Service code (6 digit):").grid(row=7, column=0)
        self.uCode = tk.StringVar()
        uCodeEntry = tk.Entry(block3, textvariable=self.uCode).grid(row=7, column=1)
        
        # feeLabel = tk.Label(tab6, text="fee (up to $999.99):").grid(row=6, column=0)
        # self.fee = tk.StringVar()
        # feeEntry = tk.Entry(tab6, textvariable=self.fee).grid(row=6, column=1)
        
        ucommentLabel = tk.Label(block3, text="comments(100 characters)(optional):").grid(row=8, column=0)
        self.ucomment = tk.StringVar()
        ucommentEntry = tk.Entry(block3, textvariable=self.ucomment).grid(row=9, column=0, ipadx=20,ipady=30)
        
        tk.Button(block3, text = 'Update Claim', fg = 'blue',command = self.updateServiceClaim).grid(row=10, column=0)
        
        #Tab 7
        block1 = tk.LabelFrame(tab3, text="Submit Report", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block1.grid(column=0, row=0)
        mNameLabel = tk.Label(block1, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        mNameEntry = tk.Entry(block1, textvariable=self.mName).grid(row=1, column=1)
        
        mNumberLabel = tk.Label(block1,text="Member Number:").grid(row=2, column=0)  
        self.mNumber = tk.StringVar()
        mNumberEntry = tk.Entry(block1, textvariable=self.mNumber).grid(row=2, column=1)
        
        sMonthLabel = tk.Label(block1,text="Start Month:").grid(row=3, column=0)  
        self.sMonth = tk.StringVar()
        sMonthEntry = tk.Entry(block1, textvariable=self.sMonth).grid(row=3, column=1)
        
        sDayLabel = tk.Label(block1,text="Start Day:").grid(row=4, column=0)  
        self.sDay = tk.StringVar()
        sDayEntry = tk.Entry(block1, textvariable=self.sDay).grid(row=4, column=1)
        
        sYearLabel = tk.Label(block1,text="Start Year:").grid(row=5, column=0)  
        self.sYear = tk.StringVar()
        sYearEntry = tk.Entry(block1, textvariable=self.sYear).grid(row=5, column=1)
        
        eMonthLabel = tk.Label(block1,text="End Month:").grid(row=6, column=0)  
        self.eMonth = tk.StringVar()
        eMonthEntry = tk.Entry(block1, textvariable=self.eMonth).grid(row=6, column=1)
        
        eDayLabel = tk.Label(block1,text="End Day:").grid(row=7, column=0)  
        self.eDay = tk.StringVar()
        eDayEntry = tk.Entry(block1, textvariable=self.eDay).grid(row=7, column=1)
        
        eYearLabel = tk.Label(block1,text="End Year:").grid(row=8, column=0)  
        self.eYear = tk.StringVar()
        eYearEntry = tk.Entry(block1, textvariable=self.eYear).grid(row=8, column=1)
        tk.Button(block1, text = 'Submit Report', fg = 'blue',command = self.submitReport).grid(row=9, column=0)
        
        #Tab 8
        block2 = tk.LabelFrame(tab3, text="Submit Summary Report", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block2.grid(column=1, row=0)
        pNameLabel = tk.Label(block2, text="Provider Name:").grid(row=1, column=0)
        self.pName = tk.StringVar()
        pNameEntry = tk.Entry(block2, textvariable=self.pName).grid(row=1, column=1)
        
        pNumberLabel = tk.Label(block2,text="Provider Number:").grid(row=2, column=0)  
        self.pNumber = tk.StringVar()
        pNumberEntry = tk.Entry(block2, textvariable=self.pNumber).grid(row=2, column=1)
        
        spMonthLabel = tk.Label(block2,text="Start Month:").grid(row=3, column=0)  
        self.spMonth = tk.StringVar()
        spMonthEntry = tk.Entry(block2, textvariable=self.spMonth).grid(row=3, column=1)
        
        spDayLabel = tk.Label(block2,text="Start Day:").grid(row=4, column=0)  
        self.spDay = tk.StringVar()
        spDayEntry = tk.Entry(block2, textvariable=self.spDay).grid(row=4, column=1)
        
        spYearLabel = tk.Label(block2,text="Start Year:").grid(row=5, column=0)  
        self.spYear = tk.StringVar()
        spYearEntry = tk.Entry(block2, textvariable=self.spYear).grid(row=5, column=1)
        
        epMonthLabel = tk.Label(block2,text="End Month:").grid(row=6, column=0)  
        self.epMonth = tk.StringVar()
        epMonthEntry = tk.Entry(block2, textvariable=self.epMonth).grid(row=6, column=1)
        
        epDayLabel = tk.Label(block2,text="End Day:").grid(row=7, column=0)  
        self.epDay = tk.StringVar()
        epDayEntry = tk.Entry(block2, textvariable=self.epDay).grid(row=7, column=1)
        
        epYearLabel = tk.Label(block2,text="End Year:").grid(row=8, column=0)  
        self.epYear = tk.StringVar()
        epYearEntry = tk.Entry(block2, textvariable=self.epYear).grid(row=8, column=1)
        
        tk.Button(block2, text = 'Submit Summary', fg = 'blue',command = self.submitSummaryReport).grid(row=9, column=0)
        
        #Tab9
        tk.Button(tab4, text = 'Log Out', fg = 'red',command = self.logOut).grid(row=0, column=0)
        
        self.root.mainloop()
        
    def searchAccount(self):
        result = Provider.checkAccount(self.username.get(),int(self.password.get()))
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry('400x600')
        style = ttk.Style(self.root)
        style.configure('lefttab.TNotebook', tabposition='wn')
        tabControl = ttk.Notebook(self.root,style='lefttab.TNotebook')
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        #tab4 = ttk.Frame(tabControl)
        tabControl.add(tab1, text ='Account')
        #tabControl.add(tab2, text ='Member Info')
        #tabControl.add(tab3, text = "Make a Claim")
        tabControl.add(tab2, text = "Report")
        tabControl.add(tab3, text = "Log Out")
        tabControl.pack(expand = 1, fill ="both")
        block1 = tk.LabelFrame(tab1, text="Search Account", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block1.grid(column=0, row=0)
        tk.Label(block1, text ="Type in Name and Number").grid(column = 0, row = 0,padx = 0,pady = 0)
        usernameLabel = tk.Label(block1, text="User Name").grid(row=1, column=0)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(block1, textvariable=self.username).grid(row=1, column=1)
        passwordLabel = tk.Label(block1,text="Password").grid(row=2, column=0)  
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(block1, textvariable=self.password, show='*').grid(row=2, column=1)
        tk.Button(block1, text = 'Search', fg = 'blue',command = self.searchAccount).grid(row=3, column=0)
        if result == 1:
            block3 = tk.LabelFrame(tab1, text="Make a Claim", width=100,
                  height=100, borderwidth=5, relief="sunken")
            block3.grid(column=0, row=2)
            name,number,address,city,state,zipCode, statCheck = Member.getInfo(Member)
            if statCheck == -1:
                status = "Valid"
            elif statCheck == -2:
                status = "Expired"
            fee, date = Member.getDetails(Member)
            sNameLabel = tk.Label(block3, text="Service name (20 characters):").grid(row=1, column=0)
            self.sName = tk.StringVar()
            sNameEntry = tk.Entry(block3, textvariable=self.sName).grid(row=1, column=1)
            sCodeLabel = tk.Label(block3, text="Service code (6 digit):").grid(row=2, column=0)
            self.sCode = tk.StringVar()
            sCodeEntry = tk.Entry(block3, textvariable=self.sCode).grid(row=2, column=1)
            # feeLabel = tk.Label(tab3, text="fee (up to $999.99):").grid(row=3, column=0)
            # self.fee = tk.StringVar()
            # feeEntry = tk.Entry(tab3, textvariable=self.fee).grid(row=3, column=1)
            commentLabel = tk.Label(block3, text="comments(100 characters)(optional):").grid(row=4, column=0)
            self.comment = tk.StringVar()
            commentEntry = tk.Entry(block3, textvariable=self.comment).grid(row=5, column=0, ipadx=20,ipady=30)
            tk.Button(block3, text = 'Make Claim', fg = 'blue',command = self.makeServiceClaim).grid(row=6, column=0)
        else:
            block3 = tk.LabelFrame(tab1, text="Make a Claim", width=100,
                  height=100, borderwidth=5, relief="sunken")
            block3.grid(column=0, row=2)
            name,number,address,city,state,zipCode, fee, date, status = "","","","","","", "", "", ""
            tk.Label(block3,text ="Member not selected").grid(column = 0,row = 0, padx = 0,pady = 0)
        block2 = tk.LabelFrame(tab1, text="Member Info", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block2.grid(column=0, row=1)
        tk.Label(block2,text ="Members Information:").grid(column = 0,row = 0, padx = 0,pady = 0)
        tk.Label(block2,text ="Name: "+name).grid(column = 0,row = 1, padx = 5,pady = 0)
        tk.Label(block2,text ="Number: "+str(number)).grid(column = 0,row = 2, padx = 0,pady = 0)
        tk.Label(block2,text ="Address: "+address).grid(column = 0,row = 3, padx = 0,pady = 0)
        tk.Label(block2,text ="City: "+city).grid(column = 0,row = 4, padx = 0,pady = 0)
        tk.Label(block2,text ="State: "+state).grid(column = 0,row = 5, padx = 0,pady = 0)
        tk.Label(block2,text ="ZIP code: "+zipCode).grid(column = 0,row = 6, padx = 0,pady = 0)
        tk.Label(block2,text ="TotalFee: "+str(fee)).grid(column = 0,row = 7, padx = 0,pady = 0)
        tk.Label(block2,text ="Due: "+date).grid(column = 0,row = 8, padx = 0,pady = 0)
        tk.Label(block2,text ="Status: "+status).grid(column = 0,row = 9, padx = 0,pady = 0)
        tk.Button(block2, text = 'Suspend', fg = 'red',command = self.statusAccount).grid(row=10, column=0)
        block4 = tk.LabelFrame(tab2, text="Submit Report", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block4.grid(column=0, row=0)
        mNameLabel = tk.Label(block4, text="Member Name:").grid(row=1, column=0)
        self.mName = tk.StringVar()
        mNameEntry = tk.Entry(block4, textvariable=self.mName).grid(row=1, column=1)
        
        mNumberLabel = tk.Label(block4,text="Member Number:").grid(row=2, column=0)  
        self.mNumber = tk.StringVar()
        mNumberEntry = tk.Entry(block4, textvariable=self.mNumber).grid(row=2, column=1)
        
        sMonthLabel = tk.Label(block4,text="Start Month:").grid(row=3, column=0)  
        self.sMonth = tk.StringVar()
        sMonthEntry = tk.Entry(block4, textvariable=self.sMonth).grid(row=3, column=1)
        
        sDayLabel = tk.Label(block4,text="Start Day:").grid(row=4, column=0)  
        self.sDay = tk.StringVar()
        sDayEntry = tk.Entry(block4, textvariable=self.sDay).grid(row=4, column=1)
        
        sYearLabel = tk.Label(block4,text="Start Year:").grid(row=5, column=0)  
        self.sYear = tk.StringVar()
        sYearEntry = tk.Entry(block4, textvariable=self.sYear).grid(row=5, column=1)
        
        eMonthLabel = tk.Label(block4,text="End Month:").grid(row=6, column=0)  
        self.eMonth = tk.StringVar()
        eMonthEntry = tk.Entry(block4, textvariable=self.eMonth).grid(row=6, column=1)
        
        eDayLabel = tk.Label(block4,text="End Day:").grid(row=7, column=0)  
        self.eDay = tk.StringVar()
        eDayEntry = tk.Entry(block4, textvariable=self.eDay).grid(row=7, column=1)
        
        eYearLabel = tk.Label(block4,text="End Year:").grid(row=8, column=0)  
        self.eYear = tk.StringVar()
        eYearEntry = tk.Entry(block4, textvariable=self.eYear).grid(row=8, column=1)
        tk.Button(block4, text = 'Submit Report', fg = 'blue',command = self.submitReport).grid(row=9, column=0)
        
        #Tab 8
        block5 = tk.LabelFrame(tab2, text="Submit Summary Report", width=100,
                  height=100, borderwidth=5, relief="sunken")
        block5.grid(column=0, row=1)
        pNameLabel = tk.Label(block5, text="Provider Name:").grid(row=1, column=0)
        self.pName = tk.StringVar()
        pNameEntry = tk.Entry(block5, textvariable=self.pName).grid(row=1, column=1)
        
        pNumberLabel = tk.Label(block5,text="Provider Number:").grid(row=2, column=0)  
        self.pNumber = tk.StringVar()
        pNumberEntry = tk.Entry(block5, textvariable=self.pNumber).grid(row=2, column=1)
        
        spMonthLabel = tk.Label(block5,text="Start Month:").grid(row=3, column=0)  
        self.spMonth = tk.StringVar()
        spMonthEntry = tk.Entry(block5, textvariable=self.spMonth).grid(row=3, column=1)
        
        spDayLabel = tk.Label(block5,text="Start Day:").grid(row=4, column=0)  
        self.spDay = tk.StringVar()
        spDayEntry = tk.Entry(block5, textvariable=self.spDay).grid(row=4, column=1)
        
        spYearLabel = tk.Label(block5,text="Start Year:").grid(row=5, column=0)  
        self.spYear = tk.StringVar()
        spYearEntry = tk.Entry(block5, textvariable=self.spYear).grid(row=5, column=1)
        
        epMonthLabel = tk.Label(block5,text="End Month:").grid(row=6, column=0)  
        self.epMonth = tk.StringVar()
        epMonthEntry = tk.Entry(block5, textvariable=self.epMonth).grid(row=6, column=1)
        
        epDayLabel = tk.Label(block5,text="End Day:").grid(row=7, column=0)  
        self.epDay = tk.StringVar()
        epDayEntry = tk.Entry(block5, textvariable=self.epDay).grid(row=7, column=1)
        
        epYearLabel = tk.Label(block5,text="End Year:").grid(row=8, column=0)  
        self.epYear = tk.StringVar()
        epYearEntry = tk.Entry(block5, textvariable=self.epYear).grid(row=8, column=1)
        
        tk.Button(block5, text = 'Submit Summary', fg = 'blue',command = self.submitSummaryReport).grid(row=9, column=0)
        
        tk.Button(tab3, text = 'Log Out', fg = 'red',command = self.logOut).grid(row=0, column=0)
        
    def addAccount(self):
        obj = open("Login.txt","r")
        data = obj.read()
        Login = ast.literal_eval(data)
        obj.close
        number = random.randint(0, 999999999)
        if number < 100000000:
            number = str(number).zfill(9)
        while int(number) in Login:
            number = random.randint(0, 999999999)
            if number < 100000000:
                number = str(number).zfill(9)
        Manager.addAccount(self.name.get(), int(number), self.addr.get(), self.city.get(), self.state.get(), self.zipCode.get(), self.accCheck.get())
        
    def removeAccount(self):
        Manager.removeAccount(int(self.rNumber.get()))
        
    def updateAccount(self):
        Manager.updateAccount(self.nName.get(), int(self.nNumber.get()), self.nAddr.get(), self.nCity.get(), self.nState.get(), self.nZipCode.get(),self.nAccCheck.get())
    
    def statusAccount(self):
        Provider.Suspend()
        
    def makeServiceClaim(self):
        obj = open("ServiceList.txt","r")
        data = obj.read()
        codes = ast.literal_eval(data)
        obj.close
        if int(self.sCode.get()) in codes:
            Provider.makeClaim(Provider, self.sName.get(), self.sCode.get(), float(codes.get(int(self.sCode.get()))), self.comment.get())
        else:
            tk.messagebox.showerror(title="Insufficient Service Code", message="Service Code does not exist")
        
    def addServiceClaim(self):
        obj = open("ServiceList.txt","r")
        data = obj.read()
        codes = ast.literal_eval(data)
        obj.close
        if int(self.sCode.get()) in codes:
            Manager.addClaim(Manager, self.m1Name.get(), int(self.m1Number.get()), self.p1Name.get(), int(self.p1Number.get()), self.sName.get(), self.sCode.get(), float(codes.get(int(self.sCode.get()))), self.comment.get())
        else:
           tk.messagebox.showerror(title="Insufficient Service Code", message="Service Code does not exist")
        
    def removeServiceClaim(self):
        Manager.removeClaim(Manager, self.rName.get(), self.rFile.get())
        
    def updateServiceClaim(self):
        obj = open("ServiceList.txt","r")
        data = obj.read()
        codes = ast.literal_eval(data)
        obj.close
        if int(self.uCode.get()) in codes:
            Manager.updateClaim(Manager, self.uName.get(), int(self.uNumber.get()), self.upName.get(), int(self.upNumber.get()), self.uFile.get(),self.uSName.get(), self.uCode.get(), float(codes.get(int(self.uCode.get()))), self.ucomment.get())
        else:
           tk.messagebox.showerror(title="Insufficient Service Code", message="Service Code does not exist")
      
    def submitReport(self):
        Manager.report(Manager, self.mName.get(), int(self.mNumber.get()), int(self.sMonth.get()), int(self.sDay.get()),int(self.eDay.get()),int(self.sYear.get()))
        
    def submitSummaryReport(self):
        Manager.summaryReport(self.pName.get(), int(self.pNumber.get()),int(self.spMonth.get()), int(self.spDay.get()),int(self.epDay.get()),int(self.spYear.get()))
    
    def logOut(self):
        self.root.destroy()
        self.__init__()
        
ChocAnGUI()

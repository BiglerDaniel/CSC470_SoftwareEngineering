# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:22:34 2022

@author: tivon_37vlsu0
"""
import ast
import shutil
import os, glob
dir_path = os.path.dirname(os.path.realpath(__file__))
from datetime import datetime, timedelta
now = datetime.now()
dt_string = now.strftime("%m-%d-%Y %H:%M:%S")

class Member():
    def __init__(self,name,number,address,city,state,zipCode,status):
        self.name = name
        self.number = number
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.status = status
        
    def getInfo(self):
        return self.name, self.number, self.address, self.city, self.state, self.zipCode, self.status
    
    def setInfo(self, logName, logNum):
        f = open("Login.txt","r")
        data = f.read()
        logIns = ast.literal_eval(data)
        f.close()
        if logNum in logIns:
            if logIns[logNum][7] == logName:
                print('Log in')
                self.__init__(Member,logIns[logNum][0], logIns[logNum][1], logIns[logNum][2], logIns[logNum][3], logIns[logNum][4], logIns[logNum][5], logIns[logNum][6])
                return 1
            else:
                print('Incorrect name/password')
                return 0
        else:
            print('Incorrect name/password')
            return 0
    
    def getDetails(self):
        path = dir_path+"\\"+self.name+"\\Details"
        if not os.path.exists(path):
            return "0.00", ""
        else:
            f = open(path+"\\Details.txt", 'r')
            content = f.readlines()
            f.close()
            fee = float(content[2][12:])
            date = content[6]
        return fee, date
        
    

class Provider(Member):
    def __init__(self,name,number,address,city,state,zipCode):
        self.name = name
        self.number = number
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.accType = 1
    
    def getInfo(self):
        return self.name, self.number, self.address, self.city, self.state, self.zipCode

    def setInfo(self, logName, logNum):
        f = open("Login.txt","r")
        data = f.read()
        logIns = ast.literal_eval(data)
        f.close()
        if logNum in logIns:
            if logIns[logNum][7] == logName and logIns[logNum][6] == 1:
                print('Log in')
                self.__init__(Provider,logIns[logNum][0], logIns[logNum][1], logIns[logNum][2], logIns[logNum][3], logIns[logNum][4], logIns[logNum][5])
                return 1
            else:
                print('Incorrect name/number')
                return 0
        else:
            print('Incorrect name/number')
            return 0

    def checkAccount(logName,logNum):
        res = Member.setInfo(Member, logName, logNum)
        return res
    
    def setMemberDetails(memberName, fee, serviceDate):
        expDate = serviceDate.split('-')
        expDate[0] = str(int(expDate[0])+1)
        if int(expDate[0]) > 12:
            expDate[0] = '1'
            expDate[3] = str(int(expDate[3])+1)
        expDate =  '-'.join(expDate)
        path = dir_path+"\\"+memberName+"\\Details"
        if not os.path.exists(path):
            os.makedirs(path)
            f = open(path+"\\Details.txt", "w")
            f.write(f"Fee\n----------\nTotal fee: ${fee:.2f}\n")
            f.write("\n")
            f.write(f"Date of Expiration\n----------\n{expDate}")
        else:
            f = open(path+"\\Details.txt", 'r')
            content = f.readlines()
            f.close()
            fee = float(content[2][12:]) + fee
            f = open(path+"\\Details.txt", "w")
            f.write(f"Fee\n----------\nTotal fee: ${fee:.2f}\n")
            f.write("\n")
            f.write(f"Date of Expiration\n----------\n{expDate}")
            f.close()
        
    
    def makeClaim(self,serviceName, serviceCode, fee, comments):
        #serviceName = input('Service name (20 characters):\n')
        currentDate = now.strftime("%m-%d-%Y %H:%M:%S")
        serviceDate = now.strftime("%m-%d-%Y")
        #serviceCode = input('Service code (6 digit):\n')
        #fee = float(input('fee (up to $999.99):\n'))
        memberName = Member.getInfo(Member)[0]
        memberNumber = Member.getInfo(Member)[1]
        providerName = self.getInfo(Provider)[0]
        providerNumber = self.getInfo(Provider)[1]
        #comments = input('comments(100 characters)(optional):\n')
        
        path = dir_path+"\\"+memberName+"\\Claims"
        if not os.path.exists(path):
            os.makedirs(path)
        
        fileName = "Claim_"+ currentDate.replace(":","-").replace(" ","_")+".txt"
        f = open(path+"\\"+fileName, "w")
        f.write(f"Service Name: {serviceName}\nCurrent date and time: {currentDate}\nService Date: {serviceDate}\nService Code: {serviceCode}\nFee: ${fee:.2f}\nMember Name: {memberName}\nMember Number: {memberNumber}\nProvider Name: {providerName}\nProvider Number: {providerNumber}\nComments: {comments}\n")
        f.close()
        self.setMemberDetails(memberName,fee, serviceDate)
        newPath = dir_path+"\\"+providerName+"\\Claims"
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        shutil.copy2(path+"\\"+fileName,newPath+'\\'+fileName)
        return "Needs to be finished"
    
    def Suspend():
        name,number,address,city,state,zipCode,accCheck = Member.getInfo(Member)
        usernameLst = name.split(" ")
        userName = usernameLst[0][0]+usernameLst[-1]
        accCheck = -2
        found = False
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == 'Login.txt':
                    found = True
                    break
        if found == False:
            return "File does not exist"
        else:
            f = open("Login.txt","r")
            data = f.read()
            data = data.rstrip("\n")
            logIns = ast.literal_eval(data)
            logIns.update({number:[name,number,address,city,state,zipCode,accCheck,userName]})
            f.close()
            f = open("Login.txt","w")
            f.write("{\n")
            for k in logIns.keys():
                f.write(str(k))
                f.write(":")
                f.write(str(logIns[k]))
                f.write(",")
                f.write("\n")
            f.write("}")
            f.close()
        

    
class Manager():
    def __init__(self,name,number,address,city,state,zipCode):
        self.name = name
        self.number = number
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.accType = 0
    
    def getInfo(self):
        return self.name, self.number, self.address, self.city, self.state, self.zipCode
    
    def setInfo(self, logName, logNum):
        f = open("Login.txt","r")
        data = f.read()
        logIns = ast.literal_eval(data)
        f.close()
        if logNum in logIns:
            if logIns[logNum][7] == logName and logIns[logNum][6] == 0:
                print('Log in')
                self.__init__(Manager,logIns[logNum][0], logIns[logNum][1], logIns[logNum][2], logIns[logNum][3], logIns[logNum][4], logIns[logNum][5])
                return 2
            else:
                print('Incorrect name/number')
                return 0
        else:
            print('Incorrect name/number')
            return 0
    
    def addAccount(name,number,address,city,state,zipCode, accCheck=-1):
        found = False
        usernameLst = name.split(" ")
        userName = usernameLst[0][0]+usernameLst[-1]
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == 'Login.txt':
                    found = True
                    break
        if found == False:
            f = open("Login.txt","w")
            if accCheck == -1:
                logIns = {number:[name,number,address,city,state,zipCode,-1,userName]}
            else:
                logIns = {number:[name,number,address,city,state,zipCode,1,userName]}
            f.write("{\n")
            for k in logIns.keys():
                f.write(str(k))
                f.write(":")
                f.write(str(logIns[k]))
                f.write(",")
                f.write("\n")
            f.write("}")
            f.close()
        else:
            f = open("Login.txt","r")
            data = f.read()
            data = data.rstrip("\n")
            logIns = ast.literal_eval(data)
            logIns[number] = [name,number,address,city,state,zipCode,accCheck,userName]
            f.close()
            f = open("Login.txt","w")
            f.write("{\n")
            for k in logIns.keys():
                f.write(str(k))
                f.write(":")
                f.write(str(logIns[k]))
                f.write(",")
                f.write("\n")
            f.write("}")
            f.close()
    
    def removeAccount(number):
        found = False
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == 'Login.txt':
                    found = True
                    break
        if found == False:
            return "File does not exist"
        else:
            f = open("Login.txt","r")
            data = f.read()
            data = data.rstrip("\n")
            logIns = ast.literal_eval(data)
            logIns.pop(number)
            f.close()
            f = open("Login.txt","w")
            f.write("{\n")
            for k in logIns.keys():
                f.write(str(k))
                f.write(":")
                f.write(str(logIns[k]))
                f.write(",")
                f.write("\n")
            f.write("}")
            f.close()
        return "Needs to be finished"
        
    def updateAccount(name,number,address,city,state,zipCode, accCheck=-1):
        usernameLst = name.split(" ")
        userName = usernameLst[0][0]+usernameLst[-1]
        found = False
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file == 'Login.txt':
                    found = True
                    break
        if found == False:
            return "File does not exist"
        else:
            f = open("Login.txt","r")
            data = f.read()
            data = data.rstrip("\n")
            logIns = ast.literal_eval(data)
            logIns.update({number:[name,number,address,city,state,zipCode,accCheck,userName]})
            f.close()
            f = open("Login.txt","w")
            f.write("{\n")
            for k in logIns.keys():
                f.write(str(k))
                f.write(":")
                f.write(str(logIns[k]))
                f.write(",")
                f.write("\n")
            f.write("}")
            f.close()

    def addClaim(self, memName, memNum, proName, proNum, serviceName, serviceCode, fee, comments):
        Member.setInfo(Member, memName, memNum)
        Provider.setInfo(Provider, proName, proNum)
        #serviceName = input('Service name (20 characters):\n')
        currentDate = now.strftime("%m-%d-%Y %H:%M:%S")
        serviceDate = now.strftime("%m-%d-%Y")
        #serviceCode = input('Service code (6 digit):\n')
        #fee = float(input('fee (up to $999.99):\n'))
        memberName = Member.getInfo(Member)[0]
        memberNumber = Member.getInfo(Member)[1]
        providerName = Provider.getInfo(Provider)[0]
        providerNumber = Provider.getInfo(Provider)[1]
        #comments = input('comments(100 characters)(optional):\n')
        
        path = dir_path+"\\"+memberName
        if not os.path.exists(path):
            os.makedirs(path)
        
        fileName = "Claim_"+ currentDate.replace(":","-").replace(" ","_")+".txt"
        
        f = open(path+"\\"+fileName, "w")
        f.write(f"Service Name: {serviceName}\nService Date: {serviceDate}\nService Code: {serviceCode}\nFee: ${fee:.2f}\nMember Name: {memberName}\nMember Number: {memberNumber}\nProvider Name: {providerName}\nProvider Number: {providerNumber}\nComments: {comments}\n")
        f.close()
        return "Needs to be finished"
     
    def removeClaim(self,memberName,fileName):
        found = False
        path = dir_path+"\\"+memberName
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == fileName+'.txt':
                    found = True
                    break
        if found == False:
            return "File does not exist"
        else:
            os.remove(path+"\\"+fileName+".txt")
        return "Needs to be finished"
         
    def updateClaim(self,memName,memNum,proName, proNum, fileName, serviceName, serviceCode, fee, comments):
        found = False
        Member.setInfo(Member, memName, memNum)
        Provider.setInfo(Provider, proName, proNum)
        path = dir_path+"\\"+memName
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == fileName+'.txt':
                    found = True
                    break
        if found == False:
            return "File does not exist"
        else:
            #serviceName = input('Service name (20 characters):\n')
            currentDate = now.strftime("%m-%d-%Y %H:%M:%S")
            serviceDate = now.strftime("%m-%d-%Y")
            #serviceCode = input('Service code (6 digit):\n')
            #fee = float(input('fee (up to $999.99):\n'))
            memberName = Member.getInfo(Member)[0]
            memberNumber = Member.getInfo(Member)[1]
            providerName = Provider.getInfo(Provider)[0]
            providerNumber = Provider.getInfo(Provider)[1]
            #comments = input('comments(100 characters)(optional):\n')
            f = open(path+"\\"+fileName, "w")
            f.write(f"Service Name: {serviceName}\nService Date: {serviceDate}\nService Code: {serviceCode}\nFee: ${fee}\nMember Name: {memberName}\nMember Number: {memberNumber}\nProvider Name: {providerName}\nProvider Number: {providerNumber}\nComments: {comments}\n")
            f.close()
        return "Needs to be finished"    
    
    def report(self,memberName,memberNumber, month,srtDay,endDay,year):
        usernameLst = memberName.split(" ")
        userName = usernameLst[0][0]+usernameLst[-1]
        path = dir_path+"\\"+memberName
        f = open(path+"\\Report.txt","w")
        Member.setInfo(Member, str(userName), memberNumber)
        name,number,address,city,state,zipCode,status = Member.getInfo(Member)
        f.write(f"Member name: {name}\nMember number: {number}\nMember street address: {address}\nMember city: {city}\nMember state: {state}\nMember ZIP code: {zipCode}\n")
        day = srtDay
        end = int(endDay)-int(srtDay)
        for _ in range(int(srtDay), (int(srtDay)+end)+1):
            if day > 28 and int(month)==2:
                if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
                    if day > 29:
                        day = 1
                        month += 1
                else:
                    day = 1
                    month += 1
            elif day > 30 and (int(month)%2==1):
                day = 1
                month += 1
            elif day > 31 and (int(month)%2==0):
                day = 1
                month += 1
            
            if month > 12:
                month = 1
                year += 1
            for filename in glob.glob(path+"\\Claims\\Claim_"+str(month)+'-'+str(day)+'-'+str(year)+'*'):
                f2 = open(filename, 'r')
                content = f2.readlines()
                f2.close()
                if content != []:
                    serviceDate = content[2]
                    providerName = content[7]
                    serviceName = content[0]
                    f.write('----------\n'+serviceDate+providerName+serviceName)
            day += 1
        f.write(f'----------\nTotal fee: ${Member.getDetails(Member)[0]}\n')
        f.close()
        #shutil.copy2(path+"\\Report.txt",dir_path+"\\SReport.txt")
    
    def summaryReport(providerName,providerNumber, month,srtDay,endDay,year):
        usernameLst = providerName.split(" ")
        userName = usernameLst[0][0]+usernameLst[-1]
        path = dir_path+"\\"+providerName
        f = open(path+"\\SummaryReport.txt","w")
        app = 0     # store total number of appointments
        tot_fee = 0 # store cumulative fee
        Provider.setInfo(Provider, userName,providerNumber)
        name,number,address,city,state,zipCode = Provider.getInfo(Provider)
        f.write(f"Provider name: {name}\nProvider number: {number}\nProvider street address: {address}\nProvider city: {city}\nProvider state: {state}\nProvider ZIP code: {zipCode}\n")
        day = srtDay
        end = int(endDay)-int(srtDay)
        for _ in range(int(srtDay), (int(srtDay)+end)+1):
            if day > 28 and int(month)==2:
                if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
                    if day > 29:
                        day = 1
                        month += 1
                else:
                    day = 1
                    month += 1
            elif day > 30 and (int(month)%2==1):
                day = 1
                month += 1
            elif day > 31 and (int(month)%2==0):
                day = 1
                month += 1
            
            if month > 12:
                month = 1
                year += 1
            for filename in glob.glob(path+"\\Claims\\Claim_"+str(month)+'-'+str(day)+'-'+str(year)+'*'):
                f2 = open(filename, 'r')
                content = f2.readlines()
                f2.close()
                if content != []:
                    currentDate = content[1]
                    serviceDate = content[2]
                    memberName = content[5]
                    memberNumber = content[6]
                    fee = content[4][6:]
                    serviceCode = content[3]
                    app +=1
                    tot_fee += float(fee.rstrip("\n"))
                    f.write('----------\n'+serviceDate+currentDate+memberName+memberNumber+serviceCode+"$"+fee)
            day += 1
        f.write(f'----------\nTotal Consultations: {app}\nTotal Fee: %.2f\n' % (tot_fee))
        f.close()
        
    
    


# Provider.setInfo(Provider,'Sam', 1233)
# Provider.checkAccount('Bob', 1234)
# Provider.makeClaim(Provider)
# Member.setInfo(Member, "Bob", 1234)
# Member.getDetails(Member)
#Manager.report(Manager, "Bob Laker", 804452505, 11, 15, 16,2022)
# Manager.summaryReport("Sam", 1233)
# print(now)
# print(dt_string)
##Manager.removeAccount(1232)


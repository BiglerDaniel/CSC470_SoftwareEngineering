'''
Uploaded to the github of BiglerDaniel
CSC470 Software Engineering in fall of 2022
For the ChocAnon Project
Project Group Members: Daniel Bigler, Tivon Brown, Carley Brinkley

This code uses datetime and user input.
Other than that, this code runs independently.
'''
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H:%M")
def makeClaim():
    '''
    Was going to make everything their respective data type,
    but for now they are strings, unless they need to be changed

    Service name (20 characters): string
    Date of service(yyyy-mm-dd): date
    Current date and time (yyyy-mm-dd hh:mm): date
    Service code (6 digit): int
    fee (up to $999.99): int
    member name(25 characters): string
    member number(9 digits):int{key}
    provider name(25 characters): string
    provider number(9 digits): int {key}
    comments(100 characters) (optional): string
    '''
    serviceName = input('Service name (20 characters):\n')
    serviceDate = input('Date of service(yyyy-mm-dd):\n')
    serviceCode = input('Service code (6 digit):\n')
    fee = input('fee (up to $999.99):\n')
    memberName = input('member name(25 characters):\n')
    memberNumber = input('member number(9 digits):\n')
    providerName = input('provider name(25 characters):\n')
    providerNumber = input('provider number(9 digits):\n')
    comments = input('comments(100 characters)(optional):\n')
    
    fileName = memberName.replace(" ", "") + "_" + dt_string.replace("/", "-").replace(":","-").replace(" ","_")
    
    f = open(fileName, "w")
    f.write(f"Service Name: {serviceName}\nService Date: {serviceDate}\nService Code: {serviceCode}\nFee: {fee}\nMember Name: {memberName}\nMember Number: {memberNumber}\nProvider Name: {providerName}\nProvider Number: {providerNumber}\nComments: {comments}\n")
    f.close()
    
def main():
    makeClaim()

if __name__ == '__main__':
    main()

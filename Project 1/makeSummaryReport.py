'''
Uploaded to the github of BiglerDaniel
CSC470 Software Engineering in fall of 2022
For the ChocAnon Project
Project Group Members: Daniel Bigler, Tivon Brown, Carley Brinkley

This code uses datetime and user input.
This code's input is a file made by makeReport.py
If thier Report exists, just enter the member's name.
'''
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d_%H-%M")

def makeSummaryReport():
    mem_name = input("Enter the member's name:\n")
    mem_name = mem_name.replace(" ", "").lower()
    app = 0     # store total number of appointments
    tot_fee = 0 # store cumulative fee
    
    with open(mem_name, 'r') as report:
        for L in report:
            if "Service Date: " in L:
                app += 1
            elif "Fee:" in L:
                tot_fee += float(L.replace("Fee:","").replace(" ","").replace("$","").strip())
                
    fileName = mem_name + "_SR_" + dt_string.replace("/", "-").replace(":","-").replace(" ","_")
    f = open(fileName, "w")
    f.write(f'Consultations: {app}\nTotal Fee: %.2f\n' % (tot_fee))
    f.close()
    
def main():
    makeSummaryReport()

if __name__ == '__main__':
    main()

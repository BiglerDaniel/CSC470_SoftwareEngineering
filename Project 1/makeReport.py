'''
Uploaded to the github of BiglerDaniel
CSC470 Software Engineering in fall of 2022
For the ChocAnon Project
Project Group Members: Daniel Bigler, Tivon Brown, Carley Brinkley

This code uses os.path's exists, itertools's islice, and user input.
This code's input is a file made by makeClaim.py
Enter the filename of the claim, and the member's address if they don't have a recorded report
'''
from os.path import exists
from itertools import islice
'''
format:
Member's info:
    name (automatic)
    member id (automatic)
    street address (input)
    city (input)
    state (input)
    zip (input)
----------
date of consultation
provider
service
fee
(repeat from and including -'s to fee)
'''
def makeReport():
    claimName = input("To make a report, enter the filename of the claim to read from:\n")
    with open(claimName, 'r') as fn:
        line_numbers = [4, 5, 1, 6, 0, 3] #the numbers are in order of how they will be put in the file, but are sadly sorted in numerical order
                                          #called 0,1,2,3,4,5 when writing to file for 0,1,3,4,5,6 in line_numbers respectively
        lines = []
        for i, line in enumerate(fn):
            if i in line_numbers:
                lines.append(line.strip())
            elif i > 10:
                break
    fileName = lines[3].replace("Member Name: ", "").replace(" ","").lower()
    file_exists = exists(fileName)
    
    f = open(fileName, "a")

    #if their isn't a report, make one with the member info at the top
    #otherwise, append new info
    if file_exists == False:
        #MemberName -> 3
        #MemberNumber -> 4
        mem_streetAddress = input("Enter Member's Street Address:\n")
        mem_city = input("Enter Member's City of Residence:\n")
        mem_state = input("Enter Member's State of Residence:\n")
        mem_zip = input("Enter Member's Zip Code:\n")

        f.write(lines[3] + '\n' + lines[4] + f'\nStreet: {mem_streetAddress}\nCity: {mem_city}\nState: {mem_state}\nZip: {mem_zip}\n')
    f.write('----------\n' + lines[1] + '\n' + lines[5] + '\n' + lines[0] + '\n' + lines[2] + '\n')
    f.close()
def main():
    makeReport()

if __name__ == '__main__':
    main()

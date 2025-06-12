# output video is also display i hope this is the best i can do sir 
import json

with open('test.json', 'r') as file1:
    data1 = json.load(file1)
print("========================================================>")
print("To manully provide the data from the user Please Click 1 ")
print("========================================================>")
print("To take the json file data  Please Click 2 ")
print("========================================================>")
m=int(input('Enter your chice 1 or 2 '))
if(m==1):
    e=0
    b=int(input('enter the Total month Income '))
    print("========================================================>")
    g=int(input('enter the total number expences u want to add '))
    print("========================================================>")
    for i in range(0,g):
        m=input("enter the expences like Rent or Shopping or Bills or Travel ")   
        print("========================================================>") 
        if(m=='Rent' or m=='Shopping' or m=='Bills' or m=='Travel'):
            d=int(input('enter the amount'))
            e=d+e
        else:
            print('Please enter the proper foramt and start from the starting ')     
    print('Total Monthly Summary  is',b-e)
    
if(m==2):
    r=0

    for i in data1:
        r=r+i["rent"]+i["Shopping"]+i["Food"]+i["Travel"]
        print("========================================================>")
        print("Total Monthly Summary",i["Name"],"the user have",i["Salary"]-r)
        print("========================================================>")

 




                               



 
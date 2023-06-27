# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd

def create():
    print("CREATE")

def read():
    print("READ")
    student = pd.read_csv('alarm_db.csv')
    print(student)

def update():
    print("UPDATE")

def delete():
    print("UPDATE")

def menu():
    print(f"1.\tCreate\n2.\tRead\n3.\tUpdate\n4.\tDelete\n")
    reply = input("What u want?: \n")

    

    ireply = int(reply)
    
    

    if(ireply == 1):
        create()
    elif(ireply == 2):
        read()
    elif(ireply == 3):
        update()
    elif(ireply == 4):
        delete()
    else:
        print("weirdo man ka")



    print("\n\n")
    menu()

menu()
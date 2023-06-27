# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd

def create():
	print("CREATE ---------------------------------------")

def read():
	print("READ -----------------------------------------")
	student = pd.read_csv('alarm_db.csv')
	print(student)
	print("----------------------------------------------")

def update():
	print("UPDATE ---------------------------------------")

def delete():
	print("DELETE ---------------------------------------")

def menu():
	print(f"1.\tCreate\n2.\tRead\n3.\tUpdate\n4.\tDelete\n")
	reply = input("What u want?: \n")



	if(reply == '1'):
		create()
	elif(reply == '2'):
		read()
	elif(reply == '3'):
		update()
	elif(reply == '4'):
		delete()
	else:
		print("weirdo man ka")



	print("\n\n")
	menu()

menu()
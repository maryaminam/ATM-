"""import pandas as pd
import datetime

x=datetime.datetime.now()
# check if verified;
verified = False
print()
print("-----------------------------------")
print("Welcome to Kashkoal Banking System")
print("-----------------------------------")
print()
print()

class info():
    account_no=int(input("Enter Account Number: "))
    password=int(input("Enter password: "))

    df=pd.read_csv(r'project.csv')
    # print(df)

        
class Entry(info):
    length=len(info.df)
    for i in range(length):
        if info.account_no==info.df.loc[i,"Acc. No"] and info.password==info.df.loc[i,"Password"]:
            print("Welcome ",(info.df.loc[i,"Name"]))
            print("Your Current Balance is: ",(info.df.loc[i,"Balance"]))
            new_balance=(info.df.loc[i,"Balance"])
            verified = True
            print("--------------------------------------------------")

            input=input("Press 1 for Saving Account and 2 for Current Account: ")
            if input=="1":
                print("Welcome to the Saving Account!")
            elif input=="2":
                print("Wecome to the Current Account!")
            else:
                print("You have entered the wrong number! ")
                exit()
    if verified != True:
            print ("Account name or password is incorrect!")
            print ("--------------------------------------------------")
            exit()


def CashWithdrawal():
    amount=eval(input("Enter the amount you want to withdraw: "))
    if amount>Entry.new_balance:
        print("The Entered amount exceeds the current balance!")
        exit()
    
    elif amount>50000:
        print("The Maximum Amount to withdraw is 50,000")
        exit()
        
    elif amount<500:
        print("The Minimum Amount to withdraw is 500")
        exit()

    subtraction = Entry.new_balance-amount
    print("Money Withdrawn, New Balance is: ",subtraction)
    info.df.replace (to_replace= Entry.new_balance, value=subtraction, inplace=True)
    info.df.to_csv(r'new11.csv', index=False)
    print(x)
    
def moneyTransfer():
    amount=eval(input("Enter the amount you want to transfer:"))
    if amount>Entry.new_balance:
        print("The Entered amount exceeds the current balance!")
        exit()
    elif amount>99999:
        print("Maximum transferable amount is can only be 5 digit.")
        exit()
    elif amount<100:
        print("Minimum transferable amount is 100.")
        exit()
    subtraction = Entry.new_balance-amount
    info.df.replace (to_replace= Entry.new_balance, value=subtraction, inplace=True)
    info.df.to_csv(r'new11.csv', index=False)
    address=eval(input("Enter the 16 digit conventional/IBAN number to which the money is to be transfered:"))
    print("Money Transfered, New Balance is: ",subtraction)
    print(x)

def cashDeposit():
    amount=eval(input("Enter the amount you want to deposit:"))
    print("Insert the money from the receving area.")
    print("The money has been deposited.")
    addition = Entry.new_balance+amount
    info.df.replace (to_replace= Entry.new_balance, value=addition, inplace=True)
    info.df.to_csv(r'new11.csv', index=False)
    print("Money Deposited, New Balance is: ",addition) 
    print(x)

#def balanceInquiry():

class Saving(Entry):
    print("--------------------------------------------------")
    print("What do you want to perform?")
    print("             -               ")
    print("Press 1 for Cash Withdrawal")
    print("Press 2 for Money Transfer")
    print("Press 3 for Cash Deposit")
    print("Press 4 for Balance Inquiry")

    input_saving=input("Enter the number here: ")
    if input_saving=="1":
        CashWithdrawal()
    elif input_saving=="2":
        moneyTransfer()
    elif input_saving=="3":
        cashDeposit()"""

from distutils.log import Log
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import Canvas, Text

from setuptools import Command
# calling face_recog for login
from face_recog import *
import os

root = ctk.CTk()
root.title("ATM System Project")

canvas = tk.Canvas(root, height=700,width=700,bg='#212325')
canvas.pack()


def Login():
    canvas.delete('all')
    canvas.create_text(300, 40, text="Enter ID", fill="#b2bec3", font=('Symbola 20 bold'))
    canvas.pack()

    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

    

    player_name = Entry(frame)
    player_name.pack(pady=50)
    

    ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=Login_file).pack()
    

def Login_file():
    information.login()




def info():
    account_no=int(input("Enter Account Number: "))
    password=int(input("Enter password: "))

    df=pd.read_csv(r'project.csv')
    # print(df)

def withdrawAmount():
    canvas.delete('all')
    canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
    canvas.pack()
    

    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
     
    def printValue():
        pname = int(player_name.get())
        if pname>=500:
            Label(frame, text=f'{pname}rs added to your account!', pady=20, fg='white',bg='#2a2d2e').pack()
            

        else:
            Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()
            
        df=pd.read_excel(r'project.xlsx')
        print(df)
        df.dropna(inplace = True)

        before= df.dtypes

        df["Acc. No"]= df["Acc. No"].astype(int)
    
        account=df["Acc. No"]
        print(account)

    player_name = Entry(frame)
    player_name.pack(pady=50)

    ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=printValue).pack()


def moneyTransfer():

    canvas.delete('all')
    canvas.create_text(300, 40, text="Enter The Amount", fill="#b2bec3", font=('Symbola 20 bold'))
    canvas.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)
    def transfer():
        pname = int(player_name.get())
        if pname>=500:
            Label(frame, text=f'{pname}rs Transferred!', pady=20, fg='white',bg='#2a2d2e').pack()
        else:
            Label(frame,text="Enter the amount more than 500!", pady=20, fg='white',bg='#2a2d2e').pack()

            
        
        

    player_name = Entry(frame)
    player_name.pack(pady=50)

    ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=transfer).pack()



verified=False
    


def PageFour():
    canvas.delete('all')
    canvas.create_text(300, 40, text="Select The Action You Want To Perform", fill="#b2bec3", font=('Symbola 20 bold'))
    canvas.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    withdrawButton = ctk.CTkButton(frame, text="Cash Withdrawal",pady=50, padx=10 , bg="#16a085", command=withdrawAmount)
    withdrawButton.pack()


    balanceButton = ctk.CTkButton(frame, text="Balance inquiry",pady=50, padx=10 , bg="#16a085")
    balanceButton.pack()

    transferButton = ctk.CTkButton(frame, text="Transfer Money",pady=50, padx=10 , bg="#16a085", command=moneyTransfer)
    transferButton.pack()





# def pageThree():
#     canvas.delete('all')
#     canvas.create_text(300, 40, text="Enter PIN", fill="#b2bec3", font=('Symbola 20 bold'))
#     canvas.pack()


#     frame = tk.Frame(root, bg='#2a2d2e')
#     frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)

#     player_name = Entry(frame)
#     player_name.pack(pady=50)

#     ctk.CTkButton(frame,text="Enter", padx=10, pady=5).pack()

#     if player_name==info.df.loc["Acc. No"] and info.password==info.df.loc["Password"]:
#         ctk.CTkButton(frame,text="Enter", padx=10, pady=5,command=PageFour).pack()

    




# defining page one

class PageOne:
    canvas.create_text(300, 40, text="Choose Login Method", fill="#b2bec3", font=('Symbola 25 bold'))
    canvas.pack()


    frame = tk.Frame(root, bg='#2a2d2e')
    frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    PinButton = ctk.CTkButton(frame, text="PIN", pady=10, padx=10 , bg="#16a085",)
    PinButton.place(x=100 ,y=130)



    FaceButton = ctk.CTkButton(frame, text="Biometric",pady=10, padx=10 , bg="#16a085", command=Login)
    FaceButton.place(x=100,y=200)



# def PageTwo():


root.mainloop()





# Saving Account
    # canvas.create_text(300, 40, text="Choose Your Account Type", fill="#b2bec3", font=('Symbola 25 bold'))
    # canvas.pack()


    # frame = tk.Frame(root, bg='#2a2d2e')
    # frame.place(relheight=0.8, relwidth=0.6, relx=0.2,rely=0.15)



    # savingButton = ctk.CTkButton(frame, text="Saving Account", pady=10, padx=10 , bg="#16a085", command=pageThree)
    # savingButton.place(x=100 ,y=130)


    # currentButton = ctk.CTkButton(frame, text="Current Account",pady=10, padx=10 , bg="#16a085", command=pageThree)
    # currentButton.place(x=100,y=200)
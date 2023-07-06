import pandas as pd
data=pd.read_csv("project.csv")

print()
print()
print("-----------------------------------")
print("Welcome to Kashkool Banking System")
print("-----------------------------------")
print()
print()
print("Place your face near the camera\n         or")
pin=eval(input("Enter your login pin:"))
print("\n  \n  \n")
print("Select your type of account:\na)Savings (1)\nb)Current (2)")
account_type=eval(input("Enter 1 or 2:"))


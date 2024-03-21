Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to the tip calculator")
Welcome to the tip calculator
>>> T_bill = input("What was the total bill? $")
What was the total bill? $232.24
>>> t_bill = float(T_bill)
>>> P_tip =  input("What percentage tip would you like to give? 10, 12, or 15? ")
... 
What percentage tip would you like to give? 10, 12, or 15? 12
>>> p_tip = int(P_tip)
>>> Spl_bill = input("How many people to split the bill? ")
How many people to split the bill? 7
>>> spl_bill = int(Spl_bill)
>>> tip_money = t_bill*p_tip/100
>>> Tip_Money = float(tip_money)
>>> total_bill = Tip_Money + t_bill
>>> Total_Bill = float(total_bill)
>>> Each_person = Total_Bill/spl_bill
>>> Each_Person = float(Each_person)
>>> e_p=round(Each_Person,2)
>>> print(f"Each person sgould pay:round{e_p}")
Each person sgould pay:round37.16
>>> print(f"Each person sgould pay:{e_p}")
Each person sgould pay:37.16

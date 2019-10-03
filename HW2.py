#Problem 1
#Introduction
from tabulate import tabulate
name = input("What is your name")
print(f"Welcome to Denny's Market {name}! We have the following items for sale")
print("T-shirt $18.95 15% off \nChips $1.79 15% off \nCoke $2.99")

#collect user input
tshirts = int(input("How many T-shirts do you want?"))
chips = int(input("How many bags of potato chips?"))
coke = int(input("What about 12-pack Coke?"))
payment = int(input("Please enter your payment:"))

#Calculate everything
tshirt_total = tshirts * 18.95
chip_total = chips * 1.79
coke_total = coke * 2.99
coke_dep = 1.20 * coke
total = tshirt_total + chip_total + coke_total + coke_dep
chip_discount = (chips * .15) 
tshirt_discount = (tshirts * .15)
total_discount = (tshirts - tshirt_discount) + (chips - chip_discount)
tax = (total_discount + total) * .06
tax_total = (total_discount + total) - tax
change = payment - tax_total

#Print receipt using tabulate
print(f"{name}, here is your receipt:")
print(tabulate([["Item","Unit Price","How Many","Cost"],["T-shirt",18.95, tshirts, tshirt_total]
,["Chips",1.79, chips, chip_total],["Coke",2.99, coke, coke_total],["Deposit", " ", " ",coke_dep],
 [" ", " ", " "," "],["Subtotal", " ", " ",total], ["Discount", " ", " ",total_discount],
 ["Tax", " ", " ",tax],[" ", " ", " ", " "],["Total", " ", " ",tax_total],["Payment", " ", " ",payment],
 ["Your change", " ", " ",change]],headers="firstrow"))
 
 #Problem 2
 #include <bits/stdc++.h> 
n = int(input("Enter the max column number (Must be positive odd integer number. Enter -1 for exit):"))
print(n)
for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()
if n == -1:
    print("Thanks for using my program")
    
#Problem 3
import random

gridSize = 5
minNum = 1
maxNum = 50
cards = 1

for h in range(cards):
    card = []
    randRange = range(minNum, maxNum)
    card = random.sample(randRange, gridSize * gridSize)
    for i in range(gridSize):
        string = ""
        for j in range(gridSize):
            string +=  str(card[i + j * gridSize]) + "t"
        print(string)  

    print("n")


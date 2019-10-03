'''
Problem 1
'''
Width = int(input("What is the width?"))
Height = int(input("What is the height?"))
print("The area is" , Width * Height)
'''
Problem 2
'''
first_name = input("What is your first name?")
last_name = input("What is your last name?")
print(last_name[::-1] , first_name[::-1])
'''
Problem 3
'''
number = int(input("Please enter a number."))
if number > 0:
    print("The number" , number , "is positive")
else:
    print("The number" , number , "is negative")
'''
Problem 4
'''
# Count vowels in a different way 
# Using dictionary 
def count_vowel(string, vowels): 
      
    string = string.casefold() 
      
    count = {}.fromkeys(vowels, 0) 
       
    for character in string: 
        if character in count: 
            count[character] += 1    
    return count 
      
vowels = 'aeiou'
sentence = input("Please enter a sentence")
print (count_vowel(sentence, vowels))
'''
Problem 5
'''
n = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of",n,"is",factorial) 
'''
Problem 6
'''
with open('numbers.txt', 'r') as f:
    longest_number = f.readline()
    f.seek(0)
    shortest_number = f.readline()
    for number in f:
        if len(number) > len(longest_number):
            longest_number = number
        if len(number) < len(shortest_number):
            shortest_number = number
    
    print(longest_number)
    print(shortest_number)
'''
Problem 7
'''
# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
           
    elif str1[-2:] == "AM": 
        return str1[:-2] 
        
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
       
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("10:34:55 AM"))

#Write a Python Program to print name of the day according to 
# its number entered by user.
"""
num = int(input("Enter the number to print its corresponding day:"))

if num == 1:
    print("Sunday")
elif num == 2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wednesday")
elif num == 5:
    print("Thrusday")
elif num == 6:
    print("Friday")
elif num == 7:
    print("Saturday")
"""

#Write a program to print all the numbers from 50 to 100 and skip all even numbers. 
"""
listt = []
for i in range(50,101):
    if i % 2 == 0:
        continue
    else:
        listt.append(i)

print("List of numbers is :",listt)
"""

#Write a program to print n natural numbers.
"""
n = int(input("Enter the value of n:")) 
for i in range(1,n+1):
    print(i)

"""

#Also write a program to check for the leap year.
"""
year = int(input("Enter the Year :"))

if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
    print(f"{year} is Leap year.")

else:
    print(f"{year} is not a leap year.")
"""

# Write a Program to print sum of the series: 
"""
# i) 1+4+9+16+25+………………+100 
sum = 0
for i in range(1,11):
    sum = sum + (i**2)

print(sum)

# ii)1+9+27+64+125+……………+1000 
sum1 = 0
for i in range(1,11):
    sum1 = sum1 + (i**3)
print(sum1)
"""

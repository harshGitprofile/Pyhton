#6.	Write a program to convert kilometers into meters and centimeters. 
km = int(input("Enter Distance measure in Kilometer : "))
meter = (km * 1000)
cm = (meter * 100)
print(f"{km}km = {meter}meter.\n{km}km = {cm}cm.")

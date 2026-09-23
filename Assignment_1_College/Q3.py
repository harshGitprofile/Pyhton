"""
3.	Write a program to input height and width from user and 
calculate the area and perimeter of a rectangle. 
"""

len = int(input("Enter the length of Rectangle in cm:"))
wid = int(input("ENter the Breathe of Rectangle in cm:"))
print(f"Area of rectangle of length {len}cm and breathe {wid}cm is {len*wid}cm^2")

print(f"Perimeter of rectangle of length {len}cm and breathe {wid}cm is {2*(len*wid)}cm")
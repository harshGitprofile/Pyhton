"""
7.	Write a program to swap two numbers: 
•	using a third variable 
•	without using a third variable 
"""
a = int(input("Enter the value of 'a' : "))
b = int(input("Enter the value of 'b' : "))

temp = a
a = b
b = temp
print(f"Using third variable After swap :\na = {a}\nb = {b}")

"""
a = 2  | b = 3
a = a + b --> a = 5
b = a - b --> b = 2
a = a - b --> a = 3
"""
a = a + b
b = a - b
a = a - b
print(f"After Swap using Third Variable :\na = {a}\nb = {b}")
print("NOTE : Above swap is of swapped no. so it will gve you original value.")



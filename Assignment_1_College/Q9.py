#9.	Write a program to calculate simple interest.
# si = P * R * T / 100
print("Simple interest Calculator.")
P = int(input("Enter the value of Principle Amount: "))
R = int(input("Enter the value of Rate of interest : "))
T =int(input("Enter the value of Time period : "))
si = ((P*R*T) / 100)
print(f"Simple Interest of Above Credentials is {si}")


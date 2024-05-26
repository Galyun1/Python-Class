x = int(input("Enter the number:"))

for i in range(x):
    print(" "*(x-(i+1)), end = "")
    print("*"*(i+1))


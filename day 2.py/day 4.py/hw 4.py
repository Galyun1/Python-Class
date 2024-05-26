x = int(input("Enter the number:"))
cnt = x*2-1

for i in range(x):
    print(" "*i, end ="")
    print("*"*cnt)
    cnt-=2
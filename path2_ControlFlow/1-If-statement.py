#https://docs.python.org/3/tutorial/controlflow.html#if-statements

a = 1
b = 5
if a > b :
    print(f"{a} is Greatest number between{a,b}")
else:
    print("Not printing")
    #print(f"{b} is Greatest number between{a, b}")

x = int(input("Please input a number - "))
if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
else:
    print("More")

try:
    a= int(input("enter a number:"))
except ValueError:
    print("please enter a number")
else:
    print("square if the number is:",a*a)
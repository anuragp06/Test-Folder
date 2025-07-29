try:
    #user input for division
    numerator = int(input("enter numerator:"))
    denominator = int(input("enter denominatior:"))

    #division operation
    result = numerator / denominator

except ZeroDivisionError:
    print("error: Division by zero is not allowed.")
except ValueError:
    print
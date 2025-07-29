# Function to check if a number is a perfect number
def is_perfect_number(n):
    sum = 0  # Initialize sum to store the sum of divisors
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

# Calling the function from the main block
if __name__ == "__main__":
    mynumber = int(input("Enter a number: "))
    
    if is_perfect_number(mynumber):
        print(f"{mynumber} is a perfect number")
    else:
        print(f"{mynumber} is not a perfect number")

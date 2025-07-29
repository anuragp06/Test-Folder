def write_file():
    try:
        with open('employees.txt', 'w') as file:
            file.write("ID,Name,Department,Salary\n")
            file.write("101,John Smith,Engineering,45000\n")
            file.write("103,Emily Johnson,Finance,70000\n")
        print("Data written successfully.\n")
    except Exception as e:
        print(f"Error writing file: {e}\n")


def read_file():
    try:
        with open('employees.txt', 'r') as file:
            print("Reading file contents:\n")
            for line in file:
                print(line.strip())
        print()
    except FileNotFoundError:
        print("Error: File not found.\n")
    except Exception as e:
        print(f"Error reading file: {e}\n")


def append_file():
    try:
        with open('employees.txt', 'a') as file:
            file.write("104,Michael Brown,Marketing,62000\n")
        print("New employee added successfully.\n")
    except Exception as e:
        print(f"Error appending file: {e}\n")


def main():
    while True:
        print("Employee File Manager")
        print("1. Write File")
        print("2. Read File")
        print("3. Append File")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            write_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            append_file()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1–4.\n")


if __name__ == "__main__":
    main()

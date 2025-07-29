## writing employrr details to a file
with open('employees.txt','w') as file:
    file.write("ID,Name,Department,Salary\n")
    file.write("101,John smith,enginereer,45000\n")
    file.write("103,emily johnson,fnance,70000\n")




    try:
        with open('employees.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except  FileNotFoundError:
        print("Eroor:file not found")


        #adding new employee data
    with open('employee.txt', 'a') as file:
        file.write("104,michael brown,marketing,62000\n")

    print("new employee added successfully")

    #handling exceptions in file handling

try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("error:the file does not exist")
    
import csv

data = [
    ["Name","age","grade"]
    ["anurag",22,"a"]
    ["hani",21,"b"]
    


]

with open('studentdata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


#read the csv file

with open('studentdata.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
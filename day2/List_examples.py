fruits=["apple","banana","cherry","dates"]
 
#1] .append():
fruits.append("mango")
print(fruits)
 
#2] .pop:
removed_fruit=fruits.pop(2)
print("Removed fruits is ",removed_fruit)
print(fruits)
 
#3] .sort():
fruits.sort()
 
#4] .reverse():
fruits.reverse()
 
#5] .count():
count=fruits.count("banana")
 
#6] .index():
index_of_dates = fruits.index("dates")
 
print("List of fruits are ",fruits)
print("Count of banana is ",count)
print("Index of 'Dates' is ",index_of_dates)
 
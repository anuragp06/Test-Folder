# set of items
numbers = {1, 2, 3, 4, 5}

#add()- adds an element to the set
numbers.add(6)

#remove() removes an element from the set
numbers.remove(4)

#discard()-removes an element but soed not raise an error if not found
numbers.discard(7)

#union() returns a set containing all elements from both sets
another_set = {5, 6, 7, 8}
union_set = numbers.union(another_set)

#intersection() returns a set containing only common elements
intersection_set = numbers.intersection(another_set)

#clear() removes all elements from the set
numbers.clear()

print("union of sets:", union_set)
print("intersection of sets:",intersection_set)
print("number set after clear:", numbers)
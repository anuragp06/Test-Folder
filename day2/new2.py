def calculate_bill(price,quantity,discount=0):
    total = price * quantity
    final_amount=total-(total * discount/100)
    return final_amount

bill=calculate_bill(price=100,quantity=3,discount=10)
print("final bill amount:",bill)
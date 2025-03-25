total = float(input("Enter the total purchase amount : "))
if total > 500:
    discount = total * 0.1
    total -= discount
    print("Discount : $", discount)
print("Total cost : $", total)

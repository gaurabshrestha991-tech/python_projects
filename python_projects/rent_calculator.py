# Rent Calculator Project

print("          Rent Calculator ")

rent = float(input("Enter total rent: "))
electricity = float(input("Enter electricity bill: "))
water = float(input("Enter water bill: "))
internet = float(input("Enter internet bill: "))
people = int(input("Enter number of people: "))

total = rent + electricity + water + internet
share = total / people

print("         Rent Summary")

print(f"Rent: Rs.{rent: 2f}")
print(f"Electricity: Rs/{electricity: 2f}")
print(f"Water: Rs. {water:.2f}") 
print(f"Internet: Rs. {internet:.2f}") 
print(f"Total Cost: Rs. {total:.2f}") 
print(f"Each Person Pays: Rs. {share:.2f}")

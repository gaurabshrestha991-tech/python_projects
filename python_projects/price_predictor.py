print("     Price Predictor")

price = float(input("Enter original price: Rs. "))
discount = float(input("Enter discount percentage: "))
tax  = float(input("Enter tax percenatge: "))

discount_amount = price * discount / 100

discounted_price = price - discount_amount

tax_amount = discounted_price * tax / 100

final_price = discounted_price + tax_amount

print("     Price Details")
print(f"Orginal Price: Rs. {price:.2f}")
print(f"Discount: Rs. {discount_amount:.2f}") 
print(f"Tax: Rs. {tax_amount:.2f}") 
print(f"Final Price: Rs. {final_price:.2f}")
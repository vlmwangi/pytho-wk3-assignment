def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount rate (in %): "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after discount is: Ksh{final_price:.2f}")
else:
    print(f"No discount was applied. The final price is: Ksh{final_price:.2f}")
    
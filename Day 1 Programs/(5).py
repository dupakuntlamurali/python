def bakery_sale(loaves):
    regular_price=185*loaves
    discount=0.6*regular_price
    total_price=regular_price-discount
    return regular_price,discount,total_price

loaves=int(input("Enter the number of loaves of day old bread: "))
regular_price,discount,total_price=bakery_sale(loaves)

print("Regular price: {:.2f} rupees".format(regular_price))
print("Discount:{:.2f} rupees".format(discount))
print("Total price:{:.2f} rupees".format(total_price))

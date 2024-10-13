lovley_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''

lovely_loveseat_price = 254.00

stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
stylish_settee_price = 180.50

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ""

#Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total
customer_one_total += lovely_loveseat_price

#Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization
customer_one_itemization += lovley_loveseat_description

#Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.
customer_one_total += luxurious_lamp_price 

#Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization
customer_one_itemization += luxurious_lamp_description

#They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.
customer_one_tax = (customer_one_total * sales_tax)

#Add the sales tax to the customer’s total cost.
customer_one_total += sales_tax

#Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".
phrase1 = "Customer One Items: "
print(phrase1)
print(customer_one_itemization)

phrase2 = "Customer One Total:"
print(phrase2)
print (customer_one_total)






#Initiating values
drink_prices = { "tea": 350, "coffee": 400, "milk": 280, "sprite": 420, "icedCoffee": 380, "icedTea": 320 }
discounted_drinks = {"milk", "sprite"}
orderlist=[]
pricelist=[]
total = 0

#Printing welcome message
print("Welcome to CoffeeCafe")
print("Please enter done after your order")

#Taking input from user
while True:
    order = input("Enter your order : ")
    if order == "done":
        break
    orderlist.append(order)

#Checking the presence of drink
for i in orderlist:
    if (i in drink_prices) != True :
        print(i+" Drink is not available")
        orderlist.remove(i)

#Checking if the drink has discount
for i in orderlist:
    if (i in discounted_drinks) == True :
        bprice = drink_prices.get(i)
        fprice = bprice - ((20 * bprice) / 100)
        fp = int(fprice)
        pricelist.append(fp)
    
    else :
        baseprice = drink_prices.get(i)
        pricelist.append(baseprice)

#Calculating total billamount
for j in pricelist:
    total = total + j

print("Your bill amount: ",total)
print("Thanks for your order. VIsit again.")
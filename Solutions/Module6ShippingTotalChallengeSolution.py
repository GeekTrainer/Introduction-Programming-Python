#You may have written the solution very differently from the solution provided below. 
#As you get further into coding, you will find multiple ways to solve the same problem with code
#If you coded it differently, than just compare your solution to this solution 
#You can decide which coding style you prefer

#Declare variables
orderTotal = 0
shippingCost = 0
totalWithShipping = 0

#Ask user for their order total and convert the answer to a number
orderTotal = float(input("What was the total for your order? " ))

#Calculate the shipping cost based on the order total
if orderTotal >= 50 :
    shippingCost = 0
else :
    shippingCost = 10

#Calculate order total including shipping
totalWithShipping = orderTotal + shippingCost

#Tell the user their final total
print("Your final total, including shipping, will be: $%.2f " % totalWithShipping)






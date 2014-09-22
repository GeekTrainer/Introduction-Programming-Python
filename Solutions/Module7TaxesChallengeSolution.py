#Declare and initialize your variables
country = ""
province = ""
orderTotal = 0
totalWithTax = 0

#I am declaring variables to hold the tax values used in the calculations
#That way if a tax rate changes, I only have to change it in one place instead
#of searching through my code to see where I had a specific numeric value and updating it
GST = .05  
HST = .13
PST = .06

#Ask the user what country they are from 
country = input("What country are you from? " )

#if they are from Canada ask which province...don't forget they may enter Canada as CANADA, Canada, canada, CAnada
#so convert the string to lowercase before you do the comparison

if country.lower() == "canada" :
    province = input("Which province are you from? ")

#ask for the order total
orderTotal = float(input("What is your order total? "))

#Now add the taxes
#first check if they are from canada
if country.lower() == "canada" :
    #if they are from canada, we have to change the calculation based on the province they specified
    if province.lower() == "alberta" :
        orderTotal = orderTotal + orderTotal * GST
    elif province.lower() == "ontario" or province.lower() == "new brunswick" or province.lower() == "nova scotia" :
        orderTotal = orderTotal + orderTotal * HST
    else :
        orderTotal = orderTotal + orderTotal * PST + orderTotal * GST
#if they are not from Canada there is no tax, so the amount they entered is the total with tax
#and no modification to orderTotal is required

#Now display the total with taxes to the user, don't forget to format the number
print("Your total including taxes comes to $%.2f " % orderTotal)



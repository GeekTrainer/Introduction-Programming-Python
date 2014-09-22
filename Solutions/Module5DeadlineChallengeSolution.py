#import the datetime class
import datetime

#declare and initialize variables
strDeadline = ""
totalNbrDays = 0
nbrWeeks = 0
nbrDays = 0

#Get Today's date
currentDate = datetime.date.today()

#Ask the user for the date of their deadline
strDeadline = input("Please enter the date of your deadline (mm/dd/yyyy): ")

deadline = datetime.datetime.strptime(strDeadline,"%m/%d/%Y").date()

#Calculate number of days between the two dates
totalNbrDays = deadline - currentDate

#For extra credit calculate results in weeks & days

nbrWeeks = totalNbrDays.days / 7

#The modulo will return the remainder of the division
#which will tell us how many days are left 
nbrDays = totalNbrDays.days%7

#display the result to the user

print("You have %d weeks" %nbrWeeks + " and %d days " %nbrDays + "until your deadline.")
 


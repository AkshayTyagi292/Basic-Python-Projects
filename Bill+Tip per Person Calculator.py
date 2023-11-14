#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip Calculator!")
bill = input("What was the total bill? ")
percent = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")
tip = (int(bill)*int(percent))/100
total = (int(bill) +int(tip))/int(people)
final_Amount = round(total,2)
print(f"Each person should pay {final_Amount}")
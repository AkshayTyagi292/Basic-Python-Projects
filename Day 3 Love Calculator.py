print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
small_letter = combined_names.lower()
t = small_letter.count("t")
r = small_letter.count("r")
u = small_letter.count("u")
e = small_letter.count("e")

tens_digit = t + r + u + e

l = small_letter.count("l")
o = small_letter.count("o")
v = small_letter.count("v")
e = small_letter.count("e")

ones_digit = l + o + v + e

score = (tens_digit * 10) + ones_digit

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
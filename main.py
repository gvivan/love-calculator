print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
digit1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
digit2 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
score = str(digit1) + str(digit2)
if int(score)<10 or int(score)>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score)>40 and int(score)<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

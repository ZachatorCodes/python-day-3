# Day 3
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

bill = 0

if height >= 120:
  print("You are allowed to ride the rollercoaster")
  age = int(input("What is your age?\n"))

  if age < 12:
    print("Child tickets are $5")
    bill = 5
  elif age <= 18:
    print("Teen adult tickets are $7")
    bill = 7
  elif age <= 22:
    print("Young adult tickets are $10.")
    bill = 10
  elif age >= 45 and age <= 55:
    print("Elder tickets are free!")
  else:
    print("Adult tickets are $12")
    bill = 12
  
  want_photo = input("Do you want a photo? Y or N.\n")
  
  if want_photo == "Y":
    bill += 3
  
else:
  print("You CANNOT ride the rollercoaster. Maybe, be taller?")

print(f"Your final bill is ${bill}.")
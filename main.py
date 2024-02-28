# Day 3
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
  print("You are allowed to ride the rollercoaster")
  age = int(input("What is your age?\n"))

  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  elif age <= 22:
    print("Please pay $10.")
  else:
    print("LOL you're old. Give me $12.")
else:
  print("You CANNOT ride the rollercoaster. Maybe, be taller?")
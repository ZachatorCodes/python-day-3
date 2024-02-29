print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1.lower() + name2.lower()

t_count = combined_names.count("t")
r_count = combined_names.count("r")
u_count = combined_names.count("u")
e_count = combined_names.count("e")

first_word_count = t_count + r_count + u_count + e_count

l_count = combined_names.count("l")
o_count = combined_names.count("o")
v_count = combined_names.count("v")
e_count = combined_names.count("e")

second_word_count = l_count + o_count + v_count + e_count

score = int(str(first_word_count) + str(second_word_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
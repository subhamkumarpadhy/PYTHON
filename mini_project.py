#Guess the number

# import random

# target_number = random.randint(1, 100)
# input_num = 0
# while(input_num != target_number):
#     input_num = (input("Enter between 1 to 100 or Quit :- "))
#     if(input_num == "Quit"):
#         break
#     input_num = int(input_num)
#     if(target_number > input_num):
#         print(input_num, "is less then the target number.")
#     if(target_number < input_num):
#         print(input_num, "is greater then the target number.")
# print("The correct number is", target_number, ".")
# print("----------GAME OVER----------")


#Random Password Generator
import random
import string

pass_len = 12
Char_values = string.ascii_letters + string.digits + string.punctuation

#Using loop
# password = ""
# for i in range(pass_len):
#     password += random.choice(Char_values)

#Using list comprehension [function fir i in range(n)]
password = "".join([random.choice(Char_values) for i in range(pass_len)])

print("Your random password is:", password)
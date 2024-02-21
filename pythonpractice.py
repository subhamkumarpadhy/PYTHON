#Practice some conditional statements


# day = input("What day is today:-")
# age = int(input("Enter your age:"))

# if day == "wednesday":
#     if age >= 18:
#         print("Your ticket price is", 10, "$")
#     else:
#         print("Your ticket price is", 6, "$")
# else:
#     if age >= 18:
#         print("Your ticket price is", 12, "$")
#     else:
#         print("Your ticket price is", 8, "$")


# mark = int(input("Enter your mark to know your grade: "))
# if mark > 100:
#     print("Marks can't be greater than 100. Please check your marks again.")
# else:
#     if mark >= 90:
#         print("Your grade is A.")
#     elif mark >= 80:
#         print("Your grade is B.")
#     elif mark >= 70:
#         print("Your grade is C.")
#     elif mark >= 60:
#         print("Your grade is D.")
#     else:
#         print("Your grade is F.")


# fruit = "Banana"
# colour = input("Enter colour: ")
# if fruit == "Banana":
#     if colour == "Green" or colour == "green":
#         print("It's Unripe.")
#     elif colour == "Yellow" or colour == "yellow":
#         print("It's Ripe.")
#     elif colour == "Brown" or colour == "brown":
#         print("It's Overripe.")


# day = input("What's the day outside? \n")
# if day == "Sunny":
#     print("You should go for a walk.")
# elif day == "Rainy":
#     print("You should read a book.")
# elif day == "Snowy":
#     print("Build a snowman.")


# dist = int(input("Enter your distance: "))
# if dist < 3:
#     print("You should go by Walk.")
# elif dist < 15:
#     print("Take a Bike.")
# else:
#     print("Take the Car.")


# year = int(input("Enter the year:- \n"))
# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print("It's a leap year.")
# else:
#     print("It's not a leap year.")




#Practice of some loops questions

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count = 0
# for i in numbers:
#     if i > 0:
#         count += 1
# print(count)


# num = int(input("Enter a number:- "))
# sum = 0
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         sum += 1
# print(sum)


# number = int(input("Enter the number:- "))
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, "X", i, "=", number * i )


# input_str = ("Reverse it.")
# reverse_str = ""
# for char in input_str:
#     reverse_str = char + reverse_str
# print(reverse_str)


# input_str = "teeterfgstfhfh"
# for char in input_str:
#     if input_str.count(char) == 1:
#         print("Char is", char)
#         break


# number = 5
# fact = 1
# while number > 0:
#     fact = fact * number
#     number -= 1
# print(fact)



# while True:
#     number = int(input("Enter number:-"))
#     if 1 <= number <= 10:
#         print("Thanks.")
#         break
#     else:
#         print("Invalid number. Try again.")



# input_num = int(input("Enter a number:-"))
# is_prime = True
# if input_num > 1:
#     for i in range(2, input_num):
#         if(input_num % i) == 0:
#             is_prime = False
#             break
# print(is_prime)


# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate:", item)
#         break
#     unique_item.add(item)


import time
wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print("Attempt", attempts + 1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

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


# import time
# wait_time = 1
# max_retries = 5
# attempts = 0
# while attempts < max_retries:
#     print("Attempt", attempts + 1, "-wait time", wait_time)
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1

# class Car:
#     total_car = 0
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def full_name(self):
#         return f"{"The full name of your car is"} {self.__brand} {"-"} {self.__model} {"."}"
#         # print("The full name of your car is ", self.brand, "-", self.model,".")

#     def fuel_type(self):
#         return "Petrol or Diseal"

#     @staticmethod
#     def general_description():
#         return "Cars are costlier than bikes."

#     @property
#     def model(self):
#         return self.__model

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# car_instance = Car("Land_Rover", "Defender")
# print(car_instance.brand)
# print(car_instance.model)
# print(car_instance.full_name())
# print(car_instance.fuel_type())

# electric_car = ElectricCar("Tesla", "Model X", "100kw")
# print(electric_car.brand)
# print(electric_car.model)
# print(electric_car.battery_size)
# print(electric_car.full_name())
# print(electric_car.fuel_type())

# print(Car.total_car)

# print(car_instance.general_description())
# print(Car.general_description())

# print(isinstance(electric_car, ElectricCar))
# print(isinstance(electric_car, Car))



# class Battery:
#     def battery_info(self):
#         return "This is battery class."
# class Engine:
#     def engine_info(self):
#         return "This is engine class."

# class Electric_Car(Battery, Engine, Car):
#     pass

# my_electric_car = Electric_Car("Toyota", "Land_Crusier")
# print(my_electric_car.engine_info())
# print(my_electric_car.battery_info())



#Decorators practice
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end - start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(5)





# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
#         print(f"calling: {func.__name__} with args {args_value} & kwargs {kwargs_value}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def hello():
#     print("Hello")

# @debug
# def greet(name, greeting = "Hello"):
#     print(f"{greeting}, {name}")

# hello()
# greet("Chai", greeting = "hanji")





import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_runnign_function(a, b):
    time.sleep(5)
    return a + b

print(long_runnign_function(2, 3))
print(long_runnign_function(2, 3))
print(long_runnign_function(4, 3))







































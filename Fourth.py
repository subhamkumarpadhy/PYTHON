# Dictionary in python

# info = {
    #we can make any data type to key value except lists & Dictionary coz they are mutable
    #But in value we can use any of the data types
#     "key" : "value",
#     "name" : "subham",
#     "reg no" : 2101109363,
#     "topic" : ("communication", "dsp", "vlsi"),
#     "is_adult" : True,
#     "marks" : [7.78, 7.00, 7.82, 7.38],
#     67.87 : 56
# }
# print(info)
# print(type(info))

# properties of dict:-
# It is unordered, mutable & don't allow duplicate keys

# Accessing dict elements with the help of keys
# print(info["marks"])
# print(info["name"])
# print(info["topic"])

# changing the elements of dict
# info["name"] = "kanha"
# info["surname"] = "padhy"
# print(info)

# Empty dict
# null_dict = {}
# print(null_dict)
# null_dict["name"] = "ke_pi_stu" #Add data to the empty dict
# print(null_dict)

# Nested dict
# student = {
#     "name" : "samir",
#     "subjects" : { #nested dict
#         "VLSI" : 54,
#         "DSP" : 75,
#         "ADC" : 86,
#         "COA" : 69,
#         "MPMC" : 73
#     },
#     "pass" : True,
#     "Grade" : 'E'
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["VLSI"])

# Some dict methods
# print(student.keys()) #return all the keys
# print(list(student.keys())) #typecast to list type
# print(len(list(student.keys()))) #Finding the length of the dict

# print(student.values()) #return all the values
# print(list(student.values())) #typecast to list type

# print(student.items()) #return all (key,val) pairs as tuples
# print(list(student.items()))
# pairs = list(student.items())
# print(pairs[1]) #accessing individual tuples

# print(student.get("subjects")) #return the key according to the value
# why to use this method if you already have student["key"] this? coz 
# if one line is causing error then after that line all other codes should
# be in working condition, unless the system is not a stable system.

# student.update({"attendance" : 79, "behaviour" : 82.52}) #inserts the specified items to the dict
# new_dict = {"attendance" : 79, "behaviour" : 82.52}
# student.update(new_dict)
# print(student)


# Sets in python:-
#set is collection of unordered items
#Each element in the set must be unique & immutable
#We can't stored dicts & lists in sets coz they are mutable

# collection = {1, 2, 4, 4, 4, "kurkure", "kurkure", 5.42, 96.4} #duplicate values will be ignored in sets always & prints unorderly
# print(collection)
# print(type(collection))
# print(len(collection))

#Creating empty set
core = set() #syntax
# print(core)
# print(type(core))

# Thing to remember:- Sets are mutable but the elements in the sets are immutable

#Set Methods:- 
# core.add("kanha") #adds element
# core.add(45.65)
# core.add(5)
# core.add(5)
# core.add((1,5,7))
# # core.add([1,5,7]) #error come can'd add lists
# core.remove(45.65) #removes the item
# # core.clear() #empties the set
# # core.pop() #removes a random value & return the removed value
# print(core)

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4, 5}
# print(set1.union(set2)) #combines both sets & return a new set
# print(set1.intersection(set2)) #combines common values & returns new set

#Some practice questions

# store following word meanings in a dict
# word = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"] #we can store in the form of lists or tuples also
# }
# print(word)

#create a set & find it's length
# subjects = {"python", "java", "c++", "python", "javascript", "python", "java", "python", "java", "c++", "c"}
# print(len(subjects))

#Empty dict to start, input 3 marks of a sub & store in a dict & store one by one. key = subj name & val = marks.
# result = {}
# marks1 = int(input("Enter your mark in PHY:-"))
# result.update({"PHY" : marks1})
# marks2 = int(input("Enter your mark in CHEM:-"))
# result.update({"CHEM" : marks2})
# marks3 = int(input("Enter your mark in MATHs:-"))
# result.update({"MATHs" : marks3})
# print(result)

#Figure out a way to store 9 & 9.0 in a set
values = {"9.0", 9} #one way
value = { #storing in a tuple
    ("float", 9.0)
    ("int", 9)
}
print(values)
print(value)









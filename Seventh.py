#File I/o in python

# f = open("Linkedinpost.txt", "rt")
# data = f.read() #reads the entire file
# data = f.read(20)
# print(data)
# print(type(data))
# line1 = f.readline() #reads one line at a time
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

#Writing to a file
# f = open("Linkedinpost.txt", "w") 
# f = open("Linkedinpost.txt", "a") #It will append the content at the last
# f.write("\nI hope you are fine") #Writing starts with an empty file
# f.close()

#In "w" or "a" mode if we don't have the specified file, then it will autmatically create that for us

#Read & write both
# f = open("Linkedinpost.txt", "r+") #It starts writing from the start of the file
# f.write("Nice") 
# print(f.read()) #It will start printing after what is written.
# f.close()

#"With" Syntax
# with open("Linkedinpost.txt", "r") as f:
#     data = f.read()
#     print(data)
# with open("Linkedinpost.txt", "w") as f:
#     data = f.write("This is newly inserted data")
#     print(data)

#Deleting a file with the help of OS module
# import os
# os.remove("Linkedinpost.txt")

#Some practice questions

#Create a new file & add data
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone")
#     f.write("\nWe are learning File I/O")
#     f.write("\nusing Java")
#     f.write("\nI like programming in Java")

#Replace all occurrance of Java with python in the above file
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)
# #It will overwrite in the original file
# with open("practice.txt", "w") as f:
#     data = f.write(new_data)

#Find the word "learning" in the above file
# def check_for_word() :
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")
# check_for_word()

#WAF to find in which line the word "learning" occure first
# def check_for_line() :
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()

#Print the count of even numbers from file having numbers separated by comma
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

#From scratch ie:- withour any in_build function just print the data
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

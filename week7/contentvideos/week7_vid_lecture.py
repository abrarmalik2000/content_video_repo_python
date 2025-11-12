# # opening a file in read mode 
# # file = open("D:\Courses USU\Intro to Python\example.txt", "r")

# #reading the entire contents of the file 
# # content = file.read()
# # print("content :",content)
# # print()

# # read the file line by line 
# # lines = file.readlines()
# # for line in lines:
# #     print("line: ", line)

# # #closing the line 
# # file.close()

# #opening a file in write mode
# file = open("output.txt", "w")

# #writing data to the file 
# file.write("Hello world !\n")
# file.write("This is a new line in my file !!!\n")
# # close the file 
# # file.close()
# content = file.read()
# print(content)

# import os
# file1 = open("output1.txt", "w")
# file1.write("hello\n")
# file1.write("goodbye\n")
# file1.close()

# os.rename("output1.txt", "output_renamed.txt")
# os.mkdir("fun_directory")
# os.system("mkdir -p fun_directory/new_directory/new")
# os.system ("ls")
# os.system ("pwd")
# os.system("whoami")

# os.mkdir("test_directory")

import numpy
# create list of 4 floats 
# homework_scores = [49.5, 48.3, 47.6, 50]
# print(homework_scores)

#convert the list to numpy array 
# hw_np = numpy.array(homework_scores)
# print (hw_np)
# import random
# list = []
# for i in range(10):
#     list.append(random.randint(1,100))
# print(list)
# list_np = numpy.array(list)
# print(list_np)

#initialize numpy array of size 10 
# import numpy
# np1 = numpy.zeros(100)
# print(np1)

# np2 = numpy.ones(100)
# print(np2)


try:
    userinput = int(input("input an integer: "))
    print(userinput)
except:
    print('"invalid input"')

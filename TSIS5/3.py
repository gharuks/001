#a Python program to append text to a file and display the text.
# import os
text=input()
with open('test.txt', 'w') as f:
    f.write(text)
    res=open('test.txt')
    print(res.read())
# def file_read(fname):
#         from itertools import islice
#         with open(fname, "w") as myfile:
#                 myfile.write("Python Exercises\n")
#                 myfile.write("Java Exercises")
#         txt = open(fname)
#         print(txt.read())
# file_read('test.txt')
#a Python program to read first n lines of a file
# with open('text.txt', 'r') as f:
#     n=int(input())
#     for line in range(n):
#         print(f.readline())
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('text.txt',1)
#a Python program to read last n lines of a file
with open('text.txt', 'r') as f:
    t=f.read()
    for line in range(int(input()),):
        print(f.readline())
#По данному натуральному числу N выведите такое наименьшее целое число k, что 2k≥N.
import math
n=int(input())
print(math.ceil(math.log(n, 2)))
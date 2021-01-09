#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

txt = open("regex_sum_2.txt")
#suma=0
#for line in txt:
#    numbers=re.findall('[0-9]+',line)
#    if len(numbers) != 0:
#        for number in numbers:
#            suma=int(number)+sum
#print(suma)

print (sum([int(numbers) for numbers in re.findall('[0-9]+',txt.read())] ))
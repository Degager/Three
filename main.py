import random
import sys

number_list = list()
min_number = sys.maxsize
max_number = 0

for x in range(100):
    random_number = random.randrange(0,1000000001)
    number_list.append(random_number)

for number in number_list:
    if number % 3 == 0:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number


print(min_number)
print(max_number)
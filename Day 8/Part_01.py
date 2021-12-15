
from itertools import permutations

def find_digit(pattern):
	digit_list = pattern.split(' ')
	unique_digits = list()
	for a in digit_list:
		if len(a) == 2:
			unique_digits.append(a)
		if len(a) == 4:
			unique_digits.append(a)
		if len(a) == 3:
			unique_digits.append(a)
		if len(a) == 7:
			unique_digits.append(a)
	return unique_digits

def combos(value):
	combinations = list(permutations(value))
	combinations = [''.join(a) for a in combinations]
	return combinations

with open('Seven Segment Display.txt', 'r') as my_file:
	input_list = my_file.readlines()

input_list = [x.split('|') for x in input_list]
pattern_list,output_list = list(),list()
output_count = 0
for x in input_list:
	pattern_list.append(x[0].strip())
	output_list.append(x[1].strip())
output_list = [x.split(' ') for x in output_list]
for enum,single_pattern in enumerate(pattern_list):
	for digit in find_digit(single_pattern):
		if len(digit) == 7:
			for x in output_list[enum]:
				if len(x) == 7:
					output_count += 1
		else:
			for a in combos(digit):			
				output_count += output_list[enum].count(a)
print(f"Total count for '1','4','7','8' in output values is {output_count}")
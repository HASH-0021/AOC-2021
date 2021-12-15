
from itertools import permutations

def find_digit(pattern):
	digit_list = pattern.split(' ')
	unique_digits = dict()
	for a in digit_list:
		if len(a) == 2:
			unique_digits.update({1 : a})
		if len(a) == 4:
			unique_digits.update({4 : a})
		if len(a) == 3:
			unique_digits.update({7 : a})
		if len(a) == 7:
			unique_digits.update({8 : a})
	seg_1 = ''.join(x for x in unique_digits[7] if x not in unique_digits[1])
	seg_36 = unique_digits[1]
	seg_24 = ''.join(x for x in unique_digits[4] if x not in unique_digits[1])
	seg_57 = ''.join(x for x in unique_digits[8] if x not in unique_digits[4] and x not in seg_1)
	for a in digit_list:
		if len(a) == 6:
			for x in seg_36:
				if x not in a:
					seg_3 = x
					unique_digits.update({6 : a})
	seg_6 = ''.join(x for x in seg_36 if x not in seg_3)
	for a in digit_list:
		if len(a) == 6:
			for x in seg_57:
				if x not in a:
					seg_5 = x
					unique_digits.update({9 : a})
	seg_7 = ''.join(x for x in seg_57 if x not in seg_5)
	for a in digit_list:
		flag = True
		if len(a) == 6:
			for x in seg_36+seg_57:
				if x not in a:
					flag = False
			if flag:
				seg_4 = ''.join(x for x in unique_digits[8] if x not in a)
				unique_digits.update({0 : a})
	seg_2 = ''.join(x for x in seg_24 if x not in seg_4)
	for a in digit_list:
		digit_2 = seg_1+seg_3+seg_4+seg_57
		digit_3 = seg_1+seg_36+seg_4+seg_7
		digit_5 = ''.join(x for x in unique_digits[9] if x not in seg_3)
		two_flag = True
		three_flag = True
		five_flag = True
		if len(a) == 5:
			for x in a:
				if x not in digit_2:
					two_flag = False
				if x not in digit_3:
					three_flag = False
				if x not in digit_5:
					five_flag = False
			if two_flag:
				unique_digits.update({2 : a})
			if three_flag:
				unique_digits.update({3 : a})
			if five_flag:
				unique_digits.update({5 : a})
	return unique_digits

def combos(value):
	combinations = list(permutations(value))
	combinations = [''.join(a) for a in combinations]
	return combinations

with open('Seven Segment Display.txt', 'r') as my_file:
	input_list = my_file.readlines()

input_list = [x.split('|') for x in input_list]
pattern_list,output_list = list(),list()
total = 0
for x in input_list:
	pattern_list.append(x[0].strip())
	output_list.append(x[1].strip())
output_list = [x.split(' ') for x in output_list]
for e1,single_pattern in enumerate(pattern_list):
	digit_dict = find_digit(single_pattern)
	digit_key_list = list(digit_dict.keys())
	digit_value_list = list(digit_dict.values())
	output_value = str()
	for digit in output_list[e1]:
		for a in combos(digit):			
			if a in digit_value_list:	
				pos = digit_value_list.index(a)	
				output_value += str(digit_key_list[pos])
	total += int(output_value)
print(total)
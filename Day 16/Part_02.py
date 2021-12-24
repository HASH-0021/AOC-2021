
def binary_decode(b_string):
	global ver_total
	global pos
	values = list()
	number = int(b_string)
	if number:
		string_length = len(b_string)
		if string_length >= 3:
			binary_v = b_string[:3]
			version = int(binary_v, 2)
			ver_total += version
		if string_length >= 6:
			binary_type = b_string[3:6]
			type_id = int(binary_type, 2)
			if type_id == 4:
				pos = 0
				binary_literal = find_literal(b_string[6:],'')
				if binary_literal:
					literal_value = int(binary_literal, 2)
					return (literal_value, b_string[6+pos:])
			else:
				if string_length >= 7:
					binary_label_id = b_string[6:7]
					label_id = int(binary_label_id, 2)
					if label_id:
						if string_length >= 18:
							binary_label_length = b_string[7:18]
							label_length = int(binary_label_length, 2)
							b_string = b_string[18:]
							for i in range(label_length):								
								literal_value,b_string = binary_decode(b_string)
								values.append(literal_value)
							literal_value = evaluation(type_id,values)
							return (literal_value, b_string)
					else:
						if string_length >= 22:
							binary_label_length = b_string[7:22]
							label_length = int(binary_label_length, 2)
							b_string_2 = b_string[22:22+label_length]
							while b_string_2:
								literal_value,b_string_2 = binary_decode(b_string_2)
								values.append(literal_value)
							literal_value = evaluation(type_id,values)
							return (literal_value, b_string[22+label_length:])


def find_literal(b_string,binary_literal):
	global pos
	string_length = len(b_string)
	if string_length >= 5:
		group = b_string[:5]
		pos += 5
		if group[0] == '1':
			binary_literal += group[1:]
			return find_literal(b_string[5:], binary_literal)
		else:
			binary_literal += group[1:]
			return binary_literal
	else:
		return binary_literal

def evaluation(type_id, values):
	list_length = len(values)
	if type_id == 0:
		return sum(values)
	elif type_id == 1:
		product = 1
		for i in values:
			product *= i
		return product
	elif type_id == 2:
		return min(values)
	elif type_id == 3:
		return max(values)
	elif type_id == 5:
		if values[0] > values[1]:
			return 1
		else:
			return 0
	elif type_id == 6:
		if values[0] < values[1]:
			return 1
		else:
			return 0
	elif type_id == 7:
		if values[0] == values[1]:
			return 1
		else:
			return 0
	else:
		print("Something is wrong")
		return 0

with open('Transmission Data.txt', 'r') as my_file:
	transmission = my_file.read()

transmission = transmission.strip()
hexadecimal_string = list(transmission)
binary_number = list()
for x in hexadecimal_string:
	binary_number.append(bin(int(x, 16)))
binary_number = [b.split('0b')[1] for b in binary_number]
for e,b in enumerate(binary_number):
	if len(b) == 3:
		binary_number[e] = '0'+binary_number[e]
	if len(b) == 2:
		binary_number[e] = '00'+binary_number[e]
	if len(b) == 1:
		binary_number[e] = '000'+binary_number[e]
binary_data = list()
for b in binary_number:
	binary_split = list(b)
	for x in binary_split:
		binary_data.append(x)
ver_total = 0
pos = 0
binary_string = ''.join(binary_data)
computed_value,extra_bits = binary_decode(binary_string)
print(f"Evaluating the expression represented by your hexadecimal-encoded BITS transmission is {computed_value}")
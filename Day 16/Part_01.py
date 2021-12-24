
def binary_decode(b_string):
	global ver_total
	global pos
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
					print(f"v - {version}, t - {type_id}, lv - {literal_value}")
				if string_length >= 7+pos:
					binary_decode(b_string[6+pos:])
			else:
				if string_length >= 7:
					binary_label_id = b_string[6:7]
					label_id = int(binary_label_id, 2)
					if label_id:
						if string_length >= 18:
							binary_label_length = b_string[7:18]
							label_length = int(binary_label_length, 2)
							print(f"v - {version}, t - {type_id}, i - {label_id}, l - {label_length}")
							if string_length >= 19:
								binary_decode(b_string[18:])
					else:
						if string_length >= 22:
							binary_label_length = b_string[7:22]
							label_length = int(binary_label_length, 2)
							print(f"v - {version}, t - {type_id}, i - {label_id}, l - {label_length}")
							if string_length >= 23:
								binary_decode(b_string[22:])

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
binary_decode(binary_string)
print(f"Version total for decoded structure of hexadecimal-encoded BITS transmission is {ver_total}")
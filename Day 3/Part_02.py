
class BinaryNumberException(Exception):
	'''Exception raised for custom purpose.
	
	Attributes:
		message -- explanation of the exception
	'''
	def __init__(self, message):
		self.message = message

def reduce_oxygen_generator_rating(oxygen_generator_rating, i, no):
	not_oxygen = list()
	for b in oxygen_generator_rating:
		if b[i] == no:
			not_oxygen.append(b)
	for b in not_oxygen:
		oxygen_generator_rating.remove(b)

def reduce_co2_scrubber_rating(co2_scrubber_rating, i, no):
	not_co2 = list()
	for b in co2_scrubber_rating:
		if b[i] == no:
			not_co2.append(b)
	for b in not_co2:
		co2_scrubber_rating.remove(b)

with open('Diagnostic Report.txt', 'r') as my_file:
	binary_list = my_file.read().split('\n')

count_zero,count_one,i = 0,0,0
oxygen_generator_rating,co2_scrubber_rating = binary_list[:],binary_list[:]

try:
	while i < len(binary_list[0]):

		for b in oxygen_generator_rating:
			if b[i] == '0':
				count_zero += 1
			elif b[i] == '1':
				count_one += 1
			else:
				raise BinaryNumberException("Please enter valid binary numbers in 'Diagnostic Report.txt'..")
		if len(oxygen_generator_rating) > 1:
			if count_zero > count_one:
				reduce_oxygen_generator_rating(oxygen_generator_rating, i, '1')
			if count_zero <= count_one:
				reduce_oxygen_generator_rating(oxygen_generator_rating, i, '0')
		count_zero,count_one = 0,0
		
		for b in co2_scrubber_rating:
			if b[i] == '0':
				count_zero += 1
			elif b[i] == '1':
				count_one += 1
			else:
				raise BinaryNumberException("Please enter valid binary numbers in 'Diagnostic Report.txt'..")
		if len(co2_scrubber_rating) > 1:
			if count_zero > count_one:
				reduce_co2_scrubber_rating(co2_scrubber_rating, i, '0')
			if count_zero <= count_one:
				reduce_co2_scrubber_rating(co2_scrubber_rating, i, '1')
		count_zero,count_one = 0,0
		i += 1

	ogr = int(oxygen_generator_rating[0], 2)
	csr = int(co2_scrubber_rating[0], 2)
	print(f"Life support rating is {ogr*csr}")
except BinaryNumberException as bne:
	print(f"Exception Message: {bne.message}")

class BinaryNumberException(Exception):
	'''Exception raised for custom purpose.
	
	Attributes:
		message -- explanation of the exception
	'''
	def __init__(self, message):
		self.message = message

with open('Diagnostic Report.txt', 'r') as my_file:
	binary_list = my_file.read().split('\n')

count_zero,count_one,i = 0,0,0
gamma_rate,epsilon_rate = str(),str()

try:
	while i < len(binary_list[0]):
		for b in binary_list:
			if b[i] == '0':
				count_zero += 1
			elif b[i] == '1':
				count_one += 1
			else:
				raise BinaryNumberException("Please enter valid binary numbers in 'Diagnostic Report.txt'..")
		if count_zero > count_one:
			gamma_rate += '0'
			epsilon_rate += '1'
		if count_zero < count_one:
			gamma_rate += '1'
			epsilon_rate += '0'
		count_zero,count_one = 0,0
		i += 1
	gamma_rate = int(gamma_rate, 2)
	epsilon_rate = int(epsilon_rate, 2)
	print(f"Power consumption is {gamma_rate*epsilon_rate}")
except BinaryNumberException as bne:
	print(f"Exception Message: {bne.message}")
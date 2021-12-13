
class NegativeIntegerException(Exception):
	'''Exception raised for custom purpose.
	
	Attributes:
		message -- explanation of the exception
	'''
	def __init__(self, message):
		self.message = message

count,i = 0,0
try:
	with open('Depths.txt', 'r') as my_file:
		depths = my_file.read().split('\n')
	for enum,each_depth in enumerate(depths):
		depths[enum] = int(each_depth)
		if depths[enum] < 0:
			raise NegativeIntegerException("Atleast one of the depth value is less than zero..")
			break
	if not len(depths):
		print("Please enter some measurements in 'Depths.txt'..")
	elif len(depths) == 1:
		print("N/A - no previous measurement found..")
	else:
		while i < len(depths)-1:
			if depths[i+1] - depths[i] > 0:
				count += 1
			i += 1
		print(f"There are {count} measurements that are larger than the previous measurement.")
except ValueError:
	print("Please enter only whole numbers for depths..")
except NegativeIntegerException as nie:
	print(f"Exception Message: {nie.message}")
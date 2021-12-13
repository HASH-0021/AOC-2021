
class NegativeIntegerException(Exception):
	'''Exception raised for custom purpose.
	
	Attributes:
		message -- explanation of the exception
	'''
	def __init__(self, message):
		self.message = message

forward,depth = 0,0
try:
	with open('Course.txt', 'r') as my_file:
		course = my_file.read().split('\n')
	for command in course:
		direction = command.split(' ')[0]
		length = int(command.split(' ')[1])
		if length >= 0:
			if direction.lower() == 'forward':
				forward += length
			elif direction.lower() == 'up':
				depth -= length
			elif direction.lower() == 'down':
				depth += length
			else:
				print("Please enter directions only between 'forward', 'up' and 'down' in 'Course.txt' file..")
				break
		else:
			raise NegativeIntegerException("Atleast one of the length value is less than zero..")
			break
	print(f"Result of multiplying 'horizontal position' with 'depth' is {forward*depth}")
except ValueError:
	print("Please enter only whole numbers for lengths..")
except NegativeIntegerException as nie:
	print(f"Exception Message: {nie.message}")
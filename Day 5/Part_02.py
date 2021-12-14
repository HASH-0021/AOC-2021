
highest,lowest = 0,0

with open('Lines.txt', 'r') as my_file:
	lines = my_file.readlines()
	for e1,line in enumerate(lines):
		lines[e1] = line.strip().split(' -> ')
		for e2,point in enumerate(lines[e1]):
			lines[e1][e2] = point.split(',')
			for e3,coordinate in enumerate(lines[e1][e2]):
				coordinate_value = int(coordinate)
				lines[e1][e2][e3] = coordinate_value
				if coordinate_value > highest:
					highest = coordinate_value
	field,each_line = list(),list()
	for x in range(lowest, highest+1):
		for y in range(lowest, highest+1):
			each_line.append(0)
		field.append(each_line[:])
		each_line.clear()
	for line in lines:
		low_x = min(line[0][0], line[1][0])
		high_x = max(line[0][0], line[1][0])
		low_y = min(line[0][1], line[1][1])
		high_y = max(line[0][1], line[1][1])
		if line[0][0] == line[1][0]:
			for y in range(low_y, high_y+1):
				field[line[0][0]][y] += 1
		elif line[0][1] == line[1][1]:
			for x in range(low_x, high_x+1):
				field[x][line[1][1]] += 1
		elif line[1][0]-line[0][0] == line[1][1]-line[0][1]:
			x_coord,y_coord = low_x,low_y
			while x_coord <= high_x and y_coord <= high_y:
				field[x_coord][y_coord] += 1
				x_coord += 1
				y_coord += 1
		elif line[1][0]-line[0][0] == (-1)*(line[1][1]-line[0][1]):
			x_coord,y_coord = low_x,high_y
			while x_coord <= high_x and y_coord >= low_y:
				field[x_coord][y_coord] += 1
				x_coord += 1
				y_coord -= 1
	danger_points = 0
	print("Field map:\n")
	for e1,x in enumerate(field):
		for e2,y in enumerate(x):
			if field[e1][e2]:
				if field[e1][e2] > 1:
					danger_points += 1
			else:
				field[e1][e2] = '.'
			print(field[e1][e2], end = ' ')
		print('')
	print(f"\nNumber of dangerous points where atleast two lines overlap is {danger_points}.")
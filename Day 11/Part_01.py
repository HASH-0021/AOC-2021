
def energy_addition(level_done):
	global energy_levels_list
	global flashes
	count = flashes
	for e1,row in enumerate(energy_levels_list):
		cols_length = len(row)
		for e2,level in enumerate(row):
			if level < 10:
				if e2-1 >= 0:
					if energy_levels_list[e1][e2-1] == level_done:
						level += 1
				if e2+1 < cols_length:
					if energy_levels_list[e1][e2+1] == level_done:
						level += 1
				if e1-1 >= 0:
					if energy_levels_list[e1-1][e2] == level_done:
						level += 1
				if e1+1 < rows_length:
					if energy_levels_list[e1+1][e2] == level_done:
						level += 1
				if e2-1 >= 0 and e1-1 >= 0:
					if energy_levels_list[e1-1][e2-1] == level_done:
						level += 1
				if e2-1 >= 0 and e1+1 < rows_length:
					if energy_levels_list[e1+1][e2-1] == level_done:
						level += 1
				if e2+1 < cols_length and e1-1 >= 0:
					if energy_levels_list[e1-1][e2+1] == level_done:
						level += 1
				if e2+1 < cols_length and e1+1 < rows_length:
					if energy_levels_list[e1+1][e2+1] == level_done:
						level += 1
				if level >= 10:
					flashes += 1
					energy_levels_list[e1][e2] = level_done+1
				else:
					energy_levels_list[e1][e2] = level
	if count != flashes:
		energy_addition(level_done+1)

with open('Energy Levels.txt', 'r') as my_file:
	energy_levels_list = my_file.readlines()

energy_levels_list = [x.strip() for x in energy_levels_list]
energy_levels_list = [[int(i) for i in line] for line in energy_levels_list]
steps = 100
flashes = 0
rows_length = len(energy_levels_list)
for i in range(steps):
	for e1,row in enumerate(energy_levels_list):
		cols_length = len(row)
		for e2,level in enumerate(row):
			energy_levels_list[e1][e2] += 1
			if energy_levels_list[e1][e2] == 10:
				energy_levels_list[e1][e2] = 100
				flashes += 1
	energy_addition(100)
	for e1,row in enumerate(energy_levels_list):
		cols_length = len(row)
		for e2,level in enumerate(row):
			if level >= 100:
				energy_levels_list[e1][e2] = 0
print(f"Energy levels of each dumbo octopus after {steps} steps:")				
for row in energy_levels_list:
	for level in row:
		print(level,end = '')
	print('')
print(f"\nTotal flashes after {steps} steps is {flashes}.")
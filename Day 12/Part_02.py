
def path_calc(next_cave, cave_pattern, small_repeat):
	global map_list
	global all_paths
	for x in map_list:
		cave_pattern_2 = cave_pattern[:]
		if next_cave in x:
			next_cave_2 = ''.join(cave for cave in x if cave != next_cave)
			if next_cave_2 == 'end':
				if cave_pattern_2 not in all_paths:
					cave_pattern_2.append(next_cave_2)
					all_paths.append(cave_pattern_2[:])
			elif next_cave_2.islower():
				if next_cave_2 in cave_pattern_2:
					if not small_repeat:
						cave_pattern_2.append(next_cave_2)
						path_calc(next_cave_2, cave_pattern_2[:], 1)
					else:
						continue
				else:
					cave_pattern_2.append(next_cave_2)
					path_calc(next_cave_2, cave_pattern_2[:], small_repeat)
			else:
				if len(cave_pattern_2) > 3: 
					if not repeat_check(next_cave_2, cave_pattern_2[-3:]):
						cave_pattern_2.append(next_cave_2)
						path_calc(next_cave_2, cave_pattern_2[:], small_repeat)
					else:
						continue
				else:
					cave_pattern_2.append(next_cave_2)
					path_calc(next_cave_2, cave_pattern_2[:], small_repeat)

def repeat_check(cave, pattern):
	before_sequence = ''.join(pattern[:2])
	current_sequence = pattern[2] + cave
	if before_sequence == current_sequence:
		return before_sequence.isupper()
	else:
		return False

with open('Cave Map.txt', 'r') as my_file:
	map_list = my_file.readlines()

map_list = [x.strip() for x in map_list]
map_list = [tuple(x.split('-')) for x in map_list]
start_list,end_list = list(),list()
for x in map_list:
	if 'start' in x:
		start_list.append(x)
	if 'end' in x:
		end_list.append(x)
for x in start_list:
	map_list.remove(x)
for x in end_list:
	map_list.remove(x)
	map_list.append(x)
all_paths = list()
for x in start_list:
	cave_pattern = list()
	cave_pattern.append('start')
	next_cave = ''.join(cave for cave in x if cave != 'start')
	cave_pattern.append(next_cave)
	path_calc(next_cave, cave_pattern[:], 0)
print(f"Total paths through this cave system is {len(all_paths)}.")
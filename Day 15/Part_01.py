
def least_risk_path():
	global risks
	y_length = len(risks)
	x_length = len(risks[0])
	shortest_paths = {(0, 0) : (None, 0)}
	current_cave = (0, 0)
	visited = set()
	while current_cave != (y_length-1, x_length-1):
		adjacent_caves = list()
		visited.add(current_cave)
		(y, x) = current_cave
		if x > 0:
			adjacent_caves.append((y, x-1))
		if x < x_length-1:
			adjacent_caves.append((y, x+1))
		if y > 0:
			adjacent_caves.append((y-1, x))
		if y < y_length-1:
			adjacent_caves.append((y+1, x))
		current_risk_total = shortest_paths[current_cave][1]
		for next_cave in adjacent_caves:
			(j, i) = next_cave
			new_risk_total = risks[j][i] + current_risk_total
			if next_cave not in shortest_paths:
				shortest_paths[next_cave] = (current_cave, new_risk_total)
			else:
				previous_risk_total = shortest_paths[next_cave][1]
				if previous_risk_total > new_risk_total:
					shortest_paths[next_cave] = (current_cave, new_risk_total)
		next_paths = {cave: shortest_paths[cave] for cave in shortest_paths if cave not in visited}
		current_cave = min(next_paths, key=lambda k: next_paths[k][1])
	path = []
	least_risk_total = shortest_paths[current_cave][1]
	while current_cave is not None:
		path.append(current_cave)
		current_cave = shortest_paths[current_cave][0]
	path = path[::-1]
	return (path, least_risk_total)

with open('Risk Map.txt', 'r') as my_file:
	risks = my_file.readlines()

risks = [[int(i) for i in x.strip()] for x in risks]
path,least_risk_total = least_risk_path()
for p in path:
	y = p[0]
	x = p[1]
	risks[y][x] = '\033[92m\033[1m'+str(risks[y][x])+'\033[0m'
# This is to print path through map in bold numbers.
# Some command shells might not be able to produce bold numbers instead shows ANSI code.
# Use "risks[y][x] = '='" above if the output contains ANSI code. This shows path indicated by character '='.
print("Least risk path through map:\n")
for y in risks:
	for x in y:
		print(x, end = '')
	print('')
print(f"\nRisk total of least risk path is {least_risk_total}.")
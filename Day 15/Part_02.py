from heapq import heappush,heappop

def least_risk_path():
	global risks
	y_length = len(risks)
	x_length = len(risks[0])
	shortest_paths = [(0, (0, 0))]
	visited_paths = {(0, 0) : (None, 0)}
	visited = set()
	while shortest_paths:
		risk_total, (y, x) = heappop(shortest_paths)
		if y == y_length-1 and x == x_length-1:
			path = []
			current_cave = (y, x)
			while current_cave is not None:
				path.append(current_cave)
				current_cave = visited_paths[current_cave][0]
			path = path[::-1]
			return (path, risk_total)
		if (y, x) in visited:
			continue
		visited.add((y, x))
		adjacent_caves = list()
		if x > 0:
			adjacent_caves.append((y, x-1))
		if x < x_length-1:
			adjacent_caves.append((y, x+1))
		if y > 0:
			adjacent_caves.append((y-1, x))
		if y < y_length-1:
			adjacent_caves.append((y+1, x))
		for cave in adjacent_caves:
			(j, i) = cave
			new_risk_total = risks[j][i] + risk_total
			if cave not in visited:
				heappush(shortest_paths, (new_risk_total, cave))
				if cave not in visited_paths:
					visited_paths[cave] = ((y, x), new_risk_total)
				else:
					if visited_paths[cave][1] >= new_risk_total:
						visited_paths[cave] = ((y, x), new_risk_total)

with open('Risk Map.txt', 'r') as my_file:
	risks = my_file.readlines()

risks = [[int(i) for i in x.strip()] for x in risks]
horizontal_updated_risks = list()
for h in range(4):
	new_risks = [[r+h+1 if r+h+1 < 10 else r+h-8 for r in x] for x in risks]
	horizontal_updated_risks.append(new_risks)
for h in range(4):
	for e,x in enumerate(risks):
		for y in horizontal_updated_risks[h][e]:
			risks[e].append(y)
vertical_updated_risks = list()
for v in range(4):
	new_risks = [[r+v+1 if r+v+1 < 10 else r+v-8 for r in x] for x in risks]
	vertical_updated_risks.append(new_risks)
for v in range(4):
	for y in vertical_updated_risks[v]:
		risks.append(y)
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
print(f"\nRisk total of least risk path in updated map is {least_risk_total}.")
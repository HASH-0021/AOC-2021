from heapq import heappush,heappop

def least_risk_path():
	global risks
	y_length = len(risks)
	x_length = len(risks[0])
	shortest_paths = [(0, (0, 0))]
	visited = set()
	while shortest_paths:
		risk_total, (y, x) = heappop(shortest_paths)
		if y == y_length-1 and x == x_length-1:
			return risk_total
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
least_risk_total = least_risk_path()
print(f"\nRisk total of least risk path in updated map is {least_risk_total}.")
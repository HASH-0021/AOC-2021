
def find_basin(x,y,count):
	if y-1 >= 0:
		if caves_2[x][y-1] != 9 and caves_2[x][y-1] != 'done':
			count += 1
			caves_2[x][y-1] = 'done'
			count = find_basin(x,y-1,count)
	if y+1 < len(caves_2[x]):
		if caves_2[x][y+1] != 9 and caves_2[x][y+1] != 'done':
			count += 1
			caves_2[x][y+1] = 'done'
			count = find_basin(x,y+1,count)
	if x-1 >= 0:
		if caves_2[x-1][y] != 9 and caves_2[x-1][y] != 'done':
			count += 1
			caves_2[x-1][y] = 'done'
			count = find_basin(x-1,y,count)
	if x+1 < floors_length:
		if caves_2[x+1][y] != 9 and caves_2[x+1][y] != 'done':
			count += 1
			caves_2[x+1][y] = 'done'
			count = find_basin(x+1,y,count)
	return count

with open('Height map.txt', 'r') as my_file:
	caves = my_file.readlines()

caves = [x.strip() for x in caves]
caves = [[int(i) for i in x] for x in caves]
caves_2 = list()
for l in caves:
	caves_2.append(l[:])
floors_length = len(caves)
basin_size_list = list()
for e1,floor in enumerate(caves):
	points_length = len(floor)
	for e2,point in enumerate(floor):
		lowest_check = True
		if e2-1 >= 0:
			if point >= floor[e2-1]:
				lowest_check = False
		if e2+1 < points_length:
			if point >= floor[e2+1]:
				lowest_check = False
		if e1-1 >= 0:
			if point >= caves[e1-1][e2]:
				lowest_check = False
		if e1+1 < floors_length:
			if point >= caves[e1+1][e2]:
				lowest_check = False
		if lowest_check:
			caves_2[e1][e2] = 'done'
			basin_size = find_basin(e1,e2,1)
			basin_size_list.append(basin_size)
three_largest_basins = sorted(basin_size_list,reverse = True)[:3]
product_basin_sizes = 1
for i in three_largest_basins:
	product_basin_sizes *= i
print(f"Product of sizes of three largest basins is {product_basin_sizes}.")

with open('Height map.txt', 'r') as my_file:
	caves = my_file.readlines()

caves = [x.strip() for x in caves]
caves = [[int(i) for i in x] for x in caves]
low_points = list()
floors_length = len(caves)
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
			low_points.append(point)
risk_levels = [i+1 for i in low_points]
total_risk = sum(risk_levels)
print(f"Sum of risk levels of all low points on height map is {total_risk}.")
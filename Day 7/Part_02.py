
def fuel_consumption(horizontal_position, position):
	total = 0
	for i in horizontal_position:
		distance = abs(position - i)
		distance = distance*(distance+1)//2
		total += distance
	return total

with open('Crab Position.txt', 'r') as my_file:
	horizontal_position = my_file.read().split(',')

horizontal_position = [int(i) for i in horizontal_position]
farthest = max(horizontal_position)
least_fuel_total = sum(horizontal_position)
least_fuel_total = least_fuel_total*(least_fuel_total+1)//2
least_fuel_position = 0
for p in range(farthest+1):
	fuel_total = fuel_consumption(horizontal_position, p)
	if fuel_total <= least_fuel_total:
		least_fuel_total = fuel_total
		least_fuel_position = p
print(f"Least fuel possible position is {least_fuel_position}.")
print(f"Total fuel consumption for position {least_fuel_position} is {least_fuel_total}.")
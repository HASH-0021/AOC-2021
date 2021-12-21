
def fold_horizontal(fold_loc):
	global paper
	paper_2 = [y[:] for enum,y in enumerate(paper) if enum < fold_loc]
	paper_3 = [y[:] for enum,y in enumerate(paper) if enum > fold_loc]
	extra_len = abs(len(paper_2)-len(paper_3))
	if len(paper_2) > len(paper_3):
		paper_2 = [y[:] for enum,y in enumerate(paper_2) if enum >= extra_len]
	elif len(paper_3) > len(paper_2):
		paper_3 = [y[:] for enum,y in enumerate(paper_3) if enum < len(paper_3)-extra_len]
	for e1,y in enumerate(paper_3):
		for e2,x in enumerate(y):
			paper_2[-e1-1][e2] += x
	paper = [y[:] for y in paper_2]

def fold_vertical(fold_loc):
	global paper
	paper_2 = [[x for enum,x in enumerate(y) if enum < fold_loc] for y in paper]
	paper_3 = [[x for enum,x in enumerate(y) if enum > fold_loc] for y in paper]
	extra_len = abs(len(paper_2)-len(paper_3))
	if len(paper_2) > len(paper_3):
		paper_2 = [[x for enum,x in enumerate(y) if enum >= extra_len] for y in paper_2]
	elif len(paper_3) > len(paper_2):
		paper_3 = [[x for enum,x in enumerate(y) if enum < len(paper_3)-extra_len] for y in paper_3]
	for e1,y in enumerate(paper_3):
		for e2,x in enumerate(y):
			paper_2[e1][-e2-1] += x
	paper = [y[:] for y in paper_2]

with open('Instructions.txt', 'r') as my_file:
	instructions = my_file.readlines()

instructions = [x.strip() for x in instructions]
split_index = instructions.index('')
coordinates = instructions[:split_index]
coordinates = [x.split(',') for x in coordinates]
coordinates = [[int(i) for i in x] for x in coordinates]
fold_directions = instructions[split_index+1:]
fold_directions = [x.split(' ')[2] for x in fold_directions]
fold_tuples = [x.split('=') for x in fold_directions]
max_x,max_y = 0,0
for p in coordinates:
	if max_x < p[0]:
		max_x = p[0]
	if max_y < p[1]:
		max_y = p[1]
paper = list()	
for y in range(max_y+1):
	row = list()
	for x in range(max_x+1):
		row.append(0)
	paper.append(row[:])
for point in coordinates:
	x_coord = point[0]
	y_coord = point[1]
	paper[y_coord][x_coord] += 1
fold = fold_tuples[0]
if fold[0] == 'x':
	fold_vertical(int(fold[1]))
elif fold[0] == 'y':
	fold_horizontal(int(fold[1]))
dot_count = 0
for e1,y in enumerate(paper):
	for e2,x in enumerate(y):
		if x:
			dot_count += 1
			paper[e1][e2] = '#'
		else:
			paper[e1][e2] = '.'
print(f"Number of dots in overlapped section after first fold is {dot_count}.")
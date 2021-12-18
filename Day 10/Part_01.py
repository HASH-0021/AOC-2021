
with open('Navigation Subsystem Syntax.txt', 'r') as my_file:
	syntax_lines = my_file.readlines()

syntax_lines = [x.strip() for x in syntax_lines]
left_bound = ['(', '[', '{', '<']
right_bound = [')', ']', '}', '>']
illegal_char_list = list()
syntax_error_points = [3, 57, 1197, 25137]
syntax_error_score = 0
syntax_lines_2 = syntax_lines[:]
syntax_lines_2 = [[x for x in line] for line in syntax_lines_2]
for e1,line in enumerate(syntax_lines_2):
	for e2,x in enumerate(line):
		if x in right_bound:
			temp = e2-1
			pos = right_bound.index(x)
			if temp >= 0:
				while syntax_lines_2[e1][temp] == 'done':
					temp -= 1
				if syntax_lines_2[e1][temp] == left_bound[pos]:
					syntax_lines_2[e1][temp] = 'done'
					syntax_lines_2[e1][e2] = 'done'
				else:
					illegal_char_list.append(x)
					break
			else:
				illegal_char_list.append(x)
				break	
for x in illegal_char_list:
	pos = right_bound.index(x)
	syntax_error_score += syntax_error_points[pos]
print(f"Total syntax error score for the errors is {syntax_error_score}.")
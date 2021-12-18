
from statistics import median

with open('Navigation Subsystem Syntax.txt', 'r') as my_file:
	syntax_lines = my_file.readlines()

syntax_lines = [x.strip() for x in syntax_lines]
left_bound = ['(', '[', '{', '<']
right_bound = [')', ']', '}', '>']
corrupted_lines = list()
point_value = [1, 2, 3, 4]
total_scores = list()
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
					corrupted_lines.append(syntax_lines_2[e1])
					break
			else:
				corrupted_lines.append(syntax_lines_2[e1])
				break	
incomplete_lines = [x for x in syntax_lines_2 if x not in corrupted_lines]
completion_strings = list()
for line in incomplete_lines:
	completion_strings.append([left_bound.index(x) for x in line if x != 'done'])
for enum,string in enumerate(completion_strings):
	completion_strings[enum] = [right_bound[x] for x in string[::-1]]
for string in completion_strings:
	score = 0
	for x in string:
		pos = right_bound.index(x)
		score = (score*5)+point_value[pos]
	total_scores.append(score)
middle_score = median(total_scores)
print(f"Middle score of all completion string scores is {middle_score}.")

with open('Polymer Formula.txt', 'r') as my_file:
	formula = my_file.readlines()

formula = [x.strip() for x in formula if x != '\n']
polymer_template = formula[0]
pair_insertion_rules = [x.split(' -> ') for x in formula[1:]]
steps = 40
elements = dict()
pair_count = dict()
for x in pair_insertion_rules:
	pair_count.update({x[0] : 0})
	elements.update({x[1] : 0})
polymer_length = len(polymer_template)
pair_count_2 = {k:v for k,v in pair_count.items()}
for i in range(polymer_length-1):
	pair = polymer_template[i:i+2]
	pair_count_2[pair] += 1
for x in polymer_template:
	elements[x] += 1
new_pair_count = {k:v for k,v in pair_count_2.items()}
for step in range(steps):
	for x in pair_count:
		if pair_count_2[x] != pair_count[x]:
			element = ''.join(y[1] for y in pair_insertion_rules if y[0] == x)
			pair = element.join(x)
			count_diff = abs(pair_count[x]-pair_count_2[x])
			elements[element] += count_diff
			new_pair_count[pair[:2]] += count_diff
			new_pair_count[pair[1:]] += count_diff
	pair_count = {k:v for k,v in pair_count_2.items()}
	pair_count_2 = {k:v for k,v in new_pair_count.items()}
most_count = max(elements.values())
least_count = min(elements.values())
print(f"Difference between quantities of most common element and least common element is {most_count-least_count}.")
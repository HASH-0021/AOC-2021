
with open('Polymer Formula.txt', 'r') as my_file:
	formula = my_file.readlines()

formula = [x.strip() for x in formula if x != '\n']
polymer_template = formula[0]
pair_insertion_rules = [x.split(' -> ') for x in formula[1:]]
steps = 10
for step in range(steps):
	next_template = str()
	polymer_length = len(polymer_template)
	for i in range(polymer_length-1):
		pair = polymer_template[i:i+2]
		for rule in pair_insertion_rules:
			if rule[0] == pair:
				pair = rule[1].join(pair)
				break
		if i:
			next_template += pair[1:]
		else:
			next_template += pair
	polymer_template = next_template
elements = dict()
for x in polymer_template:
	elements.update({x : 0})
for x in polymer_template:
	elements[x] += 1
most_count = max(elements.values())
least_count = min(elements.values())
print(f"Difference between quantities of most common element and least common element is {most_count-least_count}.")
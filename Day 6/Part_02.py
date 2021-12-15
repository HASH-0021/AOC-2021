
with open('Creation Timer List.txt', 'r') as my_file:
	fish_timer_list = my_file.read().split(',')
	for enum,t in enumerate(fish_timer_list):
		fish_timer_list[enum] = int(t)
	timer_count_list = [fish_timer_list.count(i) for i in range(9)]
	days = 256
	for d in range(days):
		zero_timer_count = timer_count_list[0]
		for i in range(8):
			timer_count_list[i] = timer_count_list[i+1]
		timer_count_list[6] += zero_timer_count
		timer_count_list[8] = zero_timer_count
	count = sum(timer_count_list)
	print(f"After {days} days, there are a total of {count} lanternfish.")
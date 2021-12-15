
with open('Creation Timer List.txt', 'r') as my_file:
	fish_timer_list = my_file.read().split(',')
	for enum,t in enumerate(fish_timer_list):
		fish_timer_list[enum] = int(t)
	print("Initial state: ",end = '')
	print(",".join(str(t) for t in fish_timer_list))
	days = 80
	for d in range(1,days+1):
		new_fish_count = 0
		for enum,t in enumerate(fish_timer_list):
			if t:
				fish_timer_list[enum] -= 1
			else:
				fish_timer_list[enum] = 6
				new_fish_count += 1
		for i in range(new_fish_count):
			fish_timer_list.append(8)
		if d == 1:
			print(f"After {d} day: ",end = '')
			print(",".join(str(t) for t in fish_timer_list))
		else:
			print(f"After {d} days: ",end = '')
			print(",".join(str(t) for t in fish_timer_list))
	print(f"After {days} days, there are a total of {len(fish_timer_list)} lanternfish.")
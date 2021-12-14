
def board_check(board):
	for i in board:
		if i.count('done') == 5:
			return True
	return False

def inv_board(board):
	new_line = list()
	new_board = list()
	for i in range(5):
		for j in range(5):
			new_line.append(board[j][i])
		new_board.append(new_line[:])
		new_line.clear()
	return new_board

def total(board):
	total = 0
	for i in board:
		for j in i:
			if j != 'done':
				total += int(j)
	return total

flag = False

with open('Bingo.txt', 'r') as my_file:
	rand_num = my_file.readline().rstrip().split(',')
	boards,each_board = list(),list()
	for i in my_file.readlines():
		if i != '\n':
			line = i.strip().split(' ')
			for j in line:
				if not j:
					line.remove('')
			each_board.append(line)
		elif each_board:
			boards.append(each_board[:])
			each_board.clear()
	boards.append(each_board[:])
	each_board.clear()
	for i in rand_num:
		for j in boards:
			for k in j:
				if i in k:
					k[k.index(i)] = 'done'
					if board_check(j) or board_check(inv_board(j)):
						board_no = boards.index(j) + 1
						final_score = total(j) * int(i)
						flag = True
						break
			if flag:
				break
		if flag:
			break
	print(f"Board no. {board_no} won this bingo game.")
	print(f"Final score of board no. {board_no} is {final_score}.")
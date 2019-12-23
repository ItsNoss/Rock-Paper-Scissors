import random

rps = ['Rock', 'Paper', 'Scissors']

choice = str(input('Rock, Paper, or Scissors? '))

i = 0

while i == 0:
	random.shuffle(rps)
	print(rps[1])
	if rps[1] == choice:
		print("It was a tie!")
		i += 1
	elif rps[1] == 'Rock' and choice == 'Paper' or rps[1] == 'Rock' and choice == 'paper':
		print('You Win!')
		i += 1
	elif rps[1] == 'Rock' and choice == 'Scissors' or rps[1] == 'Rock' and choice == 'scissors':
		print('You Lose!')
		i += 1
	elif rps[1] == 'Paper' and choice == 'Scissors' or rps[1] == 'Paper' and choice == 'scissors':
		print('You Win!')
		i += 1
	elif rps[1] == 'Paper' and choice == 'Rock' or rps[1] == 'Paper' and choice == 'rock':
		print('You Lose!')
		i += 1
	elif rps[1] == 'Scissors' and choice == 'Paper' or rps[1] == 'Scissors' and choice == 'paper':
		print('You Lose!')
		i += 1
	elif rps[1] == 'Scissors' and choice == 'Rock' or rps[1] == 'Scissors' and choice == 'rock':
		print('You Win!')
		i += 1
	else:
		print('Please choose either Rock, Paper, or Scissors!')
		i += 1
import random

rps = ['Rock', 'Paper', 'Scissors']

x = random.shuffle(rps)

ask = str(input('Rock, Paper, or Scissors: '))

if ask != rps[0]:
    print(f'You lose. {rps[0]}')
else:
    print(f'You Win. {rps[0]}')
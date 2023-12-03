from random import randint
from random import choice
score = 0
when = randint(1, 10)
checker = 0
s = 0


def Bosslevel(score):
	print('Bonus level: \n')
	roundto = [10000, 100000]
	
	choose = choice(roundto)
	
	number = randint(1, 999999)
	print('Round ' + str(number) + ' to the nearest ' + str(choose))
	
	good=input('Your answer: ')
	
	answer = str(round(number / choose)*choose)
	
	if good == answer:
		score += 10
		print('Good Job!!!')
		checker = 0
	else:
		score -= 10
		print('Try again later!')
		checker = 0
	print('Bonus level ended: \n')
	return score


while True:
	roundto = [10, 100, 1000, 10000]
	
	choose = choice(roundto)
	
	number = randint(1000, 99999)
	print('Round ' + str(number) + ' to the nearest ' + str(choose))
	
	good=input('Your answer: ')
	
	answer = str(round(number / choose)*choose)
	
	if good.lower() == 'sleep':
		 input('Sleep')
		 break
		 
	
	if good == answer:
		score += 1
		checker += 1
		print('Correct!')
		print('Score: ' + str(score) + ' (+1)')
		print()
	else:
		score -= 1
		checker += 1
		print('Wrong, correct was: ' + answer)
		print('Score: ' + str(score) + ' (-1)')
		print()
		
		if score == 100:
			print('Good Job, keep going!')
		
		if checker == when:
			print('Join boss level? [Y, N]')
			choice2 = input()
			if choice2.lower() == 'y':
				s = Bosslevel(score)
			elif choice2.lower() == 'n':
				pass
			else:
				print('Aborted')
				checker = 0
				when = randint(1, 20)
			score = s
			s = 0

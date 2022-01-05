#Sunny Addition Practice
import random
print('Please sum the following numbers:')
x = 10
while x > 0:
	x = x - 1
	r1 = random.randint(1,10)
	r2 = random.randint(1,10)
	print(r1, '+', r2, '= ?')
	ans = input('Your answer:')
	ans = int(ans)
	if ans == r1 + r2:
		print('Excellent')
	else:
		while ans != r1 + r2:
			print('Wrong,try again')
			print(r1, '+', r2, '= ?')
			ans = input('Your answer:')
			ans = int(ans)
			if ans == r1 + r2:
				print('Excellent!')
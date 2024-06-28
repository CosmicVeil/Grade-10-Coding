
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end='')
#     print()

# import random

# number1 = random.randint(1, 1000)
# number2 = random.randint(1, 1000)
# total = number1 + number2
# print('\t', number1)
# print('+\t', number2)

# answer = int(input('Enter the answer: '))

# def check(answer, total):
#     if answer == total:
#         print('Congratulations!')
#     else:
#         print('False. The answer is', total)

# check(answer, total)

def pyramid_pattern(n):
	for i in range(0, n):
		for j in range(0, n):
			print(end=" ")
		n = n-1
		for j in range(0, i+1):
			print("*", end=" ")
		print()

pyramid_pattern(10)

string = input('Enter the string: ')
positive_sum = 0
negative_sum = 0
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
for i in range(len(string)):
	if string[i] == '-':
		if string[i + 1].isdigit():
			i += 1
			negative_sum -= int(string[i])
			if int(string[i]) % 2 == 0:
				even_sum -= int(string[i])
				even_count += 1
			else:
				odd_sum -= int(string[i])
				odd_count += 1
	elif string[i].isdigit():
		positive_sum += int(string[i])
		if int(string[i]) % 2 == 0:
			even_sum += int(string[i])
			even_count += 1
		else:
			odd_sum += int(string[i])
			odd_count += 1
print(f'Positive sum: {positive_sum}\tNegative sum: {negative_sum}')
print(f'Even sum: {even_sum}\tOdd sum: {odd_sum}')
print(f'Even count: {even_count}\tOdd count: {odd_count}')

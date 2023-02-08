def check(val:str):
	if val == val[::-1]:
		return True
	else:
		return False


a=input("Enter a number: ")
if check(a):
	print("Palindrome")
else:
	print("Not a Palindrome")
	
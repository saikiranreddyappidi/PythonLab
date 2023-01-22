di={1:10,2:20,3:30,4:40,5:50,6:60}
x=int(input("Enter a number: "))
for i in di:
	if i==x:
		print("Found: ",di[i])
		exit(2)
print("Not found")
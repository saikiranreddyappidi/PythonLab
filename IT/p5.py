str1="abcdef"
str2="defghia"
cnt=0
for i in str1:
	if i in str2:
		print(i)
		cnt+=1
print("count: ",cnt)
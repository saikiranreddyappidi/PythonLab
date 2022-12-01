import numpy

arr = numpy.random.randint(10, 30, (5, 4))
print(arr)
print("Last row: ", arr[-1], "\nLast but one row: ", arr[-2])
print("Sum of 2nd row values: ", sum(arr[3]))
maxi = numpy.where(arr == numpy.amax(arr))
print("Maximum number is: ", numpy.amax(arr))
print("They are at: ")
print(*list(zip(maxi[0], maxi[1])), sep="\n")
last = numpy.array(numpy.random.randint(0, 10, (1, 4)))
# print(last)
arr = numpy.append([arr], [[last]]).reshape(6, 4)
print(arr)
x, z = map(int, input("Enter a value to replace and replace with: ").split())
arr[x == arr] = z
print(arr)
x = int(input("Enter the x value: "))
print(arr[x > arr].size)
s = arr.size
print("All possible shapes of the array are: ")
con = "Shape ({},{}):\n"
for i in range(1, s):
	if s % i == 0:
		print(con.format(i, int(s / i)), arr.reshape(i, int(s / i)))
arr=arr.astype("float64")
print("After changing the datatype to float: \n",arr)
print("Unique elements in the given array are: ",numpy.unique(arr))
exit(3)

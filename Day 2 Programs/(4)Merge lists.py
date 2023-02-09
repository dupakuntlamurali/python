A = list(map(int,input("Enter a list of numbers separated by space: ").strip().strip().split()))
B = list(map(int,input("Enter a list of numbers separated by space: ").strip().strip().split()))
print("The list 1 is : " + str(A))
print("The list 2 is : " + str(B))
size_1 = len(A)
size_2 = len(B)
res = []
i, j = 0, 0
while i < size_1 and j < size_2:
	if A[i] < B[j]:
		res.append(A[i])
		i += 1
	else:
		res.append(B[j])
		j += 1
res = res + A[i:] + B[j:]

print("The combined sorted list is : " + str(res))

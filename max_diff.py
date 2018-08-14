# find max diff of an array such that max elem occurs after min elem.

arr = [7, 9, 5, 6, 3, 2]

ans_max = None
ans_min = None
j= None
for i in range(len(arr)):
	if i+1<len(arr):
		if arr[i+1] > arr[i]:
			ans_max = arr[i+1]
			ans_min = arr[i]
			j=i+1
			break
if not ans_max:
	print('no such elements exist')

poten_max = ans_max
poten_min = ans_min
diff = ans_max - ans_min
for i in range(j+1, len(arr)):
	if arr[i] - poten_min > diff:
		ans_max = arr[i]
		ans_min = poten_min
	elif arr[i] > ans_max:
		ans_max = arr[i]
	elif arr[i] < ans_max:
		if arr[i] < ans_min:
			poten_min = arr[i]
	diff = ans_max - ans_min

print('max diff is {},  max {},  min {}'.format(diff, ans_max, ans_min))

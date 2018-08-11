# Find max sum subarray

arr = [1,5,-3,6,-2,9,-4]


max_sum = None
current_sum = None
start = 0
end = 0
s = 0
for i  in range(len(arr)):
	if not max_sum:
		max_sum = arr[i]
		current_sum = arr[i]
		if current_sum < 0:
			current_sum = 0
	else:
		current_sum = arr[i] + current_sum
		if current_sum > max_sum:
			max_sum = current_sum
			start = s
			end = i
		if current_sum < 0:
			current_sum = 0
			s = i + 1


print('max sum is {}'.format(max_sum))
print('start {} end {}'.format(start, end))

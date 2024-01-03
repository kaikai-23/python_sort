from typing import List
import random

def merge_sort(nums_list: List[int]) -> List[int]:
	# 分割するところ
	if len(nums_list) <= 1:
		return (nums_list)

	center = len(nums_list) // 2
	left = nums_list[:center]
	right = nums_list[center:]

	left = merge_sort(left)
	right = merge_sort(right)

	# スワップするところ
	i = j = k = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			nums_list[k] = left[i]
			i += 1
		else:
			nums_list[k] = right[j]
			j += 1
		k += 1
	
	while i < len(left):
		nums_list[k] = left[i]
		i += 1
		k += 1
	
	while j < len(right):
		nums_list[k] = right[j]
		j += 1
		k += 1

	return nums_list

if __name__ == "__main__":
	# nums_list = [5, 4, 1, 8, 7, 3, 2, 9]
	nums_list = [random.randint(0, 1000) for _ in range(10)]
	print(nums_list)
	print(merge_sort(nums_list))

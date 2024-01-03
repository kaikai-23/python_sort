from typing import List
import random 

def insertion_sort(nums_list: List[int]) -> List[int]:
	list_len = len(nums_list)
	for i in range(1, list_len):
		temp = nums_list[i]
		j = i - 1
		while j >= 0 and nums_list[j] > temp:
			nums_list[j+1] = nums_list[j]
			j -= 1
		nums_list[j+1] = temp
	return nums_list

if __name__ == "__main__":
	nums = [random.randint(0, 1000) for _ in range(10)]
	# nums = [1, 7, 3, 2, 8, 5]
	print(nums)
	print(insertion_sort(nums))

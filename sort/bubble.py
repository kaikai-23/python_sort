from typing import List
import random

def bubble_sort(nums_list: List[int]) -> List[int]:
	list_len = len(nums_list)
	for i in range(list_len):
		for j in range(list_len - 1 - i):
			if nums_list[j] > nums_list[j+1]:
				nums_list[j], nums_list[j+1] = nums_list[j+1], nums_list[j]
	return nums_list

if __name__ == "__main__":
	nums_list = [random.randint(0, 1000) for _ in range(10)]
	print(nums_list)
	print(bubble_sort(nums_list))

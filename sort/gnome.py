from typing import List
import random 

def gnome_sort(nums_list: List[int]) -> List[int]:
	list_len = len(nums_list)
	index = 0
	while index < list_len:
		if index == 0:
			index += 1
		if nums_list[index-1] < nums_list[index]:
			index += 1
		else:
			nums_list[index], nums_list[index-1] = nums_list[index-1], nums_list[index]
			index -= 1
	return nums_list

if __name__ == "__main__":
	nums = [random.randint(0, 1000) for _ in range(10)]
	print(nums)
	print(gnome_sort(nums))

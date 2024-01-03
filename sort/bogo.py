import random
from typing import List

def in_order(nums_list: List[int]) -> bool:
	for i in range(len(nums_list) - 1):
		if nums_list[i] > nums_list[i + 1]:
			return False
	return True

def shuffle_list(nums_list: List[int]) -> List[int]:
	random.shuffle(nums_list)
	return nums_list

def bogo_sort(nums_list: List[int]) -> List[int]:
	while not in_order(nums_list):
		shuffle_list(nums_list)
	return (nums_list)

if __name__ == "__main__":
	nums = [random.randint(0, 1000) for _ in range(5)]
	print(nums)
	print(bogo_sort(nums))

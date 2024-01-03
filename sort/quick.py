from typing import List
import random

def partition(num_list: List[int], low: int, high: int) -> int:
	i = low - 1
	pivot = num_list[high]
	for j in range(low, high):
		if num_list[j] <= pivot:
			i += 1
			num_list[j], num_list[i] = num_list[i], num_list[j]
	num_list[i+1], num_list[high] = num_list[high], num_list[i+1]
	return i+1

def quick_sort(num_list: List[int]) -> List[int]:
	def __quick_sort(num_list: List[int], low: int, high: int) -> None:
		if low < high:
			partition_index = partition(num_list, low, high)
			__quick_sort(num_list, low, partition_index-1)
			__quick_sort(num_list, partition_index+1, high)
	
	__quick_sort(num_list, 0, len(num_list)-1)
	return num_list

if __name__ == "__main__":
	# nums = [1, 8, 3, 9, 4, 5, 7]
	nums = [random.randint(0, 100) for _ in range(10)]
	print(nums)
	print(quick_sort(nums))

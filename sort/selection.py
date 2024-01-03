from typing import List
import random 

def selection_sort(numbers: List[int]) -> List[int]:
	list_len = len(numbers)
	for i in range(list_len):
		min_index = i
		for j in range(i+1, list_len):
			if numbers[min_index] > numbers[j]:
				min_index = j
		if min_index != i:
			numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
	return numbers

if __name__ == "__main__":
	nums = [random.randint(0, 1000) for _ in range(10)]
	print(nums)
	print(selection_sort(nums))

from typing import List
import random

def counting_sort(nums_list: List[int]) -> List[int]:
	max_num = max(nums_list)
	counts = [0] * (max_num + 1)

	for num in nums_list:
		counts[num] += 1

	for i in range(1, len(counts)):
		counts[i] += counts[i-1]
	print(counts)

	result = [0] * len(nums_list)
	i = len(nums_list) - 1
	while i >= 0:
		counts_index = nums_list[i]
		result[counts[counts_index] -1] = nums_list[i]
		counts[counts_index] -= 1
		i -= 1
	return result

if __name__ == "__main__":
	nums_list = [4, 3, 6, 2, 3, 4, 7]
	# nums_list = [random.randint(0, 50) for _ in range(10)]
	print(nums_list)
	print(counting_sort(nums_list))

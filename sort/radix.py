from typing import List
import random

def counting_sort(nums_list: List[int], place: int) -> List[int]:
	# 位一つあたり0~9まででソートするから
	counts = [0] * 10

	for num in nums_list:
		index = int(num/place) % 10
		counts[index] += 1

	for i in range(1, 10):
		counts[i] += counts[i-1]
	print(counts)

	result = [0] * len(nums_list)
	i = len(nums_list) - 1
	while i >= 0:
		counts_index = int(nums_list[i]/place) % 10
		result[counts[counts_index] -1] = nums_list[i]
		counts[counts_index] -= 1
		i -= 1
	return result

def radix_sort(numbers):
	max_num = max(numbers)
	place = 1
	while max_num > place:
		numbers = counting_sort(numbers, place)
		print(numbers)
		place *= 10
	return numbers


if __name__ == "__main__":
	nums_list = [24, 10, 11, 324, 201, 101, 55]
	# nums_list = [random.randint(0, 50) for _ in range(10)]
	print(nums_list)
	print(radix_sort(nums_list))

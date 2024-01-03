from typing import List
import random 
from insertion import insertion_sort

def bucket_sort(nums_list: List[int]) -> List[int]:
	max_num = max(nums_list)
	list_len = len(nums_list)
	size = max_num // list_len

	buckets = [[] for _ in range(size)]
	for num in nums_list:
		i = num // size
		if i != size:
			buckets[i].append(num)
		else:
			buckets[size-1].append(num)
	for i in range(size):
		insertion_sort(buckets[i])

	result = []
	for i in range(size):
		print(f"iが{i}の時buckets[i]は{buckets[i]}")
		# 配列を連結
		result += buckets[i]
	return result

if __name__ == "__main__":
	# nums = [random.randint(0, 1000) for _ in range(10)]
	nums = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
	print(nums)
	print(bucket_sort(nums))

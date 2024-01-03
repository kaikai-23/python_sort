from typing import List
import random

def shell_sort(nums_list: List[int]) -> List[int]:
	list_len = len(nums_list)
	gap = int(list_len // 2)
	while gap > 0:
		for i in range(gap, list_len):
			temp = nums_list[i]
			j = i
			# jもiもgapつまり2
			while j-gap >= 0:
				if nums_list[j-gap] > temp:
					nums_list[j] = nums_list[j-gap]
					j -= gap
				else:
					break
			nums_list[j] = temp
		gap //= 2
	return nums_list

if __name__ == "__main__":
	# nums_list = [5, 6, 9, 2, 3]
	nums_list = [random.randint(0, 1000) for _ in range(10)]
	print(f"最初のかたち{nums_list}")
	print(f"最後の形{shell_sort(nums_list)}")

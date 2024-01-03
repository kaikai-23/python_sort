import random
from typing import List

def comb_sort(nums_list: List[int]) -> List[int]:
	list_len = len(nums_list)
	gap = list_len
	swap_flag = True

	while gap != 1 or swap_flag == True:
		swap_flag = False
		gap = int(gap / 1.3)
		if gap < 1:
			gap = 1			
		for i in range(0, list_len - gap):
			if nums_list[i] > nums_list[i + gap]:
				nums_list[i], nums_list[i + gap] = nums_list[i + gap], nums_list[i]
				swap_flag = True
	return nums_list

if __name__ == "__main__":
	# nums_list  = [4, 5, 6, 2, 10, 9, 8, 7]
	nums_list = [random.randint(0, 1000) for _ in range(10)]
	print(nums_list)
	print(comb_sort(nums_list))

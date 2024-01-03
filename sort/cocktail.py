import random
from typing import List

def cooktail_sort(nums_list: List[int]) -> List[int]:
	list_len = len(nums_list)
	
	start = 0
	end = list_len - 1
	swap_flag = True

	while swap_flag == True:
		swap_flag = False
		for i in range(start, end):
			if nums_list[i] > nums_list[i+1]:
				nums_list[i], nums_list[i+1] = nums_list[i+1], nums_list[i]
				swap_flag = True
		if swap_flag == False:
			break
		end -= 1

		swap_flag = False
		for i in range(end-1, start-1, -1):
			if nums_list[i] > nums_list[i+1]:
				nums_list[i], nums_list[i+1] = nums_list[i+1], nums_list[i]
				swap_flag = True
		if swap_flag == False:
			break
		start += 1
	return nums_list

if __name__ == "__main__":
	nums_list = [random.randint(0, 1000) for _ in range(10)]
	print(nums_list)
	print(cooktail_sort(nums_list))

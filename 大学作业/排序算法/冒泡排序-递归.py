# Implementation of Recursive Bubble sort 

def bubble_sort(listt): 
	for i, num in enumerate(listt): 
		try: 
			if listt[i+1] < num: 
				listt[i] = listt[i+1] 
				listt[i+1] = num 
				bubble_sort(listt) 
		except IndexError: 
			pass
	return listt 

listt = [64, 81, 2, 11, 7, 115, 32] 
bubble_sort(listt) 

print("Sorted array:"); 
for i in range(0, len(listt)): 
	print(listt[i], end=' ') 

# 输出
# Sorted array:
# 2 7 11 32 64 81 115 

# 简单递归实现

def printFun(test): 

	if (test < 1): 
		return
	else: 
	
		print( test, end = " ") 
		printFun(test-1) # statement 2 
		print( test, end = " ") 
		return
	

test = 3
printFun(test) 

# 输出
# 3 2 1 1 2 3 

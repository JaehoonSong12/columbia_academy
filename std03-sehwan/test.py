print("Hello World!")



###################################################3 DO NOT change this part
li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True] 

## given algorithm
val1, val2 = 0,'' 
for x in li: 
	if(type(x) == int or type(x) == float): 
		val1 = val1 + x
	elif(type(x) == str):
		val2 = val2 + x
	else: 
		break
print(val1, val2) 
###################################################3 DO NOT change this part


# 1. Now, try to print the same result using only `print(var)`
print(val1)
print(type(val1))
print(val2)
print(type(val2))
print(str(val1) + " " + val2) 
# print(var)




# 2. None actually means 0. and True means 1 actually, modify the result by not breaking the loop
if x is None:
	val1 = val1
else:
	val1 = val1+1

# 数组 - Python code to demonstrate the working of  
# array(), append(), insert(),  pop(), remove(), index(), reverse()
   
import array 
   
# 数组形成
arr = array.array('i', [5, 6, 7])  
  
# 输出新创建的数组
print ("The new created array is : ",end="") 
for i in range (0, 3): 
    print (arr[i], end=" ") 
  
print("\r") # 换行
  
# 用 append() 在数组末尾插入新值
arr.append(6); 
  
# 输出插入之后的数组
print("The appended array is : ", end="") 
for i in range (0, 4): 
    print (arr[i], end=" ") 
      
# 用 insert() 在特定位置插入新值
# 在第 3 个位置插入 0
arr.insert(3, 0) 
  
print("\r") 
  
# 输出插入之后的数组
print ("The array after insertion is : ", end="") 
for i in range (0, 5): 
    print (arr[i], end=" ") 

print("\r") 

# 用 pop()删除想要的元素，而让它弹出
print("The popped element is : ", end="")
print(arr.pop(2))

# 输出删除之后的数组
print("The array after popping is : ", end="")
for i in range(4):
    print(arr[i], end=" ")

print("\r")

# 使用 remove() 删除第一次出现的 6
arr.remove(6)

# 输出删除之后的数组
print("The array after removing is : ", end="")
for i in range(3):
    print(arr[i], end=" ")

print("\r")

#使用 index()输出第一次出现的 0 的位置
arr.append(0)
print("The appended array is : ", end="")
for i in range(4):
    print(arr[i], end=" ")
print("\r")
print("The index of 1st occurence of 0 is : ", end="")
print(arr.index(0))

#使用 reverse() 反转数组
arr.reverse()
print ("The array after reversing is : ",end="")
for i in range(4):
    print(arr[i], end=" ")

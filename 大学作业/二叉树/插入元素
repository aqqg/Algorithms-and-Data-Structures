# Program to insert element in binary tree 
class newNode(): 
    
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None

""" Inorder traversal of a binary tree"""
def inorder(temp): 
    
    if (not temp): 
        return
    
    inorder(temp.left) 
    print(temp.key,end = " ") 
    inorder(temp.right) 


"""function to insert element in binary tree"""
def insert(temp,key): 

    q = [] 
    q.append(temp) 

    # Do level order traversal until we find 
    # an empty place. 
    while (len(q)): 
        temp = q[0] 
        q.pop(0) 

        if (not temp.left): 
            temp.left = newNode(key) 
            break
        else: 
            q.append(temp.left) 

        if (not temp.right): 
            temp.right = newNode(key) 
            break
        else: 
            q.append(temp.right) 
    
# Driver code 
if __name__ == '__main__': 
    root = newNode(20) 
    root.left = newNode(9) 
    root.left.left = newNode(11) 
    root.right = newNode(15) 
    root.right.left = newNode(13) 
    root.right.right = newNode(6) 

    print("Inorder traversal before insertion:", end = " ") 
    inorder(root) 

    key = 12
    insert(root, key) 

    print() 
    print("Inorder traversal after insertion:", end = " ") 
    inorder(root) 
    
# Output: 
# Inorder traversal before insertion: 11 9 20 13 15 6 
# Inorder traversal after insertion: 11 9 12 20 13 15 6 

''' 
Binary search uses a technique of divide and conquer technique. 
This type of technique is used in the case of sorted lists.    
Instead of searching an element one by one in the list, it directly goes to the middle element of the list, 
divides the array into 2 parts, and decides element lies in which sub-array the element exists.

Binary Search is a high-speed searching algorithm having the complexity of (logn)

'''

def BinarySearch(Num_List, target, low=None,high=None):
    
    #lowest possible index you can check
    if low is None:
        low = 0
        
    #highest possible index
    if high is None:
        high = len(Num_List) - 1
    
    #Target is Not in the list    
    if high < low:
        return -1
        
        
    mid = (low + high ) // 2 ## 2
    
    if Num_List[mid] == target:
        return mid 
    
    elif target < Num_List[mid]:
        #using recursion to go through the list
        return BinarySearch(Num_List, target, low, mid - 1 )
    
    else:
        return BinarySearch(Num_List, target, mid + 1, high)


Num_List = [1, 2, 3, 6, 9, 10, 11, 23, 34, 45] #list must be sorted for this to work properly

target = 10

print("An item is found at index: " + str(BinarySearch(Num_List, target))) #returns the position of the number you searched for

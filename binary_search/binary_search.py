"""
Binary Search Problem.

FEATURES:
Binary search is an algorithm used in search related problems. 
It is an efficient algorithm for finding an item from a sorted list of items. 

EXAMPLE CASE: Find a number in a list of 1000 numbers.

EXPLANATION:
1. Divide a list by half. Make it as a midpoint. 
2. Check if midpoint value is higher or lower than searched number. 
3. If midpoint value is higher, make right half equal to midpoint - 1. 
4. If midpoint value is lower, make left half equal to midpoint + 1. 
5. If midpoint value is equal to searched number, show midpoint value.
6. If no searched number is found, write "None" or "-1"  

BIG O:
Time complexity: O(log n)

"""

# Simple Binary Search Example
def binary_search(mylist, item):
    l = 0
    r = len(mylist) - 1
    while l <= r: 
        middle = (l + r) // 2 # show floor number, // in python is used for getting floor
        if mylist[middle] > item: 
            r = middle - 1            
        elif mylist[middle] < item:                   
            l = middle + 1
        else:
           return middle
    return -1

my_list = [1, 3, 5, 7, 9, 11, 15] # length 6
selectedNumber = 11
print(binary_search(my_list, selectedNumber))


# Binary search with string
def binarySearchStrings(myList, name):
    first = 0
    last = len(myList) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if myList[midpoint] > name:
            last = midpoint - 1 
        elif myList[midpoint] < name:
            first = midpoint + 1
        else:
            return midpoint
    return -1

names = ["Akbar", "Botir", "Camilla", "Sherzod"]
selectedName = "Botir"
print(binarySearchStrings(names, selectedName))


# LeetCode 35. Search Insert Position
def binarySearch(mylist, item):
    l = 0
    r = len(mylist) - 1
    while l <= r: 
        middle = (l + r) // 2 # show floor
        if mylist[middle] > item: 
            r = middle - 1            
        elif mylist[middle] < item:                   
            l = middle + 1
        else:
           return middle
    return l

my_list = [1, 3, 5, 7, 9, 11, 15, 16]
selectedNumber = 17
print(binarySearch(my_list, selectedNumber))

# LeetCode 704. Binary Search
def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r: 
        middle = (l + r) // 2
        if nums[middle] > target: 
            r = middle - 1            
        elif nums[middle] < target:                   
            l = middle + 1
        else:
           return middle
    return - 1

my_list = [-1,0,3,5,9,12]
selectedNumber = 2
print(search(my_list, selectedNumber))



# LeetCode 744. Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1

    while left <= right:
        midPoint = (left + right) // 2
        if letters[midPoint] > target:
            right = midPoint - 1
        else:
            left = midPoint + 1 
        
    if left < len(letters): 
        return letters[left]
    else: 
        return letters[0]  


letters = ["c","f","j"]
target = "j"
print(nextGreatestLetter(letters, target))
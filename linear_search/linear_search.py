"""
LINEAR SEARCH


FEATURES:
A sequential search algorithm that starts at one end and goes through each element of
a list until the desired element is found. Else continue

EXAMPLE CASE: Find smallest number in an array

EXPLANATION:
1. Loop starting from the first element and check if it is the value searched for. 
2. If found, show it. If not, continue.  

BIG O:
Time complexity: O(n)

"""

# Find lowest value
def findLowestValue(arr):
    currentValue = arr[0]
    for i in range(len(arr)):
        if currentValue > arr[i]:
            currentValue = i  
    return currentValue
myArr = [7,12,9,11,3,0,-1 ]
print(findLowestValue(myArr))


# Find given value 
def findValue(array, num):
    for i in range(len(array)):
        if array[i] == num:
            return i
    return "No such value"
myArr = [7,12,9,11,3,0,-1]
print(findValue(myArr, 9))
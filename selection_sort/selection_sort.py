"""
SELECTION SORT


FEATURES:
Selection sort is a simple and efficient sorting algorithm that works by repeatedly 
selecting the smallest (or largest) element from the unsorted portion of the list 
and moving it to the sorted portion of the list. Simply speaking:
  

EXAMPLE CASE: Search for most popular downloads of bands.

EXPLANATION:
1. Get first element in an array. 
2. Loop through to check it with the rest elements to identify smallest element.
If an element in array is smaller than first element, switch with the places. 
Continue to check with each next element of an array to identify the smallest element.
If an element in array is bigger, move to next element. 

BIG O:
Time complexity: O(n**2)
"""


# Simple Example
def selectionSort(myArray):
    arrayLength = len(myArray)  
    for i in range(arrayLength):
        smallestIndex = i 
        for j in range(i + 1, arrayLength): 
            if myArray[j] < myArray[smallestIndex]: 
                smallestIndex = j         
        print("Smallest Index: ", smallestIndex)        
        # swap array elements 
        temp = myArray[i]
        myArray[i] = myArray[smallestIndex]
        myArray[smallestIndex] = temp
    return myArray

print(selectionSort([30, 14, 3, 0, 45]))

# Another example, which takes into account duplication
def selectionSort1(nums):
          arrayLength = len(nums) 
          for i in range(arrayLength):
               smallestIndex = i
               for j in range(i + 1, arrayLength): 
                    if nums[j] < nums[smallestIndex]: 
                         smallestIndex = j      
               if smallestIndex != i: # it prevents unecessary check  
                    temp = nums[i]
                    nums[i] = nums[smallestIndex]
                    nums[smallestIndex] = temp
          return nums
print(selectionSort1([5,1,1,2,0,0]))

# Another example for selection sort, using pop and insert
def selectionSort2(my_array):
     n = len(my_array)
     for i in range(n):
          min_index = i
          for j in range(i+1, n):
               if my_array[j] < my_array[min_index]:
                    min_index = j
          min_value = my_array.pop(min_index)
          my_array.insert(i, min_value)
     return my_array

my_array = [64, 34, 25, 11, 1, 11, 90, 12, 0, 0]
print(selectionSort2(my_array))



# LeetCode 179. Largest Number
def selectionSort3(nums):
     nums = [str(num) for num in nums]  # list comprehension, string  
     for i in range(len(nums)):
          maxIndex = i
          for j in range(i + 1, len(nums)):
               if str(nums[j]) + str(nums[maxIndex]) > str(nums[maxIndex]) + str(nums[j]):
                    maxIndex = j
          nums[i], nums[maxIndex] = nums[maxIndex], nums[i]
     return str(int(''.join(nums))) # take into account only 000 make them 0
print(selectionSort3([3,30,34,5,9,0]))  # "9534330"


# LeetCode 179. Another solution
def selectionSort4(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i] # swap
    result = "".join(str(i) for i in nums) 
    return str(int(result)) # this will prevent miltiple 000. Convert to in then str
print(selectionSort4([3, 30, 34, 5, 9]))  # "9534330"

# LeetCode 75. Sort Colors
def selectionSort5(nums):
     for i in range(len(nums)):
          smallestIndex = i
          for j in range(i+1, len(nums)):
               if nums[smallestIndex] > nums[j]:
                    smallestIndex = j
          nums[i],nums[smallestIndex] = nums[smallestIndex],nums[i] 
     return nums
print(selectionSort5([2,0,1]))
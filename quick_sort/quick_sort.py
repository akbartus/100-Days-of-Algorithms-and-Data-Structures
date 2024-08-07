"""
QUICK SORT ALGORITHM.

FEATURES:
The height of the call stack is O(log n), whereas each level takes O(n) time. 
Therefore it is O(n log n). 
Pivots can be first/last/middle element or random. For best sceario select random.
Worst case is usually when pivot is first element or last element.

EXAMPLE CASE: Sort colors .

EXPLANATION:
1. Choose a pivot.  
2. Partition. Rearrange elements, so that what is to the left
of pivot are smaller numbers, what is to the right - bigger numbers.
3. Sort left and right parts. 

BIG O:
Time complexity: O(n log n)
Space complexity O(log n)

When pivot is smallest or largest element: 
Time complexity: O(n**2)
When pivot is random, then it is best case or average case:
Time complexity: O(n log n)

"""


# Quick sort with repeated numbers
def sortRepeated(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[len(nums)//2]
        left = [x for x in nums if x < pivot] # list comprehension
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
    return sortColors(left) + middle + sortColors(right)      
print(sortColorsRepeated([2,0,2,1,1,0]))

# Quick sort without repeated numbers
def sortNonRepeated(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[len(nums)//2]
        left = [x for x in nums if x < pivot]
        right = [x for x in nums if x > pivot]
    return selectionSort(left) + [pivot] + selectionSort(right)      
print(sortNonRepeated([2,0,2,1,1,0]))



# LeetCode 75. Sort Colors. 
def sortColors(nums):
    def quickSort(nums):
        if len(nums) <= 1:
            return nums
        else: 
            pivot = nums[len(nums)//2]
            left = [x for x in nums if x < pivot]
            right = [x for x in nums if x > pivot]
            middle = [x for x in nums if x == pivot]
            return quickSort(left) + middle + quickSort(right)
    nums[:] = quickSort(nums) # this replaces original array nums
    print(nums)
print(sortColors([2,0,2,1,1,0]))
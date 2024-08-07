"""
RECURSION

Recursion is a technique in which the function calls itself.
Recursion consists of: 
1. Base case, which shows terminating condition 
2. Recursive case, which tries to reduce the code complexity to base case.

It is used to break the code into sub-problems.
It uses Divide-and-Conquer problem solving approach.

Time Complexity: Higher due to the overhead of maintaining the function call stack.	
Space Complexity:	Higher than iteration.
Memory:	Uses more memory
Speed:	Slower than Iteration technique


"""

# Simple recursion example
def countTillTen(i):
    print(i)
    if i == 10:           # base case
        return
    else:                 # recursive case
        countTillTen(i+1) # reduce to base case
countTillTen(2)

# Recursion demonstrating loop like function
def loopToRecursion(nums):
    if len(nums) > 1:
        nums.pop()
        print(nums)
        loopToRecursion(nums)
nums = [1,5,6,7,8,9]
loopToRecursion(nums)


# Recursion used to convert string into reverse order
def reverseString(txt):
    newTxt = []
    for i in range(len(txt)-1, -1, -1): # start, end, step
        newTxt.append(txt[i])
    return newTxt
text = "akbar"
print(reverseString(text))


# Leetcode 344. Reverse string
def print_reverse(s):
    def recursiveReverse(l,r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            recursiveReverse(l+1, r-1)
    recursiveReverse(0, len(s)-1)
    print(s)
print(print_reverse(["h","e","l","l","o"]))
<b>Binary Tree or Binary Tree search</b> is the algorithm applied in search related tasks. Its takes as inputsorted array and an item and helps to identify its the index (position). Basic idea behind this algorithm is the following: 

1. when searching for the item in an array, rather than going one by one (linear search), we take half of the array and check if the being searched item is in one of them.
2. We take that half and divide it again into 2 halves and check if the item is present in one of them.
3. We do this until we find the item.

Consider the following example. To find 99th items in an array of 100 items, when using linear search we need 99 steps. 
When doing search using binary tree, we just need 7 steps:<br>
- <b>Step 1.</b> 100/2.
- <b>Step 2.</b> 50/2
- <b>Step 3.</b> 25/2
- <b>Step 4.</b> 13/2
- <b>Step 5.</b> 7/2
- <b>Step 6.</b> 4/2
- <b>Step 7.</b> 2/2 and get the item being searched

In terms of Big O notation: 

<b>O(log n)</b>.  

<b>log n</b> - logarithmic time or log time.

<b>n</b> - number of operations.

It is a very fast algorithm. 

```js
// Conditions: Sorted array and and item present in array
function binarySearch(myArray, selectedNumber) {
            // We take very first element in the array and last element in the array
            let left = 0;
            let right = myArray.length - 1;
            // Run the while loop 
            while (left <= right) {
                // inside loop, we find mid point or half        
                const midPoint = Math.floor((left + right) / 2);
                // we check if the number we are looking for is bigger or smaller than mid point and accordingly reduce or increase mid point by one
                // when the the item is found, it is neither bigger or smaller than mid point and therefore we return mid point or index of the item searched for                  
                if (selectedNumber < myArray[midPoint]) {
                    right = midPoint - 1;
                } else if (selectedNumber > myArray[midPoint]) {
                    left = midPoint + 1;
                } else {
                    return midPoint;
                }
            }

            return -1;
        }

        const my_arr = [-1, 0, 3, 5, 9, 12, 15, 24, 56, 88];
        const selectedNumber = 56;
        // Call function    
        console.log(binarySearch(my_arr, selectedNumber));
```

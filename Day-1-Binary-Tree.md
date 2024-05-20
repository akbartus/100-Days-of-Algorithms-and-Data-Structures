<b>Binary Tree or Binary Tree search</b> is the algorithm applied in search related tasks. Its takes as inputsorted array and an item and helps to identify its the index (position). Basic idea behind this algorithm is the following: 

1. when searching for the item in an array, rather than going one by one (linear search), we take half of the array and check if the being searched item is in one of them.
2. We take that half and divide it again into 2 halves and check if the item is present in one of them.
3. We do this until we find the item.

Consider the following example. To find 99th items in an array of 100 items, when using linear search we need 99 steps. 
When doing search using binary tree, we just need 7 steps :
Step 1. 100/2.
Step 2. 50/2
Step 3. 25/2
Step 4. 13/2
Step 5. 7/2
Step 6. 4/2
Step 7. 2/2 and get the item being searched

In terms of Big O notation: 

<b>O(log n)</b>.  

<b>log n</b> - logarithmic time or log time.

<b>n</b> - number of operations.

It is a very fast algorithm. 

```js
function binarySearch(myArray, selectedNumber) {
            let left = 0;
            let right = myArray.length - 1;

            while (left <= right) {
                const midPoint = Math.floor((left + right) / 2);

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

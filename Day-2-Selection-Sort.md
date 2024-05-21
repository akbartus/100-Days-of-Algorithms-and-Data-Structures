Example of selection sort algorithm in JavaScript:

```js
 function selectionSort(nums) {
      for (let i = 0; i < nums.length-1; i++) {
        // it cannot be zero, otherwise it will not change
        // Start from index 0
        let minIndex = i; 
        // Compare with the next element
        for (let j = i + 1; j < nums.length; j++) {
          // if number after is smaller than number before
          if (nums[j] < nums[minIndex]) {
            // min value index found  
            minIndex = j;
          }
        }
      // Swap places
      const tempnums = nums[i];
      nums[i] = nums[minIndex]; // in given nums, assign minimum nums value based on index
      nums[minIndex] = tempnums;

      }
      return nums;
    }
    console.log(selectionSort([2, 3, 5, 8, 7, 9, 1, 4])); // [-3, 1, 3, 5, 8, 9]

```

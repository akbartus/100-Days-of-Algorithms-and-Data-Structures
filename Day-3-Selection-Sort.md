<b>Selection</b> sort is not very fast algorithm. Selection sort works by taking the smallest element in an unsorted array and bringing it to the front. 
We go through each item (from left to right) until we find the smallest one. If it is found, it takes the place of the first item, that item goes to found item's place. 
Then we move to the second item and do the same. It is more suitable for smaller lists/arrays. 

In terms of Big O:
- O(n2)

Below is a sample code:
```js
let selectionSort = (nums) => {
      for (let i = 0; i < nums.length; i++) {
        let minNumber = i; // this is from where we start
        // we assign another loop, where we say that 
        // we will start from another element, right after i
        for (let j = i + 1; j < nums.length; j++) {
          // if 2 and other numbers are smaller than 1 number
          // we assign smaller number index
          if (nums[j] < nums[minNumber]) {
            minNumber = j;
          }

        }

        // then we swap the places of numbers
        // [nums[i], nums[minNumber]] = [nums[minNumber], nums[i]];
        // or do in this way
        let temp = nums[i];
        console.log(temp);
        nums[i] = nums[minNumber];
        console.log(nums[i])
        nums[minNumber] = temp;
      }

      //return nums; // we call from here, after swap was complete 
    }


    console.log(selectionSort([0, 3, 5, 2])); // [-3, 1, 3, 5, 8, 9]
```

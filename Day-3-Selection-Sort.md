<b>Selection sort</b> works by taking the smallest element in an unsorted array and bringing it to the front. 

1. Go through the array to find the lowest value.
2. Move the lowest value to the front of the unsorted part of the array. Start from next item.
3. Go through the array again as many times as there are values in the array.

Selection sort is not very fast algorithm. When smallest value is taken from array and put in front, we need to shift all other items as well (not one). And this shifting requires extra time!

In terms of Big O:
- O(n2)

Below is a exampl of selection sort (swapping version, more efficient) :
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

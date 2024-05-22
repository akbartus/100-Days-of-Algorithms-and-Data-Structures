Example of selection sort algorithm in JavaScript:

```js
// There is an array of elements. The task is to sort them using selection sort.
    // 1. We get the first element. Compare it with other elements in the array.
    // if it is smaller, we do not swap it with another element. 
    // If it is bigger, we swap it with the element which is smallest in array.
    // 2. We move on to the second element and do the same. 
    // So basically we have two run 2 loops.

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

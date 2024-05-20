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

        console.log(binarySearch(my_arr, selectedNumber));
```

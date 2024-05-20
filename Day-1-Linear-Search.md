<b>Linear search</b> is sequential search algorithm. It starts from first item in array and checks every item there until the desired item is found.

In terms of Big O notation: 

<b>O(n)</b>

<b>n</b> - linear time.

It is a much slower algorithm. See below the example implementation in JavaScript.

```js
// Input array and item to be searched for
    let linearSearch = ( array, item ) => {
        // Loop through the array one by one
        for(let i = 0; i < array.length; i++){
            // if array item value is equal to item value
            if(array[i] == item){
                // return its index position
                return i;
            }
        }
    }

    console.log(linearSearch([1,4,5,6,8,9,35,45,90 ], 45));
```

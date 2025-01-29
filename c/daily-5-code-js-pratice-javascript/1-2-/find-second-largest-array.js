// function secondLargest(arr) {
//   arr.sort();
//   let sortarr = [];
//   // console.log("sortedarray-->", arr)
//   for (let i = arr.length - 1; i >= 0; i--) {
//     // console.log("arr[i]--->", arr[i]);
//     sortarr.push(arr[i]); // Use arr[i] instead of arr[i - 1]
//     return { secondLargest: sortarr };

// }
// // return { secondLargest: sortarr };

// }
// console.log(secondLargest([3, 6, 4, 5, 97]))


function secondLargest(arr) {
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let num of arr) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

console.log(secondLargest([3, 6, 4, 5, 97])); // Output: 6



function uniqueElementFromarray(inputArray) {
  let temp = [];
  if (inputArray.length > 0) {
    temp.push(inputArray[0]);
    console.log(inputArray)
    for (let i = 1; i < inputArray.length; i++) {
      if (inputArray[i] !== inputArray[i + 1]) {
        temp.push(inputArray[i]);
      }
    }
  } else {
    return null;
  }
  return temp;
}
console.log(uniqueElementFromarray([4,3,4,5,44,3,2,3,4,4,4]))
//using set
// function uniqueElementFromarray(arry) {
//   return new Set(arry);
// }
// uniqueElementFromarray([1, 3, 4, 5, 3, 2, 3, 4, 2]);

function unquieValesArray(arrayVal) {
  let temp = [];
  for (let i = 0; i < arrayVal.length; i++) {
    if (!temp.includes(arrayVal[i])) {
      temp.push(arrayVal[i]);
    }
  }
  return temp;
}
unquieValesArray([1, 2, 3, 3, 4, 5, 5, 4, 5, 5]);

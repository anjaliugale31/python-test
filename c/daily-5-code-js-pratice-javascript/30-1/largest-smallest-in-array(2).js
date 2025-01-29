function largestSmallest(array) {
  let numlarg = array[0];
  let numsmall = array[0];
  for (let i = 0; i <= array.length; i++) {
    if (array[i] > numlarg) {
      numlarg = array[i];
    } else if (array[i] < numsmall) {
      numsmall = array[i];
    }
  }
  return { numlarg, numsmall };
}
largestSmallest([3, 5, 6, 33, 87]);

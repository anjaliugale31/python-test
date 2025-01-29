function nElementArray(arr, n) {
  var temp = [];
  if (n >= arr.length) {
    return 0;
  } else {
    for (let i = 0; i <= n; i++) {
      temp.push(arr[i]);
    }
  }
  return temp;
}

// nElementArray([5, 4, 3, 2, 5, 3, 6, 5, 9, 8, 5], 2);

function lastNElementfromArray(arr, n) {
  var temp = [];
  if (n >= arr.length) {
    return 0;
  } else {
    for (let i = arr.length - 1; i >= arr.length - n; i--) {
      temp.push(arr[i]);
    }
  }
  return temp;
}
lastNElementfromArray([5, 6, 3, 2, 4, 7], 4);

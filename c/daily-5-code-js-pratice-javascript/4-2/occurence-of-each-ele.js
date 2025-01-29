function occurenace(inputString) {
  let chartCount = {};
  for (let i = 0; i < inputString.length; i++) {
    let char = inputString.charAt(i);
    if (chartCount[char]) {
      chartCount[char]++;
    } else {
      chartCount[char] = 1;
    }
  }
  return chartCount;
}

occurenace("an");

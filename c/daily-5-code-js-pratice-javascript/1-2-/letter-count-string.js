function chartCount(stringVal, letter) {
  let count = 0;
  for (let i = 0; i < stringVal.length; i++) {
    if (stringVal.charAt(i) == letter) {
      count += 1;
    }
  }
  return { countletter: count };
}
chartCount("Anjali Ugale", "a");

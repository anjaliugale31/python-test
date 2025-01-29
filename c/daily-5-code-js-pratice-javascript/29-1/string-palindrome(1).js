function stringPalindrome(valueStr) {
  if (valueStr === valueStr.split("").reverse().join("")) {
    return true;
  }
  return false;
}
stringPalindrome("Anjali");

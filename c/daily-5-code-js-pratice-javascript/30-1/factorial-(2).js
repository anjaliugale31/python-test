function facto(numValue) {
  if (numValue === 0 || numValue === 1) {
    return 1;
  } else return numValue * facto(numValue - 1);
}
facto(4);

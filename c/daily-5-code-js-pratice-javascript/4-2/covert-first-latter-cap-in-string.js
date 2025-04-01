function toUppercaseFirstLetter(stringValue) {
  let res = stringValue.split(" ");
  console.log(res)
  for (let i = 0; i < res.length; i++) {
    res[i] = res[i].charAt(0).toUpperCase() + res[i].slice(1);
  }
  return res.join(" ");
}
console.log(toUppercaseFirstLetter("my first letter"));

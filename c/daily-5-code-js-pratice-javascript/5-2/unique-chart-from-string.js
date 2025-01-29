function uniqueFromString(InputString) {
  let resString = "";
  for (let i = 0; i < InputString.length; i++) {
    if (!resString.includes(InputString[i]))
      resString = resString.concat(InputString[i]);
  }
  return resString;
}
uniqueFromString("anjali");

function reverseEachWord(inputString) {
  let temp = inputString.split(" ");
  for (let i = 0; i < temp.length; i++) {
    temp[i] = temp[i].split("").reverse().join("");
    console.log(temp)
  }
  let result = temp.join(" ");
  console.log(result);
}

reverseEachWord("Welcome to Shrirampur");

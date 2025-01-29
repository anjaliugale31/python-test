// function addDash(numVal) {
//   var res = "";
//   var resVal = numVal.toString();
//   for (let i = 0; i < numVal.length; i++) {
//     res += resVal[i];
//     if (
//       resVal[i] % 2 === 0 &&
//       resVal[i] - (1 % 2) === 0 &&
//       i <= resVal.length - 1
//     ) {v
//       res += "-";
//     }
//     return res;
//   }
// }
// addDash(7658765);

function insertDashesBetweenEvens(inputNumber) {
  const inputStr = inputNumber.toString();
  let result = "";

  for (let i = 0; i < inputStr.length; i++) {
    result += inputStr[i];
    if (
      inputStr[i] % 2 === 0 &&
      inputStr[i + 1] % 2 === 0 &&
      i < inputStr.length - 1
    ) {
      result += "-";
    }
  }

  return result;
}
insertDashesBetweenEvens(3426543);

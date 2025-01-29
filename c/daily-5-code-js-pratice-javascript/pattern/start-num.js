function pyramid(n) {
  for (var i = 0; i < n; i++) {
    var str = "";
    for (var j = 0; j < i; j++) {
      str += "*";
    }

    console.log(str);
  }
}

pyramid(5);

// *
// **
// ***
// ****

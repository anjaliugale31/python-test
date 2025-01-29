function inseq(num) {
  var cnt = 1;
  for (var i = 1; i <= num; i++) {
    var str = "";
    for (var j = 1; j <= i; j++) {
      str += cnt;
      cnt++;
    }
    console.log(str);
  }
}
inseq(4);

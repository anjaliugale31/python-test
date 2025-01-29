function revStr(strRev) {
  var revstring = "";
  for (let i = strRev.length - 1; i >= 0; i--) {
    revstring += strRev[i];
  }
  return revstring;
}
revStr("anjali");

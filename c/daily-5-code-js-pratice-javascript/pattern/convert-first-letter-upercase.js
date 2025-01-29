function stringVal(stringConvrt) {
  let res = stringConvrt.split(" ");
  console.log("🚀 ~ toUppercase ~ res:", res);
  for (let i = 0; i < res.length; i++) {
    res[i] = res[i].charAt(0).toUpperCase() + res[i].slice(1);
    console.log("🚀 ~ stringVal ~ res[i]:", res[i]);
  }
}
stringVal("My name us anjali");

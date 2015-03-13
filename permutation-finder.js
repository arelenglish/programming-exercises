// Find if a string is a permutation of the other

function isPermutation(str1, str2){
  if(str1.length === str2.length){
    var tmpArr1 = [];
    var tmpArr2 = [];
    for(var i = 0; i < str1.length; i++){
      tmpArr1.push(str1[i]);
      tmpArr2.push(str2[i]);
    }
    return normalizeToStr(tmpArr1) === normalizeToStr(tmpArr2);
  }
  return false;
}

function normalizeToStr(arr){
  arr.sort().toString().toLowerCase();
}

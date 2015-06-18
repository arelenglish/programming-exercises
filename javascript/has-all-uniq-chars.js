// Checks if a string has only uniq characters. So "Arel" would 
// return true, but "sailboat" would return false because it as 
// two "a" characters. 

function hasAllUniqChars(string){
  for(var i = 0; i<string.length; i++){
    var char = string[i]
    for(var j = 0; j<string.length; j++){
      if(char === string[j] && i !== j){
        return false;
      }
    }
  }
  return true;
}

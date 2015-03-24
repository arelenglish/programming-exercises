// A function that removes spaces from strings
// and replaces them the space encoding %20

function percentEncode(string) {
  var encodedString = "";
  for(var i = 0; i<string.length; i++){
    if(string[i] === " "){
      encodedString += "%20";
    } else {
      encodedString += string[i];
    }
  }
  return encodedString;
}

// This example assumes you don't want 
// any extra spaces. 

function percentEncodeStrip(string){
  string = removeExtraWhiteSpace(string);
  return percentEncode(string);
}

function removeExtraWhiteSpace(string){
  string = string.replace(/ +/g, ' ');
  if(string[0] === " "){
    string = string.slice(1);
  }
  if(string[string.length - 1] === " "){
    string = string.slice(0,-1);
  }
  return string;
}

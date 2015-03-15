// A method to compress a string of alphabetical characters. 
// Eg: AAAABBBGGGEEE would become A4B3G3E3

function stringCompressor(str){
  var compressed_string = "";
  var count = 1;
  for(var i = 0; i<str.length; i++){
    if(str[i] == str[i+1]){
      count++
    } else {
      compressed_string += str[i];
      compressed_string += count.toString();
      count = 1;
    }
  }
  return compressed_string;
}

// Find if a string is a permutation of the other
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

readline.question(`This program checks for permutations. What's your first string? `, stringOne => {
  readline.question("What's your second string? ", stringTwo => {
    console.log(isPermutation(stringOne, stringTwo))
    readline.close()
  })
})

function isPermutation(str1, str2) {
  if(str1.length === str2.length) {
    var sortedString1 = str1.split('').sort().join('').toLowerCase()
    var sortedString2 = str2.split('').sort().join('').toLowerCase()
    if (sortedString1 === sortedString2) {
      return "Those strings are permutations of each other! 🥳"
    }
  }
  return "Sorry. Those strings are not permutations of each other 💩";
}

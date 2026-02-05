
function isEven(num){
    if(num % 4 == 0){
        return true;
    } else {
        return false;
    }
}

// modulo operation (you output the remainder of intger division, %)

// 7 % 2 == 1

for (var i = 0; i < 100; i++) {
    console.log("i is now " + i + ", is it multiple of 4? " + isEven(i));
}



// #3
var numbers = [5, 3, 9, 4, 11];  
function changeNums(numList, addNum, subtractNum) {
  for (var i = 0; i < numList.length; i++) {
    if (numList[i] % 2 == 0) {
      // If the number is even, add the addNum
      numList[i] = numList[i] + addNum;
    } else {
      // If the number is odd, subtract the subtractNum
      numList[i] = numList[i] - subtractNum;
    }
  }
}

// Execute the function with the given arguments
changeNums(numbers, 4, 3);

// [2, 0, 6, 8, 8]

// Output the result
console.log(numbers);






// // #4
// var numbers = [2, 9, 4, 3, 7];

// function changeNums(numList, addNum, subtractNum) {
//   for (var i = 0; i < numList.length; i++) {
//     // Check if the current number is even
//     if (numList[i] % 2 == 0) {
//       numList[i] = numList[i] + addNum;
//     } else {
//       // If the number is odd, subtract the subtractNum
//       numList[i] = numList[i] - subtractNum;
//     }
//   }
// }

// // Call the function with the array and values 2 and 8
// changeNums(numbers, 2, 8);

// // Print the updated array to the console
// console.log(numbers);

// [4, 1, 6, -5, -1]




var numbers = [4, 9, 6, 5, 7, 0];
function findIt(numList,num){
    for(var i=0; i<numList.length; i++) {
        if(numList[i] == num) {
            return "Found it!"
        }
    }
    return "not Found it!"
    
}


console.log(findIt(numbers, 2));
console.log(findIt(numbers, 7));
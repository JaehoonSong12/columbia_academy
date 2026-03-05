
function copyEvens(nums, count) {
  // TODO: Implement your solution here


  // other counting purposed variable, to only count the number of even numbers
  answer = []
  countEven = 0;
  for (var i = 0; i < nums.length; i++) {
    evenNum = (nums[i] % 2 == 0);
    // if count is already satisfied, you can just exit.
    if (countEven == count) {
      break;
    }
    if (nums[i] % 2 == 0) { 
      answer.push(nums[i]);
      // count it!
      countEven+=1;
      
    }
  }
  return answer;
  // https://www.w3schools.com/js/js_arrays.asp
  // https://www.w3schools.com/js/js_array_methods.asp
}


console.log(copyEvens([6, 1, 2, 4, 5, 8], 3));
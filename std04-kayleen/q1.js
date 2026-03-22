var stateNames = getColumn("US States", "State Name");
var statePopulations = getColumn("US States", "Population");
var countryNames = getColumn("Countries and Territories", "Country Name");
var countryPopulations = getColumn("Countries and Territories", "Population");


largestSmallest("states", stateNames, statePopulations);
largestSmallest("countries", countryNames, countryPopulations);

function largestSmallest(typeOfList, list1, list2){
  var message = "There are many " + typeOfList;
  message = message + " but the one with the smallest population is " + smallestMatchingString(list1, list2);
  message = message + " and the one with the largest population is " + largestMatchingString(list1, list2);
  console.log(message);
}

// Finds the string at the matching index of the smallest number in a list of the same length
// list1 {list} - a list of strings to search through
// list2 {list} - a list of numbers to search through
// return {string} - the string at the matching index of the largest value from list1
function smallestMatchingString(list1, list2){
  
  var smallestNum = list2[0];
  var smallestNumMatchingString = list1[0];
  for(var i = 0; i < list1.length; i++){
    if (list2[i]<smallestNum){
      smallestNum = list2[i];
      smallestNumMatchingString = list1[i];
    }
  }
  
  return smallestNumMatchingString;
}

// Finds the string at the matching index of the largest num word in a list
// list1 {list} - a list of strings to search through
// list2 {list} - a list of numbers to search through
// return {string} - the string at the matching index of the largest value from list1
function largestMatchingString(list1, list2){
  var largestNum = list2[0];
  var largestNumMatchingString = list1[0]; 
  for (var i = 0; i < list1.length; i++) {
    if (list2[i] > largestNum){
        largestNum = list2[i];
        largestNumMatchingString = list1[i];
    }
  }
  return largestNumMatchingString;
}
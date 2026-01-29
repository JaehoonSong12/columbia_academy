// takes the game title and returns it to the sale volume
//the variable gameSales takes from the amount of sales each game has
//the variable allgameName takes from the names of the games
//the variable index links the sales and game to each other 
function topSales(gameName) {
  var gameSales = getColumn("Best Selling Video Games", "Sales");
  var allgameName = getColumn("Best Selling Video Games", "Title");
  var index;
  for (var i = 0; i<=(gameSales.length); i++) {
    if (allgameName[i] == gameName) {
      index = i;
    }
    }
  return (gameSales[index]);
}

//It takes any game name and returns a random title out of the 51 games in the dataset
//The variable gameTitles stores the titles of the games in the dataset
function randomGames() {
  var gameTitles = getColumn("Best Selling Video Games", "Title");
  return (gameTitles[randomNumber (0,gameTitles.length-1)]);
}




// declaration or definition of function. (step 1.)
function doSomething(a, b) { // function {functionName}(param1, param2)
    var param1 = a;
    var param2 = b;
    return param1 + param2; // return {value} / return; (step 3)
}




console.log("HREREADRFdafdasfdsfsdf");

var sum = doSomething(2, 5);  // function call with arguments (step 2.)

console.log(sum);

// //console.log used to to test the code by calling the functions which display a random game 
// console.log(randomGames());
// //console.log used to test the code by calling the function topSales, which shows a certain game's sales 
// console.log(topSales(	"Red Dead Redemption 2"));
var titleList = getColumn("Netflix Content", "Title");
var typeList = getColumn("Netflix Content", "Type");
var ratingList = getColumn("Netflix Content", "Rating");
var filteredTitles = [];

onEvent("pickBtn", "click", function( ) {
  searchTypeList(getText("typeDropdown"), getText("ratingDropdown"));
});

function searchTypeList(typeInput, ratingInput) {
  filteredTitles = [];
  for (var i = 0; i < titleList.length; i++) {
    if(typeInput == typeList[i] && ratingInput == ratingList[i]){
      appendItem(filteredTitles, titleList[i]);
    }
  }
  var output = "The following " + typeInput + "s are rated " + ratingInput + ":\n";
  var index;
  for (var k = 0; k < 5; k++) {
    index = randomNumber(0,filteredTitles.length-1);
    output = output + "\n" + (k+1) + ". " + filteredTitles[index];
  }
  setText("picksOutput", output);
  
}

/**
 * Kayleen Lee
 * 
 * Do This

Try using this simple ordering app.
The totalWithTax() functions has a bug. Find and fix it.
Add comments for each function using the format below
// function purpose...
// parameterName {type} - explanation of parameter
// return {type} - description of what's returned
 * 
 * 
 */
onEvent("totalButton", "click", function(){
  setText("outputLabel", totalCost());
});

onEvent("taxButton", "click", function(){
  setText("outputLabel", totalWithTax(totalCost()));
});

/**
 * Calculates the total cost of selected items.
 * @returns {number} The total cost of selected items.
 */
function totalCost(){
  var total = 0;
  
  for(var i=0; i<5; i++){
    if(getChecked("check" + i)){
      total = total + getNumber("cost" +i);
    }
  }
  return total;
}

/**
 * Calculates the total amount including a 7% tax.
 * @param {number} amount 
 * @returns {number} The total amount including tax.
 */
function totalWithTax(amount){
  var total = amount + amount * 0.07;
  total = Math.round(total * 100) / 100;
  return total;
}
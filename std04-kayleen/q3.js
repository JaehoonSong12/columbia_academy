//Description: Create a program that determines if it is 
//okay to sleep in or not.

//If it is *not* a weekday OR you're on vacation: say "Sleep In"
//If it is a weekday and you are not on vacation: say "Get Up"

//For Example:
//Thursday / Yes -> Sleep In (because even though it is a weekday, you are on vacation)
//Monday / No -> Get Up (because it’s a weekday and you are not on vacation)

//This function should return a string telling 
//you if it's ok to sleep it or not
//day (String) - the day of the week
//vacation (Boolean) - true if you are vacation, false if not
//return (String) - either "Sleep In" or "Get Up"

function sleepIn(day, vacation){
    if (day == "Saturday" || day == "Sunday" || vacation) return "Sleep In";
    return "Get Up";
}

console.log(sleepIn("Tuesday", true));
console.log(sleepIn("Sunday", false));
console.log(sleepIn("Friday", false));
console.log(sleepIn("Saturday", true));



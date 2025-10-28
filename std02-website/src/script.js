// https://www.w3schools.com/js/
// https://the-winter.github.io/codingjs/



// dsadsadsas dsadsad
// sadsadsa
// dsadsa
// d

/*
    Multi-line comment
    dsadsadsads
    adsadsa
    dasd
    sad
    sa
    dsa
    ds
    ad
*/



console.log("Testings.....");


let text = "Hello, World!";

// Extract from index 0 up to (but not including) index 5
let part1 = text.substring(0, 5); // "Hello" 
console.log(part1);

// Extract from index 7 to the end of the string
let part2 = text.substring(7); // "World!"
console.log(part2);

// Extract from index 7 up to (but not including) index 12
let part3 = text.substring(7, 12); // "World"
console.log(part3);


console.log("Testings.....");









// let player1 = "Alice";
// let player2 = "Oriana";

// if (player2.use('R').on(player1)) {
//     console.log(player1 + " has been hit by " + player2 + "'s R!");
//     player1.moveTo(player2.getBallPosition());
// }




// Count the number of 'xx' in the given string. 
// We'll say that overlapping is allowed, 
// so 'xxx' contains 2 'xx'.
// 
// Examples
// countXX('abcxx') -> 1
// countXX('xxx') -> 2
// countXX('xxxx') -> 3
function countXX(str){
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (str.substring(i, i + 2) == "xx") { // substring(i, i + 2) means i <= 번째 < i + 2
            count = count + 1;
        }
    }
    return count;
}


console.log("Testing countXX function:");
console.log("Input: 'abcxxdefxx'");

countResult = countXX("abcxxdefxx");

console.log("Value: " + countResult);



let str3 = "dasjfkldsngklfsdmg";
for (let i = 0; i < str3.length; i++) {
    console.log(str3[i]);
}







function frontTimes(str, n){
    let result = "";
    for (let i = 0; i < n; i = i + 1) {
        result += str.substring(0, 3);
    }
    return result;
}


console.log("Testing frontTimes function:");
console.log("Input: 'Chocolate', 2");
frontTimesResult = frontTimes("Chocolate", 2);
console.log("Value: " + frontTimesResult);
console.log("Expected: ChoCho");






function stringTimes(str, n){
    let result = "";
    for (let i = 0; i < n; i++) {
        result = result + str;
    }
    return result;
}



console.log("Testing stringTimes function:");
console.log("Input: 'Hi', 3");
stringTimesResult = stringTimes("Hi", 3);
console.log("Value: " + stringTimesResult);
console.log("Expected: HiHiHi");





function myFunction(str, n){ 
    let result = "";
    for (let i = 0; i < n; i++) {
        result= result + str;
    }
    return result;
}

let resultValue = myFunction("Hello", 5);
console.log(resultValue); // HelloHelloHelloHelloHello


// 1. seqencial 순서대로
// 2. selection 조건 (if, switch)
// 3. loop 반복 (for, while)









/**
 * JSDoc Comment
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @return {number} The sum of the two numbers.
 */
function add(a, b) {
    return a + b;
}


console.log(11 + 31);

console.log(add(5, 3));
console.log(add(10, 20));
console.log(add(100, 200));
console.log(add(1234, 5678));




// Variable: a container for data
let num = 10;
let str = "num"
let str2 = 'ber'
let strresult = str + str2; // "num" + "ber" -> "number"
/*
1. var : old variable declaration keyword (not recommended)
2. let : variable declaration keyword
3. const : constant declaration keyword
4. num : variable name
*/

console.log(strresult); // "number"
// console.log("num")
// console.log(num);
// console.log() : num
// console.log() <- num


// console.log(2);
// console.log(4 / 0);
console.log('9' * 3);












/*
    The parameter weekday is true if it is a weekday, 
    and the parameter vacation is true if we are on 
    vacation. We sleep in if it is not a weekday or 
    we're on vacation. Return true if we sleep in.

    sleepIn(true, true) -> true
    sleepIn(true, false) -> false
    sleepIn(false, true) -> true
 */
function sleepIn(weekday, vacation){ // weekday = true, vacation = true

    // == : equality operator
    // < : less than operator
    // > : greater than operator
    // <= : less than or equal to operator
    // >= : greater than or equal to operator
    // != : not equal operator
    // ! : not operator
    // && : and operator
    // || : or operator

    if (!weekday) { // conditional statement
        return true; // 1
    }
    if (vacation) {
        return true; // 1
    }
    return false; // 0
}
// function: group of code you want to reuse later on!
// parameter (variable inside function): input for the function

// return: output of the function



sleepIn(true, true) // argument: actual value you pass to the function when you call it
sleepIn(true, false) 
sleepIn(false, true)




console.log(1 == 2); // false









// We have two monkeys, a and b, and the parameters 
// aSmile and bSmile indicate if each is smiling. 
// We are in trouble if they are both smiling or 
// if neither of them is smiling. Return true if we are in trouble.
function monkeyTrouble(aSmile, bSmile) {

    // == : equality operator
    // < : less than operator
    // > : greater than operator
    // <= : less than or equal to operator
    // >= : greater than or equal to operator
    // != : not equal operator
    // ! : not operator
    // && : and operator
    // || : or operator

    if (aSmile && bSmile) {
        return true;
    }
    if (!aSmile && !bSmile) {
        return true;
    }
    return false;
}











const header = document.createElement('header');

const h1 = document.createElement('h1');
h1.textContent = 'Jihoo Choi';
const h2 = document.createElement('h2');
h2.textContent = '야호';
const pHeader = document.createElement('p');
pHeader.textContent = '2025 월즈 재밌겠다';

header.appendChild(h1);
header.appendChild(pHeader);
header.appendChild(h2);

document.body.appendChild(header);







// Create About section
const aboutSection = document.createElement('section');
const h2About = document.createElement('h2');
const pAbout = document.createElement('p');
aboutSection.appendChild(h2About);
aboutSection.appendChild(pAbout);
document.body.appendChild(aboutSection);
// Data
aboutSection.id = 'about';
h2About.textContent = 'About Me';
pAbout.textContent = 'I enjoy building things with LEGOs, drawing comics, and playing soccer.';





// Create Projects section
const projectsSection = document.createElement('section');
const h2Projects = document.createElement('h2');
projectsSection.appendChild(h2Projects);

// Data
projectsSection.id = 'projects';
h2Projects.textContent = 'My Projects';




const projectA = document.createElement('div');
const h3A = document.createElement('h3');
const pA = document.createElement('p');
const img = document.createElement('img');
projectA.appendChild(h3A);
projectA.appendChild(pA);
projectA.appendChild(img);


// Data
projectA.className = 'project-card';
h3A.textContent = 'Project A';
pA.textContent = "오공 '원숭이 왕'.";
img.src = 'https://image.xportsnews.com/contents/images/upload/article/2020/0318/mb_1584511700334801.jpg';
img.alt = '설명 텍스트';
img.width = 300;









const projectB = document.createElement('div');
const h3B = document.createElement('h3');
const pB = document.createElement('p');
projectB.appendChild(h3B);
projectB.appendChild(pB);

// 1. 테이블 요소 생성
const table = document.createElement('table');
table.style.borderCollapse = 'collapse';


const lolItems = [
    "https://cdn.lol.ps/assets/img/items/6655_40.webp",
    "https://cdn.lol.ps/assets/img/items/4645_40.webp",
    "https://cdn.lol.ps/assets/img/items/3157_40.webp",
    "https://cdn.lol.ps/assets/img/items/3089_40.webp",
    "https://cdn.lol.ps/assets/img/items/3135_40.webp",
    "https://cdn.lol.ps/assets/img/items/3137_40.webp",
];

// 2. 2행 3열 생성
let i = 0;
for (let row = 0; row < 2; row++) {
    const tr = document.createElement('tr');
    for (let col = 0; col < 3; col++) {
        const td = document.createElement('td');
        td.textContent = `(${row + 1}, ${col + 1})`;
        const img = document.createElement('img');
        // Data
        img.src = lolItems[i];
        img.width = 200;
        td.appendChild(img);
        tr.appendChild(td);
        i++;
    }
    table.appendChild(tr);
}

// 3. 테이블을 body에 추가
projectB.appendChild(table);



// Data
projectB.className = 'project-card';
h3B.textContent = 'Project B';
pB.textContent = 'I built a working robot using a Raspberry Pi!';

function toggleClass() {
    const p = document.getElementById("text");
    p.classList.toggle("red-text");  // 클래스 토글
}





projectsSection.appendChild(projectA);
projectsSection.appendChild(projectB);
document.body.appendChild(projectsSection);

// Create Contact section
const contactSection = document.createElement('section');
const h2Contact = document.createElement('h2');
const pContact = document.createElement('p');
contactSection.appendChild(h2Contact);
contactSection.appendChild(pContact);
document.body.appendChild(contactSection);


// Data
contactSection.id = 'contact';
h2Contact.textContent = 'Contact';
pContact.innerHTML = 'Email: <a href="mailto:myemail@example.com">myemail@example.com</a>';
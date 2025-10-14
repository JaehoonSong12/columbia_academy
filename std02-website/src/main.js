console.log("Hello, World !")
const a = 10;
const b = 20;
console.log(a+b);


const body = document.body; // "document" means the whole HTML

const changeColorBtn = document.createElement("button");
changeColorBtn.innerText = "Change Background Color";
changeColorBtn.style.padding = "10px 20px";
changeColorBtn.style.fontSize = "16px";
changeColorBtn.style.cursor = "pointer";
changeColorBtn.style.marginTop = "20px";

changeColorBtn.addEventListener("click", () => {
    const currentColor = body.style.backgroundColor;
    body.style.backgroundColor = currentColor === "lightblue" ? "white" : "lightblue";
});

body.appendChild(changeColorBtn); // Append the button to the body


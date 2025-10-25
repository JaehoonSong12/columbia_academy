/**
 * Initial Setup (Construction)
 * 
 */
document.body.style.backgroundColor = "DarkseaGreen";

// let loadedH1List = document.getElementsByTagName("h1");
// for (let i = 0; i < loadedH1List.length; i++){
//     const loadedH1 = document.getElementsByTagName("h1")[i];
//     // 5. modify the value of h1
//     loadedH1.style.color = "lemonchiffon";
//     loadedH1.style.fontFamily = "Georgia, serif";
//     loadedH1.style.marginTop = "20px";
// }

// let loadedSections = document.getElementById('section');
// loadedSections.style.textAlign = "center";





/**
 * Event Listeners
 */
// event-driven programming
const styleButton = document.getElementById('btn-style');
if (styleButton) {
    styleButton.addEventListener('click', () => {
    // 4. Load the h1 element by its tag name
    let loadedH1List = document.getElementsByTagName("h1");
    for (let i = 0; i < loadedH1List.length; i++){
        const loadedH1 = document.getElementsByTagName("h1")[i];
        // 5. modify the value of h1
        loadedH1.style.color = "lemonchiffon";
        loadedH1.style.fontFamily = "Georgia, serif";
        loadedH1.style.marginTop = "20px";
    }
    });
}

// another button to center any elements by IDs
const centerButton = document.getElementById('btn-centering');
if (centerButton) {
    centerButton.addEventListener('click', () => {
        let loadedSections = document.getElementById('section');
        console.log(loadedSections);
        loadedSections.style.textAlign = "center";
    });
}

// button to redirect to another page
const redirectButton = document.getElementById('btn-redirect');
if (redirectButton) {
    redirectButton.addEventListener('click', () => {
        // Redirect to another page, prettybackground.html
        window.location.href = "prettybackground.html";
    });
}

// button to go back to home page
const backButton = document.getElementById('btn-backhome'); 
if (backButton) {
    backButton.addEventListener('click', () => {
        window.location.href = 'index.html'; // Adjust the URL as needed
    });
}
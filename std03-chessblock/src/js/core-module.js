// js/core-module.js
// Core utility functions and component implementations used by page modules.

export function initialSetup() {
    document.body.style.backgroundColor = "DarkseaGreen";
}

export function stylePage() {
    const styleButton = document.getElementById('btn-style');
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

export function addCenteringFunctionality() {
    // another button to center any elements by IDs
    const centerButton = document.getElementById('btn-centering');
    centerButton.addEventListener('click', () => {
        let loadedSections = document.getElementById('section');
        console.log(loadedSections);
        loadedSections.style.textAlign = "center";
    });
}



export function enableButtonRedirect(className='btn-redirect') {
    const buttons = document.getElementsByClassName(className);
    // debug log using for each
    Array.from(buttons).forEach((button) => {
        button.addEventListener('click', () => {
            let href = button.getAttribute('href');
            if (href == null) {
                href = 'index.html';
            }
            window.location.href = href;
        });
    });
}

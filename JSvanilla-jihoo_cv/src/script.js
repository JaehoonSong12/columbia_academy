const header = document.createElement('header');
const h1 = document.createElement('h1');
const pHeader = document.createElement('p');
header.appendChild(h1);
header.appendChild(pHeader);
document.body.appendChild(header);

// Data
h1.textContent = 'Jihoo Choi';
pHeader.textContent = '2025 월즈 재밌겠다';






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
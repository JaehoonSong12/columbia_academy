<!-- 
 @requires
 1. VSCode extension: Markdown Preview Enhanced
 2. Shortcut: 'Ctrl' + 'Shift' + 'V'
 3. Split: Drag to right (->)

 @requires
 1. VSCode extension: Markdown All in One
 2. `File` > `Preferences` > `Keyboard Shortcuts`
 3. toggle code span > `Ctrl + '`
 4. toggle code block > `Ctrl + Shift + '`

 @usage
 1. End of Proof (Q.E.D.): <div style="text-align: right;">&#11035;</div>
 2. End of Each Section: 

     <br /><br /><br />

     ---



     <p align="right">(<a href="#readme-top">back to top</a>)</p>

 3. ![image_title_](images/imagefile.png)
 4. [url_title](URL)
 -->
<!-- Anchor Tag (Object) for "back to top" -->
<a id="readme-top"></a> 




# Columbia Academy Project

Welcome to the Columbia Academy project repository! This README provides quick access to project documentation and code.

## Table of Contents
- [Columbia Academy Project](#columbia-academy-project)
  - [Table of Contents](#table-of-contents)
- [To My Students](#to-my-students)
- [Project Overview](#project-overview)
  - [Documentation](#documentation)
  - [Code Access](#code-access)
  - [Contributing](#contributing)
- [Instructions\`](#instructions)
  - [Python (GT CS 1301 / AP CS A)](#python-gt-cs-1301--ap-cs-a)










<br /><br /><br />

---

# To My Students
Follow the steps below to get started!

1. open the terminal by pressing `ctrl` + `~`. (In the case of shared session by Live Share, click share terminal)
2. type-in `./on_venv.sh` in bash.
3. copy and paste the command shows up in bash. (`source ../venv/Scripts/activate && pip install setuptools && clear`)
4. If you can see `(venv)` at the front of your terminal line, you are all set.
5. Now, get into your space, for example, `cd std02-jihoo`
6. Run your python file. `python main.py`




<br /><br /><br />

---

# Project Overview
This project is designed to support students at Columbia Academy in studying AP subjects, specifically 
1. AP CS Principles - **JavaScript**
2. GT CS 1301: Intro to Computing (CS A) - **Python**
3. GT CS 1331: Introduction to Object-Oriented Programming (CS A). - **Java**


## Documentation

For detailed documentation, including project specifications, development guidelines, and usage instructions, please visit our documentation on Google Docs:

[CA Academy Documentation](https://docs.google.com/document/d/1i9pj0_u_sC0Z9-4tyLOnjUu3n8dCZWJT_7c9r-XcJHQ/edit?usp=sharing)

## Code Access

The code for this project is hosted on GitHub in this repository. You can explore the source code, contribute, and access different branches as necessary:

[GitHub Repository - CA Academy Project](https://github.com/JaehoonSong12/ca_academy)

## Contributing

We welcome contributions! If you would like to suggest improvements, please submit a pull request, or open an issue.


<p align="right">(<a href="#readme-top">back to top</a>)</p>










<br /><br /><br />

---

# Instructions`
To start, clone the repository using the following command:
```bash
git clone https://github.com/JaehoonSong12/columbia_academy.git
cd columbia_academy
```


## Python (GT CS 1301 / AP CS A)
After cloning, initialize the repository by running the provided bash scripts (`copy`, then `right-click` in a bash session):
1. Run the initial setup script (to download **Python Language System**):
   ```bash
   ./scripts/python01-init.sh
   ```

2. Run the project setup script (to configure **Virtual Environment** in `src` subdirectory):
   ```bash
   ./scripts/python02-config.sh
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

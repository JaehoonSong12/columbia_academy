# Full Stack Python Programming
## Introduction to Software Technology
### Spring Semester 2026 Revision 0, 3 Jan 2026
## Standards Mastery Framework Project Sequence

### Track Outlines

| Item | Grade Level | Language (Python) Track | Data Management (SQLITE3/SQL) Track | GUI (TKINTER) Track |
|------|-------------|------------------------|-------------------------------------|---------------------|
| 0 | P | Hello, World | MySQL Installation | Tk Hello, World (Button) |
| 1 | P | Printing | SQL Table Builds/Drops | Tk Hello World as a POCO |
| 2 | Minor | Calculations/Data Types | SQL Table Operations | Tk Interactive Capabilities |
| 3 | Minor | Procedures | SQL Query Basics Selections | Tk Menu - Traditional Top Menu |
| 4 | Major | Functions | SQL Insertions | Tk Decorations/Imagery |
| 5 | Minor | External Libraries | SQL Deletions | Tk Navigation Queries |
| 6 | Minor | POCO/OOP | SQL Updates | Tk Query Displays |
| 7 | Minor | Try/Except | Basic Python SQL Queries | TK Add/Delete Records |
| 8 | Major | Container Classes | Advanced Python SQL Queries | TK Edit Records |
| 9 | Major | Completed CRUD Capable GUI Program (Full Stack) | | |

## Requirements Overview

- Each student is expected to complete all three tracks
- Each item is graded as listed (Practice/Minor/Major)
- All assignments are worth 100 points with the listed weights
- Master Project receives a Major Grade for Overall Rigor, and a Major Grade for Code Quality

### Critical Calendar Dates

| Date | Total Required Completions | Rules of Completion |
|------|---------------------------|---------------------|
| January 31st | 10 | - Each Track MUST be completed in order.<br>- Each Assignment is a stand-alone programming project.<br>- Each set (10 elements) may be aggregate of all tracks.<br>- All three tracks to be completed in parallel. |
| February 27th | 20 | |
| March 27th | 30 (All Tracks Complete) | |
| April 3rd | Master Project Proposal | |
| May 6th | Master Projects Due | |

## Detail Specifications by Track

### Language Track

| Item | Language Track | Specifications |
|------|----------------|----------------|
| 0 | Hello, World | Submit a properly running Hello World Program in Python |
| 1 | Printing | Submit a program printing in a properly running program using at least 4 different types of print commands. Example:<br>- Printing literals<br>- Formatted printing<br>- Printing multiple variables (several ways) simultaneously in text |
| 2 | Calculations/Data Types | Submit a program performing calculations using at LEAST the following data types: (Predominantly trivial computations capped at 85 points)<br>- Int<br>- Float<br>- Double<br>- Decimal (or its equivalent)<br>- Long<br>- Byte (Can involve bitwise shifting) |
| 3 | Procedures | Submit a program that has multiple procedures existing outside but called from the main method |
| 4 | Functions | Submit a program that has multiple functions existing outside but called from the main method |
| 5 | External Libraries | Submit a program that links in 3 external libraries you use in your code |
| 6 | POCO/OOP | Write a POCO class and instantiate it at least three times in your main application |
| 7 | Try/Except | Write a program that uses try/except clauses to catch errors. Show one error being caught in your run sheet/run check |
| 8 | Container Classes | Write a POCO Class, then instantiate a container in your main program that holds multiple objects of your class. Demonstrate CRUD on the objects in memory (aka No Db) |
| 9 | Full Stack Project | See specific project spec for item 9 below |

### Database Track

| Item | Database Track | Specifications |
|------|---------------|----------------|
| 0 | SQLite3 Installation | Prove proper installation of SQLite 3 and any tool to allow you to manually operate databases |
| 1 | SQL Table Builds/Drops | Submit your SQL queries that resulted in proper formation of your desired schema (table) |
| 2 | SQL Table Operations | Demonstrate SQL queries that add columns, remove columns, and edit data types of columns (In SQLite there is no edit columns) |
| 3 | SQL Query Basics Selections | Demonstrate (Live) - multiple selection queries varying records and what is returned to the result set |
| 4 | SQL Insertions | Demonstrate (Live) - multiple SQL insertions |
| 5 | SQL Deletions | Demonstrate (Live) - proper SQL deletions |
| 6 | SQL Updates | Demonstrate (Live) - proper SQL updates to multiple records |
| 7 | Basic Python SQL Queries | Demonstrate (Live) - connecting to your SQLite 3 from a python POCO class |
| 8 | Advanced Python SQL Queries | Demonstrate (Live run check) - using the data from an SQLite3 query call in your python POCO in the main part of your program |
| 9 | Full Stack Project | See specific project spec for item 9 below |

### GUI Track

| Item | GUI Track | Specifications |
|------|-----------|----------------|
| 0 | Tk Hello, World (Button) | Submit a properly running Hello World Program in Tk for Python. UI must have a functional button that modifies the display in some manner visible to the user. |
| 1 | Tk Hello World as a POCO | Submit your GUI Hello World as a POCO instantiated in main. This means that your Gui must be a class independent of the main application class and be instantiated therein. |
| 2 | Tk Interactive | Write a Tk program that allows user to interact with at least:<br>- Buttons that change labels<br>- Buttons that read and write to text edit fields |
| 3 | Tk Menu | Write a Tk Menu that performs basic application functionality including:<br>- File → Exit<br>- Help → About (With an actual popup menu)<br>- 3 other functions you write |
| 4 | Tk Decorations/Imagery | Demonstrate GUI decoration by using images as backgrounds and other beautifying content. (+) Set the application icon. |
| 5 | Tk Navigation Queries | Navigate through records stored in a container object using GUI buttons |
| 6 | Tk Query Displays | Connect the data object to your database class and show records on a Tk GUI screen using navigation buttons |
| 7 | TK Add/Delete Records | Install methods to your Db POCO and perform Add/Deletes from your GUI class |
| 8 | TK Edit Records | Perform Edits on record that has navigational focus using your UI |
| 9 | Full Stack Project | See specific project spec for item 9 below |

## Project 9 All Three Tracks

Your task for the final step is to pull together a full-stack program with core CRUD functionality. Submit a fully functional running application in Tk as follows:

1. Main has less than 3 lines of functional code.
2. Tk Class is container for database class.
3. Database class performs ALL query and connections methods.
4. GUI has full navigation and CRUD capabilities.
5. Application icon and imagery included in project.
6. Full documentation.
7. Proper naming conventions for all GUI objects.
8. No GUI code in main application class OR database class.
9. Assuming cooperative users, application does not crash.
10. **NO MULTIPLE RECORD DISPLAYS ARE ALLOWED** for your first Full-Stack Program. For your master project you may use them if you so choose.

## Master Projects

Once you are completely signed off for all three tracks, you can proceed to your master project proposals. Your master projects require a unique topic of interest to you. Common ideas will not score as well. This must be uniquely your own.

What you will submit as your proposal is a 1-page detailed word-processed proposal using the template at the end of this packet. Hand-written proposals will not be accepted.

| Date | Event |
|------|-------|
| April 11th | Master Project Proposals Due |
| May 6th | Master Projects Due |

### Specifications

This semester there will be substantial guidance by the teacher as to what is expected. Take notes.

**TL;DR:**

You will write a better and more comprehensive full-stack python tkinter program that manages records of interest to you. For this one you will be graded on everything in Section 9 as well as the following items:

- User validation on fields via the GUI and at the database control layer (the database class)
- Error checking in general
- Polish on the GUI. No loud colors, etc. Professional design
- Topic selected - is it real-world enough? Meaning vs. silly or last-minute
- Depth of database table accomplished. Extra involves multiple tables or pivots (relational queries across multiple keys) This is a very big area so stay over your skis.
- Comprehensive correctness and code structure quality. (Shape, documentation, etc.).

### CODE Major Grade Required minimums (Major Grade Number 1):

- Must be OOP Python with operable UI w/Menu (UI Class is NOT main module)
- Must display data from the table
- Help About Dialog

Meeting minimums achieves a grade of **75**.

**Code Grade Enhancers:** To achieve each tier, ALL of the lower tiers must be achieved.

**To achieve an 80 or better**, code must include the following minimums:

- Must include background imagery
- Must have a full working menu as shown in class (If not sure ASK)
- Must complete CRUD operations as directed by user in some manner

**To achieve a 90 or better:**

- Must have a class modeling the data used in transfer to/from the table (See example)
- Must have full CRUD operations (CREATE, READ, UPDATE, DELETE)
- Must accompany a proposal that scores above a 90

**To achieve above a 95:**

Your program must be comprehensively produced and show significant programmatic prowess. One of the biggest ways to guarantee this after meeting the 90% minimums, is to place your table on the lab cloud, and be able to connect remotely to it. This can be a copy of your table. Connection strings will be explained in class.

- (+) Connect to a database on classroom Intranet (Rogue1/Skunkworks)
- (+) Embedded Device Project (i.e., Robot or other major challenge device)

### Presentation & Demonstration (Major Grade Number 2)

- Presentations will be done to the entire class
- This major grade will include all of the final elements:
- Professional Dress

**Default Recovery**

By definition: Submit in a with this document unless directed.

- Comprehensive DEMO that functions properly
- Presentation clarity (Do you stay on point and relevant to the demo of your software)
- Demonstration of why this is meaningful to you beyond mere statement of such
- 2 words per slide rule adherence

### Code Point Deductions

- Multiple PDF submissions/ Wrong file format (non-PDF/imagery/video)
- Non scannable code results in a zero until resubmitted. If late, school board deductions in effect
- Incorrect Order of submission (Classes, Main, Schemas, Run/Images)
- Missing submissions
- Poorly documented code
- Non-meaningful code
- Non-Working Code
- Late code in accordance with school board policy at all deadlines

# Student Management System
## Full Stack Python Programming - Master Project

### Overview
This project is a comprehensive full-stack application designed to manage student records. It demonstrates mastery of Python programming, Object-Oriented Programming (OOP), Model-View-Controller (MVC) architecture, GUI development with Kivy, and database management with SQLite3.

### Architecture: MVC
The project strictly adheres to the Model-View-Controller (MVC) design pattern to ensure separation of concerns and maintainability.

- **Model (`model.py`):** 
  - Manages the data logic and business rules.
  - `Student` class: A Data Transfer Object (DTO) / POCO that includes data validation logic (Name length, Grade range, Email format).
  - `Database` class: Handles all SQLite interactions (Connection, Create Table, CRUD operations).
  
- **View (`view.py`):**
  - Handles the presentation layer using Kivy.
  - `StudentView` class: Defines the UI layout including input fields, labels, and buttons. It observes user actions and forwards them to the Controller. It creates a form-based interface with navigation buttons, strictly following the single-record display constraint.
  
- **Controller (`controller.py`):**
  - Acts as the intermediary between the Model and View.
  - `StudentController` class: Receives user input from the View, processes it (e.g., validation checks), interacts with the Model to fetch or save data, and updates the View with the results.

- **Entry Point (`main.py`):**
  - Bootstraps the application.
  - Initializes the View and Controller, links them, and starts the Kivy main loop.

### Features
- **CRUD Capabilities:** Full Create, Read, Update, and Delete functionality for student records.
- **Navigation:** Browse through records using "Previous" and "Next" buttons.
- **Data Persistence:** All data is stored reliably in a local SQLite database (`school.db`).
- **Validation:** 
  - Name must be at least 2 characters.
  - Grade must be an integer between 1 and 12.
  - Email must be in a valid format and unique across the database.
- **Error Handling:** User-friendly error messages are displayed on the status bar for invalid inputs or database conflicts (e.g., duplicate emails).
- **Professional UI:** A clean, dark-themed interface with color-coded actions (Blue for New, Green for Save, Red for Delete) for intuitive user experience.

### Requirements
- Python 3.x
- Kivy

### Setup & Run
1.  **Install Dependencies:**
    ```bash
    pip install pipreqs
    pipreqs . --force
    pip install -r requirements.txt
    rm -rf requirements.txt
    ```
    *(Note: This installs Kivy. Ensure your environment supports Kivy installation).*

2.  **Run the Application:**
    ```bash
    python main.py
    ```

### File Structure
```
std02-jihoo-fullstack/
├── main.py          # Application Entry Point
├── model.py         # Data Model & Database Logic
├── view.py          # Kivy GUI Layout
├── controller.py    # Application Logic & Event Handling
├── requirements.txt # Project Dependencies
└── README.md        # Documentation
```

### Grade Level Implementation
This project targets the **Master Project** and **Item 9 (Full Stack Project)** requirements:
- **MVC Architecture:** Implemented without circular dependencies.
- **Database:** Full SQL integration with a persistent backend.
- **GUI:** Functional Kivy interface replacing Tkinter as requested.
- **Constraints:** Single record view (no multiple record lists) and no GUI code in the Model.

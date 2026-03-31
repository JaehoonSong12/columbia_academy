# main.py
"""
Fitness Tracker Prototype - Final Master Version
Technology Stack: Python, Kivy, SQLite3
Architecture: Model-View-Controller (MVC)

Key Features:
1. Automatic Date Handling: 'Day' is automatically set to the current date.
2. Duplicate Prevention: Logic prevents logging multiple entries for the same user on the same day.
3. Relational Report System: Re-implemented the pivot query to show diet-based progress.
4. Preference Consistency: Uses the specific 'user's preference' terminology for diet data.

All character encoding is ASCII.
"""

import sqlite3
import os
from datetime import date

# Kivy Framework Imports
try:
    from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.boxlayout import BoxLayout
    from kivy.properties import StringProperty
except ImportError:
    print("Error: Kivy library not found. Please install it using 'pip install kivy'.")

# -----------------------------------------------------------------------------
# MODEL LAYER: Data Handling and Relational Logic
# -----------------------------------------------------------------------------

class FitnessModel:
    """
    The Model layer manages the SQLite relational database.
    It handles profile creation, daily logging, and aggregate reporting.
    """
    def __init__(self, db_name="fitness_tracker.db"):
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the relational schema. 
        'profiles' table stores the 'user's preference' (diet type).
        'logs' table stores daily weight entries linked via foreign key.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Profiles table for user preferences
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    preference TEXT NOT NULL
                )
            ''')
            
            # Logs table for daily data points
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    profile_id INTEGER NOT NULL,
                    weight_val REAL NOT NULL,
                    day_int INTEGER NOT NULL,
                    FOREIGN KEY (profile_id) REFERENCES profiles (id)
                )
            ''')
            conn.commit()

    def has_record_for_today(self, username, today_int):
        """
        Checks if a record exists for this specific user and date.
        Prevents redundant form completion.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = '''
                    SELECT l.id FROM logs l
                    JOIN profiles p ON l.profile_id = p.id
                    WHERE p.username = ? AND l.day_int = ?
                '''
                cursor.execute(query, (username, today_int))
                return cursor.fetchone() is not None
        except sqlite3.Error:
            return False

    def record_data(self, username, preference, weight, day_int):
        """
        Saves user data. First updates the user's preference in the profile,
        then inserts the daily log into the relational logs table.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Update or Insert profile (User Preference)
                cursor.execute(
                    "INSERT OR IGNORE INTO profiles (username, preference) VALUES (?, ?)", 
                    (username, preference)
                )
                cursor.execute(
                    "UPDATE profiles SET preference = ? WHERE username = ?", 
                    (preference, username)
                )
                
                # Fetch Foreign Key
                cursor.execute("SELECT id FROM profiles WHERE username = ?", (username,))
                profile_id = cursor.fetchone()[0]
                
                # Insert Log Entry
                cursor.execute(
                    "INSERT INTO logs (profile_id, weight_val, day_int) VALUES (?, ?, ?)", 
                    (profile_id, weight, day_int)
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return False

    def get_pivot_report(self):
        """
        Generates an aggregate report using a relational JOIN query.
        Summarizes weight data grouped by the user's diet preference.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = '''
                    SELECT p.preference, AVG(l.weight_val), COUNT(l.id)
                    FROM profiles p
                    JOIN logs l ON p.id = l.profile_id
                    GROUP BY p.preference
                '''
                cursor.execute(query)
                return cursor.fetchall()
        except sqlite3.Error:
            return []

# -----------------------------------------------------------------------------
# VIEW & CONTROLLER LAYER
# -----------------------------------------------------------------------------

KV_INTERFACE = """
<TrackerLayout>:
    orientation: 'vertical'
    padding: 25
    spacing: 12
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.15, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "Master Fitness Tracker"
        font_size: '28sp'
        bold: True
        size_hint_y: None
        height: 60
        color: 0.2, 0.8, 0.6, 1

    # Form Area
    BoxLayout:
        orientation: 'vertical'
        spacing: 8
        size_hint_y: None
        height: 220

        Label:
            text: "User Management"
            bold: True
            halign: 'left'
            text_size: self.size

        TextInput:
            id: user_field
            hint_text: "User Name (Types check today's status)"
            multiline: False
            on_text: root.check_user_status()

        TextInput:
            id: preference_field
            hint_text: "User's Preference (e.g. Vegan, Keto)"
            multiline: False

        TextInput:
            id: weight_field
            hint_text: "Weight (Float)"
            multiline: False

    # Action Buttons
    Button:
        id: submit_btn
        text: "Submit Daily Entry"
        size_hint_y: None
        height: 50
        background_color: 0.2, 0.6, 0.4, 1
        on_release: root.process_submission()

    Button:
        text: "Generate Progress Report"
        size_hint_y: None
        height: 50
        background_color: 0.3, 0.4, 0.6, 1
        on_release: root.show_report()

    # Status and Report Output
    Label:
        id: status_msg
        text: "System Status: Ready"
        color: 0.7, 0.7, 0.7, 1
        halign: 'center'
        text_size: self.width, None

    Label:
        id: date_display
        text: "Today: --"
        font_size: '12sp'
        color: 0.5, 0.5, 0.5, 1
"""

class TrackerLayout(BoxLayout):
    """
    Controller that integrates the Model and View.
    Ensures validation rules (duplicates, data types) are followed.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = FitnessModel()
        self.today_obj = date.today()
        self.today_int = int(self.today_obj.strftime("%Y%m%d"))
        self.ids.date_display.text = f"Logging for Day: {self.today_int}"

    def check_user_status(self, *args):
        """
        Dynamically checks if a user has already completed the form today.
        Blocks the submit button if a record is found.
        """
        username = self.ids.user_field.text.strip()
        if not username:
            self.ids.submit_btn.disabled = False
            self.ids.status_msg.text = "Status: Awaiting Username"
            return

        if self.model.has_record_for_today(username, self.today_int):
            self.ids.status_msg.text = "Daily status: Record already exists. No further input needed."
            self.ids.status_msg.color = (1, 0.7, 0.3, 1)
            self.ids.submit_btn.disabled = True
        else:
            self.ids.status_msg.text = "Daily status: No record found. Please complete form."
            self.ids.status_msg.color = (0.3, 1, 0.5, 1)
            self.ids.submit_btn.disabled = False

    def process_submission(self):
        """
        Validates the user's preference and weight before recording.
        Uses robust error checking as required by project specs.
        """
        user = self.ids.user_field.text.strip()
        pref = self.ids.preference_field.text.strip()
        weight_str = self.ids.weight_field.text.strip()

        if not all([user, pref, weight_str]):
            self._update_status("Error: Missing required fields.", True)
            return

        try:
            weight_val = float(weight_str)
            
            # Save to relational database
            if self.model.record_data(user, pref, weight_val, self.today_int):
                self._update_status(f"Success: Record saved for {user}.")
                self.ids.submit_btn.disabled = True
            else:
                self._update_status("Error: Database write failed.", True)
        
        except ValueError:
            self._update_status("Error: Weight must be a valid number.", True)

    def show_report(self):
        """
        Retrieves the pivot report data and updates the GUI display.
        """
        data = self.model.get_pivot_report()
        if not data:
            self._update_status("Report: No data found in database.")
            return

        header = "Report (Preference | Avg Weight | Count):\\n"
        rows = [f"{r[0]} | {r[1]:.1f} | {r[2]}" for r in data]
        self.ids.status_msg.text = header + "\\n".join(rows)
        self.ids.status_msg.color = (0.5, 0.8, 1, 1)

    def _update_status(self, msg, is_error=False):
        self.ids.status_msg.text = f"Status: {msg}"
        self.ids.status_msg.color = (1, 0.4, 0.4, 1) if is_error else (0.4, 1, 0.6, 1)

class FitnessApp(App):
    """Main Application Entry Point."""
    def build(self):
        Builder.load_string(KV_INTERFACE)
        self.title = "Master Project: Fitness Tracker Prototype"
        return TrackerLayout()

if __name__ == "__main__":
    FitnessApp().run()
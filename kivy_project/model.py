# model.py

"""
Purpose
--------
Provide a simple, testable data layer for the app.
It must be a "class" (same as "struct" in C) because it encapsulates all database access.
CRUD operations are implemented as methods of this class.
"""

import sqlite3
from typing import List, Tuple, Optional 

# camelCase: first word lowercase, subsequent words start with capital letter
# PascalCase: every word starts with a capital letter
# snake_case: words are separated by underscores
class FrogModel:
    # self.id (hidden)
    # field means "real" data binded to objects created
    def __init__(self, id, princess, count): # constructor with parameters (special methods)
        self.id = id
        self.princess = princess
        self.count = count
    def __str__(self): # string representation (special methods)
        return f"FrogModel(id={self.id}, princess='{self.princess}', count={self.count})"
    
    # mutable data means "data can change"
    # immutable data means "data cannot change"
    def get_id(self): # method (accessor / getter)
        return self.id
    # def set_id(self, id): # method (mutator / setter)
    #     self.id = id

    def get_princess(self):
        return self.princess
    def set_princess(self, princess):
        self.princess = princess

    def get_count(self):
        return self.count
    def set_count(self, count):
        self.count = count


class User: # POCO: Plain Old Class Object
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
# Submit your GUI Hello World as POCO instantiated in main. 
# This means that your Gui must be a class independent of 
# the main application class and be instantiated therein


class Database:
    def __init__(self, db_name=":memory:"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create()

    def _create(self): # Create of CRUD
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS frogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                princess TEXT NOT NULL,
                count INTEGER NOT NULL
            )
        ''')
        self.connection.commit()
    
    def get_tables(self) -> List[Tuple[str]]:
        self.cursor.execute('''
            SELECT name FROM sqlite_master WHERE type='table';
        ''')
        return self.cursor.fetchall()

    def add_record(self, princess: str, count: int) -> int: # Create of CRUD
        self.cursor.execute('''
            INSERT INTO frogs (princess, count) VALUES (?, ?)
        ''', (princess, count))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_record(self, id: int) -> Optional[FrogModel]: # Read of CRUD
        self.cursor.execute('''
            SELECT id, princess, count FROM frogs WHERE id = ?
        ''', (id,))
        row = self.cursor.fetchone()
        if row:
            return FrogModel(row[0], row[1], row[2])
        return None

    def get_all_records(self) -> List[FrogModel]: # Read of CRUD
        self.cursor.execute('''
            SELECT id, princess, count FROM frogs
        ''')
        rows = self.cursor.fetchall()
        return [FrogModel(row[0], row[1], row[2]) for row in rows]
    
    def close(self) -> None:
        try:
            self.connection.close()
        except Exception as e:
            print(f"Error closing database connection: {e}")



if __name__ == "__main__":
    
    db = Database("my_frogs.db")
    tables = db.get_tables()
    print(f"Tables in the database: {tables}")
    



    # model = FrogModel(10, "Kaytlin", 10)
    # record_id = db.add_record(model.get_princess(), model.get_count())
    # print(f"Added record with ID: {record_id}")


    rows = db.get_all_records()
    for row in rows:
        print(f"{row}")
    



    
    # python model.py
    # print(f"Model module executed directly. The created model is: {model}")
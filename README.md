# Python To-Do List Project

This is a **command-line To-Do List application** written in **Python**, using **SQLite** for persistent data storage.  
The project is designed to practice **CRUD operations**, **basic database usage**, and **data structures** such as **Stack (LIFO)**.

---

## Features

- ➕ Add new duties  
- 📋 List all duties with **Done / Not Done** status  
- 🗑️ Delete duties by ID  
- ♻️ **Undo last delete operation (Stack-based)**  
- ✅ Mark duties as Done  
- 💾 Persistent storage using **SQLite database**

---

## Data Structures Used

- **Stack (LIFO)**  
  - Deleted duties are stored in a stack
  - The last deleted duty can be restored using the *undelete* feature

This demonstrates a real-world usage of stack data structure.

---

## Technologies Used

- Python 3
- SQLite3
- Git & GitHub

---

## How to Run

1. Make sure **Python 3** is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/azraoztrk/Python-todo-list-project.git
3.Navigate to the project folder:
   cd ToDoProject
4.Run the program:
   python todo.py

# To-Do List Application

This project implements a simple To-Do List Application using Python. The program utilizes a text file, `gorevler.txt`, to store tasks. Users can list tasks, add new ones, edit existing tasks, and remove tasks from the list.

---

## Table of Contents

- [Functions](#functions)  
  - [Load Tasks](#load-tasks)  
  - [Save Tasks](#save-tasks)  
  - [List Tasks](#list-tasks)  
  - [Add Task](#add-task)  
  - [Edit Task](#edit-task)  
  - [Delete Task](#delete-task)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Menu](#menu)  

---

## Functions

### Load Tasks

This function loads saved tasks from `gorevler.txt` into a list when the program starts. If the file doesn't exist, it creates a new task list.

### Save Tasks

This function writes the current list of tasks to `gorevler.txt` so that they are saved for future sessions.

### List Tasks

This function prints all current tasks in a numbered list format.

### Add Task

This function allows the user to add a new task by typing it in. The new task is then added to the list and saved to the file.

### Edit Task

This function displays all current tasks and allows the user to update the text of a selected task by its number.

### Delete Task

This function displays all current tasks and allows the user to delete a selected task by its number.

---

## Getting Started

To get started with the To-Do List Application, follow these steps:

1. Clone or download the repository to your local machine.  
2. Make sure you have Python installed.  
3. Run the program by executing the Python file.

> Note: The file `gorevler.txt` will be created automatically after you add your first task.

---

## Usage

After running the program, you can interact with the To-Do List Application using the menu.

---

## Menu
### TO-DO LIST MENU
1) List Tasks
2) Add Task
3) Edit Task
4) Delete Task
5) Exit

Enter the corresponding number (1–5) to perform the desired action. The program will prompt you for further input based on your selection.

---

Happy coding! 🚀

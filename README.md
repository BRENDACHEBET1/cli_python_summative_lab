# CLI Project Management System (Python)

A command-line project management tool built with Python that allows users to manage **users, projects, and tasks** with persistent JSON storage.

It demonstrates object-oriented programming, CLI design using `argparse`, and data persistence using JSON files.

---

##  Features

###  User Management
- Create users with name and email
- Prevent duplicate users
- List all users in a formatted table

###  Project Management
- Create projects linked to users
- Each project has a title, description, and due date
- View all projects in a clean CLI table

###  Task Management
- Create tasks under specific projects
- Assign tasks to users
- Mark tasks as completed


###  Data Persistence
- All data stored in JSON files
- Automatic save/load for:
  - Users
  - Projects
  - Tasks

###  Rich CLI Output
- Uses `rich` for styled terminal tables and colored output



##  Installation

### 1. Clone the repository

git clone git@github.com:BRENDACHEBET1/cli_python_summative_lab.git
cd cli_python_summative_lab

# Install dependencies
pip install -r requirements.txt

## PROJECT COMMANDS

### Create a user
python main.py add-user --name "brenda" --email brenda@gmail.com

### List all users
python main.py list-users

### Add Project
python main.py add-project \
    --title "Project Title" \
    --description "Project Description" \
    --due-date 2026-12-31 \
    --user-email brenda@gmail.com

### List projects
python main.py list-projects

### Add Task
python main.py add-task \
    --title "Task Title" \
    --assigned-to brenda@gmail.com \
    --project-title "Project Title"

### Complete task
python main.py complete-task --task-title "Task Title"

### Author
Brenda Chebet



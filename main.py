import argparse
from datetime import datetime

#import classes
from model.user import User
from model.project import Project
from model.task import Task

from utils import (load_data, save_data, find_user,)

#file paths
USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

#Data from json
users = load_data("data/users.json")
projects = load_data("data/projects.json")
tasks = load_data("data/tasks.json")

#Load objetc
users = User.load_all(load_data(USERS_FILE))
projects = Project.load_all(load_data(PROJECTS_FILE))
tasks = Task.load_all(load_data(TASKS_FILE))



#cli actions
def add_user(args):
    """ Create a new user object"""
    user =User(args.name, args.email)
    user.id = len(users) + 1 
    
    users.append(user)
    save_data("data/users.json", users)

    print(f'User created: {user['name']} ({user['email']})')


def list_users(args):
    """ display all the users"""

    if not users:
        print("No users found")
        return
    
    for user in users:
        print(f"User {user['id']}: {user['name']} {user['email']}")

#Project functions
def add_project(args):

    user = next((user for user in users if user["email"] == args.user_email), None)

    if not user:
        print("User not found")
        return

    project = Project(args.title, args.description, args.due_date, user)
    project.id = len(projects) + 1

    projects.append(project)
    save_data("data/projects.json", projects)

    print(f"Project created: {project['title']}")

def list_projects(args):
   
    #check if prjects exist
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        user = next((user for user in users if user["email"] == project["user_email"]), None)
        owner = user["name"] if user else "Unassigned"

        print(f"{project['id']}: {project['title']} | {owner}")

#Task functions
def add_task(args):
    project = next((project for project in projects if project["id"] == args.project_id), None)
    user = next((user for user in users if user["email"] == args.assigned_to), None)

    if not project:
        print("Project not found")
        return

    user = find_user(users, args.assigned_to)
    if not user:
        print("User not found")
        return

    task = {
        "id": len(tasks) + 1,
        "title": args.title,
        "status": "pending",
        "project_id": args.project_id,
        "assigned_to": args.assigned_to
    }
    

    tasks.append(task)
    save_data("data/tasks.json", tasks)

    print(f"Task created: {task['title']}")

def complete_task(args):
    task = next((task for task in tasks if task["id"] == args.task_id), None)

    if not task:
        print("Task not found")
        return

    task['status'] = "completed"

    save_data("data/tasks.json", tasks)

    print(f"Task {task['title']} completed")

    

#Command setup: cli
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    #User actions
    #subparser for add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("name")
    user_parser.add_argument("email")
    user_parser.set_defaults(func=add_user)

    #subparser for showing users
    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)


    #Project actions
    #subparser for adding a project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("title")
    project_parser.add_argument("description")
    project_parser.add_argument("due_date")
    project_parser.add_argument("user_email")
    project_parser.set_defaults(func=add_project)

    # listing-projects
    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.set_defaults(func=list_projects)

    #Task actions
    #subparser for adding task
    # Command: add-task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("title")
    task_parser.add_argument("assigned_to")
    task_parser.add_argument("project_id", type=int)
    task_parser.set_defaults(func=add_task)

    # # Command: list-tasks
    # list_tasks_parser = subparsers.add_parser("list-tasks")
    # list_tasks_parser.set_defaults(func=list_tasks)

    # Command: complete-task
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("task_id", type=int)
    complete_parser.set_defaults(func=complete_task)


    args = parser.parse_args()

    # If user typed a valid command, run it
    if hasattr(args, "func"):
        args.func(args)
    else:
        # If no command was typed, show help text
        parser.print_help()

#start program
if __name__ == "__main__":
    main()




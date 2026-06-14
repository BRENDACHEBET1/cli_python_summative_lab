import argparse
from datetime import datetime

#import classes
from model.user import User
from model.project import Project
from model.task import Task

from utils import load_data, save_data

# File paths
USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"


# Load data (raw JSON → objects)
users = User.load_all(load_data(USERS_FILE))
projects = Project.load_all(load_data(PROJECTS_FILE))
tasks = Task.load_all(load_data(TASKS_FILE))



#cli actions
#user functions
def add_user(args):
    """ Create a new user object"""
    user = User( args.name, args.email)
    

    users.append(user)
    save_data(USERS_FILE, [u.to_dict() for u in users])

    print(f"User created: {user.name} ({user.email})")


def list_users(args):
    """ display all the users"""

    if not users:
        print("No users found")
        return
    
    for user in users:
        print(f"User {user.id}: {user.name} {user.email}")

#Project functions
def add_project(args):

    user = next((user for user in users if user.email == args.user_email), None)

    if not user:
        print("User not found")
        return

    project = Project(args.title, args.description, args.due_date)
   

    projects.append(project)
    user.add_project(project)
    save_data(PROJECTS_FILE, [p.to_dict() for p in projects] )

    print(f"Project created: {project.title}")

def list_projects(args):
   
    #check if prjects exist
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        print(f"{project.id}: Project Title: {project.title}, Project Description {project.description}")
#Task functions
def add_task(args):
    project = next((project for project in projects if project.title == args.project_title), None)
    
    if not project:
        print("Project not found")
        return

    user = next((user for user in users if user.email == args.assigned_to), None)
    if not user:
        print("User not found")
        return

    task = Task(args.title,"Pending",args.assigned_to, project)
    

    tasks.append(task)
    save_data(TASKS_FILE,  [t.to_dict() for t in tasks])

    print(f"Task created: {task.title}")



def complete_task(args):
    task = next((task for task in tasks if task.title == args.task_title), None)

    if not task:
        print("Task not found")
        return

    task.status = "Completed"
    save_data(TASKS_FILE, [t.to_dict() for t in tasks])

    print(f"Task '{task.title}' completed")

    
    

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
    task_parser.add_argument("project_title")
    task_parser.set_defaults(func=add_task)


    # Command: complete-task
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("task_title")
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




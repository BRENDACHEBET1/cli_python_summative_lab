from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
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


# Load data from json fles to objects
users = User.load_all(load_data(USERS_FILE))
projects = Project.load_all(load_data(PROJECTS_FILE))
tasks = Task.load_all(load_data(TASKS_FILE))



#cli actions
#user functions
def add_user(args):
    """ Create a new user object"""
    """Prevent duplicate users"""
    for user in users:
        if user.email == args.email:
            print("[red]User already exists[/red]")
            return
    
    user = User( args.name, args.email)
    users.append(user)

    save_data(USERS_FILE, [u.to_dict() for u in users])

    print(f"[yellow]User created[/yellow]: [green]{user.name} ({user.email})[/green]")


def list_users(args):
    """ display all the users"""

    if not users:
        print("[red]No users found[/red]")
        return
    
    table = Table(title="Users")

    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Email", style="magenta")

    for user in users:
        table.add_row(str(user.id), user.name, user.email)

    console.print(table)


#Project functions
def add_project(args):
    """find user  who owns project"""
    user = next((user for user in users if user.email == args.user_email), None)

    if not user:
        print("User not found")
        return

    project = Project(args.title, args.description, args.due_date)
   

    projects.append(project)
    user.add_project(project)
    save_data(PROJECTS_FILE, [p.to_dict() for p in projects] )
    save_data(USERS_FILE, [u.to_dict() for u in users])

    print(f"[yellow]Project created:[/yellow] [green]Title: {project.title}[/green]")

def list_projects(args):
   
    #check if prjects exist
    if not projects:
        print("No projects found.")
        return
    
    table = Table(title="Projects")

    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Description", style="white")

    for project in projects:
        table.add_row(str(project.id), project.title, project.description)

    console.print(table)

def add_task(args):
    project = next((project for project in projects if project.title == args.project_title), None)
    
    if not project:
        print("Project not found")
        return

    user = next((user for user in users if user.email == args.assigned_to), None)
    if not user:
        print("User not found")
        return

    task = Task(args.title,"Pending",user.email, project)
    
    task.project = project
    tasks.append(task)
    project.add_task(task)

    save_data(TASKS_FILE,  [t.to_dict() for t in tasks])
    save_data(PROJECTS_FILE, [p.to_dict() for p in projects])

    print(f"[green] Task created:[/green] {task.title} [blue]Project:{project.title}[/blue]")



def complete_task(args):
    task = next((task for task in tasks if task.title == args.task_title), None)

    if not task:
        print("Task not found")
        return

    task.status = "Completed"
    save_data(TASKS_FILE, [t.to_dict() for t in tasks])

    print(f"[yellow]Task [/yellow]'[green]{task.title}' completed[/green]")

    
    

#Command setup: cli
def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    #User actions
    #subparser for add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True, help="User name")
    user_parser.add_argument("--email", required=True, help="User email")
    user_parser.set_defaults(func=add_user)

    #subparser for showing users
    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)


    #Project actions
    #subparser for adding a project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("--title", required=True)
    project_parser.add_argument("--description", required=True)
    project_parser.add_argument("--due-date", required=True)
    project_parser.add_argument("--user-email", required=True)
    project_parser.set_defaults(func=add_project)

    # listing-projects
    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.set_defaults(func=list_projects)

    #Task actions
    #subparser for adding task
    # Command: add-task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--title", required=True)
    task_parser.add_argument("--assigned-to", required=True)
    task_parser.add_argument("--project-title", required=True)
    task_parser.set_defaults(func=add_task)


    # Command: complete-task
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--task-title", required=True)
    complete_parser.set_defaults(func=complete_task)


    args = parser.parse_args()

    # If user typed a valid command, run 
    if hasattr(args, "func"):
        args.func(args)
    else:
        # If no command was typed, show help text
        parser.print_help()

#start program
if __name__ == "__main__":
    main()




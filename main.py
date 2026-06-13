import argparse

#import classes
from model.user import User
from model.project import Project
from model.task import Task

#temporary data storage
users = []
projects = []
tasks = []

#cli actions
def add_user(args):
    """ Create a new user object"""
    user = User(args.name, args.email)
    users.append(user)

    print(f'User created: {user}')


def list_users(args):
    """ display all the users"""
    if not users:
        print("No users found")
        return
    
    for user in users:
        print(f"User {user.id}: {user.name} {user.email}")

#Project functions
def add_project(args):
    project = Project(args.name, args.description, args.due_date)

    projects.append(project)

    print(f"Project created: {project}")


def list_projects(args):
    #check if prjects exist
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        print(f"Project {project.id}: {project.title}")

#Task functions
def add_task(args):
    task = Task(args.title, "Pending", args.assigned_to)
    tasks.append(task)
    print(f"Task created: {task}")

def complete_task(args):
    """loop through tasks"""
    for task in tasks:
        if task.id == args.task_id:
            #set status to complete
            task.status = "Completed"
            print("Task marked as complete")
            return
    #If task does not exist
    print("Task not found.")    
    

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
    project_parser.add_argument("name")
    project_parser.add_argument("description")
    project_parser.add_argument("due_date")
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




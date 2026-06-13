import json
import os

def load_data(filepath):
    """
    Load data from a JSON file.
    Returns empty list if file doesn't exist.
    """
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(filepath, data):
    """
    Save Python data to JSON file.
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


#convert object to dictionary
def user_to_dict(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }



def project_to_dict(project):
   return {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "due_date": str(project.due_date),
        "user_email": project.user.email if project.user else None
    }


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "project_id": task.project.id,
        "assigned_to": task.assigned_to.email
    }

def find_user(users, email):
    return next((u for u in users if u['email'] == email), None)


def find_project(projects, project_id):
    return next((p for p in projects if p['id'] == project_id), None)


def find_task(tasks, task_id):
    return next((t for t in tasks if t['id'] == task_id), None)

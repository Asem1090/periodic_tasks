from datetime import datetime
from json import load, dump
from os.path import isfile, getsize


class TasksManager:
    TASK_PRINT_FORMAT = "{name:<25}{repetition:<15}{last_completion_date:<20}"
    FILE_PATH = 'data/repeated_tasks.json'

    def __init__(self):
        if not isfile(TasksManager.FILE_PATH) or getsize(TasksManager.FILE_PATH) == 0:
            with open(TasksManager.FILE_PATH, "a") as file:
                dump({}, file, indent=4)

    @staticmethod
    def get_tasks() -> dict[str: dict]:
        with open(TasksManager.FILE_PATH, "r") as file:
            return load(file)

    @staticmethod
    def get_due_tasks() -> dict[str: dict]:
        tasks = TasksManager.get_tasks()

        return {task for task in tasks if (datetime.now() - task["last_completion_date"]).days >= task["repetition"]}

    @staticmethod
    def add_new_task(name, repetition, last_completion_date) -> bool:
        with open(TasksManager.FILE_PATH, "r+") as file:
            tasks = load(file)

            if name in tasks: # Task already exists
                return False

            tasks[name] = {
                "repetition": repetition,
                "last_completion_date": last_completion_date.isoformat()
            }

            file.seek(0)
            dump(tasks, file, indent=4)

    @staticmethod
    def complete_task(task_name: str) -> bool:
        with open(TasksManager.FILE_PATH, "r+") as file:
            tasks = load(file)

            if task_name not in tasks:
                return False

            tasks[task_name]["last_completion_date"] = datetime.now().isoformat()

            file.seek(0)
            dump(tasks, file, indent=4)

    @staticmethod
    def delete_task(name: str) -> bool:
        with open(TasksManager.FILE_PATH, "r+") as file:
            tasks = load(file)

            if name not in tasks:
                return False

            del tasks[name]
            return True

    @staticmethod
    def task_exists(task_name: str) -> bool:
        with open(TasksManager.FILE_PATH, "r+") as file:
            tasks = load(file)

            return task_name in tasks

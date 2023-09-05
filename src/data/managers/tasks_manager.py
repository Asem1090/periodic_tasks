from datetime import datetime

from src.data import DATETIME_FORMAT
from src.data.Task import Task


class TasksManager:
    FILE_PATH = 'data/repeated_tasks.csv'

    file = None

    def __init__(self):
        with open(TasksManager.FILE_PATH, "a"):
            ...

        if TasksManager.file is None:
            TasksManager.file = open(TasksManager.FILE_PATH, "r+")

    @staticmethod
    def get_tasks() -> set[Task]:
        TasksManager.file.seek(0)

        lines = TasksManager.file.read().splitlines()

        return {Task.from_csv(line) for line in lines}

    @staticmethod
    def get_due_tasks() -> set[Task]:
        TasksManager.file.seek(0)

        lines = TasksManager.file.read().splitlines()

        return {task for line in lines if (task := Task.from_csv(line)).is_due()}

    @staticmethod
    def add_new_task(task: Task) -> bool:
        if TasksManager.task_exists(task.name):
            return False

        TasksManager.file.seek(0, 2)
        TasksManager.file.write(task.to_csv())

        return True

    @staticmethod
    def complete_task(task_name: str) -> bool:
        TasksManager.file.seek(0)

        while (line := TasksManager.file.readline()) != "":
            name, repetition, last_completion_date = line.split(",")

            if name == task_name:
                TasksManager.file.seek(-19, 1)
                TasksManager.file.write(datetime.now().strftime(DATETIME_FORMAT))
                return True

        return False

    @staticmethod
    def delete_task(task_name: str) -> bool:
        TasksManager.file.seek(0)

        task_exists = False
        lines = TasksManager.file.readlines()

        for line_no, line_details in enumerate(lines):
            if line_details.split(",")[0] == task_name:
                lines.pop(line_no)
                task_exists = True

        if task_exists:
            TasksManager.file.seek(0)
            TasksManager.file.writelines(lines)
            TasksManager.file.truncate()

        return task_exists

    @staticmethod
    def task_exists(task_name: str) -> bool:
        for task in TasksManager.get_tasks():
            if task_name == task.name:
                return True

        return False

from datetime import datetime
from data.task import Task


class TasksManager:
    FILE_PATH = '../repeated_tasks.csv'
    __instance = None
    file = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(TasksManager, cls).__new__(cls)

        return cls.__instance

    def __init__(self):
        with open(TasksManager.FILE_PATH, "a+") as file:
            self.tasks = set()
            file.seek(0)
            raw_data = file.read().splitlines()
            for line in raw_data:
                task_name, rep, completion_date = line.split(",")
                self.tasks.add(Task(task_name, rep, datetime.strptime(completion_date, Task.DATETIME_FORMAT)))

    def save(self):
        with open(TasksManager.FILE_PATH, "w") as file:
            file.writelines((task.to_csv() for task in self.tasks))

    def get_tasks(self) -> set[Task]:
        return self.tasks

    def get_due_tasks(self) -> set[Task]:
        return {task for task in self.tasks if task.is_due()}

    def add_new_task(self, task: Task) -> bool:
        if self.task_exists(task.name):
            return False

        self.tasks.add(task)
        return True

    def complete_task(self, task_name: str) -> bool:
        for task in self.tasks:
            if task.name == task_name:
                task.last_completion_date = datetime.now()
                return True

        return False

    def delete_task(self, task_name: str) -> bool:
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.discard(task)
                return True

        return False

    def task_exists(self, task_name: str) -> bool:
        for task in self.tasks:
            if task.name == task_name:
                return True

        return False

from typing import FrozenSet

from src.data.Task import Task


class TasksManager:
    FILE_NAME = "repeated_tasks.csv"
    file = open(FILE_NAME, "r+")

    def complete_task(self, task_name: str) -> bool:
        ...

    @property
    def tasks(self) -> set[Task]:
        TasksManager.file.seek(0)

        lines = TasksManager.file.read().splitlines()

        return {Task.from_csv(line) for line in lines}

    @property
    def due_tasks(self) -> set[Task]:
        TasksManager.file.seek(0)

        lines = TasksManager.file.read().splitlines()

        return {task for line in lines if (task := Task.from_csv(line)).is_due()}

    def delete_task(self, task_name: str) -> bool:
        ...

    def add_task(self, task_name: str, task_repetition: int) -> bool:
        if self.task_exists(task_name):
            TasksManager.file.seek(0, 2)

            TasksManager.file.write()

    def task_exists(self, task_name: str) -> bool:
        for task in self.tasks:
            if task_name == task.name:
                return True

        return False

class TasksManager:
    FILE_NAME = "repeated_tasks.csv"
    file = open(FILE_NAME, "r+")

    def complete_task(self, task_name: str) -> bool:
        ...

    def get_tasks(self) -> str:
        ...

    def get_due_tasks(self) -> str:
        ...

    def delete_task(self, task_name: str) -> bool:
        ...

    def add_task(self, task_name: str, task_repetition: int):
        ...
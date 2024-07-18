from datetime import datetime
from data.task import Task


class TasksManager:
    FILE_PATH = '../repeated_tasks.csv'
    __instance: 'TasksManager' = None
    file = None

    def __new__(cls, *args, **kwargs) -> 'TasksManager':
        """If class exists, returns the existing copy.

        Returns:
            TasksManager: the only instance of the class.
        """        
        # Creates the class if it is not created yet.
        if cls.__instance is None:
            cls.__instance = super(TasksManager, cls).__new__(cls)

        return cls.__instance

    def __init__(self):
        """Reads TasksManager.FILE_PATH and stores the tasks in it in self.tasks.
        """
        self.tasks = set()  # Used for caching, to avoid reading from the file each time.

        with open(TasksManager.FILE_PATH, "a+") as file:
            file.seek(0)  # The cursor is at end of file, because file opened with a+ mode.
            raw_data = file.read().splitlines()
            for line in raw_data:
                task_name, rep, completion_date = line.split(",")
                self.tasks.add(Task(task_name, rep, datetime.strptime(completion_date, Task.DATETIME_FORMAT)))

    def get_tasks(self) -> set[Task]:
        """Returns all tasks.

        Returns:
            set[Task]: all tasks.
        """        
        return self.tasks

    def get_due_tasks(self) -> set[Task]:
        """Returns all due tasks.

        Returns:
            set[Task]: tasks that are due.
        """        
        return {task for task in self.tasks if task.is_due()}

    def save(self) -> None:
        """Writes the data in self.tasks into TasksManager.FILE_PATH.
        """        
        with open(TasksManager.FILE_PATH, "w") as file:
            file.writelines((task.to_csv() for task in self.tasks))

    def add_new_task(self, task: Task) -> bool:
        """Adds a Task, only if it does not exist.

        Args:
            task (Task): task to be added

        Returns:
            bool: True if task is added, False otherwise.
        """        
        if self.task_exists(task.name):
            return False

        self.tasks.add(task)
        return True

    def complete_task(self, task_name: str) -> bool:
        """Changes the last_completion_date of a task to now.

        Args:
            task_name (str): name of task to be completed

        Returns:
            bool: True if task is found, False otherwise.
        """        
        for task in self.tasks:
            if task.name == task_name:
                task.last_completion_date = datetime.now()
                return True

        return False

    def delete_task(self, task_name: str) -> bool:
        """Removes the task from self.tasks.

        Args:
            task_name (str): name of task to be deleted.

        Returns:
            bool: True if task is deleted, False otherwise.
        """        
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.discard(task)
                return True

        return False

    def task_exists(self, task_name: str) -> bool:
        """Checks if the task exists in self.tasks.

        Args:
            task_name (str): name of task to be checked.

        Returns:
            bool: True if task is found, False otherwise.
        """        
        for task in self.tasks:
            if task.name == task_name:
                return True

        return False

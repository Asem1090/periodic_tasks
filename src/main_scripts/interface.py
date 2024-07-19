from datetime import datetime

from data.task import Task
from data.managers.tasks_manager import TasksManager


class Interface:
    MENU = (
        """1- View Due Tasks
2- View Tasks
3- Add Task
4- Complete Task
5- Delete Task
6- Save & Exit
7- Exit Without Saving"""
    )
    OPTIONS_NO = 7
    tasks_manager = TasksManager()

    @staticmethod
    def take_option() -> int:
        """Asks the user to choose an option, and validates the input.

        Returns:
            int: the number of the option chosen by the user.
        """        
        while True:
            try:
                option = int(input(f"Please pick an option (1-{Interface.OPTIONS_NO}): "))

                if 1 <= option <= Interface.OPTIONS_NO:
                    break

            except ValueError:
                continue

        return option

    @staticmethod
    def take_new_task() -> Task:
        """Asks the user for the information for a new task.

        Returns:
            Task: the new task.
        """        
        while True:
            task_name = input("Please enter the task name: ")

            if not Interface.tasks_manager.task_exists(task_name):
                break
            else:
                print(f"A task with the name {task_name} already exists.")

        while True:
            try:
                task_repetition = int(input("Repetition (# days): "))

                if task_repetition > 0:
                    break
            except ValueError:
                continue

        return Task(task_name, task_repetition, datetime.now())

    @staticmethod
    def take_existing_task_name() -> str:
        """Asks the user for an existing task name and confirms that it exists.

        Returns:
            str: the existing task name
        """        
        while True:
            task_name = input("Please enter the task name: ")

            if Interface.tasks_manager.task_exists(task_name):
                break

        return task_name

    @staticmethod
    def print_tasks(tasks: set[Task]) -> None:
        """Prints the tasks in tabular form.

        Args:
            tasks (set[Task]): tasks to be printed
        """               
        if not tasks:
            print("No tasks found.")
            return

        print(Task.TASK_PRINT_FORMAT.format(
                name="Name:",
                repetition="Repetition",
                last_completion_date="last_completion_date"
            )
        )

        for task in tasks:
            print(task)

    @staticmethod
    def start_menu():
        """Prints options available and prompts the user to pick one.
        """        
        print(Interface.MENU)
        picked_option = Interface.take_option()

        if picked_option == 1:  # Print due tasks.
            Interface.print_tasks(Interface.tasks_manager.get_due_tasks())
        elif picked_option == 2:  # Print all tasks.
            Interface.print_tasks(Interface.tasks_manager.get_tasks())
        elif picked_option == 3:  # Add a task.
            task = Interface.take_new_task()
            Interface.tasks_manager.add_new_task(task),
        elif picked_option == 4:  # Set task as complete.
            task_name = Interface.take_existing_task_name()
            Interface.tasks_manager.complete_task(task_name)
        elif picked_option == 5:  # Delete a task.
            task_name = Interface.take_existing_task_name()
            Interface.tasks_manager.delete_task(task_name)
        elif picked_option == 6:  # Save & exit.
            Interface.tasks_manager.save()
            exit()
        elif picked_option == 7:  # Exit without saving.
            exit()

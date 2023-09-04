from datetime import datetime

from src.data.Task import Task
from src.data.managers.tasks_manager import TasksManager


class Interface:
    MENU = (
        """1- View Due Tasks
2- View Tasks
3- Add Task
4- Complete Task
5- Delete Task"""
    )
    OPTIONS_NO = 5
    tasks_manager = TasksManager()

    @staticmethod
    def take_option() -> int:
        while True:
            try:
                option = int(input(f"Please pick an option (1-{Interface.OPTIONS_NO}): "))

                if 1 <= option <= Interface.OPTIONS_NO:
                    break

            except ValueError as e:
                continue

        return option

    @staticmethod
    def take_new_task() -> Task:
        while True:
            task_name = input("Please enter the task name: ")

            if not Interface.tasks_manager.task_exists(task_name):
                break

        while True:
            try:
                task_repetition = int(input("Repetition (# days): "))

                if task_repetition > 0:
                    break
            except ValueError as e:
                continue

        return Task(task_name, task_repetition, datetime.now())

    @staticmethod
    def take_existing_task_name() -> str:
        while True:
            task_name = input("Please enter the task name: ")

            if Interface.tasks_manager.task_exists(task_name):
                break

        return task_name

    @staticmethod
    def print_tasks(tasks):
        print(f"{'Task No.':<10}{'Name':<25}{'Repetition':<5}{'last_completion_date':<20}")
        for task_no, task in enumerate(tasks, start=1):
            print(f"{'Task No.':<10}{task}")

    @staticmethod
    def start_menu():
        print(Interface.MENU)
        picked_option = Interface.take_option()

        if picked_option == 1:
            Interface.print_tasks(Interface.tasks_manager.get_due_tasks())
        elif picked_option == 2:
            Interface.print_tasks(Interface.tasks_manager.get_tasks())
        elif picked_option == 3:
            task = Interface.take_new_task()
            Interface.tasks_manager.add_new_task(task),
        elif picked_option == 4:
            task_name = Interface.take_existing_task_name()
            Interface.tasks_manager.complete_task(task_name)
        elif picked_option == 5:
            task_name = Interface.take_existing_task_name()
            Interface.tasks_manager.delete_task(task_name)

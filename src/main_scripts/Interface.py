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
    def take_option(end, start=1) -> int:
        while True:
            try:
                option = int(input(f"Please pick an option ({start}-{end}): "))

                if start <= option <= end:
                    break

            except ValueError as e:
                continue

        return option

    @staticmethod
    def take_new_task() -> tuple[str, int]:
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

        return task_name, task_repetition

    @staticmethod
    def take_existing_task_name() -> str:
        while True:
            task_name = input("Please enter the task name: ")

            if Interface.tasks_manager.task_exists(task_name):
                break

        return task_name

    def start_menu(self):
        print(Interface.MENU)
        picked_option = self.take_option()

        if picked_option == 1:
            print(Interface.tasks_manager.get_due_tasks)
        elif picked_option == 2:
            print(Interface.tasks_manager.tasks)
        elif picked_option == 3:
            task = self.take_new_task()
            Interface.tasks_manager.add_task(*task)
        elif picked_option == 4:
            task_name = self.take_existing_task_name()
            Interface.tasks_manager.complete_task(task_name)
        elif picked_option == 5:
            task_name = self.take_existing_task_name()
            Interface.tasks_manager.delete_task(task_name)

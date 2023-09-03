class Interface:
    MENU = (
        """1- View Due Tasks
2- View Tasks
3- Add Task
4- Complete Task
5- Delete Task"""
    )
    OPTIONS_NO = 5
    task_manager = TasksManager()

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

    def take_new_task(self) -> tuple[str, int]:
        while True:
            task_name = input("Please enter the task name: ")

            if not tasks_manager.task_exists(task_name):
                break

        while True:
            try:
                task_repetition = int(input("Repetition (# days): "))

                if task_repetition > 0:
                    break
            except ValueError as e:
                continue

        return task_name, task_repetition

    @static_method
    def take_existing_task_name(self) -> str:
        while True:
            task_name = input("Please enter the task name: ")

            if tasks_manager.task_exists(task_name):
                break

        return task_name

    def start_menu(self):
        print(Interface.MENU)
        picked_option = self.take_option()

        if picked_option == 1:
            print(task_manager.get_due_tasks())
        elif picked_option == 2:
            print(task_manager.get_tasks())
        elif picked_option == 3:
            task = self.take_new_task()
            task_manager.add_task(*task)
        elif picked_option == 4:
            task_name = self.take_existing_task_name()
            task_manager.complete_task(task_name)
        elif picked_option == 5:
            task_name = self.take_existing_task_name()
            task_manager.delete_task(task_name)

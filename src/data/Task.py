class Task:
    def __init__(self, task_name: str, task_repetition: int, last_completion_date: str = ""):
        self.task_name = task_name
        self.task_repetition = int(task_repetition)
        self.last_completion_date = last_completion_date

    @staticmethod
    def csv_to_task(csv_line):
        task_name, task_repetition, last_completion_date = csv_line.split(",")

    def get_csv_line(self):
        return f"{self.task_name},{self.task_repetition},{self.last_completion_date}"

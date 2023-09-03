from __future__ import annotations

from datetime import datetime


class Task:
    DATETIME_FORMAT = "%d/%m/%Y %H:%M"

    def __init__(self, name: str, task_repetition: int, last_completion_date: datetime = None):
        self.name = name
        self.repetition = int(task_repetition)
        self.last_completion_date = last_completion_date

    def __str__(self):
        return f"{self.name:<25}{self.repetition:<5}{self.last_completion_date:<20}"

    @staticmethod
    def from_csv(csv_line: str) -> Task:
        task_name, task_repetition, last_completion_date = csv_line.split(",")

        return Task(task_name, task_repetition, datetime.strptime(last_completion_date, Task.DATETIME_FORMAT))

    def to_csv(self, last_completion_date: datetime = None):
        if last_completion_date is None:
            last_completion_date = datetime.now()

        return f"{self.name},{self.repetition},{last_completion_date.strftime(Task.DATETIME_FORMAT)}"

    def is_due(self) -> bool:
        pass

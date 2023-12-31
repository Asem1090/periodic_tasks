from __future__ import annotations

from datetime import datetime


class Task:
    TASK_PRINT_FORMAT = "{name:<25}{repetition:<15}{last_completion_date:<20}"
    TASK_CSV_FORMAT = "{name},{repetition},{last_completion_date}"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M"

    def __init__(self, name: str, task_repetition: int, last_completion_date: datetime):
        self.name = name
        self.repetition = int(task_repetition)
        self.last_completion_date = last_completion_date

    def __str__(self):
        return Task.TASK_PRINT_FORMAT.format(
            name=self.name,
            repetition=self.repetition,
            last_completion_date=self.last_completion_date.strftime(Task.DATETIME_FORMAT)
        )

    @staticmethod
    def from_csv(csv_line: str) -> Task:
        task_name, task_repetition, last_completion_date = csv_line.rstrip("\n").split(",")

        return Task(task_name, task_repetition, datetime.strptime(last_completion_date, Task.DATETIME_FORMAT))

    @staticmethod
    def task_to_csv(name: str, repetition: int, last_completion_date: datetime):
        return Task.TASK_CSV_FORMAT.format(
            name=name,
            repetition=repetition,
            last_completion_date=last_completion_date.strftime(Task.DATETIME_FORMAT)
        ) + "\n"

    def to_csv(self):
        return Task.task_to_csv(self.name, self.repetition, self.last_completion_date)

    def is_due(self) -> bool:
        return (datetime.now() - self.last_completion_date).days >= self.repetition

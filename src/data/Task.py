from __future__ import annotations

from datetime import datetime


class Task:
    TASK_PRINT_FORMAT = "{name:<25}{repetition:<15}{last_completion_date:<20}"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M"

    def __init__(self, name: str, task_repetition: int, last_completion_date: datetime):
        self.name = name
        self.repetition = int(task_repetition)
        self.last_completion_date = last_completion_date

    def __str__(self):
        return Task.TASK_PRINT_FORMAT.format(self.name, self.repetition, self.last_completion_date.strftime(DATETIME_FORMAT))

    @staticmethod
    def from_csv(csv_line: str) -> Task:
        task_name, task_repetition, last_completion_date = csv_line.rstrip("\n").split(",")

        return Task(task_name, task_repetition, datetime.strptime(last_completion_date, DATETIME_FORMAT))

    @staticmethod
    def task_to_csv(name: str, repetition: int, last_completion_date: datetime):
        return Task.TASK_PRINT_FORMAT.format(name, repetition,last_completion_date.strftime(DATETIME_FORMAT))

    def to_csv(self):
        return Task.TASK_PRINT_FORMAT.format(
            self.name,
            self.repetition,
            self.last_completion_date.strftime(DATETIME_FORMAT))

    def is_due(self) -> bool:
        return (datetime.now() - self.last_completion_date).days >= self.repetition

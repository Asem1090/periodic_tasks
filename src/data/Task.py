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

    def to_csv(self):
        return Task.TASK_CSV_FORMAT.format(
            name=self.name,
            repetition=self.repetition,
            last_completion_date=self.last_completion_date.strftime(Task.DATETIME_FORMAT)
        ) + "\n"

    def is_due(self) -> bool:
        return (datetime.now() - self.last_completion_date).days >= self.repetition

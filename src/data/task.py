from __future__ import annotations

from datetime import datetime


class Task:
    """This class stores task information, and allows printing and other utilties.
    """    
    # Format templates for consistancy.
    TASK_PRINT_FORMAT = "{name:<25}{repetition:<15}{last_completion_date:<20}"
    TASK_CSV_FORMAT = "{name},{repetition},{last_completion_date}"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M"

    def __init__(self, name: str, task_repetition: int, last_completion_date: datetime):
        self.name = name
        self.repetition = int(task_repetition)
        self.last_completion_date = last_completion_date

    def __str__(self) -> str:
        """Returns the task neatly as a string, according to TASK_PRINT_FORMAT.

        Returns:
            str: formatted task information appropriate for printing.
        """        
        return Task.TASK_PRINT_FORMAT.format(
            name=self.name,
            repetition=self.repetition,
            last_completion_date=self.last_completion_date.strftime(Task.DATETIME_FORMAT)
        )

    def to_csv(self) -> str:
        """Converts Task object to csv, according to TASK_CSV_FORMAT.

        Returns:
            str: formatted task information appropriate for CSV.
        """        
        return Task.TASK_CSV_FORMAT.format(
            name=self.name,
            repetition=self.repetition,
            last_completion_date=self.last_completion_date.strftime(Task.DATETIME_FORMAT)
        ) + "\n"

    def is_due(self) -> bool:
        """Checks if the task is due.

        Returns:
            bool: True if task is due, False otherwise.
        """        
        return (datetime.now() - self.last_completion_date).days >= self.repetition

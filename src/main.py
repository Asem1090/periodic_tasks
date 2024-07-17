from main_scripts.main_class import MainClass

def main():
    MainClass.run()


if __name__ == "__main__":
    main()


# def print_tasks() -> None:
#     lines = get_tasks()
#
#     print(f"{'Task No.':<10}{'Name':<25}{'Repetition':<5}{'last_completion_date':<20}")
#     for line_no, task_details in enumerate(lines, start=1):
#         task_name, repetition, last_completion_date = task_details.split(",")
#
#         print(f"{line_no:<10}{task_name:<25}{repetition:<5}{last_completion_date:<20}")
#
#
# def print_due_tasks() -> None:
#     lines = get_tasks()
#
#     print(f"{'Task No.':<10}{'Name':<25}{'Repetition':<5}{'last_completion_date':<20}")
#     for line_no, task_details in enumerate(lines, start=1):
#         task_name, repetition, last_completion_date = task_details.split(",")
#
#         if is_due(last_completion_date):
#             print(f"{line_no:<10}{task_name:<25}{repetition:<5}{last_completion_date:<20}")
#

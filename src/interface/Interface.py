class Interface:
    MENU = (
        """1- View Due Tasks        
2- Add Task
3- Delete Task
4- Complete Task"""
    )
    OPTIONS_NO = 4

    @staticmethod
    def take_option(end, start = 1) -> int:
        while True:
            try:
                option = int(input(f"Please pick an option ({start}-{end}): "))

                if start <= option <= end:
                    break

            except ValueError as e:
                continue

        return option


    def start_menu(self):
        print(Interface.MENU)
        picked_option = self.take_option()

        if picked_option == "1":

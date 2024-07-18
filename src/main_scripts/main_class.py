from main_scripts.interface import Interface


class MainClass:
    @staticmethod
    def run() -> None:
        """This method keeps displaying the start_menu tell the user opts not to.
        """        
        while True:
            try:
                Interface.start_menu()
            except Exception as e:
                print(f"An error occurred: {e}")

            while True:
                ans = input("Continue? (Y/N): ").upper()

                if ans in {"Y", "N"}:
                    break

            if ans == "N":
                break

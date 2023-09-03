from src.main_scripts.Interface import Interface


class MainClass:
    @staticmethod
    def run():
        close = False

        while not close:
            try:
                Interface.start_menu()
            except Exception as e:
                print(f"An error occurred: {e}")

            while True:
                close = input("Continue? (Y/N): ").upper()

                if close in {"Y", "N"}:
                    break

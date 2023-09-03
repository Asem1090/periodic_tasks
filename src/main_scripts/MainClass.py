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
                ans = input("Continue? (Y/N): ").upper()

                if ans in {"Y", "N"}:
                    close = (ans == "N")
                    break

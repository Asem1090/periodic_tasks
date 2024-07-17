from main_scripts.interface import Interface


class MainClass:
    @staticmethod
    def run():
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

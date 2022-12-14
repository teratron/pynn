COMMANDS = [
    "about",
    "add",
    "config",
    "init",
    "new",
    "run",
    "stop",
    "show",
    "update",
    "version",
]


class App:
    """
    Application.
    """

    def __init__(self):
        # TODO document why this method is empty
        pass

    def run(self, exit_code: int = 0) -> int:
        print(self)
        return exit_code


def main() -> int:
    exit_code: int = App().run()
    return exit_code


if __name__ == "__main__":
    main()

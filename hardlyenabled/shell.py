import cmd
import socket

from hardlyenabled import cmdparse
from hardlyenabled import constants


COMMANDS = ["hello", "help", "exit"]


class HardlyShell(cmd.Cmd):
    intro = f"{constants.APP_NAME} {constants.VERSION}\n{constants.TAGLINE}\n"
    prompt = socket.gethostname() + ">"

    def do_hello(self, arg):
        print("Hello from the hardly shell!")

    def do_exit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def default(self, line):
        word, _, rest = line.partition(" ")
        match, error = cmdparse.resolve(word, COMMANDS)
        if error:
            if error.startswith("% Invalid"):
                print(" " * len(self.prompt) + "^")
            print(error)
            return False
        return self.onecmd(match + " " + rest)


def run():
    shell = HardlyShell()
    while True:
        try:
            shell.cmdloop()
            break
        except KeyboardInterrupt:
            print("^C")
            shell.intro = ""


if __name__ == "__main__":
    run()


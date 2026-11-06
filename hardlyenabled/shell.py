import cmd
import socket

from hardlyenabled import constants


class HardlyShell(cmd.Cmd):
    intro = f"{constants.APP_NAME} {constants.VERSION}\n{constants.TAGLINE}\n"
    prompt = socket.gethostname() + ">"

    def do_hello(self, arg):
        print("Hello from the hardly shell!")

    def do_exit(self, arg):
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HardlyShell().cmdloop()

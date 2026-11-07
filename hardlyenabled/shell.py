import cmd
import socket

from hardlyenabled import cmdparse
from hardlyenabled import constants


MODE_COMMANDS = {
    "user": ["enable", "exit"],
    "privileged": ["enable", "disable", "exit"],
}


class HardlyShell(cmd.Cmd):
    intro = f"{constants.APP_NAME} {constants.VERSION}\n{constants.TAGLINE}\n"
    hostname = socket.gethostname()
    mode = "user"

    def update_prompt(self):
        if self.mode == "user":
            self.prompt = self.hostname + ">"
        elif self.mode == "privileged":
            self.prompt = self.hostname + "#"

    def preloop(self):
        self.update_prompt()

    def precmd(self, line):
        line = line.strip()
        if not line or line == "EOF":
            return line
        word, _, rest = line.partition(" ")
        match, error = cmdparse.resolve(word, MODE_COMMANDS[self.mode])
        if error:
            if error.startswith("% Invalid"):
                print(" " * len(self.prompt) + "^")
            print(error)
            return ""
        return match + " " + rest

    def do_enable(self, arg):
        self.mode = "privileged"
        self.update_prompt()

    def do_disable(self, arg):
        self.mode = "user"
        self.update_prompt()

    def do_exit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass


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


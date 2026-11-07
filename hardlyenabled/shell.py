import cmd
import socket

from hardlyenabled import cmdparse
from hardlyenabled import constants


MODE_COMMANDS = {
    "user": ["enable", "exit"],
    "privileged": ["enable", "disable", "configure", "exit"],
    "configure": ["end", "exit"],
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
        elif self.mode == "configure":
            self.prompt = self.hostname + "(config)#"

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

    def do_configure(self, arg):
        arg = arg.strip()
        if not arg:
            arg = "terminal"
        match, error = cmdparse.resolve(arg, ["terminal"])
        if error:
            print(error)
            return
        self.mode = "configure"
        self.update_prompt()

    def do_end(self, arg):
        self.mode = "privileged"
        self.update_prompt()

    def do_exit(self, arg):
        if self.mode == "configure":
            self.mode = "privileged"
            self.update_prompt()
            return
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


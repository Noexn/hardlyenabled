def  truncated_commands(command, choices):
    matches = []
    for choice in choices:
        if choice == command:
            return [choice]
        if choice.startswith(command):
            matches.append(choice)
    return matches

if __name__ == "__main__":
    commands = ["show", "shutdown", "enable", "end", "exit"]
    print(truncated_commands("sho", commands))
    print(truncated_commands("sh", commands))
    print(truncated_commands("s", commands))
    print(truncated_commands("ena", commands))
    print(truncated_commands("en", commands))
    print(truncated_commands("e", commands))
    print(truncated_commands("x", commands))

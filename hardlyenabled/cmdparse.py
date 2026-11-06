def  truncated_commands(command, choices):
    matches = []
    for choice in choices:
        if choice == command:
            return [choice]
        if choice.startswith(command):
            matches.append(choice)
    return matches


def resolve(command, choices):
    matches =  truncated_commands(command, choices)
    if len(matches) == 1:
        return matches[0], ""
    elif len(matches) == 0:
        return "",  f"% Invalid input detected at '^' marker."
    else:
        return "",f'% Ambiguous command:  "{command}"'


if __name__ == "__main__":
    commands = ["show", "shutdown", "enable", "end", "exit"]
    for test in ["show", "sho", "sh", "s", "x"]:
        match, error = resolve(test,  commands)
        print(f"{test}: match={match!r} error={error!r}")

import subprocess


def authenticate(tool):
    result = subprocess.run([tool, "true"])
    return result.returncode == 0


if __name__ == "__main__":
    print(authenticate("sudo"))

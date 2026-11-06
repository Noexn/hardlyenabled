import os


APP_NAME = "HardlyEnabled"
APP_ID = "hardlyenabled"
VERSION = "0.1.0"
TAGLINE = "A Cisco IOS-style Command Line Interface for Linux. Not affiliated with Cisco Systems"


CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config", APP_ID)
STARTUP_CONFIG = os.path.join(CONFIG_DIR, "startup.conf")


if __name__ == "__main__":
    print(APP_NAME)
    print(APP_ID)
    print(VERSION)
    print(TAGLINE)
    print(CONFIG_DIR)
    print(STARTUP_CONFIG)

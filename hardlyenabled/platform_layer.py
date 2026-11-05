import os
import shutil


PACKAGE_MANAGERS = {
    "debian": "apt",
    "ubuntu": "apt",
    "fedora": "dnf",
    "rhel": "dnf",
    "arch": "pacman",
    "alpine": "apk",
    "opensuse": "zypper",
    "suse": "zypper",
}


MANAGER_NAMES = ["apt", "dnf", "pacman", "apk", "zypper"]


def linux_distro():
    distro_id = ""
    distro_id_like = []
    path = "/etc/os-release"
    if not os.path.exists(path):
        path = "/usr/lib/os-release"
    if not os.path.exists(path):
        return distro_id, distro_id_like
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            value = value.strip("\"'")
            if key == "ID":
                distro_id = value
            elif key == "ID_LIKE":
                distro_id_like = value.split()
    return distro_id, distro_id_like


def find_package_manager(distro_id, distro_id_like):
    if distro_id in PACKAGE_MANAGERS:
        return PACKAGE_MANAGERS[distro_id]
    for relative in distro_id_like:
        if relative in PACKAGE_MANAGERS:
            return PACKAGE_MANAGERS[relative]
    for manager in MANAGER_NAMES:
        if shutil.which(manager):
            return manager
    return ""


if __name__ == "__main__":
    distro_id, distro_id_like = linux_distro()
    package_manager = find_package_manager(distro_id, distro_id_like)
    print(distro_id)
    print(distro_id_like)
    print(package_manager)


import os


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


if __name__ == "__main__":
    distro_id, distro_id_like = linux_distro()
    print(distro_id)
    print(distro_id_like)


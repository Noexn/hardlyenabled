def linux_distro():
    distro_id = ""
    distro_id_like = []
    with open("/etc/os-release") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            value = value.strip("\"'")
            if key == "ID":
                distro_id = value
            elif key == "ID_LIKE":
                distro_id_like = value.split()
    return distro_id, distro_id_like
distro_id, distro_id_like = linux_distro()
print(distro_id)
print(distro_id_like)


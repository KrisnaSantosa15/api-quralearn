import subprocess

def update_libc():
    update_command = "sudo apt-get update && sudo apt-get install -y --only-upgrade libc6"
    try:
        subprocess.run(update_command, shell=True, check=True)
        print("libc6 updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating libc6: {e}")

def install_portaudio_dev():
    check_command = "dpkg -l | grep portaudio19-dev"

    try:
        subprocess.run(check_command, shell=True, check=True, stdout=subprocess.PIPE)
        print("PortAudio19-Dev is already installed.")
    except subprocess.CalledProcessError:
        # If the package is not found, install it
        installation_command = "sudo apt-get update && sudo apt-get install -y portaudio19-dev"
        try:
            subprocess.run(installation_command, shell=True, check=True)
            print("PortAudio19-Dev installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing PortAudio19-Dev: {e}")

def install_package():
    update_libc()
    install_portaudio_dev()
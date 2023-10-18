import uvicorn

import subprocess

# Check if PortAudio19-Dev is installed
check_command = "dpkg -l | grep portaudio19-dev"

try:
    subprocess.run(check_command, shell=True, check=True, stdout=subprocess.PIPE)
    print("PortAudio19-Dev is already installed.")
except subprocess.CalledProcessError:
    print("PortAudio19-Dev is not installed. Installing...")
    # If the package is not found, install it
    installation_command = "apt-get update && apt-get install s-y portaudio19-dev"
    try:
        subprocess.run(installation_command, shell=True, check=True)
        print("PortAudio19-Dev installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing PortAudio19-Dev: {e}")


if __name__ == "__main__":
    uvicorn.run("app:app", 
                reload=True)
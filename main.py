import uvicorn
import subprocess
import install_package

check_portaudio = "dpkg -l | grep 'libportaudio2:amd64\\|portaudio19-dev'"
try:
    subprocess.run(check_portaudio, shell=True, check=True, stdout=subprocess.PIPE)
    print("PortAudio19-Dev is already installed.")
except subprocess.CalledProcessError:
        install_package.install_package()

if __name__ == "__main__":
    uvicorn.run("app:app", 
                reload=True)
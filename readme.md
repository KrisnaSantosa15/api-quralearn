# Speech Quran Recognier (API)
## Description
This is a simple API for speech recognition of the Quran. It is based on the [Quran_speech_recognizer](https://huggingface.co/Nuwaisir/Quran_speech_recognizer). This API build on top of [FastAPI](https://fastapi.tiangolo.com/).

## Usage

### Endpoints
```
POST: api/v1/recognizer
Response: {
    "message": transcribed_text, 
    "success": True, 
    "code": 200, 
    "meta": {}, 
    "data": ""
}
```

## Installation

### INSTALL ALL REQUIRED LIBRARY
```bash
sudo apt-get update && sudo apt-get install apache2 mysql-server php libapache2-mod-php php-mysql phpmyadmin php-mbstring php-zip php-gd php-json php-curl git python3-pip portaudio19-dev ffmpeg -y
```
### Setup Apache & Firewall
```bash
sudo ufw enable && sudo systemctl enable apache2 && sudo systemctl start apache2 && sudo ufw allow in "Apache"
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 8000
```

### INSTALL & Configure MYSQL
```bash
sudo mysql_secure_installation
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'yourpassword';
```

### INSTALL ANACONDA
```bash
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
```
```bash
chmod +x Anaconda3-2023.09-0-Linux-x86_64.sh 
./Anaconda3-2023.09-0-Linux-x86_64.sh
```



### INSTALL API QURALEARN
```bash
git clone https://github.com/KrisnaSantosa15/api-quralearn.git
```

if server doesn't have cuda, install torch with this version:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### INSTALL SSL FOR HTTPS:

```bash
sudo apt update
```
```bash
sudo apt install certbot python3-certbot-apache
```
```bash
sudo certbot --apache -d quralearn.eastus.cloudapp.azure.com
http://quralearn.koreacentral.cloudapp.azure.com/
```
```bash
sudo systemctl restart apache2 
```

Copy privkey.pem and fullchain.pem to the same directory as project from /etc/letsencrypt/live/quralearn.eastus.cloudapp.azure.com/

Example
``` bash
file: main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,ssl_keyfile="privkey.pem",ssl_certfile="fullchain.pem", 
                reload=True)
```

### RUN PYTHON IN THE BACKGROUND:
```bash
nohup python3 main.py > /dev/null 2>&1 &
```

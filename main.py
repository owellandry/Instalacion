import os
import requests
import subprocess

# Función para descargar archivos
def descargar_archivo(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(response.content)

# Descargar e instalar Visual Studio Code
vscode_url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
vscode_installer = "vscode_installer.exe"
descargar_archivo(vscode_url, vscode_installer)
subprocess.run([vscode_installer, '/silent', '/mergetasks=!runcode'], check=True)
os.remove(vscode_installer)

# Instalar Git
git_installer = "git_installer.exe"
descargar_archivo("https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/Git-2.35.1.2-64-bit.exe", git_installer)
subprocess.run([git_installer, '/VERYSILENT', '/NORESTART', '/NOCANCEL'], check=True)
os.remove(git_installer)

# Instalar NVM (Node Version Manager)
nvm_installer = "nvm_installation.ps1"
descargar_archivo("https://raw.githubusercontent.com/coreybutler/nvm-windows/master/install.ps1", nvm_installer)
subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", nvm_installer], check=True)
os.remove(nvm_installer)

# Instalar Node.js
os.environ["NVM_SYMLINK"] = "C:\\Program Files\\nodejs"
os.environ["NVM_INIT"] = "1"
subprocess.run(["nvm", "install", "latest"], check=True)

print("Instalación completada.")

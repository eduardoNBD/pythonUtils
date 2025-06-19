import os
import subprocess
import platform
from pathlib import Path

def openFolder(dir): 
    system = platform.system()
     
    if system == "Windows":
        os.startfile(dir)
    elif system == "Darwin":   
       subprocess.run(["open", dir])
    elif system == "Linux":
        subprocess.run(["xdg-open", dir])
    else:
        raise NotImplementedError(f"Unsupported OS: {system}")
        subprocess.run(["open", dir])

def getDownloadsFolders():
    files = list(os.listdir(Path.home()))

    if "Downloads" in files:
        return Path.home() / "Downloads"
    
    elif "Descargas" in files:
        return Path.home() / "Descargas"
    
    else:
        return 0

if __name__ == "__main__":
    downloadFolder = getDownloadsFolders()
    openFolder(downloadFolder)
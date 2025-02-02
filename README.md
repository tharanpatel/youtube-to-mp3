<p align="center">
  <img src="https://github.com/user-attachments/assets/929ae3cf-773c-42bd-aa6a-4d3b71ef259e">
</p>

## Prerequisites
- Discord account
- Youtube account
- Firefox browser with Youtube logged in.

## Setup

There are a few enviroment variables that need to be changed for the program to function.

### Populate environment folder
- Create a ```.env``` file in  the ```backend``` folder and populate it with the following:
```
DISCORD_TOKEN="YOUR DISCORD TOKEN HERE"
DISCORD_CHANNEL_URL="YOUR DISCORD CHANNEL URL HERE"
```

### How to get your Discord token
- Log into discord on the web browser
- Enter developer tools
- Navigate to ```Application -> Local Storage -> Discord.com -> Filter -> type 'token' -> use the corresponding value```

### How to get your Discord channel url
- Log into discord on the web browser
- Enter developer tools
- Navigate to Network section
- Send a message on the web browser to the desired channel
- Find the corresponding POST request and use the URL used for the POST request.

### Change path to main.py
- Navigate to ```frontend -> buttons.js -> line 12```
- Change ```var pathToPythonFile``` to point to the absolute address of ```main.py``` in ```backend```

## Installation

### Install Chocolatey
- Run ```Get-ExecutionPolicy```. If it returns ```Restricted```, then run ```Set-ExecutionPolicy AllSigned``` or ```Set-ExecutionPolicy Bypass -Scope Process```
- Now run ```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

### Install yt-dlp using Chocolatey
- Install yt-dlp and ffmpeg using ```choco install ffmpeg yt-dlp```
- Verify installation using ```yt-dlp --version```

### Install Python dependencies
- ```pip install requests python-dotenv```

### Install Electron
- Navigate to ```frontend```
- ```npm install electron --save-dev```

### Create Electron app
- Navigate to ```frontend```
- ```npm install --save-dev @electron-forge/cli```
- ```npx electron-forge import```
- ```npm run make```
- An executable file called ```yt-dl-frontend``` contained in ```frontend/out/ytdl-frontend-win32-x64``` should now exist which is the runnable application.

# Built With :smile:

<table>
    <tr>
    <td valign="top"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Electron_Software_Framework_Logo.svg/1200px-Electron_Software_Framework_Logo.svg.png" alt="electron logo" width="150"/></td>
    <td><img src="https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png" alt="python logo" width="150"/></td>
    </tr>
</table>

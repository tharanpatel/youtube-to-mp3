# Prerequisites

- Firefox browser while you are logged into your youtube account

## Installation

### Install Chocolatey
- Run ```Get-ExecutionPolicy```. If it returns ```Restricted```, then run ```Set-ExecutionPolicy AllSigned``` or ```Set-ExecutionPolicy Bypass -Scope Process```
- Now run ```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

### Install yt-dlp using Chocolatey
- Install yt-dlp and ffmpeg using ```choco install ffmpeg yt-dlp```
- Verify installation using ```yt-dlp --version```

### Install python dependencies
- ```pip install requests python-dotenv```

# Setup

There are a few enviroment variables that need to be changed for the program to function.

## Populate environment folder
- Create a ```.env``` file in  the ```backend``` folder and populate it with the following:
```
DISCORD_TOKEN="YOUR DISCORD TOKEN HERE"
DISCORD_CHANNEL_URL="YOUR DISCORD CHANNEL URL HERE"
```

### How to get your discord token
- Log into discord on the web browser
- Enter developer tools
- Navigate to ```Application -> Local Storage -> Discord.com -> Filter -> type 'token' -> use the corresponding value```

### How to get your discord channel url
- Log into discord on the web browser
- Enter developer tools
- Navigate to Network section
- Send a message on the web browser to the server
- Find the corresponding POST request and use the URL used for the POST request.

# Done! :smile:
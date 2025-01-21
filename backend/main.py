import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_URL=os.getenv("DISCORD_CHANNEL_URL")

def download_mp3():
    try:
        url = sys.argv[1]
        os.system(
            f'yt-dlp -x --audio-format mp3 --cookies-from-browser firefox "{url}"'
        )
    except:
        print("\033[31mFile download failed.\033[0m")

def remove_file(file_name:str):
    try:
        os.remove(file_name)
    except:
        print("\033[31mFile does not exist.\033[0m")

def main():
    download_mp3()
    try:
        mp3_file_name = [f for f in os.listdir(".") if f.endswith(".mp3")]
        headers = {"Authorization": DISCORD_TOKEN}
        mp3_file = {
            "file": open(
                mp3_file_name[0],
                "rb",
            )
        }
        res = requests.post(url=DISCORD_CHANNEL_URL, files=mp3_file, headers=headers)
        mp3_file["file"].close()
        remove_file(file_name=mp3_file_name[0])
        print("\033[32mSuccess!\033[0m")  # colours terminal output green
    except:
        print(res.json())
        print("\033[31mDiscord upload failed.\033[0m")

main()

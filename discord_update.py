import requests
import tarfile
import subprocess
import os

def download_discord(fileName: str) -> None:
    print("Downloading file...")
    downloadFile = requests.get("https://discord.com/api/download/canary?platform=linux&format=tar.gz")

    with open(f"{fileName}.tar.gz", "wb") as file:
        file.write(downloadFile.content)

        print("File downloaded.  Unzipping...")
        with tarfile.open(f"{fileName}.tar.gz", "r:gz") as tar:
            tar.extractall(filter="tar")

        os.remove(f"{fileName}.tar.gz")
        print("File unzipped.")

def run_discord() -> None:
    print("Running Discord...")
    subprocess.run(["./DiscordCanary/discord-canary"],shell=True)
    print("Done.")



if __name__ == "__main__":

    try:
        currentDir = os.path.dirname(os.path.abspath(__file__))
        print(f"Using {currentDir}")
        os.chdir(currentDir)

        download_discord("discord_update_file")
        run_discord()
    except Exception as e:
        print(f"An Error occurred while downloading/unzipping: {e}")

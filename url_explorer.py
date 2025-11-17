import requests

def explore_repo():
    url = f"https://api.github.com/repos/MohamedCS1/S1/contents"
    response = requests.get(url).json()

    for item in response:
        if item["type"] == "dir":
            print("📁 Folder:", item["path"])
        else:
            print("📄 File:", item["download_url"])
            

# Example
explore_repo()
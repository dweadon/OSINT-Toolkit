import httpx

asc = r"""  /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$       /$$$$$$$$                  /$$ /$$       /$$   /$$    
 /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/      |__  $$__/                 | $$| $$      |__/  | $$    
| $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$            | $$  /$$$$$$   /$$$$$$ | $$| $$   /$$ /$$ /$$$$$$  
| $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$            | $$ /$$__  $$ /$$__  $$| $$| $$  /$$/| $$|_  $$_/  
| $$  | $$ \____  $$  | $$  | $$  $$$$   | $$            | $$| $$  \ $$| $$  \ $$| $$| $$$$$$/ | $$  | $$    
| $$  | $$ /$$  \ $$  | $$  | $$\  $$$   | $$            | $$| $$  | $$| $$  | $$| $$| $$_  $$ | $$  | $$ /$$
|  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$   | $$            | $$|  $$$$$$/|  $$$$$$/| $$| $$ \  $$| $$  |  $$$$/
 \______/  \______/ |______/|__/  \__/   |__/            |__/ \______/  \______/ |__/|__/  \__/|__/   \___/  
                                                                                                             """
print(asc)

print("An OSINT toolkit designed to gather and analyze publicly available information from multiple online sources.\nThe project focuses on username enumeration, domain intelligence, metadata collection\nand automated investigation workflows using Python and asynchronous networking.")

BASE_HEADERS = {
    "User-Agent": "osint-toolkit-v1"
}

def check_github(username: str, client: httpx.Client):
    url = f"https://api.github.com/users/{username}"

    try:
        response = client.get(url, headers=BASE_HEADERS)

        if response.status_code == 200:
            print(f"[#] GitHub user FOUND: https://github.com/{username}")

            repos_url = f"https://api.github.com/users/{username}/repos"
            repos = client.get(repos_url, headers=BASE_HEADERS).json()

            print(f"[#] Public repos: {len(repos)}")

            for repo in repos:
                print(f"{repo['name']}\n")

        elif response.status_code == 404:
            print("[#] GitHub user NOT found")

        else:
            print(f"[#] GitHub API error: {response.status_code}")

    except httpx.RequestError as e:
        print(f"[#] Request error: {e}")

def check_instagram(username: str, client: httpx.Client):
    url = f"https://www.instagram.com/{username}/"
    try:
        response = client.get(url, headers=BASE_HEADERS)
        if response.status_code == 200:
            print(f"[#] Instagram: user possibly exists (200 OK): https://www.instagram.com/{username}")
        elif response.status_code == 404:
            print("[!]Instagram: user does not exists (404 NOT FOUND)")
        elif response.status_code == 403 or response.status_code == 429:
            print("[!] Instagram: BLOCKED / RATE LIMITED(403,429)")
        else:
            print("[!] Instagram: UNKNOW ERROR, TRY AGAIN")
    except httpx.RequestError as e:
        print(f"[!] Request error: {e}")

def check_tiktok(username: str, client: httpx.Client):
    url = f"https://www.tiktok.com/@{username}/"


    try:

        response = client.get(url, headers=BASE_HEADERS)
        if response.status_code == 200:
            print(f"[#] TikTok: user possibly exists (200 OK): https://www.tiktok.com/@{username}")
        elif response.status_code == 404:
            print("[!]TikTok: user does not exists (404 NOT FOUND/FORBIDDEN)")
        else:
            print("[!] TikTok: UNKNOW ERROR, TRY AGAIN")
    except httpx.RequestError as e:
        print(f"[!] Request error: {e}")
def check_x(username: str, client: httpx.Client):
    url = f"https://x.com/{username}"
    try:
        response = client.get(url, headers=BASE_HEADERS)
        if response.status_code == 200:
            print(f"[#] X: user possibly exists (200 OK): https://x.com/{username}")
        elif response.status_code == 404:
            print("[!]X: user does not exists (404 NOT FOUND)")
        elif response.status_code == 403 or response.status_code == 429:
            print("[!]X: BLOCKED / RATE LIMITED(403,429)")
        else:
            print("[!]X: UNKNOW ERROR, TRY AGAIN")
    except httpx.RequestError as e:
        print(f"[!] Request error: {e}")
def check_youtube(username: str, client: httpx.Client):
    url = f"https://www.youtube.com/@{username}"
    try:
        response = client.get(url, headers=BASE_HEADERS)
        if response.status_code == 200:
            print(f"[#] Youtube: user possibly exists (200 OK): https://www.youtube.com/@{username}")
        elif response.status_code == 404:
            print("[!] Youtube: user does not exists (404 NOT FOUND)")
        elif response.status_code == 403 or response.status_code == 429:
            print("[!] Youtube: BLOCKED / RATE LIMITED(403,429)")
        else:
            print("[!] Youtube: UNKNOW ERROR, TRY AGAIN")
    except httpx.RequestError as e:
        print(f"[!] Request error: {e}")
def check_pinterest(username: str, client: httpx.Client):
    url = f"https://www.pinterest.com/{username}"
    try:
        response = client.get(url, headers=BASE_HEADERS)
        if response.status_code == 200:
            print(f"[#] Pinterest: user possibly exists (200 OK): https://www.pinterest.com/{username}")
        elif response.status_code == 404:
            print("[!] Pinterest: user does not exists (404 NOT FOUND)")
        elif response.status_code == 403 or response.status_code == 429:
            print("[!] Pinterest: BLOCKED / RATE LIMITED(403,429)")
        else:
            print("[!] Pinterest: UNKNOW ERROR, TRY AGAIN")
    except httpx.RequestError as e:
        print(f"[!] Request error: {e}")

def run_scan(username: str):
    with httpx.Client(follow_redirects=True, timeout=10) as client:
        print("\n[#] Starting OSINT scan...\n")

        check_github(username, client)
        check_instagram(username, client)
        check_tiktok(username, client)
        check_x(username, client)
        check_youtube(username, client)
        check_pinterest(username, client)

        print("\n[#] Scan completed.")


if __name__ == "__main__":
    user = input("Enter username: ")
    run_scan(user)
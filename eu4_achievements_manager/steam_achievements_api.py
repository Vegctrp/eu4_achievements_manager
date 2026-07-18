import os
import requests

def get_steam_achievements() -> list[dict]:
    API_KEY = os.getenv("STEAM_API_KEY")
    STEAM_ID = os.getenv("STEAM_ID")
    APP_ID = 236850  # Europa Universalis IV

    url = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/"

    params = {
        "key": API_KEY,
        "steamid": STEAM_ID,
        "appid": APP_ID,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    achievements = data["playerstats"]["achievements"]

    return achievements


if __name__ == "__main__":
    achievements = get_steam_achievements()
    for achievement in achievements:
        print(f"{achievement['apiname']}: {achievement['achieved']}")
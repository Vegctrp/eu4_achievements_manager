import os
import requests

def get_steam_achievements() -> list[dict]:
    """
    Fetches the achievements for a given Steam user and game.

    Returns:
        A list of dictionaries, each representing an achievement with its details.

        for example:
        [
            {
                "apiname": "ACHIEVEMENT_1",
                "achieved": 1,
                "unlocktime": 1620000000
            },
            {
                "apiname": "ACHIEVEMENT_2",
                "achieved": 0,
                "unlocktime": 0
            },
            ...
        ]

    Raises:
        requests.exceptions.RequestException: If the HTTP request to the Steam API fails.
    """
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
    print(achievements)
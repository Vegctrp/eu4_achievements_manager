import os
import requests

def get_eu4_achievements_schema() -> list[dict]:
    """
    Fetches the achievements schema for Europa Universalis IV from the Steam API.

    Returns:
        A list of dictionaries, each representing an achievement with its details.

        for example:
        [
            {
                "name": "ACHIEVEMENT_1",
                "defaultvalue": 0,
                "displayName": "Achievement 1",
                "hidden": 0,
                "description": "Description of Achievement 1",
                "icon": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/icons/achievements/ACHIEVEMENT_1.jpg",
                "icongray": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/icons/achievements/ACHIEVEMENT_1_gray.jpg"
            },
            ...
        ]
    """

    API_KEY = os.getenv("STEAM_API_KEY")
    APP_ID = 236850

    url = "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"

    params = {
        "key": API_KEY,
        "appid": APP_ID,
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    data = r.json()
    achievements_schema = data["game"]["availableGameStats"]["achievements"]

    return achievements_schema


if __name__ == "__main__":
    schema = get_eu4_achievements_schema()
    print(schema)
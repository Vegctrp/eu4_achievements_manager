from eu4_achievements_manager.steam_achievements_api import get_steam_achievements
from eu4_achievements_manager.steam_schema_api import get_eu4_achievements_schema

def get_achievements_info_from_steam() -> dict:
    """
    Fetches the achievements information from the Steam API for Europa Universalis IV.

    Returns:
        A dictionary of achievements, each representing an achievement with its details.

        for example:
        {
            "Achievement 1": {
                "apiname": "ACHIEVEMENT_1",
                "achieved": 1,
                "unlocktime": 1620000000,
                "description": "Description of Achievement 1",
            },
            ...
        }
    """

    achievements_schema = get_eu4_achievements_schema()
    steam_achievements = get_steam_achievements()

    achievements_info = {}
    for schema in achievements_schema:
        apiname = schema["name"]
        display_name = schema["displayName"]
        description = schema["description"]

        # Find the corresponding achievement in the user's achievements
        user_achievement = next((a for a in steam_achievements if a["apiname"] == apiname), None)

        if user_achievement:
            achieved = user_achievement["achieved"]
            unlocktime = user_achievement["unlocktime"]
        else:
            achieved = 0
            unlocktime = 0

        achievements_info[display_name] = {
            "apiname": apiname,
            "achieved": achieved,
            "unlocktime": unlocktime,
            "description": description,
        }

    return achievements_info


if __name__ == "__main__":
    achievements_info = get_achievements_info_from_steam()
    for name, info in achievements_info.items():
        print(f"{name}: {info}")
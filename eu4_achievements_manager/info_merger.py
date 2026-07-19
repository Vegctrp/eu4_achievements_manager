

def merge_achievements_info(wiki_achievements_info, steam_achievements_info):
    for achievement in wiki_achievements_info:
        title = achievement["title"]
        achievement_info = steam_achievements_info.get(title)
        if achievement_info:
            achievement["achieved"] = achievement_info["achieved"]
            achievement["unlocktime"] = achievement_info["unlocktime"]
        else:
            achievement["achieved"] = 0
            achievement["unlocktime"] = 0
    return wiki_achievements_info


if __name__ == "__main__":
    from bs4 import BeautifulSoup

    from eu4_achievements_manager.get_achievements_info_from_steam import get_achievements_info_from_steam
    from eu4_achievements_manager.get_eu4_wiki import load_eu4_wiki_html
    from eu4_achievements_manager.eu4_wiki_parser import parse_wiki_achievement_table

    html = load_eu4_wiki_html()
    wiki_achievements = parse_wiki_achievement_table(html)
    achievements_info = get_achievements_info_from_steam()

    merged_achievements = merge_achievements_info(wiki_achievements, achievements_info)
    print(merged_achievements[:5])
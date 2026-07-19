
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def render_achievements_info(merged_achievements):
    for achievement in merged_achievements:
        if achievement.get("achieved"):
            achievement["unlock_time_str"] = datetime.fromtimestamp(
                achievement["unlocktime"]
            ).strftime("%Y-%m-%d")
        else:
            achievement["unlock_time_str"] = "-"

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=False,
    )

    template = env.get_template("data/template.html")

    html = template.render(
        achievements=merged_achievements,
    )

    with open("data/output.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    from bs4 import BeautifulSoup

    from eu4_achievements_manager.get_achievements_info_from_steam import get_achievements_info_from_steam
    from eu4_achievements_manager.get_eu4_wiki import load_eu4_wiki_html
    from eu4_achievements_manager.eu4_wiki_parser import parse_wiki_achievement_table
    from eu4_achievements_manager.info_merger import merge_achievements_info

    html = load_eu4_wiki_html()
    wiki_achievements = parse_wiki_achievement_table(html)
    achievements_info = get_achievements_info_from_steam()

    merged_achievements = merge_achievements_info(wiki_achievements, achievements_info)
    render_achievements_info(merged_achievements)
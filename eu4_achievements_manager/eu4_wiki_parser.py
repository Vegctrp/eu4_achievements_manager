from bs4 import BeautifulSoup


def parse_achievement_table(table):
    achievements = []

    rows = table.find_all("tr")[1:]

    for row in rows:
        cols = row.find_all("td")

        if len(cols) != 7:
            continue

        achievement_html = cols[0].decode_contents()
        starting_condition_html = cols[1].decode_contents()
        requirements_html = cols[2].decode_contents()
        notes_html = cols[3].decode_contents()
        dlc_html = cols[4].decode_contents()
        version = cols[5].get_text(strip=True)
        difficulty = cols[6].get_text(strip=True)

        achievements.append(
            {
                "achievement_html": achievement_html,
                "starting_condition_html": starting_condition_html,
                "requirements_html": requirements_html,
                "notes_html": notes_html,
                "dlc_html": dlc_html,
                "version": version,
                "difficulty": difficulty,
            }
        )

    return achievements


if __name__ == "__main__":
    from eu4_achievements_manager.get_eu4_wiki import load_eu4_wiki_html

    html = load_eu4_wiki_html()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    achievements = parse_achievement_table(table)

    for achievement in achievements:
        print(achievement)
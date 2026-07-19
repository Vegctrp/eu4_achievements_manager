from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_wiki_achievement_table(html_raw_text):
    soup = BeautifulSoup(html_raw_text, "html.parser")
    BASE_URL = "https://eu4.paradoxwikis.com"

    # img
    for img in soup.find_all("img"):
        if img.has_attr("src"):
            img["src"] = urljoin(BASE_URL, img["src"])

    # a
    for a in soup.find_all("a"):
        if a.has_attr("href"):
            a["href"] = urljoin(BASE_URL, a["href"])

    table = soup.find("table")
    achievements = []

    rows = table.find_all("tr")[1:]

    for row in rows:
        cols = row.find_all("td")

        if len(cols) != 7:
            continue

        achievement_col = cols[0]
        title_div = achievement_col.select_one(
            "div[style*='font-weight']"
        )
        title = title_div.get_text(" ", strip=True)

        achievement_html = cols[0].decode_contents()
        starting_condition_html = cols[1].decode_contents()
        requirements_html = cols[2].decode_contents()
        notes_html = cols[3].decode_contents()
        dlc_html = cols[4].decode_contents()
        version = cols[5].get_text(strip=True)
        difficulty = cols[6].get_text(strip=True)

        achievements.append(
            {
                "title": title,
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
    achievements = parse_wiki_achievement_table(html)

    for achievement in achievements:
        print(achievement)
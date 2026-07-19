import cloudscraper
from pathlib import Path

def load_eu4_wiki_html() -> str:
    eu4_wiki_url = "https://eu4.paradoxwikis.com/Achievements"
    html_path = Path(__file__).resolve().parent.parent / "data" / "wiki_achievements.html"
    
    if html_path.exists():
        return html_path.read_text(encoding="utf-8")

    html_path.parent.mkdir(parents=True, exist_ok=True)
    scraper = cloudscraper.create_scraper()
    response = scraper.get(eu4_wiki_url)
    response.raise_for_status()
    html_path.write_text(response.text, encoding="utf-8")
    return response.text
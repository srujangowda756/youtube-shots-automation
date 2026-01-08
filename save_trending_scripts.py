import os
import requests
from datetime import datetime, timedelta

# ---------- GitHub Trending ----------
def fetch_github_trends():
    date_from = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    url = (
        f"https://api.github.com/search/repositories"
        f"?q=created:>{date_from}&sort=stars&order=desc&per_page=3"
    )
    response = requests.get(url)
    data = response.json()

    trends = []
    for repo in data.get("items", []):
        trends.append({
            "source": "GitHub",
            "hook": "This open-source project is trending fast.",
            "insight": f"{repo['name']} gained {repo['stargazers_count']} stars. {repo['description']}",
            "cta": "Follow for daily tech trends."
        })
    return trends


# ---------- Hacker News ----------
def fetch_hackernews_trends():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_ids = requests.get(top_stories_url).json()[:3]

    trends = []
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()
        if story and "title" in story and len(story["title"]) > 30:
            trends.append({
                "source": "Hacker News",
                "hook": "This tech story is getting massive attention.",
                "insight": story["title"],
                "cta": "Follow for daily tech trends."
            })
    return trends


# ---------- SAVE SCRIPTS ----------
def save_scripts(trends):
    today = datetime.now().strftime("%Y-%m-%d")
    base_dir = os.path.join("shorts_output", today)
    os.makedirs(base_dir, exist_ok=True)

    for i, trend in enumerate(trends, start=1):
        short_dir = os.path.join(base_dir, f"short_{i}")
        os.makedirs(short_dir, exist_ok=True)

        script_path = os.path.join(short_dir, "script.txt")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(f"SOURCE: {trend['source']}\n")
            f.write(f"HOOK: {trend['hook']}\n")
            f.write(f"INSIGHT: {trend['insight']}\n")
            f.write(f"CTA: {trend['cta']}\n")

    print(f"{len(trends)} scripts saved in {base_dir}")


# ---------- MAIN ----------
def main():
    trends = fetch_github_trends() + fetch_hackernews_trends()
    save_scripts(trends)


if __name__ == "__main__":
    main()

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
            "hook": f"This open-source project is trending fast.",
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
        if story and "title" in story:
            trends.append({
                "source": "Hacker News",
                "hook": "This tech story is getting massive attention.",
                "insight": story["title"],
                "cta": "Follow for daily tech trends."
            })
    return trends


# ---------- MAIN ----------
def generate_shorts_content():
    all_trends = fetch_github_trends() + fetch_hackernews_trends()

    for trend in all_trends:
        print(f"SOURCE: {trend['source']}")
        print(f"HOOK: {trend['hook']}")
        print(f"INSIGHT: {trend['insight']}")
        print(f"CTA: {trend['cta']}")
        print("-" * 40)


if __name__ == "__main__":
    generate_shorts_content()

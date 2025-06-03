import os
from news_fetcher import fetch_headlines
from commentary_generator import generate_commentary
from twitter_poster import post_to_twitter

OUTPUT_DIR = "outputs"

def run_agent():
    print("🧠 YY is scanning world events...\n")

    headlines = fetch_headlines()
    print(f"✅ Headlines fetched: {len(headlines)}\n")

    if not headlines:
        print("⚠️ No news fetched.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for i, (headline, url) in enumerate(headlines):
        print(f"📰 [{i+1}] {headline}")
        print(f"🔗 {url}")

        commentary = generate_commentary(headline, url)

        if commentary:
            # ✅ Strip quotes
            cleaned = commentary.strip().strip('"')

            print(f"\n🗣️ Binglish Commentary (Tweet):\n{cleaned}")
            print("—" * 60)

            # ✅ Post to Twitter
            post_to_twitter(cleaned)

            # ✅ Save to file
            filename = f"{OUTPUT_DIR}/yy_commentary_{i+1}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Headline: {headline}\nURL: {url}\n\nCommentary:\n{cleaned}")
        else:
            print("⚠️ Could not generate commentary.\n")

if __name__ == "__main__":
    run_agent()


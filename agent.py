from tools import (
    search_news,
    summarize_articles,
    generate_newsletter,
    save_newsletter
)


class NewsletterAgent:

    def __init__(self):
        pass

    # MAIN AGENT FUNCTION
    def run_newsletter_agent(self, goal):

        logs = []

        # STEP 1
        logs.append("🧠 Planning workflow...")

        steps = [
            "Research latest news",
            "Summarize articles",
            "Generate newsletter",
            "Save newsletter"
        ]

        for step in steps:
            logs.append(f"✅ {step}")

        # STEP 2
        logs.append("🔎 Researching news articles...")

        articles = search_news(goal)

        logs.append(f"📄 Found {len(articles)} articles")

        # STEP 3
        logs.append("✍️ Summarizing articles...")

        summary = summarize_articles(articles)

        # RETURN SUMMARY FIRST FOR HUMAN APPROVAL
        return {
            "summary": summary,
            "logs": logs,
            "articles": articles
        }

    # FINAL GENERATION AFTER APPROVAL
    def generate_final_newsletter(self, summary, goal):

        logs = []

        logs.append("📰 Generating newsletter...")

        newsletter = generate_newsletter(
            summary,
            goal
        )

        logs.append("💾 Saving newsletter...")

        save_newsletter(newsletter)

        logs.append("✅ Process Completed Successfully!")

        return {
            "newsletter": newsletter,
            "logs": logs
        }
from tavily import TavilyClient
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import os

load_dotenv()

# LOCAL LLM
llm = Ollama(model="phi3")

# TAVILY CLIENT
tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


# SEARCH TOOL
def search_news(goal):

    response = tavily.search(
        query=goal,
        max_results=3
    )

    return response["results"]


# SUMMARIZER TOOL
def summarize_articles(articles):

    combined_text = ""

    for article in articles:

        combined_text += f"""
        TITLE:
        {article['title']}
        """

    prompt = f"""
    You are an AI Newsletter Writer.

    Create a SHORT professional newsletter.

    STRICT RULES:
    - Maximum 200 words
    - Use plain readable text only.
Do not use markdown symbols like ** or ##.
    - ONLY summarize provided article titles
    - DO NOT invent fake information
    - DO NOT generate academic reports
    - DO NOT mention instructions
    - DO NOT add extra explanations
    - DO Provide Headings in bold and a proper newsletter format like take examples from news sites.

    OUTPUT FORMAT:

    Weekly AI Newsletter

    1. **Headline(from article title)**
    - short insight-provide links to original articles if possible

    2. **Headline(from article title)**
    - short insight-provide links to original articles if possible

    3. **Headline(from article title)**
    - short insight-provide links to original articles if possible

    Final Takeaway:
    - 2 sentence conclusion

    ARTICLES:
    {combined_text}
    """

    response = llm.invoke(prompt)

    return response
# NEWSLETTER GENERATOR
def generate_newsletter(summary, goal):

    html_content = f"""
    <html>

    <head>

    <style>

    body {{
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 40px;
    }}

    .container {{
        background: white;
        max-width: 1000px;
        margin: auto;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }}

    h1 {{
        color: #222;
    }}

    h2 {{
        color: #444;
    }}

    p {{
        font-size: 18px;
        line-height: 1.8;
        color: #555;
        white-space: pre-line;
    }}

    </style>

    </head>

    <body>

    <div class="container">

    <h1>AI Newsletter Agent</h1>

    <h2>{goal}</h2>

    <hr>

    <p>
    {summary}
    </p>

    </div>

    </body>

    </html>
    """

    return html_content
# SAVE TOOL
def save_newsletter(newsletter):

    os.makedirs("output", exist_ok=True)

    with open(
        "output/latest_newsletter.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(newsletter)

    print("Newsletter saved successfully!")
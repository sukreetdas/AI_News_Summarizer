from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self,llm):
        """
        Initialize the AINewsNode with API keys for Tavily and GROQ.
        """
        self.tavily = TavilyClient()
        self.llm = llm
        # this is used to capture various steps in this file so that later can be use for steps shown
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the specified frequency.
        
        Args:
            state (dict): The state dictionary containing 'frequency'.
        
        Returns:
            dict: Updated state with 'news_data' key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'year': 'y'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'year': 366}

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days=days_map[frequency],
            # include_domains=["techcrunch.com", "venturebeat.com/ai", ...]  # Uncomment and add domains if needed
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        print("=" * 60)
        print("Fetched News:")
        for item in state["news_data"]:
            print("Published Date:", item.get("published_date"))
            print("Title:", item.get("title"))
            print("URL:", item.get("url"))
            print("-" * 40)
        print("=" * 60)
        return state
    
    def summarize_news(self, state: dict) -> dict:
         
        news_items = self.state["news_data"]
        articles = []
        for item in news_items:
            date = item.get("published_date", "")
            # Keep only YYYY-MM-DD
            if date:
                date = date[:10]
            else:
                date = "Unknown Date"
            articles.append( f"""
    Publication Date: {date}
    Title: {item.get('title','')}
    Content: {item.get('content','')}
    Source: {item.get('url','')}
    """          
            )

        articles_str = "\n".join(articles)
        prompt = ChatPromptTemplate.from_messages([
        (
             "system",
            """
    You are an AI News Summarizer.
     
    IMPORTANT RULES:

    1. NEVER change the publication date.
    2. Copy the publication date EXACTLY as provided in the input.
    3. NEVER infer dates from the article content.
    4. NEVER change the month or year.
    5. If the input says 2026-06-26, output exactly 2026-06-26.
    6. Group articles by the given publication date.
    7. Sort by latest publication date.
    Format:

    ## YYYY-MM-DD

    - Summary
    Source: URL
    """
        ),
        ("user", "{articles}")
    ])

 
        response = self.llm.invoke(
        prompt.format(articles=articles_str))

        self.state["summary"] = response.content

        return self.state 
        
    def save_result(self,state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename'] = filename
        return self.state
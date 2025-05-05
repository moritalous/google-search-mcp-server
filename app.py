import json

import gradio as gr
from dotenv import load_dotenv
from langchain_google_community import GoogleSearchAPIWrapper

load_dotenv()


def perform_web_search(query: str, num_results: int = 10):
    """
    Performs a web search using the Google Search API, ideal for general queries, news, articles, and online content.
    Use this for broad information gathering, recent events, or when you need diverse web sources.
    Maximum 20 results per request, with offset for pagination.

    Args:
        query (str): Search query (max 400 chars, 50 words)
        num_results (int): Number of results (1-20, default 10)

    Returns:
        str: Search results
    """

    search = GoogleSearchAPIWrapper()

    return json.dumps(
        search.results(query=query, num_results=num_results),
        indent=2,
        ensure_ascii=False,
    )


demo = gr.Interface(
    fn=perform_web_search, inputs=[gr.Text(), gr.Number(value=10)], outputs=gr.Textbox()
)

if __name__ == "__main__":
    demo.launch(mcp_server=True)

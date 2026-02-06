import json

import requests

from app.core.config import settings


class News:

    def __init__(self, ticker: str, engine: str = "google", time_period: str = "last_month"):
        self.ticker = ticker
        self.engine = engine
        self.time_period = time_period,
        self.url = "https://www.searchapi.io/api/v1/search"
        self.organic_results = self._get_news()

    def _get_news(self) -> list[dict]:
        params = {
            "engine": self.engine,
            "q": f"opinions about {self.ticker} stock",
            "api_key": settings.SEARCH_API_KEY,
            "time_period": self.time_period
        }

        response = requests.get(self.url, params=params)
        return json.loads(response.text).get('organic_results', [])


    def get_text_summary(self) -> str:
        NEWS_INFORMATION = ""

        for result in self.organic_results:
            position = result.get("position", -1)
            title = result.get("title", "Sem título")
            link_news = result.get("link", "Sem link")
            snippet = result.get("snippet", "Sem snippet")
            
            NEWS_INFORMATION += f"""
            Posição nas buscas orgânicas: {position}
            Título: {title}
            Snippet: {snippet}
            Link da notícia: {link_news}
            """

        NEWS_INFORMATION += "\nSe position == -1, significa que não foi encontrada a posição da notícia"
        return NEWS_INFORMATION

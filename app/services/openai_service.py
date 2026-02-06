from datetime import datetime, timedelta, timezone

from langchain_core.messages import BaseMessage, SystemMessage
from langchain_openai import ChatOpenAI

from app.ai.prompts.human_prompt import HUMAN_PROMPT
from app.ai.prompts.system_prompt import SYSTEM_PROMPT
from app.ai.structured_outputs.ai_response import AIResponse
from app.core.config import settings
from app.services.finance import Finance
from app.services.news import News

data_hoje_utc = datetime.now(timezone.utc)
data_hoje = (data_hoje_utc - timedelta(hours=3)).strftime("%d/%m/%Y %H:%M:%S")

class OpenAIService:

    def __init__(self, model: str = "gpt-5.1", temperature: float = 0.2):
        self.model = ChatOpenAI(model=model, temperature=temperature, api_key=settings.OPENAI_API_KEY).with_structured_output(AIResponse)
        self.temperature = temperature


    def build_system_prompt(self, ticker: str, period: str, interval: str) -> BaseMessage:
        SYSTEM_PROMPT_FINAL = SYSTEM_PROMPT.replace('{INTERVAL}', interval)\
                                           .replace('{TICKER}', ticker)\
                                           .replace('{PERIOD}', period)\
                                           .replace('{data_hoje}', data_hoje)

        return SystemMessage(content=SYSTEM_PROMPT_FINAL)

    def build_human_prompt(self, ticker: str, period: str, interval: str) -> BaseMessage:
        finance = Finance(ticker, period, interval)
        stock_statistics = finance.get_text_summary()
        news = News(ticker)
        news_info = news.get_text_summary()
        HUMAN_PROMPT_FINAL = HUMAN_PROMPT.replace('{TICKER}', ticker)\
                                         .replace('{STOCK_STATISTICS_STRING}', stock_statistics)\
                                         .replace('{NEWS_INFORMATION}', news_info)
        return SystemMessage(content=HUMAN_PROMPT_FINAL)

    def get_response(self, ticker: str, period: str, interval: str) -> AIResponse:
        messages = [
            self.build_system_prompt(ticker, period, interval),
            self.build_human_prompt(ticker, period, interval)
        ]

        response = self.model.invoke(messages)
        return response

from typing import Any

from fastapi import APIRouter

from app.services.openai_service import OpenAIService
from app.ai.structured_outputs.ai_response import AIResponse

stock_router = APIRouter(prefix="/v1/stock")

openai_service = OpenAIService()

@stock_router.post("/analyze", response_model=dict[str, Any])
def stock_analyze(ticker: str, period: str, interval: str):
    response = openai_service.get_response(ticker, period, interval)
    return response.model_dump()

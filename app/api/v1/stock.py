from typing import Any

from fastapi import APIRouter

from app.services.openai_service import OpenAIService
from app.ai.structured_outputs.ai_response import AIResponse

from app.schemas.stock import Stock, AnalyzedResponse

stock_router = APIRouter(prefix="/v1/stock")

openai_service = OpenAIService()

@stock_router.post("/analyze", response_model=AnalyzedResponse)
def stock_analyze(stock: Stock):
    response = openai_service.get_response(stock.ticker, stock.period, stock.interval)
    return {
        "ticker": response.ticker,
        "reasoning": response.reasoning,
        "action": response.action,
        "confidence": response.confidence,
        "risks": response.risks,
        "opportunitties": response.opportunities
    }

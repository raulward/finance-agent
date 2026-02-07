from pydantic import BaseModel
from typing import Literal, List


class Stock(BaseModel):
    ticker: str
    period: str = "1y"
    interval: str = "1d"

class AnalyzedResponse(BaseModel):
    ticker: str
    reasoning: str
    action: Literal["BUY", "HOLD", "SELL"]
    confidence: float
    risks: List[str]
    opportunitties: List[str]
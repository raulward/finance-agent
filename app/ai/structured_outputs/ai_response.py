from typing import List, Literal

from pydantic import BaseModel, Field


class AIResponse(BaseModel):
    cot: str = Field(description="cadeia de pensamento interna")
    ticker: str = Field(description="Ticker analisado (por exemplo: AAPL, AMZN, NVDA...)")
    action: Literal["BUY", "SELL", "HOLD"] = Field(description="Ação a ser tomada: BUY, HOLD ou SELL")
    confidence: float = Field(le=1, ge=0, description="Confiança na resposta: entre 0 e 1")
    reasoning: str = Field(description="explicação para o usuário como especilista técnico em finanças do porque a ação deve ser tomada")
    risks: List[str] = Field(description="lista de strings com todos os riscos associados a essa ação a ser tomada (forneça link das referências)")
    opportunities: List[str] = Field(description="Lista de strings com todas as oportunidades associadas a ação a ser tomada")

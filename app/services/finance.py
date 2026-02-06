import json

import yfinance as yf


class Finance:

    def __init__(self, ticker: str, period: str = "1y", interval: str = "1d"):
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.ticker_object = yf.Ticker(ticker=ticker)

    def _get_historic(self):
        return self.ticker_object.history(period=self.period, interval=self.interval)

    def calc_statistics(self) -> dict:
        df = self._get_historic()

        if df.empty:
            return {
                "error": f"ticker {self.ticker} not found."
            }

        df['Return'] = df['Close'].pct_change()
        df['Diff'] = df['Close'].diff()

        avg_return = df['Return'].mean()
        median_return = df['Return'].median()
        volatility = df['Return'].std()
        max_return = df['Return'].max()
        max_price = df['Close'].max()
        min_return = df['Return'].min()
        min_price = df['Close'].min()
        cumulative_return = df['Close'].iloc[-1]/df['Close'].iloc[0] - 1
        current_price = df['Close'].iloc[-1]
        delta = df['Diff']
        gains = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        losses = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = (gains/losses)
        rsi = 100 - (100 / (1 + rs.iloc[-1]))

        return {
            "ticker": self.ticker,
            "period": self.period,

            "avg_daily_return": float(avg_return),
            "median_daily_return": float(median_return),
            "volatility": float(volatility),

            "max_return": float(max_return),
            "min_return": float(min_return),

            "max_price": float(max_price),
            "min_price": float(min_price),

            "cumulative_return": float(cumulative_return),
            "current_price": float(current_price),

            "rsi_14": float(rsi)
    }

    def get_text_summary(self) -> str:
        return json.dumps(self.calc_statistics(), indent=4)

finance = Finance("AAPL")

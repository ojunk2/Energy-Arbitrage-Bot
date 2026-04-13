class DynamicTrader:
    def __init__(self, window_size=24, buy_percentile=0.8, sell_percentile=1.2):
        """
        window_size: How many hours of history to look at (default 24).
        buy_percentile: Buy if price is below 80% of the moving average.
        sell_percentile: Sell if price is above 120% of the moving average.
        """
        self.history = []
        self.window_size = window_size
        self.buy_percentile = buy_percentile
        self.sell_percentile = sell_percentile

    def decide(self, current_price, soc, capacity):
        # 1. Update the price history window
        self.history.append(current_price)
        if len(self.history) > self.window_size:
            self.history.pop(0)
        
        # 2. Need at least a few hours of data before making smart moves
        if len(self.history) < 5:
            return 'hold', 0

        # 3. Calculate the Moving Average
        moving_avg = sum(self.history) / len(self.history)
        
        # 4. Logic: Buy low (relative to average), Sell high (relative to average)
        if current_price < (moving_avg * self.buy_percentile) and soc < capacity:
            return 'buy', capacity - soc
        elif current_price > (moving_avg * self.sell_percentile) and soc > 0:
            return 'sell', soc
        else:
            return 'hold', 0
import pandas as pd
from src.battery import Battery
from src.engine import DynamicTrader
import matplotlib.pyplot as plt

# 1. LOAD DATA
df = pd.read_csv('data/cleaned_illinois_summer.csv')
prices = df['Price'].tolist()

# 2. INITIALIZATION
# Change max_power_kw from 20 to 40
battery = Battery(capacity_kwh=100, max_power_kw=40, efficiency=0.9)

# Keep the same 10% thresholds we used to get $74.24
trader = DynamicTrader(window_size=24, buy_percentile=0.9, sell_percentile=1.1)

total_profit = 0
price_history = []
buy_points = []
sell_points = []

# 3. THE LONG-TERM LOOP (WITH RECORDING)
print(f"Starting Simulation with {len(prices)} hours of Illinois data...")

for i, price in enumerate(prices):
    price_per_kwh = price / 1000 
    
    action, amount = trader.decide(price_per_kwh, battery.current_soc, battery.capacity)
    
    # Save every price point for the background line
    price_history.append(price_per_kwh)
    
    if action == 'buy':
        drawn_from_grid = battery.charge(amount)
        total_profit -= (drawn_from_grid * price_per_kwh)
        buy_points.append((i, price_per_kwh)) # Save (hour, price) for green dots
        
    elif action == 'sell':
        pushed_to_grid = battery.discharge(amount)
        total_profit += (pushed_to_grid * price_per_kwh)
        sell_points.append((i, price_per_kwh)) # Save (hour, price) for red dots

print(f"FINAL PROFIT: ${total_profit:.2f}")

# 4. THE GRAPHING PART
plt.figure(figsize=(15, 7))

# Plot the price line
plt.plot(price_history, label='Illinois Hub Price ($/kWh)', color='lightgray', linewidth=1, alpha=0.7)

# Overlay Buy/Sell markers
if buy_points:
    plt.scatter(*zip(*buy_points), color='forestgreen', label='Buy Signal', s=15, zorder=5)
if sell_points:
    plt.scatter(*zip(*sell_points), color='crimson', label='Sell Signal', s=15, zorder=5)

# Formatting the chart
plt.title(f"MISO Summer Arbitrage: ${total_profit:.2f} Total Profit", fontsize=14)
plt.ylabel("Price per kWh")
plt.xlabel("Hours (July - September)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)

# This command opens the window to show your work!
plt.show()
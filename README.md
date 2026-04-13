# Energy Arbitrage & Battery Storage Simulation (MISO Hub)

A Python-based quantitative trading simulation that models energy arbitrage using real-world **Locational Marginal Pricing (LMP)** data from the Illinois Hub.

## 🚀 Project Overview
This project simulates a battery storage system trading on the MISO real-time market. The goal was to develop an algorithm that maximizes profit while accounting for physical hardware constraints and market volatility.

### Key Engineering Insights:
* **Dynamic Logic:** Implemented a 24-hour rolling window moving average to identify price spikes.
* **Physical Constraints:** Modeled a 100kWh battery with **90% round-trip efficiency** (accounting for thermal loss).
* **Optimization:** Performed a sensitivity analysis showing that increasing discharge power from 20kW to 40kW resulted in an **85% profit increase** ($74.24 → $137.80).

## 📊 Results
![MISO Summer Arbitrage]([LINK_TO_YOUR_GRAPH_IMAGE_HERE])
*The bot successfully captured high-value spikes during the July-September period, proving the logic holds even with an 'efficiency tax' applied.*

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Data Analysis:** Pandas
* **Visualization:** Matplotlib
* **Logic:** Object-Oriented Programming (OOP) for Battery and Trader modules.

## 📂 Project Structure
* `main.py`: The simulation engine.
* `src/battery.py`: Physical modeling of energy storage.
* `src/engine.py`: Trading logic and signal generation.
* `data/`: (Local only) MISO LMP CSV datasets.
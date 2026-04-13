import pandas as pd

# 1. Load the file
file_path = 'data/DA.csv' 
df = pd.read_csv(file_path)

# 2. Extract Illinois Hub data using your exact file's headers
# We want the NODE 'ILLINOIS.HUB' and the VALUE 'LMP'
il_hub = df[(df['NODE'] == 'ILLINOIS.HUB') & (df['VALUE'] == 'LMP')]

# 3. "Melt" the hour columns 
# Your file uses 'HE1' (no space) and 'MARKET_DAY'
hours = [f'HE{i}' for i in range(1, 25)]
cleaned = il_hub.melt(id_vars=['MARKET_DAY'], value_vars=hours, var_name='Hour', value_name='Price')

# 4. Save the result
cleaned.to_csv('data/cleaned_illinois_summer.csv', index=False)

print("✅ Success! 'cleaned_illinois_summer.csv' is ready.")
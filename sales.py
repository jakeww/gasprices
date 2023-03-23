import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


df = pd.read_csv('CleanData.csv', header=None, names=['Gas Price', 'Auto Sales'], skiprows=1)

df['Gas Price'] = df['Gas Price'].str.replace('$', '').astype(float)
df['Auto Sales'] = df['Auto Sales'].str.replace(',', '').astype(int)

# Create a scatter plot of Auto Sales by Gas Price
fig, ax = plt.subplots()
scatter = ax.scatter(df['Gas Price'], df['Auto Sales'], c=df['Gas Price'], cmap='viridis', alpha=0.75)
ax.set_title('Gas Prices Effect on Auto Sales', fontsize=18, fontweight='bold', color='white')

# Add color bar
cbar = plt.colorbar(scatter)
cbar.ax.set_ylabel('Gas Price', rotation=270, labelpad=15, color='white')
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

ax.set_xlabel('Gas Price', color='white')
ax.set_ylabel('Auto Sales', color='white')
plt.rcParams['font.family'] = 'Arial'

formatter = ticker.FormatStrFormatter('$%.2f')
ax.xaxis.set_major_formatter(formatter)
ax.tick_params(axis='x', colors='white')
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax.tick_params(axis='y', colors='white')

# Generate x-values for the trend line
xp = np.linspace(df['Gas Price'].min(), df['Gas Price'].max(), 100)

fig.patch.set_facecolor('#292929')

plt.savefig('gas_prices_effect.png', facecolor=fig.get_facecolor())
plt.show()

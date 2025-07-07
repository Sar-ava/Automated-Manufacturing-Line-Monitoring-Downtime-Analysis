import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Desktop\project\manufacturing_line_data.csv')


downtime_counts = df[df['Status'] == 'Stopped'].groupby('Machine').size()


plt.figure(figsize=(8, 6))
plt.bar(downtime_counts.index, downtime_counts.values, color='skyblue', edgecolor='black')

plt.title('Total Number of Downtime Events per Machine', fontsize=14)
plt.xlabel('Machine', fontsize=12)
plt.ylabel('Number of Downtime Events', fontsize=12)


for i, v in enumerate(downtime_counts.values):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

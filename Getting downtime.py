import pandas as pd

df = pd.read_csv('Desktop\project\manufacturing_line_data.csv')

print(df.head())


downtime_duration = df[df['Status'] == 'Stopped'].groupby('Machine').size()

print("\n🔹 Total Downtime Duration (minutes) per Machine:")
print(downtime_duration)


total_minutes_per_machine = df.groupby('Machine').size()
downtime_percent = (downtime_duration / total_minutes_per_machine) * 100

print("\n🔹 Downtime Percentage per Machine:")
print(downtime_percent.round(2))

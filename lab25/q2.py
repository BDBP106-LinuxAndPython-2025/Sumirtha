import pandas as pd
#Read the JSON file
df = pd.read_json('ODI-Batting Cricket Analytics.json')
# (a) Display column names
print("Column Names:\n", df.columns.tolist())
# (b) Top 5 players by ScoreRate
print("\nTop 5 players by ScoreRate:")
print(df.sort_values(by='ScoreRate', ascending=False).head(5))
# (c) Players with minimum runs
min_runs = df['Runs'].min()
print("\nPlayers with minimum runs:")
print(df[df['Runs'] == min_runs])
# (d) How many players have minimum runs?
print("\nNumber of players with min runs:", df[df['Runs'] == min_runs].shape[0])
# (e) Indian players with runs above average
avg_runs = df['Runs'].mean()
print("\nIndian players with runs above average:")
print(df[(df['Country'] == 'India') & (df['Runs'] > avg_runs)])
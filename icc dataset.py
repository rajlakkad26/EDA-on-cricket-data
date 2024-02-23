
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
icc_data = pd.read_csv("icc.csv")

# Figure 1: Scatter Plot - Overs vs. Runs

# Scatter plot of Overs vs. Runs
scatter_plot_overs_runs = sns.scatterplot(data=icc_data, x='overs', y='runs')
scatter_plot_overs_runs.set(title='Scatter Plot: Overs vs. Runs', xlabel='Overs', ylabel='Runs')
plt.show()

# Figure 2: Boxplot - Wickets by Team

# Boxplot of Wickets by Team
boxplot_wickets_team = sns.boxplot(data=icc_data, x='team', y='wickets')
boxplot_wickets_team.set(title='Boxplot: Wickets by Team', xlabel='Team', ylabel='Wickets')
plt.xticks(rotation=45, ha='right')
plt.show()

# Figure 3: Line Plot - Run Rate over Innings

# Line plot of Run Rate over Innings
line_plot_run_rate_innings = sns.lineplot(data=icc_data, x='innings', y='run_rate')
line_plot_run_rate_innings.set(title='Line Plot: Run Rate over Innings', xlabel='Innings', ylabel='Run Rate')
plt.show()

# Figure 4: Mosaic Plot - Team vs. Opponent

# Mosaic plot of Team vs. Opponent
mosaic_plot_team_opponent = sns.catplot(data=icc_data, kind='count', x='team', hue='opponent', aspect=2)
mosaic_plot_team_opponent.set(title='Mosaic Plot: Team vs. Opponent', xlabel='Team', ylabel='Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# Reference:
# <https://www.kaggle.com/>

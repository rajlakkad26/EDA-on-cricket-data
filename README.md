# EDA-on-cricket-data

# Exploring Cricket Match Data

In this analysis, we delve into patterns within a dataset of cricket match statistics, utilizing R Markdown for data visualization.

## Variables

- **Player**: The name of the cricket player involved in the match.
- **Overs**: The number of overs bowled or faced by a player or team in a cricket match.
- **Maidens**: The count of maidens (an over in which no runs are scored) bowled by a player.
- **Runs**: The total number of runs scored or conceded by a player or team in a cricket match.
- **Wickets**: The total number of wickets taken by a player or team in a cricket match.
- **Run Rate**: The average number of runs scored per over, indicating the scoring rate in a cricket match.
- **X0s, X4s, X6s**: The counts of dot balls, boundaries (4s), and sixes (6s) hit or conceded by a player or team.
- **Wd (Wide)**: The count of wides bowled by a player or team in a cricket match.
- **Nb (No Ball)**: The count of no-balls bowled by a player or team in a cricket match.
- **Team**: The cricket team to which the player belongs.
- **Opponent**: The opposing cricket team in the match.

## Figures

### Figure 1: Scatter Plot - Overs vs. Runs
Figure 1 illustrates the relationship between the number of overs played and the total runs scored in cricket matches. Each point on the scatter plot represents a specific combination of overs and runs, allowing us to observe potential correlations or patterns.

### Figure 2: Boxplot - Wickets by Team
The distribution of wickets taken by different cricket teams is shown in the boxplot. Each box shows the wickets' interquartile range (IQR), with the center line designating the median. Within 1.5 times the IQR, the whiskers reach the minimum and maximum values. This graphic offers a concise synopsis of each team's performance in taking wickets within the cricket dataset.

### Figure 3: Line Plot - Run Rate over Innings
The line plot illustrates how run rates have changed over the course of cricket matches’ various innings. The run rate for each inning is represented by a point on the line, which creates a visual story of the scoring dynamics during the games. The plot provides important insights into the overall scoring patterns over innings by allowing the identification of trends, peaks, or variations in run rates.

### Figure 4: Mosaic Plot - Team vs. Opponent
The mosaic plot visually represents the frequency of matchups between different cricket teams and their respective opponents. Each bar’s height corresponds to the count of these matchups, offering a clear overview of the competitive dynamics within the dataset. The angled x-axis labels enhance readability for numerous teams, facilitating the identification of prevalent matchups and providing valuable insights into the distribution of team-opponent pairings.

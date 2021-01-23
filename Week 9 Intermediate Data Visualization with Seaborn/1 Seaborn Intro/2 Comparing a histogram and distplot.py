he pandas library supports simple plotting of data, which is very convenient when data is already likely to be in a pandas DataFrame.

Seaborn generally does more statistical analysis on data and can provide more sophisticated insight into the data. In this exercise, we will compare a pandas histogram vs the seaborn distplot.

Instructions 1/2
50 XP
Use the pandas' plot.hist() function to plot a histogram of the Award_Amount column.

# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()

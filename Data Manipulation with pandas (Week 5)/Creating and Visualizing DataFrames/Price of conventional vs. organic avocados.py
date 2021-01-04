Creating multiple plots for different subsets of data allows you to compare groups. In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.

matplotlib.pyplot has been imported as plt and pandas has been imported as pd.

Instructions 1/3
35 XP
Subset avocados for the conventional type, and the average price column. Create a histogram.
Create a histogram of avg_price for organic type avocados.
Add a legend to your plot, with the names "conventional" and "organic".
Show your plot.

# Histogram of conventional avg_price
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

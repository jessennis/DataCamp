Linear regression is a useful tool for understanding the relationship between numerical variables. Seaborn has simple but powerful tools for examining these relationships.

For these exercises, we will look at some details from the US Department of Education on 4 year college tuition information and see if there are any interesting insights into which variables might help predict tuition costs.

For these exercises, all data is loaded in the df variable.

Instructions 1/2
50 XP
Plot a regression plot comparing Tuition and average SAT scores(SAT_AVG_ALL).
Make sure the values are shown as green triangles.

# Display a regression plot for Tuition
sns.regplot(data=df,
         y='Tuition',
         x="SAT_AVG_ALL",
         marker='^',
         color='g')

plt.show()
plt.clf()

# Display the residual plot
sns.residplot(data=df,
          y='Tuition',
          x="SAT_AVG_ALL",
          color='g')

plt.show()
plt.clf()


# Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL")

plt.show()
plt.clf()

# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()

# The final plot should include a line using a 2nd order polynomial
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5,
            order=2)

plt.show()
plt.clf()


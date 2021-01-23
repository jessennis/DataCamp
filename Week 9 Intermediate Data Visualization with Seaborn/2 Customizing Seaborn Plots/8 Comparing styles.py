Seaborn supports setting different styles that can control the aesthetics of the final plot. In this exercise, you will plot the same data in two different styles in order to see how the styles change the output.

Instructions 1/2
50 XP
Create a distplot() of the fmr_2 column in df using a dark style. Use plt.clf() to clear the figure.

Create the same distplot() of fmr_2 using a whitegrid style. Clear the plot after showing it.

sns.set_style("dark")
sns.distplot(df['fmr_2'])
plt.show()
plt.clf()


sns.set_style("whitegrid")
sns.distplot(df['fmr_2'])
plt.show()
plt.clf()
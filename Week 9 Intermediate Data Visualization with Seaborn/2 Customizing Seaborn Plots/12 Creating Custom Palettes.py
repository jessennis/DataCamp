Choosing a cohesive palette that works for your data can be time consuming. Fortunately, Seaborn provides the color_palette() function to create your own custom sequential, categorical, or diverging palettes. Seaborn also makes it easy to view your palettes by using the palplot() function.

In this exercise, you can experiment with creating different palettes.

Instructions 1/3
0 XP
Create and display a Purples sequential palette containing 8 colors.

# Create the Purples palette
sns.palplot(sns.color_palette("Purples", 8))
plt.show()

# Create the husl palette
sns.palplot(sns.color_palette("husl", 10))
plt.show()

# Create the coolwarm palette
sns.palplot(sns.color_palette("coolwarm", 6))
plt.show()




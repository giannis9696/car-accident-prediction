import matplotlib.pyplot as plt
import seaborn as sns
def violinplot_for_casualties (car_accident):
    #To compare the distribution of a numerical variable across categories
    sns.violinplot(x='Day of Week', y='Number of Casualties', data=car_accident)
    plt.title('Number of Casualties by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Casualties')
    plt.xticks(rotation=45)
    plt.show()
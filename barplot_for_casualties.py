import seaborn as sns
import matplotlib.pyplot as plt
def barplot_for_numberof_casualties (car_accident):
    average_casualties = car_accident.groupby('Road Type')['Number of Casualties'].mean().reset_index()

    sns.barplot(x='Road Type', y='Number of Casualties', data=average_casualties)
    plt.title('Average Number of Casualties by Road Type')
    plt.xlabel('Road Type')
    plt.ylabel('Average Number of Casualties')
    plt.xticks(rotation=45)
    plt.show()
import matplotlib.pyplot as plt
import seaborn as sns

def countplot_of_accidents_by_roadtype (car_accident):
    sns.countplot(x='Road Type', data=car_accident)
    plt.title('Count of Accidents by Road Type')
    plt.xlabel('Road Type')
    plt.ylabel('Count of Accidents')
    plt.xticks(rotation=45)
    plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
def accidents_per_day (car_accident):
    sns.countplot(x='Day of Week', data=car_accident, order = car_accident['Day of Week'].value_counts().index)
    plt.title('Accident Counts by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Accident Counts')
    plt.xticks(rotation=45)
    plt.show()
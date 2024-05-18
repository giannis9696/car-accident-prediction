import seaborn as sns
import matplotlib.pyplot as plt
def visuals_for_Numberof_casualties (car_accident):
    sns. boxplot(x=car_accident['Number of Casualties'])
    plt.show()

    car_accident['Number of Casualties'].hist(bins=50)
    plt.show()
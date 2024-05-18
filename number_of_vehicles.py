import seaborn as sns
import matplotlib.pyplot as plt
def visuals_for_Numberof_vehicles (car_accident):
    sns.boxplot (x=car_accident['Number of Vehicles'])
    plt.show()

    car_accident['Number of Vehicles'].hist(bins=50)
    plt.show()
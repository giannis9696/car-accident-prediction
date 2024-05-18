import matplotlib.pyplot as plt
def rel_on_speed_limit_and_Casualties (car_accident):
    plt.scatter(car_accident['Speed Limit'], car_accident['Number of Casualties'])
    plt.title('Speed Limit vs. Number of Casualties')
    plt.xlabel('Speed Limit')
    plt.ylabel('Number of Casualties')
    plt.show()
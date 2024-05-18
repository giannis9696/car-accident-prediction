import matplotlib.pyplot as plt
def distribution_of_speed_limit (car_accident):
    plt.hist(car_accident['Speed Limit'], bins=20, edgecolor='black')
    plt.title('Distribution of Speed Limits')
    plt.xlabel('Speed Limit')
    plt.ylabel('Frequency')
    plt.show()
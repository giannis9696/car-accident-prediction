import matplotlib.pyplot as plt
def accidents_over_time (car_accident):
    monthly_accidents = car_accident.resample('M').size()

    plt.figure(figsize=(15, 5))
    plt.plot(monthly_accidents, label='Number of Accidents')
    plt.title('Accidents Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Accidents')
    plt.legend()
    plt.show()
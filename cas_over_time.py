import matplotlib.pyplot as plt
import pandas as pd
def casualties_over_time (car_accident):
    car_accident['Accident Date'] = pd.to_datetime(car_accident['Accident Date'])
    car_accident.set_index('Accident Date', inplace=True)
    car_accident.resample('M')['Number of Casualties'].sum().plot()
    plt.title('Total Casualties Over Time')
    plt.xlabel('Time')
    plt.ylabel('Total Number of Casualties')
    plt.show()
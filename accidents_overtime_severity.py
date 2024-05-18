import matplotlib.pyplot as plt
def accidents_over_time_by_severity (car_accident):
    
    severity_counts = car_accident.groupby([car_accident.index, 'Accident Severity']).size().unstack().fillna(0)
    severity_counts = severity_counts.resample('M').sum()

    plt.figure(figsize=(12, 6))
    plt.stackplot(severity_counts.index, severity_counts['Slight'], severity_counts['Serious'], severity_counts['Fatal'], labels=['Slight', 'Serious', 'Fatal'])
    plt.title('Accidents Over Time by Severity')
    plt.xlabel('Time')
    plt.ylabel('Number of Accidents')
    plt.legend(loc='upper left')
    plt.show()
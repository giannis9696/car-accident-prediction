import matplotlib.pyplot as plt
def piechart_on_accident_severity (car_accident):
    # Replace 'Fetal' with 'Fatal' in the 'Accident Severity' column
    car_accident['Accident Severity'] = car_accident['Accident Severity'].replace('Fetal', 'Fatal')

    # Now, you can plot the pie chart again with the corrected values
    num_categories = car_accident['Accident Severity'].nunique()
    explode_list = [0.1] * num_categories  # Adjust this if the number of categories changes

    plt.figure(figsize=(10, 6))  # Increase the figure size
    car_accident['Accident Severity'].value_counts().plot.pie(
        autopct='%1.1f%%', startangle=90, explode=explode_list, shadow=True
    )
    plt.title('Accident Severity Proportions')
    plt.ylabel('')  # Hide the y-label
    plt.legend(loc='upper right')  # Add a legend
    plt.show()
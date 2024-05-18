def rename_columns (car_accident):
    car_accident.rename(columns={
    'Speed_limit': 'Speed Limit',
    'Day_of_Week': 'Day of Week',
    'Junction_Control': 'Junction Control',
    'Junction_Detail': 'Junction Detail',
    'Accident_Severity': 'Accident Severity',
    'Light_Conditions': 'Light Conditions',
    'Local_Authority_(District)': 'Local Authority (District)',
    'Carriageway_Hazards': 'Carriageway Hazards',
    'Number_of_Casualties': 'Number of Casualties',
    'Number_of_Vehicles': 'Number of Vehicles',
    'Police_Force': 'Police Force',
    'Road_Surface_Conditions': 'Road Surface Conditions',
    'Road_Type': 'Road Type',
    'Urban_or_Rural_Area': 'Urban or Rural Area',
    'Weather_Conditions': 'Weather Conditions',
    'Vehicle_Type': 'Vehicle Type'}, inplace = True)
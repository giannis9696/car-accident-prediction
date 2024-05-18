def drop_irrelevant_entries(car_accident, columns_to_drop):
    car_accident.drop(columns=columns_to_drop, inplace=True)
    return car_accident
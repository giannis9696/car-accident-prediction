def check_null(car_accident):
    null_counts = car_accident.isnull().sum()
    any_nulls = car_accident.isnull().values.any()
    return null_counts, any_nulls
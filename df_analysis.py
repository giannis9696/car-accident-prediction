def dataframe_analysis(car_accident):
    print(car_accident.describe())

    print("The shape of the dataframe is:", car_accident.shape)

    print("Info of the dataframe:")
    car_accident.info()
    
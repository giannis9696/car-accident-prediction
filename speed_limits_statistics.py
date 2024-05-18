def speed_limit_statistics (car_accident):
    mean_value = car_accident['Speed Limit'].mean()
    median_value = car_accident['Speed Limit'].median()
    print(mean_value)
    print(median_value)
    
    std_dev = car_accident['Speed Limit'].std()
    variance = car_accident['Speed Limit'].var()
    range_value = car_accident['Speed Limit'].max() - car_accident['Speed Limit'].min()
    Q1 = car_accident['Speed Limit'].quantile(0.25)
    Q3 = car_accident['Speed Limit'].quantile(0.75)
    IQR = Q3 - Q1

    print(std_dev)
    print(variance)
    print(range_value)
    print(IQR)

    skewness = car_accident['Speed Limit'].skew()
    kurtosis = car_accident['Speed Limit'].kurt()

    print(skewness)
    print(kurtosis)
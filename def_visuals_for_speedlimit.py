def visuals_for_speedlimit (car_accident):

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.boxplot(x=car_accident['Speed Limit'])
    plt.show()

    car_accident['Speed Limit'].hist(bins=50)
    plt.show()

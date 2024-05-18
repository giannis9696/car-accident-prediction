import pandas as pd

def loaddata(filename = "./RoadAccidentData.csv"):
    car_df = pd.read_csv(filename)
    return car_df



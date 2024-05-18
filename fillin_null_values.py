def fill_null_values_withmode(df):
    columns = ['Carriageway_Hazards', 'Road_Surface_Conditions', 'Road_Type', 'Time', 'Weather_Conditions']
    mode_values = {col: df[col].mode()[0] for col in columns if len(df[col].mode()) > 0}
    df.fillna(mode_values, inplace=True)
    return df
def hypothesis_region_severity (car_accident):
    import pandas as pd
    from scipy.stats import chi2_contingency

    contingency_table = pd.crosstab(car_accident['Urban or Rural Area'], car_accident['Accident Severity'])
    chi2, p_val, dof, expected = chi2_contingency(contingency_table)
    print(f"Chi-squared statistic: {chi2}, P-value: {p_val}")
    if p_val < 0.05:
        print("Reject the null hypothesis: there is a significant association between region and accident severity.")
    else:
        print("Do not reject the null hypothesis: there is no significant association between region and accident severity.")
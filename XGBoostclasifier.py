def XGBoostclasifier1 (car_accident):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.metrics import classification_report
    from xgboost import XGBClassifier

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(car_accident['Accident Severity'])

    X = car_accident[['Light Conditions', 'Weather Conditions', 'Road Type', 'Number of Vehicles']]

    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    numeric_features = ['Number of Vehicles']
    numeric_transformer = StandardScaler()

    categorical_features = ['Light Conditions', 'Weather Conditions', 'Road Type']
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', XGBClassifier(use_label_encoder=False, eval_metric='mlogloss'))  # Set use_label_encoder to False to avoid warnings
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))  # Use inverse_transform to get the original class names
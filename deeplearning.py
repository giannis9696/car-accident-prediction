def deep_learning1 (car_accident):
    import numpy as np
    import tensorflow as tf
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout

    categorical_features = ['Light Conditions', 'Weather Conditions', 'Road Type']
    numeric_features = ['Number of Vehicles']

    numeric_transformer = StandardScaler()

    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(car_accident['Accident Severity'])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    X_train, X_test, y_train, y_test = train_test_split(car_accident[categorical_features + numeric_features], y_encoded, test_size=0.2, random_state=42)

    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    if hasattr(X_train, "toarray"):
        X_train = X_train.toarray()
        X_test = X_test.toarray()

    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dense(len(np.unique(y_encoded)), activation='softmax')  # Update the output layer to match the number of classes
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=10, validation_split=0.2)

    model.evaluate(X_test, y_test)
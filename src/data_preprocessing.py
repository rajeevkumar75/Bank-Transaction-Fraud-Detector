import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    df = df.copy()
    
    # Handle missing values
    df.fillna("Unknown", inplace=True)

    # Encode categorical variables
    df = pd.get_dummies(df, columns=['Type', 'Location'], dummy_na=True)

    # Scale numerical features
    scaler = StandardScaler()
    X = scaler.fit_transform(df.drop(['TransactionID', 'IsFraud'], axis=1, errors='ignore'))

    return X, scaler, df

from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df[["RAM (GB)", "CPU_Frequency (GHz)"]]
    y = df["Price (Euro)"]
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def predict_price(model, ram, cpu):
    return float(model.predict([[ram, cpu]])[0])

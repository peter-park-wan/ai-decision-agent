def recommend(df, budget, purpose="general"):
    df = df[df["Price (Euro)"] <= budget].copy()

    if purpose == "gaming":
        df["score"] = df["RAM (GB)"] * 0.4 + df["CPU_Frequency (GHz)"] * 0.6
    elif purpose == "office":
        df["score"] = -df["Weight (kg)"] * 0.3 + df["RAM (GB)"] * 0.5
    else:
        df["score"] = df["RAM (GB)"] + df["CPU_Frequency (GHz)"]

    top = df.sort_values("score", ascending=False).head(3)
    return top[["Company", "Product", "Price (Euro)", "score"]].to_dict(orient="records")
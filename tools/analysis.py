import pandas as pd

def analyze_data(df: pd.DataFrame, query: str):
    if "brand" in query.lower() or "品牌" in query:
        result = df.groupby("Company")["Price (Euro)"].mean().sort_values(ascending=False)
        return result.to_dict()
    return {"msg": "无法识别分析类型"}
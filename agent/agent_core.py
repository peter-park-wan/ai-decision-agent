from config import client
from tools.analysis import analyze_data
from tools.recommendation import recommend
from tools.prediction import predict_price

class DeepSeekAgent:
    def __init__(self, df, model):
        self.df = df
        self.model = model

    def route(self, query: str):
        prompt = f"""
        你是一个AI助手，需要判断用户意图：
        1. 数据分析
        2. 商品推荐
        3. 价格预测

        用户输入: {query}
        只返回：分析 / 推荐 / 预测
        """

        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )

        return res.choices[0].message.content.strip()

    def run(self, query: str):
        intent = self.route(query)
        params = self.extract_params(query)

        if "推荐" in intent:
            result = recommend(self.df, params["budget"], params["purpose"])
        elif "预测" in intent:
            result = predict_price(self.model, 8, 2.5)
        else:
            result = analyze_data(self.df, query)

        # 让 DeepSeek 解释结果
        explain_prompt = f"""
        用户问题: {query}
        工具结果: {result}

        请用自然语言解释结果，并给出结论。
        """

        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": explain_prompt}]
        )

        explanation = res.choices[0].message.content

        return {
            "result": result,
            "explanation": explanation
        }

    def extract_params(self, query):
        prompt = f"""
        从用户输入中提取参数：
        - 预算（budget）
        - 用途（gaming / office / general）

        用户输入: {query}

        返回JSON格式，例如：
        {{\"budget\": 8000, \"purpose\": \"office\"}}
        """

        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )

        return eval(res.choices[0].message.content)
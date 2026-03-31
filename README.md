# 🔥 AI Decision Agent (DeepSeek)

## 📌 项目简介
本项目构建了一个基于大语言模型（DeepSeek）的智能决策Agent系统，能够根据用户输入自动调用数据分析、推荐系统和预测模型，实现端到端的决策支持。

---

## 🚀 核心功能
- 📊 数据分析（自动统计 + 可解释输出）
- 🤖 智能推荐（基于预算和用途）
- 📈 价格预测（机器学习模型）
- 🧠 AI解释（DeepSeek生成自然语言结论）

---

## 🧠 技术架构
- LLM：DeepSeek API
- 数据处理：Pandas
- 机器学习：Scikit-learn
- 前端：Streamlit
- Agent设计：Tool Calling + 意图识别

---

## 💡 示例
用户输入：
> 预算8000，推荐办公电脑

系统输出：
- 推荐产品列表
- 性价比分析
- AI解释推荐原因

---

## ⚙️ 运行方式

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py

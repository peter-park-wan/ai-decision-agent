import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
from tools.prediction import train_model
from agent.agent_core import DeepSeekAgent

st.title("🔥 AI Decision Agent (DeepSeek)")

# 加载数据
df = pd.read_csv("data/laptop.csv")
model = train_model(df)
agent = DeepSeekAgent(df, model)

query = st.text_input("请输入你的问题：")

if st.button("运行"):
    result = agent.run(query)
    st.subheader("📊 工具结果")
    st.write(result["result"])

    st.subheader("🧠 AI解释")
    st.write(result["explanation"])
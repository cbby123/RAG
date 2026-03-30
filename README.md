📚 Qwen2.5 RAG 聊天助手 - README.md
markdown
# RAG 项目合集 | 开源大模型 Qwen2.5 实战
基于 **Ollama + FastAPI + Streamlit + Langchain** 搭建的完整 RAG + Agent + 成语接龙 项目

## 📌 项目介绍
本项目包含课程案例 3～8.5 的全部内容：
- 本地 Qwen2.5 大模型部署
- RAG 检索增强生成
- Agent 智能体
- **Langchain-chain 链实现**
- **成语接龙游戏（AI自玩 + 玩家VS AI 对战）**

## ✨ 已完成功能
✅ 本地大模型运行（Ollama + Qwen2.5-rag）
✅ FastAPI 后端流式接口
✅ Streamlit 可视化聊天界面
✅ Langchain LCEL 链式调用
✅ **成语接龙游戏（双模式）**
  - 模式 1：AI 自动接龙自己玩
  - 模式 2：玩家 VS AI 对战
  - 基于成语文档校验，不在文档内判负
  - 随机开头，每次不重复

## 📁 项目文件结构
RAG/├── api_fastapi.py # FastAPI 后端服务├── web_streamlit.py # 聊天前端界面├── langchain_chain_idiom_game.py # Langchain 链 + 成语接龙游戏├── idioms.txt # 成语库（130+ 成语）├── README.md # 项目说明└── .gitignore # Git 忽略文件
plaintext

## 🚀 快速启动

### 1. 环境安装
```bash
pip install fastapi uvicorn openai streamlit httpx langchain langchain-openai
2. 启动聊天接口
bash
运行
python api_fastapi.py
3. 启动聊天界面
bash
运行
streamlit run web_streamlit.py
4. 启动成语接龙游戏（Langchain）
bash
运行
python langchain_chain_idiom_game.py
🎮 成语接龙游戏说明
游戏模式
AI 自己玩：自动随机开头，连续接龙
玩家 VS AI：玩家输入成语，AI 自动接，违规判负
游戏规则
成语必须来自 idioms.txt
必须用上一个成语最后一个字开头
违规 / 不在文档内 → 直接判负
📚 成语文档
包含 130+ 常用成语，支持自定义扩展。
📝 课程完成进度
开源大模型部署
Langchain-chain 链实现
8.5 成语接龙游戏（双模式） ✅ 已完成
🤖 模型信息
模型：Qwen2.5
运行：Ollama
自定义模型：qwen2.5-rag

📚 Qwen2.5 RAG 聊天助手 - README.md
markdown
# Qwen2.5 RAG 聊天助手

基于 Ollama + FastAPI + Streamlit 构建的轻量级聊天助手，完成案例3至 Langchain-chain 之前的全部功能。

## ✨ 功能特性
- 🧠 **本地模型推理**：基于 Ollama 运行 Qwen2.5 模型，无需依赖外部 API
- 🔌 **流式接口服务**：FastAPI 提供 `/chat` 流式接口，支持实时文字输出
- 🎨 **可视化聊天界面**：Streamlit 前端，支持流畅的打字机效果和多轮对话
- 📦 **一键部署**：完整的环境配置与代码结构，方便快速复用

## 📁 项目结构
RAG/├── ollama/│ └── Modelfile # Ollama 模型配置文件（定义 qwen2.5-rag）├── api_fastapi.py # FastAPI 后端服务代码├── web_streamlit.py # Streamlit 前端聊天界面├── test_ollama_api.py # Ollama API 测试脚本└── .gitignore # Git 忽略文件配置
plaintext

## 🚀 快速启动

### 1. 环境准备
- 已安装 Anaconda，创建并激活环境：
  ```bash
  conda create -n RAG python=3.10
  conda activate RAG
安装依赖：
bash
运行
pip install fastapi uvicorn openai streamlit httpx
2. 启动 Ollama 模型
bash
运行
# 拉取基础模型
ollama pull qwen2.5

# 创建自定义模型
cd ollama
ollama create qwen2.5-rag -f Modelfile
3. 启动 FastAPI 后端
bash
运行
conda activate RAG
unset SSL_CERT_FILE
unset SSL_CERT_DIR
python api_fastapi.py
服务运行在 http://localhost:6066，可访问 http://localhost:6066/docs 测试接口。
4. 启动 Streamlit 前端
新开终端执行：
bash
运行
conda activate RAG
unset SSL_CERT_FILE
unset SSL_CERT_DIR
streamlit run web_streamlit.py
访问 http://localhost:8501 即可使用聊天界面。
🧪 接口测试
方式 1：Swagger UI

访问 http://localhost:6066/docs，点击 /chat → Try it out，输入 message 参数后执行，查看流式响应。

方式 2：Python 脚本

运行 test_ollama_api.py 测试 Ollama API 连通性：

bash

python test_ollama_api.py

📌 注意事项
SSL 证书问题：启动前需执行 unset SSL_CERT_FILE 和 unset SSL_CERT_DIR，避免证书路径错误。
流式渲染优化：前端使用 st.empty() 实现流畅打字效果，避免逐行刷屏。
Git 提交：代码已上传至 GitHub 仓库，可直接克隆使用。
📝 更新日志
v1.0.0：完成基础聊天功能，包含 Ollama 模型、FastAPI 后端和 Streamlit 前端
优化流式渲染效果，提升用户体验
修复 SSL 证书相关问题
🤝 贡献
欢迎提交 Issue 或 Pull Request 改进项目！
plaintext

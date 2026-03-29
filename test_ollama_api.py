from openai import OpenAI
import httpx

# 创建不验证 SSL 的客户端
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    http_client=httpx.Client(verify=False)
)

# 发起对话请求
response = client.chat.completions.create(
    model="qwen2.5-rag",
    messages=[{"role": "user", "content": "你好，请介绍一下自己"}]
)

# 打印回复内容
print(response.choices[0].message.content)
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI
import httpx
import asyncio

app = FastAPI()
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    http_client=httpx.Client(verify=False)
)

@app.get("/chat")
async def chat(message: str):
    def generate():
        stream = client.chat.completions.create(
            model="qwen2.5-rag",
            messages=[{"role": "user", "content": message}],
            stream=True
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    return StreamingResponse(generate(), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6066)
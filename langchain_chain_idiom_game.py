# ==============================
# 8. Langchain-chain 链实现
# 8.5 成语接龙（二合一模式）
# 模式1：AI自己玩   模式2：玩家VS AI对战
# ==============================
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import random

# ----------------------
# 1. 连接本地 Ollama 模型
# ----------------------
llm = ChatOpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1",
    model="qwen2.5-rag",
    temperature=0.1
)

# ----------------------
# 2. 读取成语文档
# ----------------------
def load_idioms_from_file(file_path="idioms.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        idioms = [line.strip() for line in f if line.strip()]
    return idioms

IDIOM_LIST = load_idioms_from_file()

# ----------------------
# 工具函数
# ----------------------
def get_random_start():
    return random.choice(IDIOM_LIST)

def get_valid_candidates(current_idiom):
    last_char = current_idiom[-1]
    return [idiom for idiom in IDIOM_LIST if idiom.startswith(last_char)]

def check_in_list(idiom):
    return idiom in IDIOM_LIST

# ----------------------
# 模式1：AI 自己玩
# ----------------------
def ai_play_alone(max_round=10):
    current = get_random_start()
    print("=" * 50)
    print("🤖 模式：AI 自己玩成语接龙")
    print(f"📚 成语库：{len(IDIOM_LIST)} 个")
    print("=" * 50)
    print(f"\n🚀 随机起始：{current}\n")

    for i in range(1, max_round + 1):
        candidates = get_valid_candidates(current)
        if not candidates:
            print("❌ AI 没有可接的成语，游戏结束")
            break

        next_idiom = random.choice(candidates)
        print(f"第{i}轮：{current} → {next_idiom}")
        current = next_idiom

    print("\n🏆 AI 游戏结束！")

# ----------------------
# 模式2：玩家 VS AI
# ----------------------
def player_vs_ai():
    print("=" * 50)
    print("🎮 模式：玩家 VS AI 对战")
    print(f"📚 成语库：{len(IDIOM_LIST)} 个")
    print("规则：必须使用文档内成语，否则判负")
    print("=" * 50)

    current = get_random_start()
    print(f"\n🚀 随机起始成语：【{current}】")

    while True:
        # 玩家回合
        player = input("\n👉 请接龙：").strip()
        if not check_in_list(player):
            print(f"❌ 你输了！【{player}】不在文档里")
            break
        if not player.startswith(current[-1]):
            print(f"❌ 你输了！需以【{current[-1]}】开头")
            break

        print(f"✅ 你：{player}")
        current = player

        # AI 回合
        candidates = get_valid_candidates(current)
        if not candidates:
            print("\n🎉 你赢了！AI 接不上了！")
            break

        ai_idiom = random.choice(candidates)
        print(f"🤖 AI：{ai_idiom}")
        current = ai_idiom

    print("\n🏆 对战结束！")

# ----------------------
# 主菜单：选择模式
# ----------------------
if __name__ == "__main__":
    print("==================================")
    print("     成语接龙游戏（Langchain版）")
    print("==================================")
    print("【1】AI 自己玩")
    print("【2】玩家 VS AI 对战")
    choice = input("请选择模式（1/2）：").strip()

    if choice == "1":
        ai_play_alone(max_round=10)
    elif choice == "2":
        player_vs_ai()
    else:
        print("输入错误，退出")
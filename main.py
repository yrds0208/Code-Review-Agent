# main.py
import os
import openai
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def review_code(diff_content):
    """
    使用 Qwen 或 GPT 模型对代码 Diff 进行审查
    """
    # 这里演示使用 OpenAI 格式，实际对接通义千问只需修改 base_url 和 model 名称
    client = openai.OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"), # 使用通义千问 API Key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1" # 通义千问兼容 OpenAI 的接口地址
    )

    prompt = f"""
    你是一个资深的代码审查专家。请审查以下 Git Diff 代码：
    1. 指出潜在的 Bug。
    2. 给出优化建议。
    3. 保持语气专业且简洁。

    代码变动如下：
    {diff_content}
    """

    try:
        completion = client.chat.completions.create(
            model="qwen-plus", # 或者 qwen-max
            messages=[
                {'role': 'system', 'content': 'You are a helpful code reviewer.'},
                {'role': 'user', 'content': prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # 模拟一段代码变动
    mock_diff = """
    def add(a, b):
    -    return a - b
    +    return a + b
    """
    print("正在审查代码...")
    result = review_code(mock_diff)
    print("审查结果：")
    print(result)

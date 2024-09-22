# 先使用 pip install google-generativeai 安装 Gemini 库
import os
import google.generativeai as genai

# API 设置
GEMINI_API_KEY = ""
genai.configure(api_key=GEMINI_API_KEY)

# 代理设置 (For Clash)
os.environ['https_proxy'] = 'http://127.0.0.1:7890'
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['all_proxy'] = 'socks5://127.0.0.1:7890'

# 生成CFG设置
generation_config_dict = {
    "temperature": 1,  # 生成温度，值越高，对于同样的问题，给出不同回答的可能性越高
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,  # 生成的最大token数量，超过此值，会截断
    "response_mime_type": "text/plain",  # 应答格式，可替换为text/json
}

# 模型设置
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # 模型名称, 可替换为gemini-1.5-flash, gemini-1.5-pro-exp-0827等
    generation_config=generation_config_dict,  # 导入生成CFG字典

    system_instruction="",  # Prompts 设置
)

# 聊天记录
history = []

# 循环体
while True:
    user_input = input("MSG Gemini > ")  # 输入端

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)
    print(response.text)  # 输出端

    # 记录聊天历史
    history.append({"role": "user", "parts": [user_input]})
    history.append({f"role": "model", "parts": [response.text]})

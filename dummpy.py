from openai import OpenAI
import base64
import json
import argparse
import datetime
import os
from pathlib import Path
import tqdm


openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8001/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# models.list()返回一个模型列表，每个模型都有一个id属性
model_name = client.models.list().data[0].id

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def call_api(text, system_prompt):
    
    # base64_image = encode_image(image)
    response = client.chat.completions.create(
        # model="模型",
        model = model_name, # 图文
        messages=[
            {'role': 'system', 'content': system_prompt},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text},
                    ],
                }
        ],
    )
    return response.choices[0].message.content


    


if __name__ == "__main__":
    print("dummy program")
    while True:
        text = "请问你是谁"
        system_prompt="你是蝙蝠侠"
        outputs = call_api(text,system_prompt)



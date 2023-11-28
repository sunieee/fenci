
import os
from tqdm import tqdm
import re

files = os.listdir('文华图专老教师文章')
os.makedirs('input', exist_ok=True)

# 您要尝试的编码列表
encodings = ['utf-8', 'gbk', 'gb2312', 'big5', 'iso-8859-1']

def read_and_convert(file_path):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                text = f.read()
            return text
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Failed to decode {file_path} with given encodings.")

def preprocess_text(text):
    # 移除特殊字符和无法识别的字符
    text = re.sub(r'[^\w\s.-]', ' ', text)  # 保留字母数字中文及空格
    text = re.sub(r'\s+', ' ', text)     # 将所有空白字符替换为单个空格
    return text

for file in tqdm(files):
    # print(file)
    file_path = '文华图专老教师文章/' + file
    try:
        text = read_and_convert(file_path)
        print(len(text), end=' -> ')

        text = preprocess_text(text)
        print(len(text))
        # 将内容写入新文件，使用utf-8编码
        with open('input/' + file, 'w', encoding='utf-8') as f:
            f.write(text)
    except UnicodeDecodeError as e:
        print(e)
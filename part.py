import jieba
import os
import re
from tqdm import tqdm


def is_chinese_text(text, threshold=0.1):
    chinese_chars_count = len(re.findall(r'[\u4e00-\u9fff]', text))
    total_chars_count = len(text)
    
    # 计算中文字符所占的比例
    chinese_ratio = chinese_chars_count / total_chars_count if total_chars_count > 0 else 0

    return chinese_ratio > threshold

def segment_text(text):
    if is_chinese_text(text):
        return list(jieba.cut(text))
    else:
        return text.split()

def is_valid_line(line):
    # 检查行是否有效（不为空，且不只包含 . - 数字）
    return not re.match(r'^[.\-0-9\s]*$', line)

files = os.listdir('input')
os.makedirs('out', exist_ok=True)
for file in tqdm(files):
    file_path = 'input/' + file
    output_path = 'out/' + file

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 分词
    words = segment_text(text)
    # 保存分词结果
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in words:
            if is_valid_line(word):
                f.write(word + '\n')

import os
import json
import argparse
import re
from collections import defaultdict
import math
import jieba

# 初始化jieba分词
jieba.initialize()

def tokenize(text):
    """混合中英文分词"""
    # 移除Markdown特殊字符
    text = re.sub(r'[#*_`~\[\]!]', ' ', text)
    # 使用jieba进行中文分词
    chinese_tokens = jieba.cut_for_search(text)
    # 处理英文单词
    tokens = []
    for token in chinese_tokens:
        if re.match(r'^[a-zA-Z]+$', token):
            tokens.extend(re.findall(r'[a-zA-Z]{2,}', token.lower()))
        else:
            tokens.append(token)
    return tokens

def scan_md_files(root_dir):
    """扫描指定目录下的所有Markdown文件，构建倒排索引"""
    inverted_index = defaultdict(lambda: defaultdict(int))
    file_info = {}
    file_count = 0
    base_path = os.path.abspath(root_dir)
    
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                full_path = os.path.join(foldername, filename)
                # 生成相对于根目录的相对路径
                rel_path = os.path.relpath(foldername, os.path.dirname(base_path))
                
                # 使用文件夹路径作为标识（去除.md后缀）
                clean_path = rel_path.replace('\\', '/')  # 确保使用正斜杠
                
                # 检查该文件夹是否已有索引（避免重复处理）
                if clean_path in file_info:
                    continue
                
                # 检查index.html是否存在
                index_html_path = os.path.join(foldername, 'index.html')
                if not os.path.exists(index_html_path):
                    print(f"警告: {foldername} 中未找到 index.html，跳过")
                    continue
                
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取标题（第一个一级标题或文件名）
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else os.path.basename(foldername)
                
                # 生成摘要（前200个字符）
                summary = content.replace('\n', ' ').replace('#', '')[:200]
                if len(content) > 200:
                    summary += "..."
                
                # 文件信息 - 使用文件夹路径作为键
                file_info[clean_path] = {
                    "title": title,
                    "summary": summary,
                    "length": len(content),
                    "url": clean_path + "/index.html"  # 指向文件夹的index.html
                }
                
                # 分词并构建倒排索引
                tokens = tokenize(content)
                for token in set(tokens):  # 每个词在文档中只计一次
                    inverted_index[token][clean_path] += 1
                
                file_count += 1
                if file_count % 100 == 0:
                    print(f"已处理 {file_count} 个文件夹...")
    
    # 计算TF-IDF权重
    total_files = len(file_info)
    for token, docs in inverted_index.items():
        doc_count = len(docs)
        idf = math.log(total_files / (doc_count + 1))
        for doc_path, freq in docs.items():
            # 使用TF-IDF权重
            tf = freq / file_info[doc_path]["length"]
            docs[doc_path] = tf * idf
    
    return {
        "invertedIndex": dict(inverted_index),
        "fileInfo": file_info,
        "totalFiles": total_files
    }

def save_index(index, output_file='search_index.json'):
    """保存索引到JSON文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"索引已保存到 {output_file}")
    print(f"文件夹总数: {index['totalFiles']}")
    print(f"索引词条数: {len(index['invertedIndex'])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='静态网站搜索索引生成器')
    parser.add_argument('--dir', default='submissions', help='要扫描的目录')
    parser.add_argument('--output', default='search_index.json', help='输出索引文件名')
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"错误: 目录 '{args.dir}' 不存在")
        exit(1)
    
    print(f"开始扫描目录: {args.dir}...")
    index_data = scan_md_files(args.dir)
    save_index(index_data, args.output)

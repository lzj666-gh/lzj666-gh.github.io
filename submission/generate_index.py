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
    chinese_tokens = jieba.cut(text)
    # 处理英文单词
    tokens = []
    for token in chinese_tokens:
        if re.match(r'^[a-zA-Z]+$', token):
            tokens.extend(re.findall(r'[a-zA-Z]{2,}', token.lower()))
        else:
            tokens.append(token)
    return tokens

def remove_md_suffix(path):
    """移除路径中的.md后缀"""
    if path.lower().endswith('.md'):
        return path[:-3]
    return path

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
                rel_path = os.path.relpath(full_path, os.path.dirname(base_path))
                
                # 移除.md后缀
                clean_path = remove_md_suffix(rel_path)
                
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取标题（第一个一级标题或文件名）
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else os.path.splitext(filename)[0]
                
                # 生成摘要（前200个字符）
                summary = content.replace('\n', ' ').replace('#', '')[:200]
                if len(content) > 200:
                    summary += "..."
                
                # 文件信息
                file_info[clean_path] = {
                    "title": title,
                    "summary": summary,
                    "length": len(content),
                    "original_path": rel_path  # 保留原始路径供内部使用
                }
                
                # 分词并构建倒排索引
                tokens = tokenize(content)
                token_count = len(tokens)
                for token in set(tokens):  # 每个词在文档中只计一次
                    inverted_index[token][clean_path] += 1
                
                file_count += 1
                if file_count % 100 == 0:
                    print(f"已处理 {file_count} 个文件...")
    
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
    print(f"文件总数: {index['totalFiles']}")
    print(f"索引词条数: {len(index['invertedIndex'])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='高性能静态网站搜索索引生成器')
    parser.add_argument('--dir', default='submissions', help='要扫描的目录')
    parser.add_argument('--output', default='search_index.json', help='输出索引文件名')
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"错误: 目录 '{args.dir}' 不存在")
        exit(1)
    
    print(f"开始扫描目录: {args.dir}...")
    index_data = scan_md_files(args.dir)
    save_index(index_data, args.output)

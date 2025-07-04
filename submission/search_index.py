import json
import os

def load_index(index_file='index.json'):
    if not os.path.exists(index_file):
        print(f"错误: 索引文件 '{index_file}' 不存在")
        print("请先运行 generate_index.py 生成索引")
        exit(1)
    
    with open(index_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def search_files(index, query):
    results = []
    for path, content in index.items():
        if query in content:
            results.append(path)
    return results

if __name__ == "__main__":
    INDEX_FILE = "index.json"
    
    index_data = load_index(INDEX_FILE)
    query = input("请输入要搜索的内容: ").strip()
    
    if not query:
        print("搜索内容不能为空")
        exit(1)
    
    results = search_files(index_data, query)
    
    if results:
        print(f"\n找到 {len(results)} 个匹配文件:")
        for path in results:
            print(f"- {path}")
    else:
        print("\n未找到匹配文件")

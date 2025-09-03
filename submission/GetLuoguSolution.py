import os
import re
import json
import time
import requests
import pyluog as pl
from bs4 import BeautifulSoup
from urllib.parse import unquote

# 配置信息
BASE_DIR = 'submissions'
uid = '836542'
client_id = '29532aac789524588c21e94f1c9fde1738daee03'
headers = {
    'Referer': 'https://www.luogu.com.cn/auth/login',
    'Origin': 'https://www.luogu.com.cn',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.421.0 Safari/537.36",
    "Accept": "*/*",
    'Connection': 'keep-alive',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrf-token':'',
}

def setup_session():
    """创建并配置请求会话"""
    s = requests.session()
    requests.utils.add_dict_to_cookiejar(s.cookies,{'__client_id':client_id,'_uid':str(uid)})
    res = pl.User('*','*')
    res.sess = s
    res.client_id_ = client_id
    res.uid = uid
    session = res.sess
    
    # 获取CSRF token
    resp = session.get('https://www.luogu.com.cn', headers=headers)
    if match := re.search(r'<meta name="csrf-token" content="([^"]+)">', resp.text):
        session.headers['x-csrf-token'] = match.group(1)
    return session

def get_first_solution(session, problem_id):
    """获取指定题目的第一篇题解"""
    url = f'https://www.luogu.com.cn/problem/solution/{problem_id}'
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找包含题解数据的script标签
        script_tag = soup.find('script', id='lentille-context', type='application/json')
        if not script_tag:
            print(f"未找到题解数据标签 ({problem_id})")
            return "暂无题解"
        
        # 解析JSON数据
        json_data = json.loads(script_tag.string)
        
        # 提取题解列表
        solutions = json_data.get('data', {}).get('solutions', {}).get('result', [])
        if not solutions:
            print(f"未找到题解 ({problem_id})")
            return "暂无题解"
        
        # 返回第一篇题解内容
        return solutions[0].get('content', "题解内容为空")
    
    except Exception as e:
        print(f"获取题解失败 ({problem_id}): {str(e)}")
        return "获取题解失败"

def generate_main_index(entries):
    """生成主目录的索引HTML文件"""
    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>提交记录索引</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
        .folder { font-weight: bold; margin-top: 20px; }
        .files { margin-left: 20px; }
    </style>
</head>
<body>
    <h1>提交记录与题解索引</h1>
    <ul>
"""

    for folder in entries:
        html += f'        <li class="folder"><a href="{folder}/index.html">{folder}</a></li>\n'
    
    html += """    </ul>
</body>
</html>"""
    
    with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def generate_folder_index(folder_path, files):
    """为单个文件夹生成索引HTML文件"""
    folder_name = os.path.basename(folder_path)
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{folder_name} - 文件索引</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #0066cc; }}
        a:hover {{ text-decoration: underline; }}
        .back-link {{ margin-top: 20px; display: block; }}
    </style>
</head>
<body>
    <h1>{folder_name} 文件列表</h1>
    <ul>
"""

    for file in files:
        html += f'        <li><a href="{file}">{file}</a></li>\n'
    
    html += f"""    </ul>
    <a class="back-link" href="../index.html">返回上级目录</a>
</body>
</html>"""
    
    with open(os.path.join(folder_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    session = setup_session()
    folders = []
    
    # 创建解决方案目录（如果不存在）
    os.makedirs(BASE_DIR, exist_ok=True)
    
    # 遍历所有题目文件夹
    for folder_name in os.listdir(BASE_DIR):
        folder_path = os.path.join(BASE_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        
        folders.append(folder_name)
            
        # 从文件夹名提取题目ID
        if folder_name.startswith('luogu_'):
            problem_id = folder_name.split('_', 1)[1]  # 去掉"luogu_"前缀
        else:
            problem_id = folder_name
            
        # 获取题解并保存
        solution_path = os.path.join(folder_path, 'solution.md')
        if not os.path.exists(solution_path):
            print(f"获取题目 {problem_id} 的题解...")
            solution = get_first_solution(session, problem_id)
            with open(solution_path, 'w', encoding='utf-8') as f:
                f.write(f"# {problem_id} 题解\n\n")
                f.write(solution)
            time.sleep(1.5)  # 避免请求过快
        
        # 收集文件列表
        files = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file != 'index.html':
                files.append(file)
        
        # 为当前文件夹生成索引
        generate_folder_index(folder_path, files)
    
    # 生成主目录索引
    generate_main_index(folders)
    print("索引文件生成完成：")
    print(f"- 主目录索引: {os.path.join(BASE_DIR, 'index.html')}")
    print(f"- 每个子文件夹中都有单独的 index.html 文件")

if __name__ == "__main__":
    main()

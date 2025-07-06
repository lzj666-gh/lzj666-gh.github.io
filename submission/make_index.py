import os
import shutil

BASE_DIR = 'submissions'

def replace_filename_characters(folder_path):
    """替换文件夹中所有文件名中的 # 为空格"""
    for filename in os.listdir(folder_path):
        if '#' in filename:
            # 构建新文件名（替换 # 为空格）
            new_filename = filename.replace('#', ' ')
            
            # 构建完整文件路径
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # 重命名文件
            shutil.move(old_path, new_path)
            print(f"重命名文件: {filename} -> {new_filename}")

def generate_main_index(folders):
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

    for folder in folders:
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
        # 在链接中使用替换后的文件名
        display_name = file.replace('#', ' ')
        html += f'        <li><a href="{file}">{display_name}</a></li>\n'
    
    html += f"""    </ul>
    <a class="back-link" href="../index.html">返回上级目录</a>
</body>
</html>"""
    
    with open(os.path.join(folder_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    # 确保目录存在
    if not os.path.exists(BASE_DIR):
        print(f"目录 {BASE_DIR} 不存在")
        return
    
    folders = []
    
    # 遍历所有题目文件夹
    for folder_name in os.listdir(BASE_DIR):
        folder_path = os.path.join(BASE_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        
        folders.append(folder_name)
        
        # 替换文件名中的 # 为空格
        replace_filename_characters(folder_path)
        
        # 收集文件列表（使用替换后的文件名）
        files = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                files.append(file)
        
        # 为当前文件夹生成索引
        generate_folder_index(folder_path, files)
        print(f"已生成索引: {folder_path}/index.html")
    
    # 生成主目录索引
    if folders:
        generate_main_index(folders)
        print(f"已生成主索引: {os.path.join(BASE_DIR, 'index.html')}")
    else:
        print("未找到任何子文件夹")

if __name__ == "__main__":
    main()

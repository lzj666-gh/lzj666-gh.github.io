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
            filename = new_filename
        if '[' in filename:
            # 构建新文件名（替换 [ 为空格）
            new_filename = filename.replace('[', ' ')
            
            # 构建完整文件路径
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # 重命名文件
            shutil.move(old_path, new_path)
            print(f"重命名文件: {filename} -> {new_filename}")
            filename = new_filename
        if ']' in filename:
            # 构建新文件名（替换 ] 为空格）
            new_filename = filename.replace(']', ' ')
            
            # 构建完整文件路径
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # 重命名文件
            shutil.move(old_path, new_path)
            print(f"重命名文件: {filename} -> {new_filename}")
            filename = new_filename

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
    """为单个文件夹生成索引HTML文件，包含文件内容查看功能"""
    folder_name = os.path.basename(folder_path)
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{folder_name} - 文件索引</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 20px; 
            display: flex;
            gap: 30px;
        }}
        #file-list {{
            width: 300px;
            flex-shrink: 0;
        }}
        #file-content {{
            flex-grow: 1;
        }}
        h1 {{ 
            color: #333; 
            margin-top: 0;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #666;
            font-size: 18px;
            margin-top: 0;
        }}
        ul {{ 
            list-style-type: none; 
            padding: 0; 
        }}
        li {{ 
            margin: 8px 0; 
            padding: 8px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }}
        li:hover {{
            background-color: #f5f5f5;
        }}
        li.active {{
            background-color: #e6f7ff;
            border-left: 3px solid #0066cc;
        }}
        .file-link {{ 
            text-decoration: none; 
            color: #0066cc;
            display: block;
            cursor: pointer;
            font-size: 14px;
        }}
        .file-link:hover {{ 
            text-decoration: underline; 
        }}
        .back-link {{ 
            margin-top: 20px; 
            display: inline-block;
            color: #666;
            text-decoration: none;
            padding: 8px 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        .back-link:hover {{ 
            background-color: #f5f5f5;
            text-decoration: none;
        }}
        .code-display {{
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 6px;
            padding: 20px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            white-space: pre-wrap;
            word-wrap: break-word;
            max-height: 70vh;
            overflow-y: auto;
            line-height: 1.5;
        }}
        .file-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }}
        .file-title {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .file-info {{
            font-size: 14px;
            color: #666;
        }}
        .no-file-selected {{
            color: #999;
            font-style: italic;
            text-align: center;
            padding: 40px;
            border: 2px dashed #ddd;
            border-radius: 6px;
        }}
        .loading {{
            color: #666;
            text-align: center;
            padding: 40px;
        }}
        .error {{
            color: #dc3545;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 15px;
        }}
        .file-size {{
            font-size: 12px;
            color: #888;
            margin-left: 10px;
        }}
        .file-ext {{
            display: inline-block;
            background-color: #e9ecef;
            color: #495057;
            font-size: 12px;
            padding: 2px 8px;
            border-radius: 12px;
            margin-left: 10px;
        }}
        .file-list-title {{
            font-size: 16px;
            font-weight: bold;
            color: #495057;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #dee2e6;
        }}
    </style>
</head>
<body>
    <div id="file-list">
        <div class="file-list-title">文件列表</div>
        <ul>
"""

    # 生成文件列表
    for file in files:
        if file == 'index.html':
            continue
        display_name = file.replace('#', ' ')
        html += f'            <li data-filename="{file}">\n'
        html += f'                <a class="file-link" onclick="loadFile(\'{file}\')">{display_name}</a>\n'
        html += f'            </li>\n'
    
    html += f"""        </ul>
        <a class="back-link" href="../index.html">返回上级目录</a>
    </div>
    
    <div id="file-content">
        <div class="no-file-selected">
            <h2>选择文件查看内容</h2>
            <p>从左侧列表中选择一个文件，内容将显示在此处</p>
        </div>
    </div>
    
    <script>
        // 当前选中的文件
        let currentFile = null;
        
        // 加载文件内容
        async function loadFile(filename) {{
            // 更新当前选中的文件
            currentFile = filename;
            
            // 更新文件列表的高亮
            updateFileListHighlight(filename);
            
            // 显示加载状态
            document.getElementById('file-content').innerHTML = '<div class="loading">正在加载文件内容...</div>';
            
            try {{
                // 获取文件内容
                const response = await fetch(filename);
                
                if (!response.ok) {{
                    throw new Error(`HTTP error! status: ${{response.status}}`);
                }}
                
                const fileContent = await response.text();
                
                // 显示文件内容
                displayFileContent(filename, fileContent);
            }} catch (error) {{
                console.error('加载文件失败:', error);
                document.getElementById('file-content').innerHTML = `
                    <div class="error">
                        <strong>加载文件失败</strong><br>
                        <small>${{error.message}}</small>
                    </div>
                `;
            }}
        }}
        
        // 更新文件列表高亮
        function updateFileListHighlight(filename) {{
            // 移除所有li元素的active类
            document.querySelectorAll('#file-list li').forEach(li => {{
                li.classList.remove('active');
            }});
            
            // 为当前选中的文件添加active类
            const activeLi = document.querySelector(`#file-list li[data-filename="${{filename}}"]`);
            if (activeLi) {{
                activeLi.classList.add('active');
            }}
        }}
        
        // 显示文件内容
        function displayFileContent(filename, content) {{
            const displayName = filename.replace(/#/g, ' ');
            const fileSize = content.length;
            const fileExt = filename.split('.').pop().toUpperCase();
            
            // 转义HTML特殊字符
            const escapedContent = escapeHtml(content);
            
            const html = `
                <div class="file-header">
                    <div class="file-title">
                        ${{displayName}}
                        <span class="file-ext">${{fileExt}}</span>
                    </div>
                    <div class="file-info">
                        ${{fileSize.toLocaleString()}} 字符
                    </div>
                </div>
                <div class="code-display">${{escapedContent}}</div>
            `;
            
            document.getElementById('file-content').innerHTML = html;
            
            // 如果是代码文件，可以添加语法高亮（可选）
            highlightCodeIfNeeded(filename, content);
        }}
        
        // 转义HTML特殊字符
        function escapeHtml(text) {{
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }}
        
        // 根据文件类型进行语法高亮（基础版本）
        function highlightCodeIfNeeded(filename, content) {{
            const ext = filename.split('.').pop().toLowerCase();
            const codeDisplay = document.querySelector('.code-display');
            
            if (!codeDisplay) return;
            
            // 简单的关键词高亮（可根据需要扩展）
            if (['py', 'python'].includes(ext)) {{
                // Python语法高亮
                let highlighted = content.replace(
                    /(\b(def|class|if|else|elif|for|while|return|import|from|as|try|except|finally|with|and|or|not|in|is|lambda|pass|break|continue)\b)/g,
                    '<span style="color: #007bff; font-weight: bold;">$1</span>'
                );
                highlighted = highlighted.replace(
                    /(\b(True|False|None)\b)/g,
                    '<span style="color: #28a745;">$1</span>'
                );
                highlighted = highlighted.replace(
                    /(#.*)/g,
                    '<span style="color: #6c757d;">$1</span>'
                );
                codeDisplay.innerHTML = highlighted;
            }}
            else if (['js', 'javascript'].includes(ext)) {{
                // JavaScript语法高亮
                let highlighted = content.replace(
                    /(\b(function|var|let|const|if|else|for|while|return|class|import|export|from|try|catch|finally|new|this|typeof|instanceof)\b)/g,
                    '<span style="color: #007bff; font-weight: bold;">$1</span>'
                );
                highlighted = highlighted.replace(
                    /(\b(true|false|null|undefined)\b)/g,
                    '<span style="color: #28a745;">$1</span>'
                );
                highlighted = highlighted.replace(
                    /(\/\/.*)/g,
                    '<span style="color: #6c757d;">$1</span>'
                );
                codeDisplay.innerHTML = highlighted;
            }}
            else if (['html', 'htm'].includes(ext)) {{
                // HTML语法高亮
                let highlighted = content.replace(
                    /(&lt;\/?[a-zA-Z][^&gt;]*&gt;)/g,
                    '<span style="color: #dc3545;">$1</span>'
                );
                codeDisplay.innerHTML = highlighted;
            }}
            // 可以添加更多文件类型的支持
        }}
        
        // 页面加载完成后，检查URL中是否有文件参数
        window.addEventListener('DOMContentLoaded', () => {{
            // 从URL获取文件参数
            const urlParams = new URLSearchParams(window.location.search);
            const fileParam = urlParams.get('file');
            
            if (fileParam) {{
                // 如果URL中有file参数，自动加载该文件
                loadFile(fileParam);
            }}
        }});
    </script>
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
        
        # 为当前文件夹生成索引（现在包含文件内容查看功能）
        generate_folder_index(folder_path, files)
        print(f"已生成索引: {folder_path}/index.html")
    
    # 生成主目录索引（保持不变）
    if folders:
        generate_main_index(folders)
        print(f"已生成主索引: {os.path.join(BASE_DIR, 'index.html')}")
    else:
        print("未找到任何子文件夹")

if __name__ == "__main__":
    main()

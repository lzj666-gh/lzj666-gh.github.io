import os
import re
import time
import json
import requests
from bs4 import BeautifulSoup
import pyluog as pl

def extract_problem_id(folder_name):
    """从文件夹名称中提取题目ID"""
    match = re.match(r'^luogu_(.*)$', folder_name)
    return match.group(1) if match else None

def get_luogu_problem_content(problem_id):
    """获取洛谷题目内容和翻译"""
    url = f"https://www.luogu.com.cn/problem/{problem_id}"
    uid = '836542'
    client_id = '1f5b66b7853d8326d73e670896aa0481ad982eaa'
    headers = {
        'Referer': 'https://www.luogu.com.cn/auth/login',
        'Origin': 'https://www.luogu.com.cn',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.421.0 Safari/537.36",
        "Accept": "*/*",
        'Connection': 'keep-alive',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrf-token':'',
    }
    s = requests.session()
    requests.utils.add_dict_to_cookiejar(s.cookies,{'__client_id':client_id,'_uid':str(uid)})
    res = pl.User('*','*')
    res.sess = s
    res.client_id_ = client_id
    res.uid = uid
    
    try:
        response = res.sess.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = problem_id
        original_description = ""
        translated_description = None
        input_format = ""
        output_format = ""
        hint = ""
        time_limit = 0
        memory_limit = 0
        
        # 尝试从JSON数据中提取题目内容
        script_tag = soup.find('script', id='lentille-context')
        if script_tag:
            try:
                json_data = json.loads(script_tag.string)
                problem_data = json_data['data']['problem']
                
                # 提取标题
                title = problem_data['title']
                
                # 提取题目内容
                content = problem_data['content']
                original_description = content.get('description', '')
                input_format = content.get('formatI', '')
                output_format = content.get('formatO', '')
                hint = content.get('hint', '')
                
                # 提取翻译内容
                translation = problem_data.get('translation')
                if translation:
                    translated_description = translation
                
                # 提取时空限制
                limits = problem_data['limits']
                time_limit = limits['time'][0]  # 单位毫秒
                memory_limit = limits['memory'][0]  # 单位KB
            except Exception as e:
                print(f"解析JSON时出错: {str(e)}")
        
        # 如果JSON解析失败，回退到HTML解析
        if not original_description:
            # 获取题目标题
            title_tag = soup.find('h1')
            if title_tag:
                title = title_tag.text.strip()
            
            # 获取题目描述
            description_div = None
            for section in soup.find_all('section'):
                if section.find('h2', string='Description'):
                    description_div = section.find('div')
                    break
            
            if description_div:
                original_description = description_div.decode_contents()
        
        # 构建时空限制字符串
        if memory_limit > 0:
            memory_limit_mb = memory_limit / 1024  # 转换为MB
            limits_str = f"时间限制: {time_limit} ms\n内存限制: {memory_limit_mb:.0f} MB"
        else:
            limits_str = "时空限制信息获取失败"
        
        # 构建原始内容
        original_content = f"## 题目描述\n\n{original_description}\n\n"
        if input_format:
            original_content += f"## 输入格式\n\n{input_format}\n\n"
        if output_format:
            original_content += f"## 输出格式\n\n{output_format}\n\n"
        if hint:
            original_content += f"## 提示\n\n{hint}\n\n"
        
        # 构建翻译内容
        translated_content = None
        if translated_description:
            translated_content = f"## 题目描述\n\n{translated_description}\n\n"
            if input_format:
                translated_content += f"## 输入格式\n\n{input_format}\n\n"
            if output_format:
                translated_content += f"## 输出格式\n\n{output_format}\n\n"
            if hint:
                translated_content += f"## 提示\n\n{hint}\n\n"
        
        return title, original_content, limits_str, translated_content
    except Exception as e:
        print(f"获取题目 {problem_id} 内容时出错: {str(e)}")
        return None, None, None, None

def create_markdown_file(folder_path, title, content, limits, translated_content=None):
    """创建Markdown文件，如果有翻译则额外创建翻译文件"""
    # 移除标题中的非法字符
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
    
    # 创建原始题目文件
    file_name = f"{safe_title}.md"
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(content)
        f.write("## 时空限制\n\n")
        f.write(limits + "\n")
    
    print(f"已创建: {file_path}")
    
    # 创建翻译文件
    if translated_content:
        translated_file_name = f"translated_{safe_title}.md"
        translated_file_path = os.path.join(folder_path, translated_file_name)
        
        with open(translated_file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title} (翻译版)\n\n")
            f.write(translated_content)
            f.write("## 时空限制\n\n")
            f.write(limits + "\n")
        
        print(f"已创建翻译: {translated_file_path}")

def has_markdown_files(folder_path):
    """检查文件夹中是否已存在Markdown文件"""
    # 列出文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        # 检查是否为Markdown文件
        if file_name.endswith('.md') and file_name != 'solution.md':
            return True
    return False

def main():
    
    # 基础目录路径
    base_dir = "submissions"
    
    # 遍历所有文件夹
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        
        # 只处理luogu开头的文件夹
        if not folder_name.startswith("luogu_") or not os.path.isdir(folder_path):
            continue
            
        problem_id = extract_problem_id(folder_name)
        if not problem_id:
            print(f"跳过无效文件夹: {folder_name}")
            continue
        
        # 检查文件夹中是否已存在Markdown文件
        if has_markdown_files(folder_path):
            print(f"文件夹 {folder_name} 中已存在Markdown文件，跳过题目: {problem_id}")
            continue
            
        print(f"处理题目: {problem_id}")
        
        # 获取题目内容
        title, content, limits, translated_content = get_luogu_problem_content(problem_id)
        if not title or not content or not limits:
            print(f"获取题目内容失败: {problem_id}")
            continue
            
        # 创建Markdown文件
        create_markdown_file(folder_path, title, content, limits, translated_content)
        
        # 避免请求过快，添加延迟
        # time.sleep(1)

if __name__ == "__main__":
    main()

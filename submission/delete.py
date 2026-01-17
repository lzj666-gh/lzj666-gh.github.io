import os
import re
from pathlib import Path

def fix_double_braces_in_files(directory, extensions=None):
    """
    批量处理指定目录下文件中的 {{ 和 }}，在它们之间添加空格
    
    Args:
        directory: 要处理的目录路径
        extensions: 要处理的文件扩展名列表，默认为 ['.md', '.html', '.markdown']
    """
    if extensions is None:
        extensions = ['.md', '.html', '.markdown']
    
    directory = Path(directory)
    
    for ext in extensions:
        for file_path in directory.rglob(f'*{ext}'):
            process_file(file_path)

def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正则表达式替换 {{ 和 }}
        # 替换 {{ 为 { {，替换 }} 为 } }
        # 使用正向回顾断言确保不会替换已经处理过的
        pattern = r'(?<!\{\s)\{(?=\{)|\}(?<!\}\s)\}(?=\})'
        
        def replace_braces(match):
            if match.group() == '{{':
                return '{ {'
            elif match.group() == '}}':
                return '} }'
            return match.group()
        
        new_content = re.sub(pattern, replace_braces, content)
        
        # 如果内容有变化，保存文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"已处理: {file_path}")
            
    except UnicodeDecodeError:
        print(f"跳过（编码问题）: {file_path}")
    except Exception as e:
        print(f"处理 {file_path} 时出错: {e}")

def fix_double_braces_in_text(text):
    """
    处理字符串中的 {{ 和 }}
    
    Args:
        text: 输入文本
        
    Returns:
        处理后的文本
    """
    # 简单的字符串替换方法
    result = text.replace('{{', '{ {').replace('}}', '} }')
    return result

def fix_double_braces_smart(text):
    """
    更智能的处理，避免在特定上下文中添加空格
    
    Args:
        text: 输入文本
        
    Returns:
        处理后的文本
    """
    # 使用正则表达式，避免在特定的模板语法中处理
    # 这个正则表达式会匹配不在特定模板命令中的 {{ 和 }}
    pattern = r'(?<!\{\s)\{(?=\{)|\}(?<!\}\s)\}(?=\})'
    
    def replace_braces(match):
        if match.group() == '{{':
            return '{ {'
        elif match.group() == '}}':
            return '} }'
        return match.group()
    
    return re.sub(pattern, replace_braces, text)

def create_backup(file_path):
    """创建文件备份"""
    backup_path = file_path.with_suffix(file_path.suffix + '.bak')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已创建备份: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"创建备份失败: {e}")
        return None

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='批量处理文件中的 {{ 和 }}，避免模板引擎错误解析')
    parser.add_argument('directory', help='要处理的目录路径')
    parser.add_argument('--ext', nargs='+', default=['.md', '.html', '.markdown'],
                       help='要处理的文件扩展名（默认: .md .html .markdown）')
    parser.add_argument('--backup', action='store_true', help='创建备份文件')
    parser.add_argument('--test', action='store_true', help='测试模式，不实际修改文件')
    
    args = parser.parse_args()
    
    directory = Path(args.directory)
    
    if not directory.exists():
        print(f"错误: 目录不存在: {directory}")
        exit(1)
    
    # 收集要处理的文件
    files_to_process = []
    for ext in args.ext:
        files_to_process.extend(directory.rglob(f'*{ext}'))
    
    print(f"找到 {len(files_to_process)} 个文件需要处理")
    
    for file_path in files_to_process:
        if args.backup and not args.test:
            create_backup(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 处理文本
            new_content = fix_double_braces_in_text(content)
            
            if new_content != content:
                if args.test:
                    print(f"需要处理: {file_path}")
                    # 显示一些示例
                    lines = content.split('\n')
                    new_lines = new_content.split('\n')
                    for i, (old_line, new_line) in enumerate(zip(lines, new_lines)):
                        if old_line != new_line and '{{' in old_line or '}}' in old_line:
                            print(f"  第 {i+1} 行:")
                            print(f"    原: {old_line}")
                            print(f"    新: {new_line}")
                else:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"已处理: {file_path}")
                    
        except UnicodeDecodeError:
            print(f"跳过（编码问题）: {file_path}")
        except Exception as e:
            print(f"处理 {file_path} 时出错: {e}")
    
    print("处理完成！")
    
    # 示例用法
    print("\n示例测试:")
    test_text = """第一次修改后序列为：$\langle 8,4,4,8,5\rangle$，可行的操作是 $\langle 8{\color{red}{{}+4}},4{\color{red}{{}+6}},4{\color{red}{{}+6}},8{\color{red}{{}+4}},5{\color{red}{{}+5}}\rangle$，最小极差为 $8{\color{red}{{}+4}}-(5{\color{red}{{}+5}})=2$。"""
    
    print("原始文本:")
    print(test_text)
    print("\n处理后的文本:")
    print(fix_double_braces_in_text(test_text))

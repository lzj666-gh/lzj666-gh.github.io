import os
import re 
from datetime import datetime
 
def batch_process_md():
    # 沉浸式配置区 
    FM_TEMPLATE = """---
title: 云剪切板
date: 2025-05-13 12:26:33 
---
"""  # 注意结尾的空行
    FILE_EXT = ".md"
    ENCODING = "utf-8"
    
    # 正则表达式配置（支持宽松匹配）
    FM_PATTERN = re.compile( 
        r'^---\s*[\r\n]+.*?[\r\n]+---\s*[\r\n]*',
        flags=re.DOTALL|re.MULTILINE 
    )
    
    # 环境初始化 
    cwd = os.getcwd() 
    processed = 0
    total_md = len([f for f in os.listdir(cwd)  if f.endswith(FILE_EXT)]) 
    
    print(f"⌛ 开始处理 | 目录：{cwd} | 待处理MD文件：{total_md}")
 
    # 核心处理逻辑 
    for filename in os.listdir(cwd): 
        if not filename.endswith(FILE_EXT)  or not os.path.isfile(filename): 
            continue
        
        filepath = os.path.join(cwd,  filename)
        
        try:
            with open(filepath, "r+", encoding=ENCODING) as f:
                raw_content = f.read() 
                
                # 分阶段处理 
                phase1 = FM_PATTERN.sub('',  raw_content, count=1).lstrip()
                new_content = FM_TEMPLATE + '\n' + phase1
                
                if new_content != raw_content:
                    f.seek(0) 
                    f.truncate() 
                    f.write(new_content) 
                    status = "✔ 已注入"
                    processed +=1
                else:
                    status = "○ 无需变更"
                
                print(f"{status} | {filename}")
                
        except UnicodeDecodeError:
            print(f"✘ 编码异常 | {filename}")
        except Exception as e:
            print(f"✘ 操作失败 | {filename} | 错误：{str(e)}")
 
    # 生成数字指纹 
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S") 
    print(f"\n🔚 任务完成 | 处理文件：{processed}/{total_md} | 操作指纹：FM_{timestamp}")
 
if __name__ == "__main__":
    batch_process_md()

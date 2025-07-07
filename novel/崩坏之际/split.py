import os
import datetime

def split_sections(input_file):
    # 读取所有章节内容
    sections = []
    current_section = []
    in_section = False
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.strip()
            # 检查是否为分割行（非空且行首非空格）
            if stripped_line and not line.startswith((' ', '　', '\t')):
                if in_section:
                    # 保存当前章节并开始新章节
                    sections.append(current_section)
                    current_section = [line]
                else:
                    # 开始第一个章节
                    in_section = True
                    current_section = [line]
            else:
                if in_section:
                    current_section.append(line)
    
    # 处理最后一个章节
    if in_section and current_section:
        sections.append(current_section)
    
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_chapters = len(sections)
    
    # 为每个章节创建Markdown文件
    for i, section in enumerate(sections):
        chapter_num = i + 1
        filename = f"{chapter_num:04d}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            # 写入Front Matter
            f.write("---\n")
            f.write(f"title: 崩坏之际第{chapter_num}章\n")
            f.write(f"date: {current_time}\n")
            f.write("---\n\n")
            
            # 写入章节内容
            f.writelines(section)
            
            # 添加导航链接
            f.write("\n\n")
            
            # 上一章链接
            if chapter_num == 1:
                f.write("[上一章](index)\n\n")
            else:
                prev_chapter = f"{chapter_num - 1:04d}"
                f.write(f"[上一章]({prev_chapter})\n\n")
            
            # 下一章链接
            if chapter_num == total_chapters:
                f.write("[下一章](index)\n")
            else:
                next_chapter = f"{chapter_num + 1:04d}"
                f.write(f"[下一章]({next_chapter})\n")

if __name__ == "__main__":
    input_filename = "崩坏之际.txt"
    split_sections(input_filename)
    print(f"文件分割完成！已生成{len([f for f in os.listdir() if f.endswith('.md') and f != 'index.md'])}个MD文件")

import os
 
def replace_md_links():
    # 配置参数
    old_url = "https://www.lzj-blog/paste" 
    new_url = "https://www.lzj-blog.top/paste" 
    target_ext = ".md"
    processed_count = 0
 
    # 获取当前工作目录
    cwd = os.getcwd() 
    print(f"■ 扫描目录：{cwd}")
 
    # 遍历目录文件
    for filename in os.listdir(cwd): 
        # 过滤目标文件
        if filename.endswith(target_ext)  and os.path.isfile(filename): 
            filepath = os.path.join(cwd,  filename)
            
            try:
                # 读取并替换内容 
                with open(filepath, "r+", encoding="utf-8") as f:
                    original = f.read() 
                    modified = original.replace(old_url,  new_url)
                    
                    # 仅当内容变化时写入 
                    if modified != original:
                        f.seek(0) 
                        f.truncate() 
                        f.write(modified) 
                        print(f"✔ 已更新：{filename}")
                        processed_count += 1
                    else:
                        print(f"○ 无变更：{filename}")
            except UnicodeDecodeError:
                print(f"✘ 解码失败：{filename}（请确认文件编码为UTF-8）")
            except Exception as e:
                print(f"✘ 处理错误：{filename} - {str(e)}")
 
    # 统计结果 
    print(f"\n■ 处理完成 | 共扫描到 {len([f for f in os.listdir(cwd)  if f.endswith(target_ext)])}  个MD文件")
    print(f"■ 实际修改：{processed_count} 个文件")
 
if __name__ == "__main__":
    replace_md_links()

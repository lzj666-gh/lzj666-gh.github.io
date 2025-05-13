import os 
import shutil 
 
def classify_md_files():
    # 定义路径参数 
    current_dir = os.getcwd() 
    hash_folder = os.path.join(current_dir,  "folder_with_hash")
    nohash_folder = os.path.join(current_dir,  "folder_without_hash")
    
    # 创建目标文件夹（如果不存在）
    os.makedirs(hash_folder,  exist_ok=True)
    os.makedirs(nohash_folder,  exist_ok=True)
 
    # 遍历当前目录下的所有文件 
    for filename in os.listdir(current_dir): 
        if filename.endswith(".md")  and os.path.isfile(filename): 
            file_path = os.path.join(current_dir,  filename)
            
            # 检测文件内容 
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read() 
                    has_hash = "{#" in content 
            except UnicodeDecodeError:
                print(f"⚠️ 解码失败: {filename} 可能包含非文本内容")
                continue 
            except Exception as e:
                print(f"❌ 读取错误: {filename} - {str(e)}")
                continue 
 
            # 确定目标路径 
            target_dir = hash_folder if has_hash else nohash_folder 
            try:
                shutil.move(file_path,  os.path.join(target_dir,  filename))
                print(f"✅ 已移动: {filename} → {os.path.basename(target_dir)}") 
            except shutil.Error as e:
                print(f"⛔ 移动失败: {filename} 已存在目标文件夹中")
 
if __name__ == "__main__":
    classify_md_files()

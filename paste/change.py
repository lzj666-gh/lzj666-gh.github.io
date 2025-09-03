import os
import shutil
import logging
from pathlib import Path

def organize_markdown_files():
    """
    扫描当前文件夹下的所有md文件，为每个文件创建同名文件夹，
    并将文件移入文件夹并重命名为index.md
    """
    # 设置日志记录
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # 获取当前工作目录
    current_dir = Path.cwd()
    logger.info(f"开始扫描目录: {current_dir}")
    
    # 查找所有md文件
    md_files = list(current_dir.glob("*.md"))
    
    if not md_files:
        logger.warning("未找到任何.md文件")
        return
    
    logger.info(f"找到 {len(md_files)} 个.md文件")
    
    # 处理每个md文件
    for md_file in md_files:
        try:
            # 获取文件名（不含扩展名）
            file_stem = md_file.stem
            
            # 创建目标文件夹
            target_dir = current_dir / file_stem
            target_dir.mkdir(exist_ok=True)
            logger.info(f"创建文件夹: {target_dir}")
            
            # 目标文件路径
            target_file = target_dir / "index.md"
            
            # 如果目标文件已存在，询问是否覆盖
            if target_file.exists():
                response = input(f"文件 {target_file} 已存在，是否覆盖？(y/N): ")
                if response.lower() != 'y':
                    logger.info(f"跳过文件: {md_file}")
                    continue
            
            # 移动并重命名文件
            shutil.move(str(md_file), str(target_file))
            logger.info(f"移动文件: {md_file} -> {target_file}")
            
        except Exception as e:
            logger.error(f"处理文件 {md_file} 时出错: {str(e)}")
    
    logger.info("处理完成")

if __name__ == "__main__":
    organize_markdown_files()

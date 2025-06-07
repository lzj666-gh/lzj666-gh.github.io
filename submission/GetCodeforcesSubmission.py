import requests
from bs4 import BeautifulSoup 
import os
import time 
import re
 
def get_submissions(cookie):
    """爬取所有提交记录ID和题目ID"""
    session = requests.Session()
    session.headers.update({ 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.6241 SLBChan/103'
    })
    
    base_url = "https://codeforces.com/submissions/" 
    handle = 'lzj666_cf'
    
    submissions = []
    page = 1
    max_page = 1
    
    while page <= max_page:
        url = f"{base_url}{handle}/page/{page}"
        try:
            response = session.get(url) 
            if response.status_code  != 200:
                print(f"⚠️ 页面请求失败: HTTP {response.status_code}")
                print(response.text)
                break
                
            soup = BeautifulSoup(response.text,  'html.parser') 
            
            # 首次访问时获取最大页码 
            if page == 1:
                pagination = soup.select_one('div.pagination  ul')
                if pagination:
                    page_links = pagination.select('li:not(.active):not(.arrow)') 
                    max_page = max([int(link.text)  for link in page_links if link.text.isdigit()]  + [1])
                    print(f"📚 共发现 {max_page} 页提交记录")
            
            # 解析提交记录表格
            table = soup.select_one('table.status-frame-datatable') 
            if not table:
                print("⛔ 未找到提交记录表格")
                break
                
            rows = table.select('tr[data-submission-id]') 
            for row in rows:
                submission_id = row['data-submission-id']
                problem_id = row['data-problemid']
                contest_id = row['data-contestid']
                submissions.append({ 
                    'submission_id': submission_id,
                    'problem_id': problem_id,
                    'contest_id': contest_id 
                })
            print(f"✅ 第 {page}/{max_page} 页: 获取到 {len(rows)} 条记录")
            page += 1 
            time.sleep(1.5)   # 避免请求过快 
        
        except Exception as e:
            print(f"❌ 处理第 {page} 页时出错: {str(e)}")
            break
            
    return submissions, session 
 
def get_submission_code(session, contest_id, submission_id):
    """获取单个提交的源代码"""
    url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}" 
    try:
        response = session.get(url) 
        soup = BeautifulSoup(response.text,  'html.parser') 
        code_pre = soup.find('pre',  id='program-source-text')
        return code_pre.text  if code_pre else None 
    except Exception as e:
        print(f"⚠️ 获取代码失败 ({submission_id}): {str(e)}")
        return None
 
def save_submissions(cookie):
    """主函数：保存所有提交记录"""
    submissions, session = get_submissions(cookie)
    total = len(submissions)
    success = 0 
    
    print(f"\n🔍 开始处理 {total} 条提交记录...")
    for idx, sub in enumerate(submissions, 1):
        # 获取代码内容 
        code = get_submission_code(session, sub['contest_id'], sub['submission_id'])
        if not code:
            continue
            
        # 创建题目目录
        dir_path = f"submissions/codeforces_{sub['problem_id']}"
        os.makedirs(dir_path,  exist_ok=True)
        
        # 保存代码文件
        file_path = f"{dir_path}/{sub['submission_id']}.txt"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code) 
            
        success += 1
        print(f"📥 [{idx}/{total}] 已保存: {file_path}")
        time.sleep(1)   # 请求间隔 
    
    print(f"\n🎉 完成! 成功保存 {success}/{total} 份代码文件")
 
# ===== 使用示例 =====
if __name__ == "__main__":
    # 替换为实际Cookie（登录后从浏览器获取）
    COOKIE = "JSESSIONID=; 39ce7=; handle="
    save_submissions(COOKIE)

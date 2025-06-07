import requests 
import json
import os 
import time
import pyluog 
from collections import deque
import logging 
 
def scrape_luogu_submissions(client_id, uid, begin_page = 1, wait_time = 5, MAX_RETRIES = 3):
    """
    爬取洛谷用户提交记录并保存到本地
    :param client_id: __client_id Cookie值
    :param uid: _uid Cookie值
    :param begin_page: 开始页码
    :param wait_time: 记录与记录之间的等待时间（秒）
    :param MAX_RETRIES: 最大重试次数
    """
    # 1. 配置日志系统 
    logging.basicConfig( 
        filename='submissions/error.log', 
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
    )
    
    # 2. 创建会话并设置Cookie 
    res = pyluog.User('*','*')
    s = requests.session() 
    requests.utils.add_dict_to_cookiejar(s.cookies,  {'__client_id': client_id, '_uid': uid})
    res.sess  = s 
    res.client_id_  = client_id
    res.uid  = int(uid)
    
    headers = {
        'Referer': 'https://www.luogu.com.cn/auth/login', 
        'Origin': 'https://www.luogu.com.cn', 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.421.0 Safari/537.36",
        "Accept": "*/*",
        'Connection': 'keep-alive',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrf-token': '',
        '__client_id': client_id,
        '_uid': uid
    }
    
    # 3. 创建存储目录 
    os.makedirs('submissions',  exist_ok=True)
    
    # 4. 初始化重试队列和失败计数器 
    retry_queue = deque()
    failure_count = {}
    
    # 5. 分页爬取提交记录 
    page = begin_page 
    while True:
        api_url = f'https://www.luogu.com.cn/record/list?_contentOnly=1&user=836542&page={page}'  
        try:
            print(f"正在爬取第 {page} 页...")
            response = res.sess.get(  
                api_url,
                headers=headers 
            )
            response.raise_for_status() 
            
            # 6. 解析API返回的JSON数据 
            data = response.json() 
            records = data['currentData']['records']['result']
            
            if not records:
                print("所有提交记录已爬取完毕")
                break
                
            print(f"第 {page} 页获取成功，共 {len(records)} 条记录")
            
            # 7. 处理每条提交记录
            for record in records:
                record_id = record['id']
                problem_id = record['problem']['pid']
                
                # 检查是否已在重试队列中 
                if record_id in failure_count:
                    continue
                    
                # 创建题目目录
                problem_dir = f"submissions/luogu_{problem_id}"
                os.makedirs(problem_dir,  exist_ok=True)
                save_path = f"{problem_dir}/{record_id}.txt"
                
                # 检查文件是否已存在 
                if os.path.exists(save_path): 
                    print(f"记录 {record_id} 已存在，跳过")
                    continue
                
                # 尝试获取代码
                try:
                    code = fetch_submission_code(res.sess,  record_id, headers)
                    
                    if code:
                        with open(save_path, 'w', encoding='utf-8') as f:
                            f.write(f"//  OJ: 洛谷\n")
                            f.write(f"//  提交ID: {record_id}\n")
                            f.write(f"//  题目ID: {problem_id}\n")
                            f.write(code)  
                        print(f"成功保存: {save_path}")
                    else:
                        # 首次失败加入重试队列 
                        failure_count[record_id] = 1
                        retry_queue.append((record_id,  problem_id))
                        print(f"记录 {record_id} 获取失败，加入重试队列")
                        
                except Exception as e:
                    failure_count[record_id] = 1 
                    retry_queue.append((record_id,  problem_id))
                    print(f"记录 {record_id} 处理异常: {str(e)}，加入重试队列")
                
                time.sleep(wait_time)   # 单条记录间隔
            
            page += 1 
            time.sleep(wait_time)    # 页面间间隔
            
        except Exception as e:
            print(f"页面 {page} 爬取失败: {str(e)}")
            time.sleep(wait_time)
            time.sleep(wait_time)   # 页面失败后延长等待 
            page += 1
    
    # 8. 处理重试队列 
    print(f"\n开始处理重试队列，共 {len(retry_queue)} 条记录需要重试...")
    while retry_queue:
        record_id, problem_id = retry_queue.popleft() 
        save_path = f"submissions/luogu_{problem_id}/{record_id}.txt"
        
        # 再次检查文件是否已在重试期间生成
        if os.path.exists(save_path): 
            print(f"记录 {record_id} 已存在，跳过重试")
            continue 
            
        try:
            print(f"重试记录 {record_id} (尝试 {failure_count[record_id]}/{MAX_RETRIES})")
            code = fetch_submission_code(res.sess,  record_id, headers)
            
            if code:
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(f"//  OJ: 洛谷\n")
                    f.write(f"//  提交ID: {record_id}\n")
                    f.write(f"//  题目ID: {problem_id}\n")
                    f.write(code) 
                print(f"重试成功: {record_id}")
            else:
                # 更新失败计数 
                failure_count[record_id] += 1
                
                if failure_count[record_id] < MAX_RETRIES:
                    retry_queue.append((record_id,  problem_id))
                    time.sleep(wait_time)   # 失败后等待
                else:
                    error_msg = f"记录 {record_id} 重试 {MAX_RETRIES} 次仍失败，跳过并记录日志"
                    print(error_msg)
                    logging.error(f"Record  failed after {MAX_RETRIES} retries: {record_id}, Problem: {problem_id}")
                    
        except Exception as e:
            failure_count[record_id] += 1 
            
            if failure_count[record_id] < MAX_RETRIES:
                retry_queue.append((record_id,  problem_id))
                print(f"记录 {record_id} 重试异常: {str(e)}，准备再次重试")
                time.sleep(5) 
            else:
                error_msg = f"记录 {record_id} {MAX_RETRIES} 次重试均异常: {str(e)}，记录日志"
                print(error_msg)
                logging.error(f"Record  failed after {MAX_RETRIES} retries with exception: {record_id}, "
                             f"Problem: {problem_id}, Error: {str(e)}")
        
        time.sleep(wait_time)   # 重试间隔 
    
    print("所有记录处理完成，程序结束")
 
def fetch_submission_code(session, record_id, headers):
    """获取单条提交的源代码"""
    try:
        code_url = f'https://www.luogu.com.cn/record/{record_id}?_contentOnly=1'  
        response = session.get(code_url,  headers=headers)
        response.raise_for_status()   # 检查HTTP状态码
        
        
        data = response.json() 
        
        # 检查JSON结构中是否包含源代码 
        if 'currentData' in data and 'record' in data['currentData']:
            return data['currentData']['record']['sourceCode']
        else:
            print(f"记录 {record_id} 返回数据格式异常")
            return None
            
    except requests.exceptions.RequestException  as req_err:
        print(f"请求错误 [{record_id}]: {str(req_err)}")
        return None
    except json.JSONDecodeError as json_err:
        print(f"JSON解析错误 [{record_id}]: {str(json_err)}")
        return None 
    except Exception as e:
        print(f"获取代码异常 [{record_id}]: {str(e)}")
        return None
 
if __name__ == "__main__":
    # 输入您的Cookie值（从浏览器开发者工具中获取）
    YOUR_CLIENT_ID = ""
    YOUR_UID = ""
    
    scrape_luogu_submissions(YOUR_CLIENT_ID, YOUR_UID, 1, 0.5, 5)

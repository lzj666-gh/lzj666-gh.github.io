from requests import*
import json
headers = {
    'Referer': 'https://www.luogu.com.cn/auth/login',
    'Origin': 'https://www.luogu.com.cn',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.421.0 Safari/537.36",
    "Accept": "*/*",
    'Connection': 'keep-alive',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrf-token':'',
    '__client_id':'7d4ce942a344e7a568229d274c7d1138cc450ea8',
    'uid':'836542'
}
res=get('https://www.luogu.com.cn/api/team/members/14398?limit=100&orderBy=group.no&page=1',headers=headers)
for t in json.loads(res.text)['members']['result']:
    print('    - {\n      title: \'%s\',\n      intro: \'%s\',\n      link: https://www.luogu.com.cn/user/%d,\n      avatar: \'%s\'\n    }'%(t['user']['name'],t['user']['slogan'],t['user']['uid'],t['user']['avatar']))

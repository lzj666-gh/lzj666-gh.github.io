# P2136 题解

第一次A这道题的时候刚学spfa，n=999的点和其他题解一样特判过，一直以为是数据错了。

今天围观一位dalao写这道题，困惑于WA90，恰好看到讨论里管理员说数据无误，思考了一段时间，发现坑点，终于能够不用特判A这道题了……

关键点：“拉近距离”的不一定是小明，也可能是小红。

题目中没有给出具体的源点汇点（不算迷惑人的题目背景的话），所以在做spfa的时候，分别以1和n为源点各做一遍，取min，才能得到正确答案。n=999的点就是在小红主动的情况下的解。

所以这是一道语文模板题（雾）

放一下正确解法代码




```cpp
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
const int mxn = 1007;
const int mxm = 10003;
int n,m,cnte,pre[mxn],cnt[mxn],dis[mxn];
struct edge{
    int v,nxt,w;
}e[mxm];
bool vis[mxn];
inline void adde(int u,int v,int w){e[++cnte].w = w,e[cnte].v = v,e[cnte].nxt = pre[u],pre[u] = cnte;}
void spfa(int x){
    queue<int> q;
    memset(dis,0x3f,sizeof(dis));
    dis[x] = 0;q.push(x);vis[x] = 1;
    while(!q.empty())
    {
        int t=q.front();q.pop();
        vis[t] = 0;
        if(cnt[t] > n){puts("Forever love");exit(0);}
        for(int i = pre[t];i;i = e[i].nxt)
            if(dis[t] + e[i].w < dis[e[i].v])
            {
                dis[e[i].v] = dis[t] + e[i].w;
                if(!vis[e[i].w]) q.push(e[i].v),cnt[e[i].v]++,vis[e[i].v] = 1;
            }
    }
    return;
}
int main(){
    int s,t,w;
    cin>>n>>m;
    for(int i = 1;i <= m;i++)
    {
        scanf("%d%d%d",&s,&t,&w);
        adde(s,t,-w);
    }
    spfa(1);
    int ans = dis[n];
    spfa(n);
    printf("%d",min(ans,dis[1]));
    return 0;
}
```
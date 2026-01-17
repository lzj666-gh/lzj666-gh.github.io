# P3254 题解

/\*
网络流的二分图匹配问题

可以直观的想到，二分图的左边是单位，右边是桌子

由于我们的特殊限制  每个单位只能在一个桌子坐一个人

所以我们就把每个单位向各个桌子连一道流量为1的边

由源点向每个单位连上 连上单位人数的边

由每个圆桌向汇点连上 圆桌人数的边

然后跑一下最大匹配  如果最大匹配数等于所有单位的人数和

那么就可以     完全安排  否则不能完全安排

这个题目的统计答案要比前两个好弄一点 枚举即可

\*/
    
    
    
    
    
    
    
```cpp
    #include<cstdio>
    #include<algorithm>
    #include<iostream>
    #include<cstring>
    #define INF 0x3e3e3e3e
    #include<queue>
    #define MAXN 100010
    using namespace std;
    struct Edge{
        int to;
        int nxt;
        int cup;
        int flow;
    }edge[MAXN << 1];
    int deep[MAXN];
    int head[MAXN];
    int cnt = 1,ans = 0;
    int n,m,s,t;
    queue<int>q; 
    int read()
    {
        int nm = 0,f = 1;
        char c = getchar();
        for(;!isdigit(c);c = getchar())if(c == '-')f = -1;
        for(;isdigit(c);c = getchar())nm = nm * 10 + c - '0';
        return nm * f;
    }
    void push(int vi,int vj,int wei)
    {
        cnt++;edge[cnt].to = vj;edge[cnt].cup = wei;edge[cnt].nxt = head[vi];head[vi] = cnt;
        cnt++;edge[cnt].to = vi;edge[cnt].nxt = head[vj];head[vj] = cnt;
    }
    bool bfs(int be,int ed)
    {
        while(!q.empty()) q.pop();
        memset(deep,0,sizeof(deep));
        deep[be] = 1;
        q.push(be);
        while(!q.empty())
        {
            int op = q.front();
            q.pop();
            for(int i = head[op]; i; i = edge[i].nxt)
            {
                int vj = edge[i].to;
                if(deep[vj] || edge[i].cup <= edge[i].flow)continue;
                deep[vj] = deep[op] + 1;
                q.push(vj);
                if(vj == ed)
                    return true;
            }
        }
        return false;
    }
    int dfs(int now,int ed,int flow)
    {
        if(flow == 0 || now == ed)return flow;
        int tot = 0,f;
        for(int i = head[now];i;i = edge[i].nxt)
        {
            int vj = edge[i].to;
            if(deep[vj] != deep[now] + 1)continue;
            int op = min(edge[i].cup - edge[i].flow,flow);
            if(f = dfs(vj,ed,op))
            {
                edge[i].flow += f;
                edge[i ^ 1].flow -= f;
                tot += f;
                flow -= f;
            }
            if(flow == 0)break;
        }
        if(tot == 0)deep[now] = 0;
        return tot;
    }
    void Dinic(int be,int ed)
    {
        while(bfs(be,ed))
            ans -= dfs(be,ed,INF);
    }
    int main()
    {
        n = read();m = read();s = n + m + 1;t = s + 1;
        for(int i = 1;i <= n;i++)
        {
            for(int j = 1;j <= m;j++)
            {
                push(i,j + n,1);
            }
        }
        for(int i = 1;i <= n;i++)
        {
            int op = read();
            push(s,i,op);
            ans += op;
        }
        for(int j = 1;j <= m;j++)
        {
            int op = read();
            push(j + n,t,op);
        }
        Dinic(s,t);
        if(ans == 0){
            printf("1\n");
            for(int i = 1;i <= n;i++)
            {
                for(int j = head[i];j;j = edge[j].nxt)
                {
                    int vj = edge[j].to;
                    if(vj != s && edge[j].flow)
                    {
                        printf("%d ",edge[j].to - n);
                    }
                }
                printf("\n");
            }
        }
        else{
            printf("0\n");
        }
        return 0;
}
```
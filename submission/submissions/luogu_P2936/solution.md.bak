# P2936 题解

## 首先感谢@JK_LOVER大犇相助，解决了我的困惑

	简化题意：求A到Z的最大流；

	本题作为网络流的板题，其实也并不是很板，还是考察了一些细节的：
1. 题目上的****管理员注****，其实注了跟没注一样，这是在我的满篇~~WA~~提交下实践出来的，所以duck直接处理建边：
   
   
   ![](https://cdn.luogu.com.cn/upload/image_hosting/ggdzvkgo.png)；
   
   
   2.本题使用卡无优化版本的dinic，会T飞7个点，但是其它题解上好像并未出现此问题~~可能是本人码风问题~~；
   
   
30pts代码：
```cpp
#include<bits/stdc++.h>
#define rg register int 
using namespace std;
int N,cnt=1,head[400040],dep[400040];
struct node{
	int nxt;
	int to;
	int w;
}edge[400040];
void add_edge(int u,int v,int w)
{
	edge[++cnt].nxt=head[u];
	edge[cnt].to=v;
	edge[cnt].w=w;
	head[u]=cnt;
}
bool bfs()
{
	memset(dep,0,sizeof dep);
	queue< int >x;x.push(1);
	dep[1]=1;
	while(!x.empty())
	{
		int u=x.front();
		for(rg i=head[u];i;i=edge[i].nxt)
		{
			int v=edge[i].to;
			if(!dep[v]&&edge[i].w)
			{
				dep[v]=dep[u]+1;
				x.push(v);
			}
			if(v==26) return 1;
		}
		x.pop();
	}
	return 0;
}
int dinic(int u,int flow)
{
	if(u==26) return flow;
	int k;int res=flow;
	for(rg i=head[u];i&&res;i=edge[i].nxt)
	{
		int v=edge[i].to;
		if(dep[v]==dep[u]+1&&edge[i].w)
		{
			k=dinic(v,min(edge[i].w,res));
			if(!k) dep[v]=0;
			edge[i].w-=k;
			edge[i^1].w+=k;
			res-=k;
		}
	}
	return flow-res;
}
int ans,flo;
signed main()
{
	scanf("%d",&N);
	while(N--)
	{
		char a,b;int w;
		cin>>a>>b>>w;
//		if(a>=97) a-=96;if(b>=97) b-=96;if(a>=65&&a<=90) a-=64;if(b>=65&&b<=90) b-=64;
		add_edge(int(a)-'A'+1,int(b)-'A'+1,w);
		add_edge(int(b)-'A'+1,int(a)-'A'+1,0);
	}
	while(bfs())
	{
		while(flo=dinic(1,INT_MAX)) ans+=flo;
	}
	printf("%d\n",ans);
	return 0;
}
```
100pts代码：
```cpp
#include<bits/stdc++.h>
#define rg register int 
using namespace std;
int N,cnt=1,head[4101],dep[4100];
int ans,flo;
struct node{
    int nxt;
    int to;
    int w;
}edge[11200];
void add_edge(int u,int v,int w)
{
    edge[++cnt].nxt=head[u];
    edge[cnt].to=v;
    edge[cnt].w=w;
    head[u]=cnt;
}
bool bfs()
{
    memset(dep,0,sizeof dep);
    queue< int >x;x.push(1);
    dep[1]=1;
    while(!x.empty())
    {
        int u=x.front();x.pop();
        for(rg i=head[u];i;i=edge[i].nxt)
        {
            int v=edge[i].to;
            if(!dep[v]&&edge[i].w)
            {
                dep[v]=dep[u]+1;
                if(v==26) return 1;
                x.push(v);
            }
        }
    }
    return 0;
}
int cur[4010];
int dinic(int u,int flow)
{
    if(u==26 || flow == 0) return flow;
    int k;int res=0;
    for(rg i=cur[u];i;i=edge[i].nxt)
    {
        cur[u] = i;
        int v=edge[i].to;
        if(dep[v]==dep[u]+1&&edge[i].w)
        {
            k=dinic(v,min(edge[i].w,flow));
            if(!k) continue;
            edge[i].w-=k;
            edge[i^1].w+=k;
            res+=k;flow -=k;
            if(flow == 0) break;
        }
    }
    return res;
}
signed main()
{
    scanf("%d",&N);
    while(N--)
    {
        char a,b;int w;
        cin>>a>>b>>w;
        add_edge(int(a-'A'+1),int(b-'A'+1),w);
        add_edge(int(b-'A'+1),int(a-'A'+1),0);
    }
    while(bfs())
    {
        memcpy(cur,head,sizeof(cur));
        int maxflow = dinic(1,19260817);
        ans += maxflow;
    }
    printf("%d\n",ans);
    return 0;
}
```

%%%，犇篇完结


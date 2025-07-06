# P4001 题解

### 大家都是网络流，这是最短路,我给大家来一种最短路的解法
![](https://cdn.luogu.com.cn/upload/pic/63309.png)
    从上图可以看出来，最小割就是最短路，把左下角作为起点，右上角作为终点，只要从左下角走到了右上角，就一定可以把图分成两份，
最短路就是最短的方式把图分成两份，然后再把每一个小三角形看成一个点，~~再跑最短路就行了~~

```cpp
#include<cstdio>
#include<algorithm>
#include<queue>
#include<cstring>
#define inf 2147483647
#define re register
#define maxn 9100000
using namespace std;
int head[maxn],n,m,k,start,end,ans,deep[maxn],dis[maxn],book[maxn];
struct node{int to,next,w;}edge[maxn];
void add(int u,int v,int w){edge[++k].next=head[u];edge[k].to=v;edge[k].w=w;head[u]=k;}
void read()
{
	re int temp,t1,t2;
	for(re int i=1;i<m;i++) scanf("%d",&temp),add(i*2,end,temp);
	for(re int i=2;i<n;i++)
	for(re int j=1;j<m;j++)
	{
		scanf("%d",&temp);
		t1=2*(i-2)*(m-1)-1+2*j;
		t2=2*(i-1)*(m-1)+2*j;
		add(t1,t2,temp);
		add(t2,t1,temp);
	}
	for(re int i=1;i<m;i++)
	{
		scanf("%d",&temp);
		t1=2*(n-2)*(m-1)-1+2*i;
		add(start,t1,temp);
	}//横 
	
	for(int i=1;i<n;i++)
	for(int j=1;j<=m;j++)
	{
		scanf("%d",&temp);
		t1=2*(i-1)*(m-1)-1+2*j;
		t2=t1-1;
		if(j==1) add(start,t1,temp);
		else if(j==m) add(t2,end,temp);
		else
		{
			add(t1,t2,temp);
			add(t2,t1,temp);
		}
	}//竖 
	
	for(int i=1;i<n;i++)
	for(int j=1;j<m;j++)
	{
		t1=2*(i-1)*(m-1)-1+2*j;
		t2=t1+1;
		scanf("%d",&temp);
		add(t1,t2,temp);
		add(t2,t1,temp);
	}
	//斜 
}
struct point
{
    int value;//距离 
    int id;//点
    point(int x,int y)
    {
        id=x;
        value=y;
    }
    friend bool operator <(point a,point b)
    {
        return a.value>b.value;
    } 
};
priority_queue<point> q;
int dijkstra(int s)
{
    for(int i=1;i<=end;i++) dis[i]=inf;
    dis[s]=0;
    q.push(point(s,0));
    while(!q.empty())
    {
        int u=q.top().id;
        q.pop();
        if(book[u]) continue;
        book[u]=1;
        for(int i=head[u];i>0;i=edge[i].next)
        {
            int v=edge[i].to;
            if(dis[v]>dis[u]+edge[i].w)
            {
                dis[v]=dis[u]+edge[i].w;
                if(!book[v])
                q.push(point(v,dis[v]));
            }
        }
    }
    return dis[end];
}
int main()
{
	scanf("%d %d",&n,&m);
	end=(2*n-2)*(m-1)+1;
	read();
	printf("%d",dijkstra(0));
	return 0;
}
```

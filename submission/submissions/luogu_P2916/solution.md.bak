# P2916 题解

此题明显是最小生成树的模板题...

kruskal算法...

值得注意的一点是：与奶牛谈话也需要时间，而且每条路都需要来回走两遍。

所以每条边的权值为：起点权值+终点权值+路的长度\*2.

然后就能直接跑最小生成树了......

PS：别忘了加上权值最小的点哦


下面粘上蒟蒻的丑陋代码...


```cpp
#include<bits/stdc++.h>
using namespace std;
int a[10001];
struct edge
{
    int l,r,v;
}
e[100001];
int f[10001];
bool cmp(edge a,edge b)
{
    return a.v<b.v;
}
int n,ans;
int find(int n)
{
    if(f[n]==n)
    {
        return n;
    }
    f[n]=find(f[n]);
    return f[n];
}
void bing(int m,int n)
{
    int x,y;
    x=find(m);
    y=find(n);
    f[x]=y;
}
int main()
{
    int p,num=0,road=0,s=0x7fffffff;
    scanf("%d%d",&n,&p);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
        s=min(s,a[i]);
    }
    for(int i=1;i<=p;i++)
    {
        num++;
        scanf("%d%d%d",&e[num].l,&e[num].r,&e[num].v);
        e[num].v=e[num].v*2+a[e[num].l]+a[e[num].r];   //改变边权
    }
    sort(e+1,e+num+1,cmp);
    for(int i=1;i<=n;i++)
    {
        f[i]=i;
    }
    for(int i=1;road<n-1;i++)    //最小生成树
    {
        if(find(e[i].l)!=find(e[i].r))
        {
            ans+=e[i].v;
            bing(e[i].l,e[i].r);
            road++;
        }
    }
    printf("%d",ans+s);
    return 0;
}
```
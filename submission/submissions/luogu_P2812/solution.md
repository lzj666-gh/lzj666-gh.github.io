# P2812 题解

tarjan的模板题（嗯可以看lrj的书


-第一问：至少要给多少个学校软件，才能保证所有学校都有软件用，也就是求缩点后入度为0的点的个数（因为入度为0的话没有其他学校能传软件给它）

-第二问：使缩点后所有学校的入度和出度都大于0（这样就可以给任意学校软件，然后所有学校都能用上软件


**如果是一个强连通图需要特判。**


```cpp
/*
ID: ylx14271
PROG: schlnet
LANG: C++
*/
#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<cstdio>
using namespace std;
int read()
{
    char ch=getchar();
    int x=0;
    while(ch<'0'||ch>'9')ch=getchar();
    while(ch>='0'&&ch<='9')x=(x<<3)+(x<<1)+ch-'0',ch=getchar(); 
    return x;
}
int s[20100],top;
int low[21000];//存能搜到的最早的点 
int pre[21000];//存自己的时间 
int dfs_clock; 
struct node
{
    int x,y,d;
} a[4000000];
int po[21000],m;
int n,x1;
int scc[21000],id;
int c[21000];//出度 
int r[21000];//入度 

void dfs(int u)
{
    top++;
    s[top]=u;
    low[u]=++dfs_clock; //存自己的时间和 
    pre[u]=dfs_clock; 
    for (int i=po[u];i!=0;i=a[i].d)
    {
        int v=a[i].y;//提出点 
        if (pre[v]==0)//没有扫过 
        {
            dfs(v);//扫一遍 
            low[u]=min(low[u],low[v]);//更新 
        } else
        if (scc[v]==0)//如果在别的联通块就不管了 
        {
            low[u]=min(low[u],pre[v]);
        }
    }
    int k; 
    if (pre[u]==low[u])//自己是自己的祖先（也就是扫不到时间更早的点了 
    {
        id++;
        while (1)
        {
            k=s[top];top--;
            scc[k]=id;
            if (k==u) break;
        }
    }
}
int main()
{
    freopen("schlnet.in","r",stdin);
    freopen("schlnet.out","w",stdout);
    n=read();
    for (int i=1;i<=n;i++)
    {
        x1=read();
        while (x1!=0)
        {
            m++;
            a[m].x=i;
            a[m].y=x1;
            a[m].d=po[a[m].x];
            po[a[m].x]=m;
            x1=read();
        }
    }//读入 
    for (int j=1;j<=n;j++)
    {//因为并不一定是个连通图，so 
        if (pre[j]==0) dfs(j);
    }
    for (int i=1;i<=m;i++)
    {
        if (scc[a[i].x]!=scc[a[i].y])//自己图内不管 
        {
            c[scc[a[i].x]]++;//x的出度+1 
            r[scc[a[i].y]]++;//y的入度+1 
        }
    } 
    int ans1=0;
    int ans2=0;
    for (int i=1;i<=id;i++)//统计出度入度为0的点的出现次数 
    {
        if (r[i]==0) ans1++;
        if (c[i]==0) ans2++;
    }
    ans2=max(ans2,ans1);//第二问，所有点要出度不为0而且入度不为0 
    if (id==1) ans1=1,ans2=0;//嗯要特判 
    printf("%d\n%d\n",ans1,ans2);
    return 0;
}
```
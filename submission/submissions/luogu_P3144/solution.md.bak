# P3144 题解

感觉楼上用并查集的题解注释太少，看起来好吃力，趁自己明白给大家讲讲自己的并查集做法...

首先读入相连的点，但这里不能直接合并建立并查集，因为并查集没有Ctrl+Z操作(就是无法分离两个已经合并的集合)，所以我们要先存起来，等所有的询问都读入之后，倒着进行操作。

我们考虑怎样倒着操作：

首先，读入数据，把所有的数据都存起来，其中x[i],y[i]表示第i次读入的关系，order[i]表示第i次读入的数是多少，ss[i]表示i是否在并查集里面，如果存在，则为0，不存在则为1。

之后，把所有没有去掉的点之间的关系都加到并查集里面，但是在这个题看来，应该tan90，因为读入节点个数N之后，就进行了N次关闭操作，但是为了代码的普适性，我保留了这部分代码。（其实是开始没注意，一些题解才发现这里可以删掉...）

接着，倒着处理读入的询问。从第i=n次开始，把与点order[i]有关的边读入，合并并查集，之后在把和该点有关的所有的可加入的边都加入并查集以后，判断并查集中集合的个数，并记录在ans[i]中，然后i--，重复以上步骤。

最后，从1开始到n-1，判断ans是否为1，如果为1，说明所有的点都是联通的，输出YES，否则输出NO，第n次询问的时候，所有的点都已经从并查集删除，因此一定是联通的，输出YES。


代码如下：

```cpp
#include<cstdio>
#include<cstring>
using namespace std;
int n,m,g[3001],x[3001],y[3001],order[3001],ss[3001],ans[3001],w;
//x[i],y[i]表示第i次读入的关系，order[i]表示第i次读入的数是多少，ss[i]表示i是否在并查集里面，如果存在，则为0，不存在则为1
//g[i]存储并查集，ans[i]存储第i次询问时并查集中有多少个集合。
int find(int u)
{
    if(g[u]!=u)g[u]=find(g[u]);
    return g[u];
}
void merg(int u,int v)
{
    u=find(u);
    v=find(v);
    if(u==v)return;
    g[u]=v;
}
int main()
{
    memset(ss,0,sizeof(ss));
    scanf("%d%d",&n,&m);
    for(int j=1;j<=n;j++)g[j]=j;
    for(int i=1;i<=m;i++)
        scanf("%d%d",&x[i],&y[i]);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&w);
        order[i]=w;
        ss[w]=1;
    }
```
/\*
//如果题目中关闭农场的个数小于N的时候要加上这段代码

    for(int i=1;i<=m;i++)

        if(ss[x[i]]==0&&ss[y[i]]==0)

            merg(x[i],y[i]);

\*/
```cpp
    for(int i=n;i>0;i--)
    {
        ss[order[i]]=0;
        for(int j=1;j<=m;j++)
            if(ss[x[j]]==0&&ss[y[j]]==0)
                merg(x[j],y[j]);
        ans[n]=0;
        for(int j=1;j<=n;j++)
            if(find(j)==j&&ss[j]==0)
                ans[i]++;
    }
    for(int i=1;i<=n-1;i++)
        if(ans[i]==1)printf("YES\n");
        else printf("NO\n");
    printf("YES");
    return 0;
}
```
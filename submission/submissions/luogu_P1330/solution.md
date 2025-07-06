# P1330 题解

这一题是一个好题。如果知道思路了，便会非常简单。但是如果不知道思路，却比较的难想出来。

我们来分析一下题目。首先，肯定要明确一点，那就是这个图是不一定联通的。于是，我们就可以将整张图切分成许多分开的连同子图来处理。然而最重要的事情是：如何处理一个连通图？

乍看下去，似乎无从下手，因为方案好像有很多种，根本就枚举不完。但是，关键要注意到题目中重要的两个条件，我们把它抽象成这两个要素：

##①每一条边所连接的点中，至少要有一个被选中。②每一条边所连接的两个点，不能被同时选中。由此，可以推断出：

#每一条边都有且仅有一个被它所连接的点被选中。

又因为我们要处理的是一个连通图。所以，对于这一个图的点的选法，可以考虑到相邻的点染成不同的颜色。

#于是，对于一个连通图，要不就只有两种选法（因为可以全部选染成一种色的，也可以全部选染成另一种色的），要不就是impossible！

所以，我们只需要找到每一个子连通图，对它进行黑白染色，然后取两种染色中的最小值，然后最后汇总，就可以了。

另外，要判断impossible，只需要加一个used数组，记录已经遍历了哪些点。如果重复遍历一个点，且与上一次的颜色不同，则必然是impossible的。

具体细节请见代码：

```cpp
#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>
#include<string>
#include<algorithm>
using namespace std;
struct Edge
{
    int t;
    int nexty;
}edge[200000];
int head[20000];
int cnt=0;//链式前向星
void add(int a,int b)//存边
{
    cnt++;
    edge[cnt].t=b;
    edge[cnt].nexty=head[a];
    head[a]=cnt;
}
bool used[20000]={0};//是否遍历过
int col[20000]={0};//每一个点的染色
int sum[2];//黑白两种染色各自的点数
bool dfs(int node,int color)//染色（返回false即impossible）
{
    if(used[node])//如果已被染过色
    {
        if(col[node]==color)return true;//如果仍是原来的颜色，即可行
        return false;//非原来的颜色，即产生了冲突，不可行
    }
    used[node]=true;//记录
    sum[col[node]=color]++;//这一种颜色的个数加1，且此点的颜色也记录下来
    bool tf=true;//是否可行
    for(int i=head[node];i!=0&&tf;i=edge[i].nexty)//遍历边
    {
        tf=tf&&dfs(edge[i].t,1-color);//是否可以继续染色
    }
    return tf;//返回是否完成染色
}
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    int a,b;
    while(m--)
    {
        scanf("%d%d",&a,&b);
        add(a,b);
        add(b,a);//存的是有向边，所以存两次
    }
    int ans=0;
    for(int i=1;i<=n;i++)
    {
        if(used[i])continue;//如果此点已被包含为一个已经被遍历过的子图，则不需重复遍历
        sum[0]=sum[1]=0;//初始化
        if(!dfs(i,0))//如果不能染色
        {
            printf("Impossible");
            return 0;//直接跳出
        }
        ans+=min(sum[0],sum[1]);//加上小的一个
    }
    printf("%d",ans);//输出答案
    return 0;
}
```
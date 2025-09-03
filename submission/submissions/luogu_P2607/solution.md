# P2607 题解

本题解比较啰嗦

尽力用最容易明白的语言来讲

希望对大家有帮助


基环树

一个听起来很高大上的名词

但是不要被这个名字吓跑了

其实这个题

思路很简单

没比一道普通的树形DP难多少

(依然不懂这个题为什么省选/NOI-,明明和树形DP入门题没有上司的舞会那么像)

只是细节比较多而已

(其实也不算很多啦)


认真读完题目我们会发现

因为一个骑士有且只有一个最讨厌的人

而且这个骑士不会讨厌自己

即该图中是没有自环的


然后
从网上搜的很多题解都是用无向图存边

然后用一些高超的技巧(如位运算)判断卡掉无向二元环

但是题解中的kczno1

这位神犇就没有使用无向图

事实证明存无向图是完全没有必要的


因为本身有向图就携带着指向上一个节点的信息

而且这个信息更利于维护我们删边之后的操作

这样
不仅省去了判断的麻烦

还有利于维护信息

何乐而不为?


所以
考虑这个有向图

我们把x所讨厌的人y设为x的父亲节点

这样考虑**每一个人都有且只有一条出边**

所以对一个"联通块"

只有根节点**有机会**形成环

即环一定包含根节点


为什么呢?

**因为一个点的出度只能为1**

考虑非根节点

它的出度一定是贡献给它的父亲的

而根节点它的出度只能贡献给它的后代

(这里的"根节点""叶子节点"都只是为了描述方便,并不严谨,也许可以理解为"删边以后的叶子和根"?)


所以我们又解决了一个问题:

**每个联通块内有且只有一个简单环**


这样
我们考虑把每个联通块的环上删一条边

这样它必然构成树

然后要注意

删掉的边所连接的两点x,y

是不能同时选的

所以我们分别强制x,y其中一个点不选

对新树跑DP

显然相邻的点是不能选的

所以得到状态转移方程:

用f[i][0/1]表示以i为根节点的子树选i/不选i所能获得的最大价值

则
f[i][0]=sigema(max(f[son][0],f[son][1])); for each son of i

f[i][1]=sigema(f[son][0]); for each son of i

应该就很清楚了


再一个细节就是

答案会爆int

我交了数遍

都卡在这里


代码:






```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#define maxn 2000000
using namespace std;
int n,cnt;
long long ans;
int root;
long long f[maxn][2];
int head[maxn],val[maxn],vis[maxn],fa[maxn];
struct edge
{
    int pre,to;
}e[maxn];
inline void add(int from,int to)
{
    e[++cnt].pre=head[from];
    e[cnt].to=to;
    head[from]=cnt;
}
void dp(int now)
{
    vis[now]=1;
    f[now][0]=0,f[now][1]=val[now];
    for(int i=head[now];i;i=e[i].pre)
    {
        int go=e[i].to;
        if(go!=root)
        {
            dp(go);
            f[now][0]+=max(f[go][1],f[go][0]);
            f[now][1]+=f[go][0];
        }
        else
        {
            f[go][1]=-maxn;
        }
    }
}
inline void find_circle(int x)
{
    vis[x]=1;
    root=x;
    while(!vis[fa[root]])
    {
        root=fa[root];
        vis[root]=1;
```
}//找环


 
```cpp
    dp(root);
    long long t=max(f[root][0],f[root][1]);
    vis[root]=1;
    root=fa[root]; 
    dp(root);
    ans+=max(t,max(f[root][0],f[root][1]));
    return;
}
inline int in()
{
    char a=getchar();
    while(a<'0'||a>'9')
    {
        a=getchar();
    }
    int t=0;
    while(a<='9'&&a>='0')
    {
        t=(t<<1)+(t<<3)+a-'0';
        a=getchar();
    }
    return t;
}
//写一下伪代码 
//在存的时候存一下每个人最讨厌的人为他的父亲
//对每个没访问的点DFS 
//在这个没访问的点所在的连通块上找环
//找到以后强制不选它的父亲对它进行DP
//然后强制不选它对它的父亲进行DP
//然后取一个最大值即可 
//在DP里面
//先考虑f[x][0]是不选x,初始值为0
//f[x][1]是选x,初值为val[x]
//这是一个很好的赋值方法
//然后跑DP就行了 
int main()
{
    n=in();
    for(int i=1;i<=n;i++)
    {
        val[i]=in();
        int x=in();
        add(x,i);
    //    add(i,x);
        fa[i]=x;
    }
    for(int i=1;i<=n;i++)
    {
        if(!vis[i])
        {
            find_circle(i);
        }
    }
    printf("%lld\n",ans);
    return 0;
}
```
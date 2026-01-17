# P4151 题解

[我的主页（阅读效果更好）打开即可$RP++$](https://www.luogu.org/space/show?uid=39914)

题目要求很多条边的最大异或和，从这一点我们可以想到线性基。这里归纳一下线性基的几点性质：

设$V$是某个神奇的向量空间，$B$是$V$的基，则$B$应满足以下条件：

> 1.$V$是$B$的极小生成集，就是说只有$B$能张成$V$，而它的任何真子集都不张成全部的向量空间。

> 2.$B$是$V$中线性无关向量的极大集合，就是说$B$在$V$中是线性无关集合，而且$V$中没有其他线性无关集合包含它作为真子集。

> 3.$V$中所有的向量都可以按唯一的方式表达为$B$中向量的线性组合。

这也就是说，我们可以用不超过$log_{2}{m}$个基就能表示所有的异或和，考虑题目中一句重要的话：

> 路径可以重复经过某些点或边，当一条边在路径中出现了多次时，其权值在计算 XOR 和时也要被计算相应多的次数

这句话给了我们一点启发，假设某条路$k$被重复走了两次，那么它的权值对答案的贡献就是$0$，但是通过这条路径$k$，我们可以到达它连接的另一个点。

显然我们没法枚举$1$~$N$的每一条路，但我们可以将路径拆成两部分，第一部分是环，第二部分是链。

假设我们选择了一条从$1$~$N$的链，当然，它不一定是最优秀的。但是别忘了，我们可以选择一些环来增广这条链。举个例子：

![](http://wx3.sinaimg.cn/mw690/0060lm7Tly1ft7x5h09fvj30ir090weg.jpg)

假设$k$是连接这条链和某个环的某条路径，那么显然，链和环都将走过一遍，而这条路径$k$会被走过两遍（从链到环一遍，从环到链一遍）。根据我们上面的推论，$k$对答案的贡献是$0$。于是我们发现，我们根本就没有必要算出这条路径$k$！（反正贡献是$0$）

于是我们枚举所有环，将环上异或和扔进线性基，然后用这条链作为初值，求线性基与这条链的最大异或和。

``` cpp
void dfs(int u,LL res) {//枚举所有环
    del[u]=res,vis[u]=1;
    for (int i=head[u];i;i=e[i].next)
        if (!vis[e[i].to]) dfs(e[i].to,res^e[i].w);
        else insert(res^e[i].w^del[e[i].to]);
}
LL query(LL x) {//最大异或和
    LL res=x;
    for (int i=63;i>=0;i--)
        if ((res^num[i])>res)
            res^=num[i];
    return res;
}
```

最后说一下怎么选最开始的这条链，其实**它可以随便选**。我们考虑以下这种情况：
![](http://wx4.sinaimg.cn/mw690/0060lm7Tly1ft7xo17vhuj30if09xmx5.jpg)

假设路径$A$比路径$B$优秀一些，而我们最开始选择了路径$B$。显然，$A$与$B$共同构成了一个环。如果我们发现路径$A$要优秀一些，那么我们用$B$异或上这个大环，就会得到我们想要的$A$！

所以这道题的算法是：找出所有环，扔进线性基，随便找一条链，以它作为初值求最大异或和就可以了。

附上AC代码：

``` cpp
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long
LL num[70];
bool insert(LL x) {
    for (int i=63;i>=0;i--)
        if ((x>>i)&1) {
            if (!num[i]) {
                num[i]=x;
                return true;
            }
            x^=num[i];
        }
    return false;
}
LL query(LL x) {
    LL res=x;
    for (int i=63;i>=0;i--)
        if ((res^num[i])>res)
            res^=num[i];
    return res;
}
struct edge {
    int to,next;
    LL w;
}e[200010];
int head[50010],ecnt;
inline void adde(int from,int to,LL w) {
    e[++ecnt]=(edge){to,head[from],w},head[from]=ecnt;
    e[++ecnt]=(edge){from,head[to],w},head[to]=ecnt;
}
int vis[50010];LL del[50010];
void dfs(int u,LL res) {
    del[u]=res,vis[u]=1;
    for (int i=head[u];i;i=e[i].next)
        if (!vis[e[i].to]) dfs(e[i].to,res^e[i].w);
        else insert(res^e[i].w^del[e[i].to]);
}
int main() {
    int n,m,a,b;LL c;scanf("%d%d",&n,&m);
    for (int i=1;i<=m;i++) scanf("%d%d%lld",&a,&b,&c),adde(a,b,c);
    dfs(1,0);
    printf("%lld\n",query(del[n]));
}
```
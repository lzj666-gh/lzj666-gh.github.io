# P2341 题解

[题目传送门](https://www.luogu.org/problemnew/show/P2341)

标签：$tarjan$求强联通分量

### 何为强联通分量

有向图强连通分量：在有向图$G$中，如果两个顶点$V_i,V_j$间（$V_i>V_j$）有一条从$V_i$到$V_j$的有向路径，同时还有一条从$V_i$到$V_j$的有向路径，则称两个顶点强连通。如果有向图$G$的每两个顶点都强连通，称$G$是一个强连通图。有向图的极大强连通子图，称为强连通分量。 ——百度百科
                          
事实上，你大概可以理解为：如果一个图的子图中，任意两点可以相互到达，那么这就组成了一个强联通分量。

如果还不理解怎么办？没关系，我们上图像来理解

![](http://www.th7.cn/d/file/p/2015/03/16/37f854f9c53856f0bf6d323e36e942d3.png)

如图，在这个有向图中，一共有$\{1,2,3,4\},\{5\},\{6\}$三个强联通分量

### 如何求强联通分量

我们需要两个非常重要的数组，在这里先说明一下

$1.dfn$，表示这个点在$dfs$时是第几个被搜到的。

$2.low$，表示这个点以及其子孙节点连的所有点中$dfn$最小的值

$3.stack$，表示当前所有可能能构成是强连通分量的点。

$4.vis$，表示一个点是否在$stack$数组中。

我们使用$tarjan$的方法
(1)、首先初始化$dfn[u]=low[u]=$第几个被$dfs$到

(2)、将$u$存入$stack[ ]$中，并将$vis[u]$设为$true$

(3)、遍历$u$的每一个能到的点，如果这个点$dfn[ ]$为$0$，即仍未访问过，那么就对点$v$进行$dfs$，然后$low[u]=min\{low[u],low[v]\}$

(4)、假设我们已经$dfs$完了$u$的所有的子树那么之后无论我们再怎么$dfs$，$u$点的$low$值已经不会再变了。

至此，$tarjan$完美结束

那么如果$dfn[u]=low[u]$这说明了什么呢？

再结合一下$dfn$和$low$的定义来看看吧

$dfn$表示$u$点被$dfs$到的时间，$low$表示$u$和$u$所有的子树所能到达的点中$dfn$最小的。

这说明了$u$点及$u$点之下的所有子节点没有边是指向u的祖先的了，即我们之前说的$u$点与它的子孙节点构成了一个最大的强连通图即强连通分量

此时我们得到了一个强连通分量，把所有的u点以后压入栈中的点和u点一并弹出，将它们的$vis[ ]$置为$false$，如有需要也可以给它们打上相同标记（同一个数字）


------------


$Q:$ $dfn$可以理解，但为什么$low$也要这么做呢？

$A:$因为low的定义如上，也就是说如果没有子孙与u的祖先相连的话，$dfn[u]$一定是它和它的所有子孙中$dfn$最小的（因为它的所有子孙一定比他后搜到）。

$Q:$ $stack[]$有什么用？

$A:$如果$u$在$stack$中，$u$之后的所有点在$u$被回溯到时$u$和栈中所有在它之后的点都构成强连通分量。

$Q:$ $low[ ]$有什么用？

$A:$应该能看出来吧，就是记录一个点它最大能连通到哪个祖先节点（当然包括自己）

如果遍历到的这个点已经被遍历到了，那么看它当前有没有在$stack[ ]$里,如果有那么$low[u]=min\{low[u],low[v]\}$

如果已经被弹掉了，说明无论如何这个点也不能与$u$构成强连通分量，因为它不能到达$u$

如果还在栈里，说明这个点肯定能到达$u$，同样$u$能到达他，他俩强联通。

接下来，就是非$(sang)$常$(xin)$简$(bing)$单$(kuang)$的手$\%$过程了

从节点$1$开始$DFS$，把遍历到的节点加入栈中。搜索到节点$u=6$时，$DFN[6]=LOW[6]$，找到了一个强连通分量。退栈到$u=v$为止，$\{6\}$为一个强连通分量。

![](http://www.th7.cn/d/file/p/2015/03/16/d8aa8e62b42fd3d5da5ade0fe90cffa6.png)

之后返回节点$5$,发现$DFN[5]=LOW[5]$，于是我们又找到了一个新的强联通分量$\{5\}$

![](http://www.th7.cn/d/file/p/2015/03/16/ce2022b95cc040b0fbb2109df448dbbd.png)

返回节点$3$，继续搜索到节点$4$，把$4$加入堆栈。发现节点$4$向节点$1$有后向边，节点$1$还在栈中，所以$LOW[4]=1$。节点$6$已经出栈，$(4,6)$是横叉边，返回$3$，$(3,4)$为树枝边，所以$LOW[3]=LOW[4]=1$。

![](http://www.th7.cn/d/file/p/2015/03/16/7d6d8c0516311035c8fe6f897eb7b911.png)

继续回到节点$1$，最后访问节点$2$。访问边$(2,4)$，$4$还在栈中，所以$LOW[2]=DFN[4]=5$。返回$1$后，发现$DFN[1]=LOW[1]$，把栈中节点全部取出，组成一个连通分量$\{1,3,4,2\}$。

![](http://www.th7.cn/d/file/p/2015/03/16/b962e2b6b609aaf75d5e096d510a4251.png)

至此，$tarjan$算法结束，我们找到了全部的$3$个强联通分量$\{1,2,3,4\},\{5\},\{6\}$

程序实现代码如下
```cpp
inline int tarjan(int u) 
{
	low[u]=dfn[u]=++dfn_sum;
	stack[top++]=u;
	for(int i=head[u];i;i=e[i].next)
	{
		int v=e[i].to;
		if(dfn(v))
			low[u]=min(low[u],dfn[v]);
		else
		{
			tarjan(v);
			low[u]=min(low[u],low[v]);
		}
	}
	if(low[u]==dfn[u])
	{
		int now=stack[--top];s_sum++;
		s[u]+=s_sum;
		while(now!=u)
		{
			s[now]=s_num;
			now=s[--top];
		}
	}
}
```

所以，我们再来分析一下这道题。

首先，不难发现，如果这所有的牛都存在同一个强联通分量里。那么它们一定互相受欢迎。

那么，我们怎么来找明星呢。

很简单，找出度为$0$的强联通分量中的点。这样可以保证所有的人都喜欢它，但是它不喜欢任何人，所以说不存在还有人事明星。

此题还有一个特殊情况：

如果有两个点分别满足出度为零的条件，则没有明星，这样无法满足所有的牛喜欢他。

有了上边的解释，题目就不是那么难了，代码如下
```cpp
#include<bits/stdc++.h>
#define ri register int
using namespace std;
const int maxn=1e4+5;
const int maxm=5e4+5;
int to[maxm],nex[maxm],fir[maxn];
int col,num,dfn[maxn],low[maxn],de[maxn],si[maxn];
int tot=0,co[maxn],n,m;
int top,st[maxn];
template<class T> inline void read(T &x)
{
    x=0;
    register char c=getchar();
    register bool f=0;
    while (!isdigit(c)) f ^=c=='-',c=getchar();
 	while (isdigit(c)) x=x*10+c-'0',c=getchar();
    if(f)x=-x;
}
template <class T> inline void print(T x)
{
    if(x<0)putchar('-'),x=-x;
    if(x>9)print(x/10);
    putchar('0'+x%10);
}
inline void ins(int x,int y)
{
    to[++tot]=y;
    nex[tot]=fir[x];
    fir[x]=tot;
}
void Tarjan(int u)
{
    dfn[u]=low[u]=++num;
    st[++top]=u;
    for(int i=fir[u];i;i=nex[i])
    {
        int v=to[i];
        if(!dfn[v])
        {
            Tarjan(v);
            low[u]=min(low[u],low[v]);
        }
        else if(!co[v])low[u]=min(low[u],dfn[v]);
    }
    if(low[u]==dfn[u])
    {
        co[u]=++col;
        ++si[col];
        while(st[top]!=u)
        {
            ++si[col];
            co[st[top]]=col;
            --top;
        }
        --top;
    }
}
int main()
{
    int x,y;
    read(n);read(m);
    for(ri i=1;i<=m;i++)
    {
        read(x);read(y);
        ins(y,x);
    }
    for(ri i=1;i<=n;i++)
        if(!dfn[i])Tarjan(i);
    for(ri i=1;i<=n;i++)
        for(ri j=fir[i];j;j=nex[j])
            if(co[i]!=co[to[j]])de[co[to[j]]]++;
    int ans=0,u=0;
    for(ri i=1;i<=col;i++)if(!de[i])ans=si[i],u++;
    if(u==1)print(ans);
     else print(0);
 	return 0;
}
```
# P3402 题解

$\text{Upd. 2024/11/28}$ 修补了 $\LaTeX$，和一些错误，感谢评论区的提醒。还望管理员通过。

作为可持久化大家族的一员，题解区竟然没有多少在线的做法，真是可悲啊 ~~太好了，可以交题解了~~

#### [传送门](https://www.luogu.com.cn/problem/P3402)

------------
相比与之前的并查集，我们多出了返回之前版本的操作。

那么版本和版本之间的根本差别就是 $\text{fa}$ 数组。

我们考虑对 $\text{fa}$ 数组进行可持久化，具体的，我们在开始操作前建立一棵可持久化线段树。

线段数的叶子 $[l,l]$ 表示的是编号为 $l$ 的数的父亲。

但是这样是不够的。考虑原本的并查集的 $\text{find}$ 函数。

```cpp
int find(int now)
{
	if(fa[now]==now)return now;
	reutrn fa[now]=find(fa[now]);
}
```

我们知道，平常时候使用的并查集优化是路径压缩，查询复杂度是均摊 $O(n\alpha)$ 的。
 
但是均摊并不可以，因为我们无法保证某次查询复杂度不为 $O(n)$，这样对于可持久化来说是毁灭性的，如果你操作一次为 $O(n)$，那么我们可能会被要求返回这个版本，再次进行这种~~不讲武德~~的操作。
 
所以我们要寻找一种 $\text{find}$ 方式，使得我们的复杂度为单次严格 $O(\log n)$ 的。

这时候，按秩合并就出现了，他就有单次 $O(\log n)$ 的优美复杂度，还是严格的。

具体的，按秩合并有多重方式，

1. 按照深度

2. 按照大小

3. 随机

好的我们考虑前两个~~因为第3个被卡掉了~~

这里只讲深度，因为比较好理解，一次查询的复杂度应该为 $u\to root$ 的距离，虽然这是棵树，但是不能保证~~邪恶的~~出题人不会给我们一条链子。


- 按照深度：我们不但记录某个点的 $\text{fa}$ 还需要记录这个点的子树的深度 $\text{dep}$。

对于一次操作合并 $u,v$。

我们让 $u=\text{find}(u),v=\text{find}(v)$。

考虑把两者合并起来（假定 $\color{red}{\text{dep}_u\ge \text{dep}_v}$）

我们显然应该把 $v$ 的子树合并到 $u$ 的下面。

只有这样才能保证深度尽可能的小。

我们考虑 $\text{dep}_u$ 变成了什么？

- 如果 $\text{dep}_u=\text{dep}_v$，那么我们把 $v$ 放到 $u$ 的下方，$\text{dep}_v$ 增大了 $1$。由于 $\text{dep}_u$ 表示的是以 $u$ 为根节点的深度所以 $\text{dep}_u=\text{dep}_v+1$

- 如果 $\text{dep}_u>\text{dep}_v$ 深度不变。

如果按这样合并的顺序的话，全部合并完，我们的树高最大也只有 $\log n$。

所以复杂度为严格单次 $O(\log n)$。

那么具体的，对于一次修改，我们需要新建 **$\color{red}\text{2}$** 个版本。

首先将这个版本中的 $\text{fa}_v$ 变为 $u$，接着，我们需要修改 $\text{dep}_u$。

### 注意！

这个过程中新建立了两个版本！！！！

不能贪心的在修改 $\text{dep}_u$ 的时候直接在原本的版本上修改。

如果这样的话你会获得 $88\text{pts}$ 的好成绩。

上代码~

ps.复杂度还是很可以的，不开O2依然很稳。

### $\text{CODE}$

```cpp
#include<bits/stdc++.h>
#define N 300005
using namespace std;
int read()
{
	int x=0,f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	return x*f;
}
int n,m,now,to,cnt,rt[N];
struct tree
{
	int ls,rs,fa,dep;
}tr[N*20];
inline int build(int l,int r)
{
	int to=++cnt;
	if(l==r)
	{
		tr[to].fa=l;
		return to;
	}
	int mid=(l+r)>>1;
	tr[to].ls=build(l,mid);
	tr[to].rs=build(mid+1,r);
	return to;
}
inline int que(int now,int l,int r,int x)
{
	if(l==r)return now;
	int mid=(l+r)>>1;
	if(mid>=x)return que(tr[now].ls,l,mid,x);
	else return que(tr[now].rs,mid+1,r,x);
}
inline int find(int now,int a)
{
	int fa=que(rt[now],1,n,a);
	if(tr[fa].fa==a)return fa;
	return find(now,tr[fa].fa);
}
inline int news(int now)
{
	int to=++cnt;
	tr[to]=tr[now];
	return to;
}
inline int hb(int now,int l,int r,int x,int f)
{
	int to=news(now);
	if(l==r)
	{
		tr[to].fa=f;
		return to;
	}
	int mid=(l+r)>>1;
	if(mid>=x)tr[to].ls=hb(tr[now].ls,l,mid,x,f);
	else tr[to].rs=hb(tr[now].rs,mid+1,r,x,f);
	return to;
}
inline int add(int now,int l,int r,int x)
{
	int to=news(now); 
	if(l==r)
	{
		tr[to].dep++;
		return to;
	}
	int mid=(l+r)>>1;
	if(mid>=x)tr[to].ls=add(tr[now].ls,l,mid,x);
	else tr[to].rs=add(tr[now].rs,mid+1,r,x);
	return to;
}
inline void merge(int now,int a,int b)
{
	rt[now]=rt[now-1];
	a=find(now,a);b=find(now,b);
	if(tr[a].fa!=tr[b].fa)
	{
		if(tr[a].dep>tr[b].dep)swap(a,b);
		rt[now]=hb(rt[now-1],1,n,tr[a].fa,tr[b].fa);
		if(tr[a].dep==tr[b].dep)rt[now]=add(rt[now],1,n,tr[b].fa);
	} 
}
inline bool pan(int now,int a,int b)
{
	a=find(now,a),b=find(now,b);
	if(tr[a].fa==tr[b].fa)return 1;
	else return 0;
}
int main()
{
	n=read();m=read();
	rt[0]=build(1,n);
	int op,a,b;
	for(int i=1;i<=m;i++)
	{
		op=read();a=read();
		if(op==1)
		{
			b=read();
			merge(i,a,b);
		}
		if(op==2)rt[i]=rt[a];
		if(op==3)
		{
			b=read();
			if(pan(i-1,a,b))cout<<1<<"\n";
			else cout<<0<<"\n";
			rt[i]=rt[i-1];
		}
	}
	return 0;
}
```

如果你不是很懂为什么需要建立两个版本可以看这里：

首先我们需要明确新建的两个版本是什么。

1. 将 $\text{fa}_v$ 变成 $u$ 这一步很好理解，没有什么问题。

2. 将 $\text{dep}_u$ 更新，这里很重要，一定要新建一个版本来更新 $\text{dep}_u$ 否则会复杂度错误。

如果你不新建版本而是直接修改 $\text{dep}_u$ ，那么假如当前版本是 $now$，我们知道 $now$ 这个版本是 $now-1$ 版本修改 $\text{fa}_v$ （即 1. ） 产生的，因此 $now$ 和 $now-1$ 所对应的 $\text{dep}_u$ 实际上是同一个数组。

如果你在 $now$ 版本直接修改了 $\text{dep}_u$ 那么意味着 $now-1$ 版本的 $\text{dep}_u$ 同时被修改了，那么这时候，我们的 $\text{dep}$ 数组就有可能不满足按秩合并的优美性质了，此时如果数据让我们回溯到 $now-1$ 版本修改，那么可能就会导致按秩合并出错，从而导致复杂度错误。
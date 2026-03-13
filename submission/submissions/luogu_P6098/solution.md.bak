# P6098 题解

# Solution For P6098  
$By\text{ }ShadderLeave$  
这道题目是一道点权树链剖分叠线段树的题目，码量相对不高，适合入门练手。  
比起最最朴素（维护点权和/最大值）的树链剖分来说，略略有一点点变化，就是需要维护的操作有些奇怪是[异或](https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677?fr=aladdin)，但是没什么影响，有的盆友担心异或不能用线段树维护，~~不要害怕，维护异或的最好方法是面对异或~~，因为异或可以看做是每一个数变成了 $31(int)$ 个 $01$ 然后排成一张表，对于每一位只用关心有奇数个还是偶数个 $1$ 就行了（翻译：**异或运算满足交换律与结合律**）  
那么这道题就变成板子题目了，线段树的节点表示其代表区间内所有节点的异或值，刚刚已经说过满足交换律和结合律，所以回答询问的时候直接按照一般的树链剖分方法来就行。  
换句话说 将一条路径根据划分的轻重链来分成几个区间，然后使用线段树维护区间异或值，由于满足结合律所以先计算**一个个的区间异或值最后异或在一起的结果 和 要求的路径异或值相等**，所以线段树的维护是正确的。  
（别打着打着迷路了，**运算符都是异或**）  
那么....上代码？  
```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn=100007;
int N,Q,ix;
struct E{
	int u,v;
}e[maxn<<1];
int first[maxn],nt[maxn<<1],ES;
int TREE[maxn<<2];
int depth[maxn],sz[maxn],top[maxn],A[maxn];
//A数组是点权
int son[maxn],id[maxn],anti[maxn],fa[maxn];
//id是节点->线段树编号的映射 anti是线段树编号->节点的映射(反向映射)
inline void addE(int u,int v)
{
	e[++ES]=(E){u,v};
	nt[ES]=first[u];
	first[u]=ES;
	e[ES+N]=(E){v,u};
	nt[ES+N]=first[v];
	first[v]=ES+N;
	return ;
}
inline int Re()
{
	char c;
	int re,f=1;
	while((c=getchar())>'9'||c<'0')
	if(c=='-') f=-1;
	re=c-48;
	while((c=getchar())>='0'&&c<='9')
	re=re*10+c-48;
	return re*f;
}
inline void DFS(int u)
{
	sz[u]=1;
	int v;
	for(int i=first[u];i;i=nt[i])
	{
		v=e[i].v;
		if(v!=fa[u])
		{
			depth[v]=depth[u]+1;
			fa[v]=u;
			DFS(v);
			sz[u]+=sz[v];
			if(sz[v]>sz[son[u]]) son[u]=v;
		}
	}
	return ;
}
inline void dfs(int u,int tp)
{
	top[u]=tp;
	id[u]=++ix;anti[ix]=u;
	if(son[u]) dfs(son[u],tp);
	int v;
	for(int i=first[u];i;i=nt[i])
	{
		v=e[i].v;
		if(v!=fa[u]&&v!=son[u])
			dfs(v,v);
	}
	return ;
}
#define mid (L+R>>1)//习惯加上括号因为位运算优先级低谁也不知道会发生什么qwq
inline void Build(int L,int R,int i)
{
	if(L==R)
	{
		TREE[i]=A[anti[L]];
		return ;
	}
	Build(L,mid,i<<1);
	Build(mid+1,R,i<<1|1);
	TREE[i]=TREE[i<<1]^TREE[i<<1|1];
	return ;
}
inline void Update(int L,int R,int x,int i,int k)
{
	if(L==R)//单点修改 [L,R]是当前区间
	{
		TREE[i]=k;
		return ;
	}
	if(x<=mid) Update(L,mid,x,i<<1,k);
	else Update(mid+1,R,x,i<<1|1,k);//单点修改非此即彼直接else即可
	TREE[i]=TREE[i<<1]^TREE[i<<1|1];//使用异或运算符更新
	return ;
}
inline int QwQ(int L,int R,int l,int r,int i)
{//[L,R]是当前区间，[l,r]是待查区间
	if(l<=L&&R<=r)
		return TREE[i];
	int ans=0;//切记初始化为0
	if(l<=mid) ans^=QwQ(L,mid,l,r,i<<1);//全部是异或
	if(r>mid) ans^=QwQ(mid+1,R,l,r,i<<1|1);
	return ans;
}
inline int Query_Path(int x,int y)
{
	int ans=0;//切记初始化为0
	while(top[x]!=top[y])
	{
		if(depth[top[x]]<depth[top[y]]) swap(x,y);
		ans^=QwQ(1,N,id[top[x]],id[x],1);
		x=fa[top[x]];
	}
	if(depth[x]>depth[y]) swap(x,y);
	ans^=QwQ(1,N,id[x],id[y],1);
	return ans;
}
int main()
{
	N=Re();Q=Re();
	int u,v,s;
	for(int i=1;i<=N;i++)
		A[i]=Re();
	for(int i=1;i<N;i++)
	{
		u=Re();v=Re();
		addE(u,v);
	}
	DFS(1);dfs(1,1);
	Build(1,N,1);
	for(int i=1;i<=Q;i++)
	{
		s=Re();u=Re();v=Re();
		if(s==1)
			 Update(1,N,id[u],1,v);
		else printf("%d\n",Query_Path(u,v));
	}
	return 0;
}
```
这是较为简单的一道树链剖分题目，没有懒惰标记，也没有大的变形，大家在熟练掌握点权树链剖分之后可以开始了解维护边权树链剖分以及一些在原有的算法上巧妙变形的题目。[边权树链剖分板子](https://www.luogu.com.cn/blog/ShadderLeave/solution-p3038)，另外因为有些树链剖分题目实在太毒瘤，窝建立了一个题单来巩固代码熟练程度，[欢迎大家来van](https://www.luogu.com.cn/training/1654#problems)。  
谢谢管理大大审核^_^
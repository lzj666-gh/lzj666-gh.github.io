# P3038 题解

Upd On 2020-03-18 既然题单都出了那么就把原来的剪贴板换成题单吧qwq  
此篇题解意在提供一套树链剖分边权转点权的板子。
# A Solution For P3038
需要的前置芝士(没吃过的请加餐):  
[线段树](https://www.luogu.com.cn/problem/P3373)  [轻重链剖分](https://www.luogu.com.cn/problem/P3384)  
前置芝士次掉以后,你应该知道了使用树链剖分和线段树结合来处理以下几种基本问题:  
- 维护树上任意两点间简单路径包含的点的点权 和/最大值
- 维护树上任意单点的点权信息
- 维护树上任意一棵子树内的点权 和/最大值  

核心思想是通过剖分将其划分成可用线段树操作的区间,再利用线段树进行维护  
但是对于这一道题目,是要维护树上边权的相关信息,怎么办呢？
我们可以将边权转化为点权。（这个人又在说废话了）  
但是怎么转化？？  
我们的转化肯定是要将边映射到点上,很明显我们不可以让一个点同时对应多条边,也不可以让一条边对应多个点,这两种情况都是无法使用线段树进行相应维护的  
所以只能一对一进行映射  
画一棵树,观察一下,很快就可以发现,对于每一条边的两端的节点,我们只能选一个映射,而我们会选择深度较深的点进行映射,否则如果这个深度较浅的节点有多个儿子,这些儿子都会映射到这个节点上,GG。  

**下面给出树链剖分边权转点权的模板,代码后会有核心代码总结。**  

包含操作  
- 路径 询问/更新(边权和)
- 子树 询问/更新(边权和)  

```cpp
#include<bits/stdc++.h>
using namespace std;
int N,Q; 
inline int max_(const int &x,const int &y)
{
	return x>y?x:y;
}
const int maxn=2007;//总结点数
int TREE[maxn<<2];//四倍空间线段树
int lazy[maxn<<2];//懒惰标记数组,大小要开成与线段树一一对应
struct E{
	int u,v,w;
}e[maxn<<1];//树不定形要存双向边 
int first[maxn],nt[maxn<<1],ES;//邻接表
inline void addE(int u,int v,int w)//加边函数 
{
	e[++ES]=(E){u,v,w};
	nt[ES]=first[u];
	first[u]=ES;
	return ;
}
int sz[maxn]/*树大小*/,fa[maxn]/*直属父亲*/,top[maxn]/*链头结点*/;
int son[maxn]/*重儿子*/,depth[maxn]/*深度*/;
int id[maxn]/*结点->线段树编号*/,anti[maxn]/*线段树编号->结点*/;
int ix,A[maxn]/*在做点权树剖时的点权数组*/;
inline void DFS(int u)
{
	int v;sz[u]=1;//大小初始化 
	for(int i=first[u];i;i=nt[i])
	{
		v=e[i].v;
		if(v!=fa[u])//不能死转圈
		{
			depth[v]=depth[u]+1;
			fa[v]=u;//v的父亲是u
			A[v]=e[i].w;//转化关键代码1,将连向子节点的边权直接赋给子节点
			DFS(v);
			sz[u]+=sz[v];//维护大小
			if(sz[son[u]]<sz[v]) son[u]=v;//重儿子 
		}
	}
	return ; 
}
inline void dfs(int u,int tp)
{
	id[u]=++ix;anti[ix]=u;//建立正反映射
	top[u]=tp;//链头
	if(son[u]) dfs(son[u],tp);//优先遍历重儿子
	int v;
	for(int i=first[u];i;i=nt[i])
	{
		v=e[i].v;
		if(v==son[u]||v==fa[u]) continue;
		dfs(v,v);
	}
	return ;
}
#define mid (L+R>>1)
#define L(i) (i<<1)
#define R(i) (i<<1|1)//涉及到优先级较低的位运算建议加括号 
inline void Build(int L,int R,int i)
{
	if(L==R)
	{
		TREE[i]=A[anti[L]];//之前已经进行了转化可以不改变这里
		return ; 
	}
	Build(L,mid,L(i));
	Build(mid+1,R,R(i));
	TREE[i]=TREE[L(i)]+TREE[R(i)];
	return ;
}
inline void LAZY(int L,int R,int i)
{
	if(!lazy[i]) return ;
	lazy[L(i)]+=lazy[i];
	lazy[R(i)]+=lazy[i];
	TREE[L(i)]+=(mid-L+1)*lazy[i];
	TREE[R(i)]+=(R-mid)*lazy[i];
	lazy[i]=0;//高频错点！！ 
	return ;
}
inline void Update(int L,int R,int l,int r,int i,int k)
{
	if(l<=L&&R<=r)
	{
		TREE[i]+=k*(R-L+1);
		lazy[i]+=k;
		return ;
	}
	LAZY(L,R,i);//任何时候访问子节点都需要下传标记 
	if(l<=mid) Update(L,mid,l,r,L(i),k);
	if(r>mid) Update(mid+1,R,l,r,R(i),k);
	TREE[i]=TREE[L(i)]+TREE[R(i)];
	return ;
}
inline int Query(int L,int R,int l,int r,int i)
{
	if(l<=L&&R<=r)
		return TREE[i];
	LAZY(L,R,i);
	int ans=0;
	if(l<=mid) ans+=Query(L,mid,l,r,L(i));
	if(r>mid) ans+=Query(mid+1,R,l,r,R(i));
	return ans; 
}
inline void Update_Path(int x,int y,int k)
{
	while(top[x]!=top[y])
	{
		if(depth[top[x]]<depth[top[y]]) swap(x,y);
		Update(1,N,id[top[x]],id[x],1,k);
		x=fa[top[x]];
	}
	if(depth[x]>depth[y]) swap(x,y);
	Update(1,N,id[x],id[y],1,k);
	Update(1,N,id[x],id[x],1,-k);//核心代码2 
	return ;
}
inline int Query_Path(int x,int y)
{
	int ans=0;
	while(top[x]!=top[y])
	{
		if(depth[top[x]]<depth[top[y]]) swap(x,y);
		ans+=Query(1,N,id[top[x]],id[x],1);
		x=fa[top[x]];
	}
	if(depth[x]>depth[y]) swap(x,y);
	ans+=Query(1,N,id[x],id[y],1); 
	ans-=Query(1,N,id[x],id[x],1);//核心代码3 
	return ans;
}
inline int Re()
{
	char c;
	int re;
	while((c=getchar())>'9'||c<'0');
	re=c-48;
	while((c=getchar())>='0'&&c<='9')
	re=re*10+c-48;
	return re;
}
int main()
{
	N=Re();Q=Re();
	int u,v,w;
	for(int i=1;i<N;i++)
	{
		u=Re();v=Re();w=Re();
		addE(u,v,w);addE(v,u,w);
	}
	DFS(1);dfs(1,1);
	Build(1,N,1);
	int op;
	for(int i=1;i<=Q;i++)
	{
		op=Re();
		if(op==1)//路径更新
		{
			u=Re();v=Re();w=Re();
			Update_Path(u,v,w);
		}
		else if(op==2)//子树更新
		{
			u=Re();w=Re();
			Update(1,N,id[u],id[u]+sz[u]-1,1,w);
		}
		else if(op==3)//路径询问
		{
			u=Re();v=Re();
			printf("%d\n",Query_Path(u,v));
		}
		else//子树询问
		{
			u=Re();
			printf("%d\n",Query(1,N,id[u],id[u]+sz[u]-1,1));
		}
	}
	return 0;
}
```
上面这份板子是我认为最简单的转化方式,与点权树链剖分相比仅仅多了 $3$ 句话  
- 在进行 $DFS$ 遍历时即将进入子节点时将边权赋给子节点  
$A[v]=e[i].w$   

- 在进行路径更新的时候最后一步在 $LCA$ 上减去 $k$,因为 $LCA$ 代表的边权并不在所更新路径中(自己画图可以感受一下,画那种同一个父亲从一个子树到另外一个子树的路径就会发现父节点代表的边不算),$Update(1,N,id[x],id[x],1,-k)$

- 在进行路径查询的时候最后也会把多查询的 $LCA$ 代表的边权减掉   
$ans-=Query(1,N,id[x],id[x],1)$    


这是利于理解的版本哦,实际上我们在用的时候第二条和第三条都没有,而是将原来的  
```cpp
Update(1,N,id[x],id[y],1,k)  Query(1,N,id[x],id[y],1)
```
直接修改为  
```
Update(1,N,id[x]+1,id[y],1,k)  Query(1,N,id[x]+1,id[y],1)
```
而为什么我在这里没有写呢？
因为有时候当 $x$ 和 $y$ 跳到同一条链上时二者刚好重合,这时候加一会让进入线段树时出现 $l>r$ 这是不符合定义的,不利于理解。  
只不过线段树的 $feature$ 刚好让这种 $l=r+1$ 的情况什么都查不到就退出了函数,所以修改后因为加过一次 $1$ 而此时 $x$ 和 $y$ 恰好在一条链上,可以刚好忽略点 $x$ 的权值达到我们的目的，修改一句话就达到了两句话的效果。  

那么这道题在泥掌握上面的模板之后就可以轻松切掉了。  

树链剖分是像我这样的蒟蒻经常窒息的一个东西,最怕的就是 $\text{Segment Fault}$ 但是总是有一个过程的啊,[如果泥多练](https://www.luogu.com.cn/training/1654#information),每次都直接重新打,~~在你吐之前~~一定能够**熟练**掌握这个算法！！  
那些十几分钟切树剖一次过的神仙并不是刚学就这样,也只有一个信条  
**无他,唯手熟尔**  
$\text{The End}$
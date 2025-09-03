# P1505 题解

   **90分的自行看第三点**

由于看不懂大佬发的题解就自己发了一篇

对于这道题，题目要求我们支持5种操作，其中显然操作2-4要求使用树剖来实现（主要是更高级的算法我也不会了(；′⌒`)）

但是这道题的难点对于本蒟蒻来说还是很多的（比如第一篇说的边权转点权我就不会awa）

所以我对自己不会的点都进行了解析！

$1.$  **边权转点权**

我们考虑把连接父亲与儿子的边的边权赋值到儿子上，即我们在写线段树与跑第二个DFS的时候对于权值用dfs序和链式前向星存储顺序进行转换，没想明白的可以看看我代码中dfs1和dfs2中的应用，还可以先去做[P4315 月下“毛景树”](https://www.luogu.com.cn/problem/P4315)


```c++
inline void dfs1(int x,int f){
	dep[x]=dep[f]+1;fa[x]=f;siz[x]=1;
	for(int i=head[x];i;i=nex[i]){
		int v=to[i];
		if(v==f) continue;
		dfs1(v,x);
		tmp[v]=val[i];//边权转点权
		siz[x]+=siz[v];
		if(siz[son[x]]<siz[v]) son[x]=v;
	}
}

inline void dfs2(int x,int topf){
	dfn[x]=++idx;
    w[idx]=tmp[x];//边权转点权
    top[x]=topf;
	if(son[x]) dfs2(son[x],topf);
	for(int i=head[x];i;i=nex[i]){
		int v=to[i];
		if(v==fa[x]||v==son[x]) continue;
		dfs2(v,v);
	}
}
```

$2.$   当树剖中跳出$while(top[x]!=top[y])$这个循环的时候，$top[x]$此时就是x和y的$LCA$ ,由于$top[x]$的点权是$top[x]$与$fa[top[x]]$的连边的边权，所以我们此时不计算它，另外当$x==y$ 的时候，所有需要统计的边权都被统计到了直接返回即可,这里是一个例子：

```c++
if(x!=y) res+=qsum(1,1,n,dfn[x]+1,dfn[y]);
```

$3.$  **很多人都被hack的一点**，感谢@[傅思维666](https://www.luogu.com.cn/user/175131)大佬指出的错误

修改第$i$条边时，我们应该修改的是$(u,v)$这个点集中深度更大的点的点权，而不是直接修改点i，具体操作在代码中

$4.$  剩下的就没什么难的了，用$lazy[$  $]$异或维护这个点是否需要取反，$sum[$  $]$直接$\times-1$就行了，$maxn[$  $]$和$minn[$  $]$交换之后取反就可以了

然而最优解居然是暴力。。。

另外，建议各位打树剖用结构体存图，我把top写成to找了一小时

蒟蒻码字不易，如果对您有帮助的话请点个赞呗？以及非常感谢管理员大大的审核

$AC$  $CODE$



```c++
#include<bits/stdc++.h> 

#define int long long
#define mid ((l+r)>>1)
#define lson rt<<1,l,mid
#define rson rt<<1|1,mid+1,r
using namespace std;

inline int read(){
	int x=0,f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-48;ch=getchar();}
	return x*f;
}

inline void write(int x){
	if(x<0){putchar('-');x=-x;}
	if(x>9)write(x/10);
	int xx=x%10;
	putchar(xx+'0');
}

const int N=2e5+10;
int n,m;
int cnt,head[N],to[N<<1],nex[N<<1],val[N<<1];
//链式前向星

int idx,fa[N],son[N],top[N],dep[N],dfn[N],siz[N],tmp[N],w[N];
//树链剖分 

int sumn[N<<2],maxn[N<<2],minn[N<<2],lz[N<<2];
//线段树 

struct node{
	int x,y;
}id[N];

inline void add(int x,int y,int w){
	nex[++cnt]=head[x];to[cnt]=y;val[cnt]=w;head[x]=cnt;
}

inline void dfs1(int x,int f){
	dep[x]=dep[f]+1;fa[x]=f;siz[x]=1;
	for(int i=head[x];i;i=nex[i]){
		int v=to[i];
		if(v==f) continue;
		dfs1(v,x);
		tmp[v]=val[i];//边权转点权
		siz[x]+=siz[v];
		if(siz[son[x]]<siz[v]) son[x]=v;
	}
}

inline void dfs2(int x,int topf){
	dfn[x]=++idx;w[idx]=tmp[x];top[x]=topf;
	if(son[x]) dfs2(son[x],topf);
	for(int i=head[x];i;i=nex[i]){
		int v=to[i];
		if(v==fa[x]||v==son[x]) continue;
		dfs2(v,v);
	}
}
//以下为线段树 

inline void pushup(int rt){
	sumn[rt]=sumn[rt<<1]+sumn[rt<<1|1];
	maxn[rt]=max(maxn[rt<<1],maxn[rt<<1|1]);
	minn[rt]=min(minn[rt<<1],minn[rt<<1|1]);
}

inline void build(int rt,int l,int r){
	if(l==r){
		sumn[rt]=maxn[rt]=minn[rt]=w[l];
		return;
	}
	build(rt<<1,l,mid);build(rt<<1|1,mid+1,r);
	pushup(rt);
}

inline void pushdown(int rt){
	lz[rt<<1]^=1;lz[rt<<1|1]^=1;
	sumn[rt<<1]=-sumn[rt<<1];sumn[rt<<1|1]=-sumn[rt<<1|1];
	maxn[rt<<1]=-maxn[rt<<1];maxn[rt<<1|1]=-maxn[rt<<1|1];
	minn[rt<<1]=-minn[rt<<1];minn[rt<<1|1]=-minn[rt<<1|1];
	swap(maxn[rt<<1],minn[rt<<1]);
	swap(maxn[rt<<1|1],minn[rt<<1|1]);
	lz[rt]=0;
}

inline void update(int rt,int l,int r,int q,int k){
	if(l==r){
		sumn[rt]=maxn[rt]=minn[rt]=k;
		return;
	}
	if(lz[rt]) pushdown(rt);
	if(q<=mid) update(rt<<1,l,mid,q,k);
	if(q>mid)  update(rt<<1|1,mid+1,r,q,k);
	pushup(rt);
}

inline void change(int rt,int l,int r,int L,int R){
	if(L<=l&&r<=R){
		lz[rt]^=1;
		sumn[rt]=-sumn[rt];
		maxn[rt]=-maxn[rt];
		minn[rt]=-minn[rt];
		swap(maxn[rt],minn[rt]);
		return;
	}
	if(lz[rt]) pushdown(rt);
	if(L<=mid) change(rt<<1,l,mid,L,R);
	if(R>mid)  change(rt<<1|1,mid+1,r,L,R);
	pushup(rt);
}

inline int qsum(int rt,int l,int r,int L,int R){
	int res=0;
	if(L<=l&&r<=R) return sumn[rt];
	if(lz[rt]) pushdown(rt);
	if(L<=mid) res+=qsum(rt<<1,l,mid,L,R);
	if(R>mid)  res+=qsum(rt<<1|1,mid+1,r,L,R);
	pushup(rt);
	return res;
}

inline int qmax(int rt,int l,int r,int L,int R){
	int res=-2147483647;
	if(L<=l&&r<=R) return maxn[rt];
	if(lz[rt]) pushdown(rt);
	if(L<=mid) res=max(res,qmax(rt<<1,l,mid,L,R));
	if(R>mid)  res=max(res,qmax(rt<<1|1,mid+1,r,L,R));
	pushup(rt);
	return res;
}

inline int qmin(int rt,int l,int r,int L,int R){
	int res=2147483647;
	if(L<=l&&r<=R) return minn[rt];
	if(lz[rt]) pushdown(rt);
	if(L<=mid) res=min(res,qmin(rt<<1,l,mid,L,R));
	if(R>mid)  res=min(res,qmin(rt<<1|1,mid+1,r,L,R));
	pushup(rt);
	return res;
}
//以上是线段树
//以下是树链剖分

inline void update(int x,int y){
	while(top[x]!=top[y]){
		if(dep[top[x]]<dep[top[y]]) swap(x,y);
		change(1,1,n,dfn[top[x]],dfn[x]);
		x=fa[top[x]];
	}
	if(dep[x]>dep[y]) swap(x,y);
	if(x!=y) change(1,1,n,dfn[x]+1,dfn[y]);
}

inline int qsum(int x,int y){
	int res=0;
	while(top[x]!=top[y]){
		if(dep[top[x]]<dep[top[y]]) swap(x,y);
		res+=qsum(1,1,n,dfn[top[x]],dfn[x]);
		x=fa[top[x]];
	}
	if(dep[x]>dep[y]) swap(x,y);
	if(x!=y) res+=qsum(1,1,n,dfn[x]+1,dfn[y]);
	return res;
}

inline int qmax(int x,int y){
	int res=-2147483647;
	while(top[x]!=top[y]){
		if(dep[top[x]]<dep[top[y]]) swap(x,y);
		res=max(res,qmax(1,1,n,dfn[top[x]],dfn[x]));
		x=fa[top[x]];
	}
	if(dep[x]>dep[y]) swap(x,y);
	if(x!=y) res=max(res,qmax(1,1,n,dfn[x]+1,dfn[y]));
	return res;
}

inline int qmin(int x,int y){
	int res=2147483647;
	while(top[x]!=top[y]){
		if(dep[top[x]]<dep[top[y]]) swap(x,y);
		res=min(res,qmin(1,1,n,dfn[top[x]],dfn[x]));
		x=fa[top[x]];
	}
	if(dep[x]>dep[y]) swap(x,y);
	if(x!=y) res=min(res,qmin(1,1,n,dfn[x]+1,dfn[y]));
	return res;
}

signed main(){
	n=read();
	for(int i=1;i<n;i++){
		int a,b,c;
		a=read()+1;b=read()+1;c=read();
		add(a,b,c);add(b,a,c);
		id[i].x=a;id[i].y=b;
	}
	dfs1(1,0);dfs2(1,1);
	build(1,1,n);
	m=read();
	while(m--){
		char s[10];int a,b;
		scanf("%s",s);a=read();b=read();
		if(s[0]=='C'){
			int tmpp;
			if(dep[id[a].x]>dep[id[a].y]) tmpp=id[a].x;
			else tmpp=id[a].y;
			update(1,1,n,dfn[tmpp],b);
		}
		else if(s[0]=='N'){
			a++,b++;
			update(a,b);
		}
		else if(s[0]=='S'){
			a++,b++;
			write(qsum(a,b));puts("");
		}
		else if(s[0]=='M'&&s[1]=='A'){
			a++,b++;
			write(qmax(a,b));puts("");
		}
		else if(s[0]=='M'&&s[1]=='I'){
			a++,b++;
			write(qmin(a,b));puts("");
		}
	}
	return 0;
}
```


# P3976 题解

题面稍绕。给出一棵有点权的树，每次询问一条链，给出起点和终点，要求在这条链上选两个点，答案是第二个点的权值减去第一个点的权值，求这个数的最大值（必须是从起点走到终点途中后经过的减去先经过的），结果为负数输出 $0$。然后再把这条链上所有点权值加一个给定的数。

大力树剖！套线段树！

那么线段树维护点啥呢？最大值？最小值？这两个量感觉还不大够。合并区间信息、计算答案的时候都难以实现。

那维护点啥呢？我是受到了树上最大子段和的启发，以“左”“右”分类维护一些东西，我们把走下来的过程看做起点走到 LCA，然后到终点。考虑到查询的时候可能一条路径上行，一条下行，那就维护**这一段数字从左到右走一遍获得的最大值，以及从右向左走一遍获得的最大值**。这里“从右向左”“从左向右”和题面意义一致，都是后面经过的减前面经过的。对了，还有区间加的标记。

下面是线段树维护的变量以及区间信息合并：

+ `maxx` 和 `minn` 维护最大值、最小值，很好维护。

+ `lmax` 维护线段树一个节点代表的这一段区间上的数字从左到右走获得的最大值。合并：先考虑不跨区间，那就是该节点左右儿子的 `lmax`；跨区间，那就是右儿子的 `maxx` 减去左儿子的 `minn`。三者取最大值。

+ `rmax` 维护线段树一个节点代表的这一段区间上的数字从右到左走获得的最大值。合并：先考虑不跨区间，那就是该节点左右儿子的 `rmax`；跨区间，那就是左儿子的 `maxx` 减去右儿子的 `minn`。三者取最大值。

+ `tag` 维护区间加的标记。

线段树部分就是这样，比较简明~~吧~~。

注意“从左到右”的概念放到树上就是按时间戳从小到大。“从右往左”同理。

接下来是树剖部分。

起点所在的一端、终点所在的一端，分别用 `L`、`R` 两个变量维护**目前已经跳过的部分的信息**。树剖往上跳的时候如果当前跳的是起点一端的链，就把这次查询的结果和 `L` 合并。否则和 `R` 合并。树上合并的规则和线段树子区间信息合并规则是一样的。

`L` `R` 初始化：

```
L.lmax=L.rmax=0;
L.maxx=-INF;
L.minn=INF;
R=L;

```

由于一条“不拐弯的”链上，上面的点的时间戳肯定小于下面的点。所以最终答案：`ans=max(max(L.rmax,R.lmax),R.maxx-L.minn);`

如何理解？从起点出发向上走，那就是逆着时间戳走，也就是“从右向左”。而到了最高处向终点走，是顺着时间戳走的，也就是“从左向右”，虽然我们是从下往上合并信息。

还有点蒙？看看代码吧！


完整代码：

```
#include<bits/stdc++.h>
using namespace std;
const int N=50010;
const int INF=1000000099;
int t[N],a[N];//初始点权和建立在时间戳上的点权
int head[N],to[N*2],nex[N*2],cnt;
void add(int x,int y){
	cnt++;
	to[cnt]=y;
	nex[cnt]=head[x];
	head[x]=cnt;
}
int tot,dfn[N],tp[N],fa[N],sz[N],son[N],dep[N];
void dfs1(int x,int f){
	fa[x]=f;
	dep[x]=dep[f]+1;
	sz[x]=1;
	int maxn=-1;
	for(int i=head[x];i;i=nex[i]){
		int y=to[i];
		if(y==f)
			continue;
		dfs1(y,x);
		sz[x]+=sz[y];
		if(sz[y]>maxn){
			maxn=sz[y];
			son[x]=y;
		}
	}
}
void dfs2(int x,int top){
	tp[x]=top;
	tot++;
	dfn[x]=tot;
	a[tot]=t[x];
	if(son[x])
		dfs2(son[x],top);
	for(int i=head[x];i;i=nex[i]){
		int y=to[i];
		if(y==fa[x]||y==son[x])
			continue;
		dfs2(y,y);
	}
}
struct ST{
	int maxx;
	int minn;
	int lmax;
	int rmax;
	int tag;
}st[N*4];
void build(int root,int l,int r){
	if(l==r){
		st[root].maxx=a[l];
		st[root].minn=a[l];
		return;
	}
	int mid=(l+r)/2;
	build(root*2,l,mid);
	build(root*2+1,mid+1,r);
	st[root].maxx=max(st[root*2].maxx,st[root*2+1].maxx);
	st[root].minn=min(st[root*2].minn,st[root*2+1].minn);
	st[root].lmax=max(max(st[root*2].lmax,st[root*2+1].lmax),st[root*2+1].maxx-st[root*2].minn);
	st[root].rmax=max(max(st[root*2].rmax,st[root*2+1].rmax),st[root*2].maxx-st[root*2+1].minn);
}
void push_down(int root){
	int k=st[root].tag;
	st[root].tag=0;
	st[root*2].maxx+=k;
	st[root*2].minn+=k;
	st[root*2+1].maxx+=k;
	st[root*2+1].minn+=k;
	st[root*2].tag+=k;
	st[root*2+1].tag+=k;
}
void change(int root,int l,int r,int x,int y,int k){
	if(l>=x&&r<=y){
		st[root].maxx+=k;
		st[root].minn+=k;
		st[root].tag+=k;
		return;
	}
	if(st[root].tag!=0&&l!=r)
		push_down(root);
	int mid=(l+r)/2;
	if(mid>=x)
		change(root*2,l,mid,x,y,k);
	if(mid+1<=y)
		change(root*2+1,mid+1,r,x,y,k);
	st[root].maxx=max(st[root*2].maxx,st[root*2+1].maxx);
	st[root].minn=min(st[root*2].minn,st[root*2+1].minn);
	st[root].lmax=max(max(st[root*2].lmax,st[root*2+1].lmax),st[root*2+1].maxx-st[root*2].minn);
	st[root].rmax=max(max(st[root*2].rmax,st[root*2+1].rmax),st[root*2].maxx-st[root*2+1].minn);
}
ST ask(int root,int l,int r,int x,int y){
	if(l>=x&&r<=y)
		return st[root];
	if(st[root].tag!=0&&l!=r)
		push_down(root);
	int mid=(l+r)/2;
	if(mid>=y)
		return ask(root*2,l,mid,x,y);
	else{
		if(mid+1<=x)
			return ask(root*2+1,mid+1,r,x,y);
		else{
			ST L=ask(root*2,l,mid,x,y);
			ST R=ask(root*2+1,mid+1,r,x,y);
			ST res;
			res.maxx=max(L.maxx,R.maxx);
			res.minn=min(L.minn,R.minn);
			res.lmax=max(max(L.lmax,R.lmax),R.maxx-L.minn);
			res.rmax=max(max(L.rmax,R.rmax),L.maxx-R.minn);
			return res;
		}
	}
}
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
		scanf("%d",&t[i]);
	for(int i=1;i<n;i++){
		int x,y;
		scanf("%d%d",&x,&y);
		add(x,y);
		add(y,x);
	}
	dfs1(1,1);
	dfs2(1,1);
	build(1,1,n);
	int m;
	cin>>m;
	for(int i=1;i<=m;i++){
		int x,y,k;
		ST L,R;
		L.lmax=L.rmax=0;
		L.maxx=-INF;
		L.minn=INF;
		R=L;
		scanf("%d%d%d",&x,&y,&k);
		int xx=x;
		int yy=y;
		while(tp[x]!=tp[y]){
			if(dep[tp[x]]<dep[tp[y]]){//跳终点一端的链 
				ST res=ask(1,1,n,dfn[tp[y]],dfn[y]);
				R.lmax=max(max(res.lmax,R.lmax),R.maxx-res.minn);
				R.rmax=max(max(res.rmax,R.rmax),res.maxx-R.minn);
				R.maxx=max(R.maxx,res.maxx);
				R.minn=min(R.minn,res.minn);
				y=fa[tp[y]];
			}
			else{//跳起点一端的链 	
				ST res=ask(1,1,n,dfn[tp[x]],dfn[x]);
				L.lmax=max(max(res.lmax,L.lmax),L.maxx-res.minn);
				L.rmax=max(max(res.rmax,L.rmax),res.maxx-L.minn);
				L.maxx=max(L.maxx,res.maxx);
				L.minn=min(L.minn,res.minn);
				x=fa[tp[x]];
			}
		}
		if(dep[x]<dep[y]){//跳终点一段的链 
			ST res=ask(1,1,n,dfn[x],dfn[y]);
			R.lmax=max(max(res.lmax,R.lmax),R.maxx-res.minn);
			R.rmax=max(max(res.rmax,R.rmax),res.maxx-R.minn);
			R.maxx=max(R.maxx,res.maxx);
			R.minn=min(R.minn,res.minn);
		}
		else{//跳起点一端的链 
			ST res=ask(1,1,n,dfn[y],dfn[x]);
			L.lmax=max(max(res.lmax,L.lmax),L.maxx-res.minn);
			L.rmax=max(max(res.rmax,L.rmax),res.maxx-L.minn);
			L.maxx=max(L.maxx,res.maxx);
			L.minn=min(L.minn,res.minn);
		}
		int ans=max(max(L.rmax,R.lmax),R.maxx-L.minn);
		printf("%d\n",ans);
		x=xx;//修改之前恢复成原来的 x、y 值 
		y=yy;
		while(tp[x]!=tp[y]){
			if(dep[tp[x]]<dep[tp[y]])
				swap(x,y);
			change(1,1,n,dfn[tp[x]],dfn[x],k);
			x=fa[tp[x]];
		}
		if(dep[x]>dep[y])
			swap(x,y);
		change(1,1,n,dfn[x],dfn[y],k);
	}
	return 0;
}

```
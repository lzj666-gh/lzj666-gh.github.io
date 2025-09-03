# P3950 题解

# 树链剖分吼啊
## ~~一看就看出是LCT模板题啦~~
# 前记
见这么多人写LCT，却很少人写树链剖分，于是我就来一发树链剖分（其实是因为自己不会LCT）

本蒟蒻的写法和诸位写树链剖分的大神有点不同

# 思路
树链剖分，简单题

## 操作
操作1：'C' 操作 ： 简单的说就是把x到y的边cut掉，题目又保证x,y相邻，~~肯定直接LCT啦~~，那么我们就可以将x，y的所以边权加1，表示那些边多了一次战争。

操作2：'U' 操作 ： 简单的说就是把之前cut的边加回来，我们只需要记录之前每一次战争的两个部落编号，战争结束就把那两个部落直接的边权减去1就可以了，表示那些边少了一次战争。

操作3：'Q' 操作 ： 简单的说就是询问x,y之间的边权和，如果是0，表示经过的边一次战争也没有，就是yes；不然就有战争，是no。

这么一看，思路是不是很简单。

但还有些问题，树链剖分是针对点权的，我们如何转换为边权呢？

## 点权转边权
方法有很多，例如在每一条边都多加1个点，在加的那个点上记录权值。

但是，这里讲一下我的做法：**直接忽略**！

在一颗树内，点有n个，边有n-1条，所以我们可以让每一条边对应到点上，对应方式就是边的编号是边上两点深度小的点编号。

那么就只会有根是没有边对应的所以我们可以假设有一条编号为根的边和根相连。

将x,y的边权加就等于将x,y的点权全部加，然后LCA(x,y)的点权减回去（可以自己画图尝试一下）

查询x,y的边权和就等于将x,y的点权全部累加，然后减去LCA(x,y)的点权（可以自己画图尝试一下）

于是我们整个思路就出来了(这样就不用改线段树啦>w< )

# 代码
```cpp
#include<bits/stdc++.h>
#define maxn 4000001
#define L(x) (x<<1)
#define R(x) ((x<<1)|1)
using namespace std;
int tree[maxn],tag[maxn];
int rev[maxn],dep[maxn],size[maxn],seg[maxn],top[maxn],son[maxn],father[maxn];
int n,m,root,x,y,z,a[maxn],visx[maxn],visy[maxn],tot;
int cnt,from[maxn],to[maxn],Next[maxn],head[maxn];
char mode;
void add(int x,int y){
	cnt++;
	from[cnt]=x;to[cnt]=y;
	Next[cnt]=head[x];head[x]=cnt;
}
//线段树
void pushdown(int node,int begin,int end){
	if(tag[node]){
		tag[L(node)]+=tag[node];
		tag[R(node)]+=tag[node];
		int mid=(begin+end)>>1;
		tree[L(node)]+=(mid-begin+1)*tag[node];
		tree[R(node)]+=(end-mid)*tag[node];
		tag[node]=0;
	}
}
void update(int node,int begin,int end,int x,int y,int val){
	if(begin>y||end<x)return;
	if(begin>=x&&end<=y){
		tag[node]+=val;
		tree[node]+=(end-begin+1)*val;
		return;
	}else{
		pushdown(node,begin,end);
		int mid=(begin+end)>>1;
		if(x<=mid)update(L(node),begin,mid,x,y,val);
		if(y>mid) update(R(node),mid+1,end,x,y,val);
		tree[node]=tree[L(node)]+tree[R(node)];
	}
}
int query(int node,int begin,int end,int x,int y){
	if(begin>y||end<x)return 0;
	if(begin>=x&&end<=y){
		return tree[node];
	}else{
		pushdown(node,begin,end);
		int mid=(begin+end)>>1,sum=0;
		if(x<=mid)sum+=query(L(node),begin,mid,x,y);
		if(y>mid) sum+=query(R(node),mid+1,end,x,y);
		return sum;
	}
}
//线段树
int dfs1(int x){						//树链剖分模板
	size[x]=1;
	dep[x]=dep[father[x]]+1;
	for(int i=head[x];i!=-1;i=Next[i]){
		int v=to[i],big=0;
		if(father[x]==v)continue;
		father[v]=x;
		big=dfs1(v);
		size[x]+=big;
		if(big>size[son[x]])son[x]=v;
	}
	return size[x]; 
}
void dfs2(int x){						//树链剖分模板
	if(son[x]){
		seg[son[x]]=++seg[0];
		top[son[x]]=top[x];
		rev[seg[0]]=son[x];
		dfs2(son[x]);
	}
	for(int i=head[x];i!=-1;i=Next[i]){
		int v=to[i];
		if(!top[v]){
			seg[v]=++seg[0];
			top[v]=v;
			rev[seg[0]]=v;
			dfs2(v);
		}
	}
}
void linkadd(int x,int y,int z){
	int fx=top[x],fy=top[y];
	while(fx!=fy){
		if(dep[fx]<dep[fy])swap(x,y),swap(fx,fy);
		update(1,1,seg[0],seg[fx],seg[x],z);
		x=father[fx];fx=top[x];
	}
	if(dep[x]>dep[y])swap(x,y);
	update(1,1,seg[0],seg[x],seg[y],z);
	update(1,1,seg[0],seg[x],seg[x],-z);			//LCA特殊处理
}
int linkquery(int x,int y){
	int fx=top[x],fy=top[y],ans=0;
	while(fx!=fy){
		if(dep[fx]<dep[fy])swap(x,y),swap(fx,fy);
		ans+=query(1,1,seg[0],seg[fx],seg[x]);
		x=father[fx];fx=top[x];
	}
	if(dep[x]>dep[y])swap(x,y);
	ans+=query(1,1,seg[0],seg[x],seg[y]);
	ans-=query(1,1,seg[0],seg[x],seg[x]);			//减LCA
	return ans;
}
int main(){
	memset(head,-1,sizeof(head));
	scanf("%d%d",&n,&m);root=1;
	for(int i=1;i<=n-1;i++){
		scanf("%d%d",&x,&y);
		add(x,y);add(y,x);
	}
	dfs1(root);
	seg[root]=++seg[0];
	rev[seg[0]]=root;
	top[root]=root;
	dfs2(root);
	for(int i=1;i<=m;i++){
		scanf("%s",&mode);
		if(mode=='C'){
			scanf("%d%d",&x,&y);
			visx[++tot]=x;visy[tot]=y;		//记录每一次战争的两个部落
			linkadd(x,y,1);			//x到y的边权加1
		}
		if(mode=='U'){
			scanf("%d",&x);
			linkadd(visx[x],visy[x],-1);		//战争结束就减回去
		}
		if(mode=='Q'){
			scanf("%d%d",&x,&y);
			int q=linkquery(x,y);	//查询x到y的边权和
			if(q==0)printf("Yes\n");else	//如果q为0就可以
			printf("No\n");			//不行就……
		}
	}
}
```
# 另外推荐题目
[P3258 [JLOI2014]松鼠的新家](https://www.luogu.org/problemnew/show/P3258) 即其[题解](https://www.luogu.org/blog/juruohyfhaha/solution-p3258)

# 谢谢观赏，点个赞呗！
# P1273 题解

欢迎访问我的博客：[https://www.cnblogs.com/luyouqi233](https://www.cnblogs.com/luyouqi233)

本题解的目的是想给大家一个显然的时间复杂度为$O(nm)$的做法，~~从此再也不用苦苦去纠结代码时间复杂度到底是多少~~。

首先仍然安利这位大佬对$O(nm)$树形背包的讲解，配合观看效果更佳：[https://www.luogu.com.cn/blog/P6174/solution-p2014](https://www.luogu.com.cn/blog/P6174/solution-p2014)

这道题是一道裸的树形背包题，设$f[i][j]$表示以$i$为根往下找$j$个叶子的最大价值，那么答案就是所有$f[1][j]\ge 0$当中最大的$j$。

在dp之前，我们按照后序遍历序列重新编号（即遍历到一个节点时，先搜索节点的子树，为它们编号后再为这个节点编号）。

然后开始dp，首先初始化，对$f[i][j]$赋值$-INF$，当$j==0$时$f[i][j]=0$。

之后转移：

如果$i$点是叶子节点那么有$f[i][j]=max(f[i-1][j-1]+c[i],f[i-1][j])$和一般的0/1背包没什么区别

如果不是的话就有意思了，如果我们取$i$的话$f[i][j]=f[i-1][j]+c[i]$没什么问题，但是如果不取的话它和它的子树就一个都不能取了。

巧的是，由后序遍历定义不难推出$i$的子树节点编号在$[i-sz[i]+1,i]$之间（$sz[i]$为子树$i$的大小）。

所以不取的话$f[i][j]=f[i-sz[i]][j]$，综上$f[i][j]=max(f[i-1][j]+c[i],f[i-sz[i]][j])$

时间复杂度很容易看出是$O(nm)$的，这也是我写这篇题解的原因。

```cpp
#include<cmath>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
const int N=3010; 
const int INF=1e9;
inline int read(){
	int X=0,w=0;char ch=0;
	while(!isdigit(ch)){w|=ch=='-';ch=getchar();}
	while(isdigit(ch))X=(X<<3)+(X<<1)+(ch^48),ch=getchar();
	return w?-X:X;
}
struct node{
	int to,nxt;
}e[N];
int n,m,cnt,head[N],c[N];
inline void add(int u,int v){
	e[++cnt].to=v;e[cnt].nxt=head[u];head[u]=cnt;
}
int f[N][N],idx[N],sz[N],tot;
void dfs(int u){
	sz[u]=1;
	for(int i=head[u];i;i=e[i].nxt){
		int v=e[i].to;
		dfs(v);sz[u]+=sz[v];
	}
	idx[++tot]=u;
}
int main(){
	n=read(),m=read();
	for(int u=1;u<=n-m;u++){
		int k=read();
		for(int j=1;j<=k;j++){
			int v=read();c[v]=-read();
			add(u,v);
		}
	}
	for(int u=n-m+1;u<=n;u++)c[u]+=read();
	dfs(1);
	for(int i=0;i<=tot;i++)
		for(int j=1;j<=m;j++)
			f[i][j]=-INF;
	for(int i=1;i<=tot;i++){
		int u=idx[i];
		for(int j=1;j<=m;j++){
			if(n-m+1<=u)f[i][j]=max(f[i-1][j-1]+c[u],f[i-1][j]);
			else f[i][j]=max(f[i-1][j]+c[u],f[i-sz[u]][j]);
		}
	}
	for(int i=m;i>=0;i--){
		if(f[tot][i]>=0){
			printf("%d\n",i);return 0;
		}
	}
	return 0;
}
```

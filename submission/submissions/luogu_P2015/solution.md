# P2015 题解

PS：这只是个更新啊，求管理员给个通过

$update:2019-3-6$

之前说的话很多地方比较模糊，重新组织一下语言，改成了更易理解的描述方式，希望管理员给个通过\托腮

-----

一道题意清晰的树形DP模板题，不会树形DP的可以去看我的博客[**树形DP入门详解**](https://www.cnblogs.com/hanruyun/p/9788170.html)

这道题有一个隐含的条件，当某条边被保留下来时，从根节点到这条边的路径上的所有边也都必须保留下来

设$f[u][i]$表示$u$的子树上保留$i$条边，至多保留的苹果数目

那么状态转移方程也就显而易见了

$f[u][i]=max(f[u][i],f[u][i-j-1]+f[v][j]+e[i].w)(~1 \le i \le min(q,sz[u]),0 \le j \le min(sz[v],i-1)~)$

$u$表示当前节点，$v$是$u$的一个子节点，$sz[u]$表示$u$的子树上的边数，q就是题目中要求的最多保留边数

那么为什么是这个方程呢？

首先，为什么是$f[u][i-j-1]$而不是$f[u][i-j]$？

为前文提到了，保留一条边必须保留从根节点到这条边路径上的所有边，那么如果你想从$u$的子节点$v$的子树上留边的话，也要留下$u,v$之间的连边

那么取值范围$k$为什么要小于等于$i-1$而不是$i$呢？

同上，因为要保留$u,v$连边

对了，别忘了$i,j$要倒序枚举因为这是$01$背包

下放代码

```cpp
#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cctype>
#define ll long long
#define gc getchar
#define maxn 105
using namespace std;

inline ll read(){
	ll a=0;int f=0;char p=gc();
	while(!isdigit(p)){f|=p=='-';p=gc();}
	while(isdigit(p)){a=(a<<3)+(a<<1)+(p^48);p=gc();}
	return f?-a:a;
}int n,m,f[maxn][maxn];

struct ahaha{
	int w,to,next;
}e[maxn<<1];int tot,head[maxn];
inline void add(int u,int v,int w){
	e[tot]={w,v,head[u]};head[u]=tot++;
}

int sz[maxn];
void dfs(int u,int fa){
	for(int i=head[u];~i;i=e[i].next){
		int v=e[i].to;if(v==fa)continue;
		dfs(v,u);sz[u]+=sz[v]+1;
		for(int j=min(sz[u],m);j;--j)
			for(int k=min(sz[v],j-1);k>=0;--k)
				f[u][j]=max(f[u][j],f[u][j-k-1]+f[v][k]+e[i].w);
	}
}

int main(){memset(head,-1,sizeof head);
	n=read();m=read();
	for(int i=1;i<n;++i){
		int u=read(),v=read(),w=read();
		add(u,v,w);add(v,u,w);
	}
	dfs(1,-1);
	printf("%d\n",f[1][m]);
	return 0;
}
```

如果有不明白的地方，欢迎私信向我提问，如果对你有帮助，请点个赞吧

## 感谢观看 请勿抄袭
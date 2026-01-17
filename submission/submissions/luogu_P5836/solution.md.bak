# P5836 题解

# 不得不说，这题看上去就是一道裸的LCA...
但是，我们要记住，USACO的**silver**并不难！

于是，就出现了（并查集）这个代码难度极小的做法

这一棵树只有两种颜色，故我们只要记录树上一个个颜色相同的连通块，只有当所查询两点是同一连通块且连通块颜色与目标颜色不同时输出0。

代码如下：
```cpp
#include<bits/stdc++.h>
using namespace std;
int fa[100010],ans[100010],M,N;
char col[100010];
int find(int x)
{
	if(x==fa[x])	return x;
	return fa[x]=find(fa[x]);
}
void merge(int x,int y)
{
	fa[find(x)]=find(y);
}
int main()
{
	int cnt=0;
	cin>>N>>M;
	for(int i=1;i<=N;i++)
	{
		fa[i]=i;
		cin>>col[i];
	}	
	for(int i=1;i<=N-1;i++)
	{
		int u,v;cin>>u>>v;
		if(col[u]==col[v])	merge(u,v);
	}
	for(int i=1;i<=M;i++)
	{
		int a,b;	cin>>a>>b;
		char c;		cin>>c;
		if(find(a)==find(b)&&col[a]!=c)		ans[++cnt]=0;//判断路径上是否有偏好的牛奶
		else	ans[++cnt]=1;
	}
	for(int i=1;i<=cnt;i++)	cout<<ans[i];
	return 0;
}
```

听大佬说，有利用连通块的O（n）做法，可以留给大家自行思考
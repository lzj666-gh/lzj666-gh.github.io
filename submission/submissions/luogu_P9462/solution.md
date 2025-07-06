# P9462 题解

## Solution

考虑 $fa_i<i$ 的部分分，我们尝试依次确定 $3,4,\cdots,n$ 的父亲。

我们规定 $1$ 的父亲是 $2$，对于每个点 $x$ 先令临时父亲 $y=1$，然后每次在 $y$ 和 $fa_y$ 中选择距离为偶数的点，尝试更新父亲直到更新后父亲相同为止。每次 $x$ 与 $y$ 的距离 $d$ 会变成 $\lceil\frac{d}{2}\rceil$，因此在 $\log n$ 次迭代后肯定会相同，需要 $n+\sum\limits_{i=1}^n\lceil\log_2i\rceil$ 次操作。

对于任意树的情况，我们先尝试找到两个相邻的点：

先询问每个点和 $1$ 的中点，找到和 $1$ 的距离 $\text{lowbit}$ 最大的（即能取中点次数最多的）不断取中点即可得到一个和 $1$ 相邻的点。

然后考虑使用 bfs 优化上述迭代过程：我们在临时父亲 $y$ 为一个不确定父亲的点时将询问挂在 $y$ 上，然后每次确定一个点的父亲时处理挂在它上面的所有询问即可。

操作次数为较难卡满的 $n+\sum\limits_{i=1}^n\lceil\log_2 i\rceil$，实测 $2n+\sum\limits_{i=1}^n\lceil\log_2 i\rceil$ 甚至 $3n+\sum\limits_{i=1}^n\lceil\log_2 i\rceil$ 在随机选根时也可以通过。

## Code

```cpp
#include<bits/stdc++.h>
using namespace std;
inline int read(){
   int s=0,w=1;
   char ch=getchar();
   while(ch<'0'||ch>'9'){if(ch=='-')w=-1;ch=getchar();}
   while(ch>='0'&&ch<='9') s=s*10+ch-'0',ch=getchar();
   return s*w;
}
int query(int x,int y)
{
	printf("? %d %d\n",x,y),
	fflush(stdout);
	return read();
}
int a[10003],b[10003],fa[10003];
vector<int> v[10003],d[10003];
void dfs(int x)
{
	for(int y:v[x])
		dfs(y),b[x]=max(b[x],b[y]+1);
	return ;
}
signed main()
{
	int n=read(),id=2;
	a[1]=1;
	for(int i=2; i<=n; ++i)
	{
		a[i]=query(1,i);
		if(a[i]) v[a[i]].push_back(i),a[i]=1;
	}
	for(int i=2; i<=n; ++i)
	{
		if(!a[i]) dfs(i);
		if(b[i]>b[id]) id=i;
	}
	queue<int> q;
	fa[1]=id,fa[id]=1,q.push(1),q.push(id);
	for(int i=2; i<=n; ++i) if(i!=id) d[1].push_back(i);
	while(!q.empty())
	{
		int x=q.front();
		q.pop();
		for(int y:d[x])
		{
			if(a[x]^a[y])
			{
				int z=query(fa[x],y);
				if(z==x) fa[y]=x,q.push(y);
				else d[z].push_back(y);
			}
			else d[query(x,y)].push_back(y);
		}
		vector<int>().swap(d[x]);
	}
	puts("!");
	for(int i=2; i<=n; ++i) printf("%d %d\n",fa[i],i);
	return 0;
}
```
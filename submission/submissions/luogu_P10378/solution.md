# P10378 题解

# P10378 [GESP202403 七级] 交流问题 题解

------------

[题目传送门](https://www.luogu.com.cn/problem/P10378)

~~GESP 为什么有时候很简单（比如这个题），有时候又很难，但是随便瞎搞一下又能过，看正解后又发现自己不是正解。。。~~

------------

## 题意

给你一个二分图（至于为什么是二分图，见后面的分析），可能不联通，给这个二分图染色，问染成某个颜色的点数的最小可能和最大可能。

关于二分图和二分图染色，不知道读者的可以看[这里](https://oi-wiki.org/graph/bi-graph/)。

------------

## 分析

首先拿到一道题目读完题之后第一时间应该看的是数据范围。

$1\leq u_i,v_i\leq n\leq 10^5$，$1\leq m\leq 2\times 10^5$。

因为 $n$ 和 $m$ 的规模是一样的，我们不妨令 $m$ 就是 $n$。

所以根据数据范围，我们需要一个大概是 $O(n)$ 或者 $O(n\log n)$ 的算法。

容易发现这个题给的交流关系可以构成一张图，并且对于这张图上截取的每一条链，都是 `A-B-A-B...` 或者 `B-A-B-A...`的状态。

**也就是说这个图是一个二分图！**

由于题目保证“输入是合法的，即交流一定是跨校开展的”，所以我们不用考虑这个图不是二分图的情况

题目求 $B$ 校的规模，那我们就应该给二分图染色。

那题目转换为求某个颜色个数的最小值和最大值。

由于这个图不联通，先来想想如果联通怎么做。

为方便表述，接下来的染色叫做红蓝染色。

那我们是不是只要给这个二分图红蓝染色，然后：

1. **红色的蓝色个数个数的最小值就是 $B$ 校人数的最小值；**
2. **红色的蓝色个数个数的最大值就是 $B$ 校人数的最大值。**

画个图理解一下：

![](https://cdn.luogu.com.cn/upload/image_hosting/xuw5a2jt.png)

比如对于这个图，可以这样染色：

![](https://cdn.luogu.com.cn/upload/image_hosting/v83mqvzo.png)

这个时候 $B$ 校的最小值就是红色的颜色个数，即为 $2$。

$B$ 校的最大值就是蓝色的颜色个数，即为 $3$。

为什么可以这样呢，因为我们可以把红色当成 $B$ 校，也同时可以把蓝色当成 $B$ 校。

当然如果把红蓝反过来染也是一个道理，所以我们刚刚的结论是正确的。

对于不联通的图怎么办呢？

**我们可以把每一个联通块都这样处理，最小值加起来就是最终的最小值答案（至少），最大值加起来就是最终的最大值答案（至多）。**

嗯，这就分析完了。

时间复杂度 $O(n)$，因为每个点只被访问一次。

------------

## AC 代码

```cpp
#include<bits/stdc++.h>
#define Code using
#define by namespace
#define wjb std
Code by wjb;
int in()
{
	int k=0,f=1;
	char c=getchar();
	while(c<'0'||c>'9')
	{
		if(c=='-')f=-1;
		c=getchar();
	}
	while(c>='0'&&c<='9')k=k*10+c-'0',c=getchar();
	return k*f;
}
void out(int x)
{
	if(x<0)putchar('-'),x=-x;
	if(x<10)putchar(x+'0');
	else out(x/10),putchar(x%10+'0');
}
const int N=1e5+10;
vector<int>e[N]; // 存储边 
bool b[N]; // 这个点是否被访问过了 
void dfs(int u,int &s1,int &s2,bool f) // 注意这里的 s1 和 s2 要引用传参 
// 当前点在 u，染了 s1 个红色，s2 个蓝色，f=1 表示当前要染红色，f=0 表示当前要染黑色 
{
	b[u]=true; // 标记已经放问过了 
	if(f)s1++; // 染色 
	else s2++;
	for(int v:e[u])
		if(!b[v])dfs(v,s1,s2,!f); // 进行下一个点的染色，注意 !f 
}
int main()
{
	int n=in(),m=in();
	while(m--)
	{
		int u=in(),v=in();
		e[u].push_back(v),e[v].push_back(u); //存 边 
	}
	int s1=0,s2=0;
	for(int i=1;i<=n;i++)
		if(!b[i]) // 处理每一个联通块 
		{
			int ss1=0,ss2=0;
			dfs(i,ss1,ss2,true); // 这里传入 true 和 false 都可以
			s1+=min(ss1,ss2),s2+=max(ss1,ss2); // 红蓝最小值和红蓝最大值 
		}
	out(s1),putchar(' '),out(s2);
	return 0;
}
```

------------

后记 1：版权所有@[KobeBeanBryantCox](https://www.luogu.com.cn/user/865625)，请勿抄袭代码。

后记 2：写代码的习惯一定要好，代码不要乱七八糟，优秀的码风是很醉人的~

~~还有，能不能不要脸地要个赞呀 QwQ~~
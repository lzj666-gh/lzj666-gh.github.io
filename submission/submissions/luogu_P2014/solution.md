# P2014 题解

[题目传送门](https://www.luogu.org/problemnew/show/P2014)

首行求赞，反正不FA钱$\ \text{qwq}$

## 0. 前置

- 动态规划基础
- 知道树是什么，以及存图方式

## 1. 题意简述

- 一堆树构成的森林，共$N$个点。
- 每个点有一个权值$s_i$
- 一个点可以被选择，当且仅当它到根节点的路径上的**所有点**都被选择。

共选择$M$个点，求被选择的点的权值和的最大值

## 2. 一个小技巧

我们发现，如果0算一个节点的话，整张图就是一棵树了

这样的好处：

1. 一棵树就不用分别考虑各棵树然后合并了
2. 输入方便很多，不用特别处理$0$的情况


但是$M$就会受影响

因为根节点$0$是必选的，所以只要让$M$增加$1$就好了

---

**确保您理解了以上内容再看下面的部分，如果不理解可以自己画图体会**

---


## 3. dp及初步设计状态

首先，不难看出，父节点的信息可以由子节点合并得到并且不会影响子节点

所以使用 dp/记忆化搜索 就好了$\ \text{qwq}$

不难想到，用$\text{dp[u][i]}$表示以节点$u$为根的子树 ，选择$i$个点可以获得的最大权值和

然后想如何转移

。。。好像遇到麻烦了

显然合并子节点的信息一定能得到父节点的信息，但使用简单的算法好像不行了

~~没事反正数据范围小~~

可以考虑dp套dp（当然这个题算比较简单的）

## 4. 背包

继续观察，发现每个子节点都会占用父节点$i$的一部分，又有一个贡献，可以选择或不选择

重量。。。价值。。。总重。。。

这不是01背包吗？

不同之处在于，每个子节点的重量都是变量

### 重新设计状态

用$dp[u][i][j]$表示节点$u$的前$i$个子节点，限重为$j$能得到的最大权值和（价值和）

像01背包一样压缩空间，得到：

```dp[u][j]表示节点u，限重j的最大权值和（价值和）```

代码：

```cpp
for(int i=head[u]; i; i=e[i].next)//遍历所有子节点
	for(int j=m, v=e[i].to; j>0; --j)//这里和01背包一样，总重从大到小循环
		for(int k=0; k<j; ++k)//这里是不同之处，子节点的重量需要规定
			chk_max(dp[u][j], dp[u][j-k]+dp[v][k]);//此函数是将前一个参数设为二者的最大值（您不会不知道吧），不明白下面有代码
```

5. code

```cpp
#include<cstdio>
const int MAXN = 300 + 5;
const int MAXM = 300 + 5;

inline void chk_max(int &a,int b){ if(a<b) a=b;}

//前向星存图
struct Edge
{
	int next,to;
}e[MAXN];
int head[MAXN],ecnt=0;
inline void add(int u,int v)
{
	++ecnt;
	e[ecnt].next=head[u];
	e[ecnt].to=v;
	head[u]=ecnt;
}

int m;
int dp[MAXN][MAXM];

void solve(int u)
{
	for(int i=head[u]; i; i=e[i].next)
		solve(e[i].to);//先处理子节点
	
    //背包部分
	for(int i=head[u]; i; i=e[i].next)
		for(int j=m, v=e[i].to; j>0; --j)
			for(int k=0; k<j; ++k)
				chk_max(dp[u][j], dp[u][j-k]+dp[v][k]);
}

int main(void)
{
	
	int n;
	scanf("%d%d",&n,&m);
	++m;//上文提到了
	for(int i=1; i<=n; ++i)
	{
		int fa;
		scanf("%d%d",&fa,&dp[i][1]);//思考：为什么直接用dp[i][1]？
		add(fa,i);
	}
	
	solve(0);
	printf("%d",dp[0][m]);
	return 0;
}
```

本题解主要用于理清自己思路，如果有与他人方法重复也不要喷qaq

实际还写了蛮长时间的。。。码字手酸，见谅qwq

如果您觉得题解有错误，可以私信或者评论

当然别忘了点赞qwq
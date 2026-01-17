# P8267 题解

# 前置知识

1. 若 $a\leqslant b,x\leqslant a$，则 $x\leqslant b$
2. 若 $a\geqslant b,x\geqslant a$，则 $x\geqslant b$
3. 若 $a>b,x\geqslant a,x\leqslant b$，则 $x$ 无解

# 题解

首先，我们将字符为 `L` 和 `G` 分别加入数组 $a$ 和 $b$ 中，并进行排序。然后我们 $O(n^2)$ 枚举，不妨假设枚举到 $a_i$ 和 $b_j$，数组 $a,b$ 的大小分别为 $x,y$。  

由前置知识，我们可以得到：  

1. $a_{i},a_{i+1},\cdots,a_x$ 都是满足条件的
2. $b_1,b_2,\cdots,b_{j}$ 都是满足条件的
3. 如果 $a_i<b_j$ 则无解。  

因此，我们先判断一下 $a_i$ 和 $b_j$ 的大小关系，如果符合条件，$ans=\min\{ans,i-1+y-j\}$，这样就得出答案了。

## 优化

[数据加强版](https://www.luogu.com.cn/problem/U208878)  

其实这道题是可以 $O(n\log n)$ 的。注意到枚举每一个 $a_i$ 时，$i-1$ 是固定的，我们要让 $y-j$ 尽量小，就是让 $j$ 尽量大。简单来说，就是要求 $b$ 数组中小于等于 $a_i$ 的最大值，在 $b$ 数组中二分即可，下面的代码还是 $O(n^2)$ 的。

## 注意

- 最坏情况下有 $1$ 只奶牛猜的是对的，所以 $ans$ 要初始化为 $n-1$。

- 有可能说 `L` 或说 `G` 的奶牛全都是错的，注意细节。

## Code

```cpp
#include<bits/stdc++.h>
using namespace std;
#define N 1005
int n,t,x,y,a[N],b[N],ans;
char c;
int main()
{
	scanf("%d",&n);
	b[++y]=-1;
	for(int i=1;i<=n;i++)
	{
		scanf("\n%c%d",&c,&t);
		if(c=='L') a[++x]=t;
		else b[++y]=t;
	}
	sort(a+1,a+x+1);
	sort(b+1,b+y+1);
	a[++x]=1e9+1,ans=n-1;
	for(int i=1;i<=x;i++)
	{
		for(int j=1;j<=y;j++)
		{
			if(a[i]>=b[j]) ans=min(ans,i-1+y-j);
			else break;
		}
	}
	printf("%d\n",ans);
	return 0;
}
```
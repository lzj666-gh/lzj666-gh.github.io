# P8816 题解

正式比赛中一遍切的动态规划真不多见(⊙o⊙)…，本题解，与上面两个题解有略微不同。

## 题目概述
在一个二维平面内，给定 $n$ 个整数点 $(x_i, y_i)$，此外你还可以自由添加 $k$ 个整数点。

你在自由添加 $k$ 个点后，还需要从 $n + k$ 个点中选出若干个整数点并组成一个序列，使得序列中任意相邻两点间的欧几里得距离恰好为 $1$ 而且横坐标、纵坐标值均单调不减，即 $x_{i+1} - x_i = 1, y_{i+1} = y_i$ 或 $y_{i+1} - y_i = 1, x_{i+1} = x_i$。请给出满足条件的序列的最大长度。  
$n \leq 500$，$k \leq 100$，$x_{i},y_{i} \leq 10^9$。

## 思路概述

看完题面，是不是有点像二维最长不下降子序列？所以考虑 $dp$。
这么小的数据范围，我们可以使用三次方级别的算法通过。  


首先我们需要对输入的点进行排序，以 $x$ 为第一关键字，以 $y$ 为第二关键词，方便我们未来状态的转移。

设状态 $f_{i,j}$ 为枚举到第 $i$ 个点，我们还剩余 $j$ 个添加自由点的机会，此时满足题意的点的最大长度。  
易得如下方程。
$$f_{i,j}=\max(f_{k,j+d}+d+1)$$
$$k\in \left[1,i-1\right]$$
$$d=\operatorname{abs}(x_{i}-x_{k})+\operatorname{abs}(y_{i}-y_{k})-1$$

最终答案为 $\max(f_{i,j}+j)  \ j \in [0,k]$。  
复杂度为 $O(n^2k)$。

你可能有几个疑惑。  
$d$ 是什么呢？$d$ 就是在点 $x$ 和点 $y$ 之间，我们需要加多少个自由点才能满足题意。  
为什么最终方程里转移的时候我们要加一呢？因为我们不仅仅加上中间加的点呀，我们还需要把 $y$ 点给加上。  
还有一些小细节在下方代码中有注释。


到这里基本上你已经理解了本题的解题过程，先尝试自己写一下代码，再看下方给出的代码吧。

## code
代码中在重要部分/细节处有注释解释。
```cpp
#include<bits/stdc++.h>
using namespace std;

const int N=510,K=110;

int n,k;
struct node{
	int x,y;
	bool operator< (const node &w) const
	{
		if(x==w.x)	return y<w.y;
		return x<w.x;
		//此处为运算符重载，这里的意思就是以x为第一关键字，以y为第二关键词从小到大进行排序
	}
}a[N];
int f[N][K];

int main()
{
//	freopen("1.in","r",stdin);
//	freopen("1.out","w",stdout);
	scanf("%d%d",&n,&k);
	for(int i=1;i<=n;i++)
		scanf("%d%d",&a[i].x,&a[i].y);
	sort(a+1,a+1+n);
	for(int i=1;i<=n;i++)
	{
		f[i][k]=1;
		for(int j=0;j<=k;j++)
		{
			for(int t=1;t<i;t++)
			{
				if(a[t].x>a[i].x||a[t].y>a[i].y)	continue;//要符合题意的序列限制
				int dx=abs(a[i].x-a[t].x);
				int dy=abs(a[i].y-a[t].y);
				int d=dx+dy-1;//求在x,y之间我们要加多少个自由点
				if(j+d>k)	continue;//如果要加的自由点超过k个，就不能再转移了
				f[i][j]=max(f[i][j],f[t][j+d]+d+1);
			}
		}
	}
	int ans=0;
	for(int i=1;i<=n;i++)
		for(int j=0;j<=k;j++)
		{
			ans=max(ans,j+f[i][j]);
			//因为我们最终可能有剩余的自由点，所以在取答案的时候，我们需要再加上剩余的自由点数量
		}
	cout<<ans;
	return 0;
}
```
代码较丑，不喜勿喷。
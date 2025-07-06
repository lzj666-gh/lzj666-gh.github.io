# P10453 题解

[也许更好的阅读体验](https://www.cnblogs.com/yzxgg/p/18204641/solution-P10453)

[题目传送门](https://www.luogu.com.cn/problem/P10453)

最近在板刷蓝书，所以来写个题解加深自己的印象。

首先发现行和列互不影响，所以可以分开看。所以就是对行和列都做一次环形均分纸牌问题，也就是这个题[糖果传递](https://www.luogu.com.cn/problem/P2512)。

### 先来看一下普通的均分纸牌

普通的均分纸牌就是 $n$ 个小朋友排成一列，各有 $a_i$ 张牌，每个人只能给相邻的人传递纸牌，问至少需要传递多少张纸牌才能使每个小朋友纸牌的数量相等。

最后每个人手里的牌一定是牌总数的平均值，即 $ave=\frac{sum}{n}(sum=\sum {a_i})$，设 $g_i=a_i-ave$，答案就是 $\sum |s_i|$，其中 $s_i=\sum\limits_{j=1}^i g_j$，即 $g$ 的前缀和。

可以这么理解，$g$ 表示的是到最终目标牌数差的数量，目标是将 $g$ 都变为 $0$，那么对 $g$ 取前缀和表示的就是把前面的牌都转移到自己，所以 $s_i$ 就是 $i$ 转移出去的代价。

### 再来看一下环形均分纸牌

环形的问题就是小朋友坐成了一圈，等同于最后一个人与第一个人相邻。

思考后可以发现环形均分纸牌的一个性质：必定至少有两个相邻的人不需要从对方那里获得纸牌（这是显然的，不妨设这两个人的位置为 $i$ 和 $i+1$，$T$ 代表均分纸牌的目标个数，则环形序列中必定有满足 $a_i\le T,a_{i+1}\ge T$ 的两个相邻位置，这样 $i$ 和 $i+1$ 就不会交换，因为 $a_i\le T$ 的会从 $i-1$ 处得到纸牌，$a_{i+1}\ge T$ 可以把牌传递给 $i+2$）。

所以我们可以根据上面的性质，把环变成链，枚举不需要交换的两个人。

按开始的序列顺序，像普通均分纸牌一样处理出$g$ 的前缀和 $s$ 数组，那么假设枚举的位置为 $k$，则类比普通均分纸牌求法，新的 $s_i=s_i-s_k$，于是 $ans=\sum{|s_i-s_k|}$，发现 $s_k$ 为 $s$ 的中位数时 $ans$ 最小，于是该问题就得到了解决。

### 回到这个题

应该先判断有没有解，即行和列的 $sum$ 是否可以分别被行数 $n$ 和列数 $m$ 整除。然后对行和列做两次环形均分纸牌即可。

细节可以参考代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e5+5;
inline int read();
int n,m,t,row[N],col[N];
long long srow[N],scol[N],rowsum,colsum,rowans,colans;
int main()
{
	n=read();m=read();t=read();
	for(int i=1;i<=t;i++)
	{
		int x,y;
		x=read();y=read();
		row[x]++,col[y]++;
		rowsum++,colsum++;
	}
	if(rowsum%n!=0&&colsum%m!=0) return puts("impossible"),0;
	if(rowsum%n==0)
	{
		int rowave=rowsum/n;
		for(int i=1;i<=n;i++)
		{
			row[i]-=rowave;
			srow[i]=srow[i-1]+row[i];
		}
		sort(srow+1,srow+1+n);
		int k=(n+1)/2;
		for(int i=1;i<=n;i++)
		{
			rowans+=abs(srow[i]-srow[k]);
		}
	}
	if(colsum%m==0)
	{
		int colave=colsum/m;
		for(int i=1;i<=m;i++)
		{
			col[i]-=colave;
			scol[i]=scol[i-1]+col[i];
		}
		sort(scol+1,scol+1+m);
		int k=(m+1)/2;
		for(int i=1;i<=m;i++)
		{
			colans+=abs(scol[i]-scol[k]);
		}
	}
	if(colsum%m!=0) printf("row %lld",rowans);
	else if(rowsum%n!=0) printf("column %lld",colans);
	else printf("both %lld",rowans+colans);
	return 0;
}

inline int read()
{
	int x=0,f=1;
	char ch;
	ch=getchar();
	while(ch>'9'||ch<'0'){if(ch=='-') f=-f;ch=getchar();}
	while(ch<='9'&&ch>='0')
	{
		x=(x<<1)+(x<<3)+(ch&15);
		ch=getchar();
	}
    return x*f;
}
```

UPD on 2024.10.13
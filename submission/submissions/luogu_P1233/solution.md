# P1233 题解

有的题解存在一些问题，而数据好像有一点水，导致他们好像也 $AC$ 了，在这里讲一下。
这里主要指出，在对木棒排序的时候，应当以长度 $l$ 降序， $l$ 相同时按    $w$ 降序，忽略了按 $w$ 降序这一环节的会被以下数据 $hack$：

```
3
1 1
1 2
1 3
```

答案是应当是 $1$ , 然而有题解会给出 $3$  $QwQ$

解题思路大概提一下：因为题目要求二维数据都**不上升**，那么这就启发我们先排序(按上面的方法)，最后计算另一维的序列中**最少分割为多少个不上升子序列**(满足加工顺序),由~~不会证的~~$dilworth$定理 , 答案与该序列的**最长上升子序列长度**相同，这个问题很容易 $dp$ 求解。

$O(n^2)$与$O(nlog_2n)$的 $dp$ 应该都可以通过本题，$O(n^2)$算法大家应该都会这里就不多提了。


大概讲一下$O(nlogn)$的方法：$f[i]$ 表示长度为 $i$ 的(木棒宽度的)上升子序列结尾最小是多少，在 $f[ans]$ 比当前木棒宽度小时更新 $ans$ ，否则二分查找( $f$ 数组显然单调)找到比当前木棒宽度大的第一个位置更新。

这里就可以说明为什么要 $l$ 相同时按    $w$ 降序，我们需要答案尽量小，而以 $w$ 降序时可以不浪费时间的按顺序加工完，因此这样排序，对应到模型里就是减少最长上升子序列的长度(按上面的例子，宽度序列需要为 $3$ $2$ $1$而非 $1$ $2$ $3$ , 后一种加工方法浪费了时间)

给出$O(nlogn)$ 代码。

$Code$：
```cpp
#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

#define lenc 100000

inline char gc()
{
	static char buf[lenc],*p1,*p2;
	return p1==p2&&(p2=(p1=buf)+fread(buf,1,lenc,stdin),p1==p2)?EOF:*p1++;
}

inline int read()
{
	register int q=0;
	register char c=gc();
	while(!isdigit(c))
		c=gc();
	while(isdigit(c))
		q=(q<<3)+(q<<1)+(c^48),c=gc();
	return q;
}
//上面是快读 忽略即可
struct stick
{
	int l,w;
}a[5010];

int n,f[5010],ans;

bool cmp(stick q,stick w)
{
	if(q.l!=w.l)
		return q.l>w.l;
	return q.w>w.w;
}

int main()

{
	n=read();
	for(register int i=1;i<=n;i++)
		a[i].l=read(),a[i].w=read();
	sort(a+1,a+1+n,cmp);
	for(register int i=1;i<=n;i++)
	{
		if(a[i].w>f[ans])
			f[++ans]=a[i].w;
		else
		{
			int tmp=lower_bound(f+1,f+1+ans,a[i].w)-f;
			f[tmp]=a[i].w;
		}
	}
	printf("%d",ans);
	return 0;
}
```